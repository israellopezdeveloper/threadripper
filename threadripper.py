import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re
import time
import streamlit as st
import argparse
# Asegúrate de tener instalada esta biblioteca para cargar la imagen
from PIL import Image

# Configuración de la página de Streamlit en ancho completo
st.set_page_config(layout="wide", page_title="Threadripper",
                   page_icon="/opt/threadripper/logo.png")

# Cargar el logo desde /opt/threadripper/logo.png y mostrarlo en la aplicación
logo_path = "/opt/threadripper/logo.png"
logo = Image.open(logo_path)
st.image(logo, width=150)
# Argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Monitor real-time log updates.")
parser.add_argument("log_file", type=str,
                    help="Path to the log file to monitor.")
args = parser.parse_args()

# Función para parsear cada línea


def parse_log_line(line):
    data = {}
    marker_match = re.search(r'<\s*(.*?)\s*>', line)
    data['marker'] = marker_match.group(1) if marker_match else None
    line = re.sub(r'<\s*.*?\s*>', '', line).strip()
    parts = re.split(r'\|>', line)
    parts = [part.strip() for part in parts if part.strip()]

    if parts:
        kv_pairs = re.findall(r'(\w+)=([^\s|>]+)', parts[0])
        for key, value in kv_pairs:
            data[key] = value

    for part in parts[1:]:
        kv_pairs = re.findall(r'(\w+)=([^\s|>]+)', part)
        for key, value in kv_pairs:
            data[key] = value
        position_match = re.search(r'position=([^\s|>]+)', part)
        if position_match:
            position = position_match.group(1)
            data['position'] = position
            part = part.replace(f'position={position}', '').strip()
        if part and not re.match(r'(\w+)=([^\s|>]+)', part):
            data['message'] = part.strip()

    return data

# Función para cargar y procesar los logs desde un archivo


def load_logs(log_file):
    with open(log_file, 'r') as f:
        logs = f.readlines()

    parsed_logs = [parse_log_line(line.strip())
                   for line in logs if line.strip()]
    df = pd.DataFrame(parsed_logs)
    df['time'] = pd.to_numeric(df['time'], errors='coerce')
    df['line'] = pd.to_numeric(df['line'], errors='coerce')
    df['depth'] = pd.to_numeric(df['depth'], errors='coerce')
    df = df.drop(columns=['parents', 'function_id'], errors='ignore')
    df = df.sort_values(by=['th_id', 'time']).reset_index(drop=True)
    df['event_id'] = df.groupby(
        ['th_id', 'function', 'depth', 'position']).cumcount()
    print(df)
    df_init = df[df['position'] == 'init']
    df_end = df[df['position'] == 'end']
    df_merged = pd.merge(df_init, df_end,
                         on=['th_id', 'function', 'depth', 'event_id'],
                         how='left', suffixes=('_begin', '_end'))
    df_merged['begin'] = df_merged['time_begin']
    df_merged['end'] = df_merged['time_end']
    df_result = df_merged[['marker_begin', 'th_id', 'time_begin', 'time_end',
                           'file_begin', 'line_begin', 'depth', 'function',
                           'position_begin', 'begin', 'end']]
    df_result = df_result.rename(columns={
        "marker_begin": "marker", "th_id": "th", "file_begin": "file",
        "line_begin": "line"
    })
    df_result = df_result.drop(
        columns=["time_begin", "time_end", "position_begin"])

    df_punctual = df[df['position'] == 'punctual'].reset_index(drop=True)
    df_punctual = df_punctual.rename(
        columns={"th_id": "th", "time": "begin"})
    df_punctual = df_punctual.drop(columns=["position", "event_id"])
    new_order = ['marker', 'th', 'file', 'line',
                 'depth', 'function', 'begin']
    df_punctual = df_punctual.reindex(columns=new_order)
    df_punctual['end'] = df_punctual['begin']

    df = pd.concat([df_result, df_punctual], axis=0,
                   ignore_index=True).sort_values(by='begin')
    min_timestamp = df['begin'].min()
    df['begin'] = pd.to_datetime(
        df['begin'] - min_timestamp, unit='ms', origin='unix')
    df['end'] = pd.to_datetime(
        df['end'] - min_timestamp, unit='ms', origin='unix')
    df['th_function'] = df['th'].astype(str) + " - " + df['function']
    return df


# Configuración de Streamlit para mostrar el gráfico en tiempo real
st.title("Real-Time Log Monitoring")

# Crear un contenedor vacío para el gráfico
plot_container = st.empty()

df_previous = None
while True:
    # Cargar y procesar los logs
    df = load_logs(args.log_file)

    if df_previous is None or not df_previous.equals(df):
        fig = px.timeline(df[df['marker'] == '📘'],
                          x_start="begin", x_end="end",
                          y="th_function", color="marker",
                          hover_name="th", hover_data={
                              'marker': False,
                              'th': False,
                              'th_function': False,
                              'function': True,
                              'file': True,
                              'line': True,
                              'depth': False,
                              'begin': False,
                              'end': False
        })

        # Configuración para maximizar el uso del espacio
        fig.update_layout(
            xaxis_title="Time",
            yaxis_title="Threads",
            showlegend=False,
            margin=dict(l=10, r=10, t=10, b=10)  # Márgenes mínimos
        )

        df_bombs = df[df['marker'] != "📘"]
        for i, row in df_bombs.iterrows():
            symbol = row['marker']
            fig.add_trace(
                go.Scatter(
                    x=[row['begin'], row['end']],
                    y=[row['th_function'], row['th_function']],
                    mode="lines+text",
                    text=symbol,
                    textposition="middle right",
                    showlegend=False,
                    hovertemplate=(
                        "<b>TH:</b> " + str(row['th']) + "<br>" +
                        "<b>Function:</b> " + row['function'] + "<br>" +
                        "<b>File:</b> " + row['file'] + " (" + str(row['line'])
                        + ")<br>")
                )
            )

        # Actualizar el gráfico en el contenedor con un key único
        plot_container.plotly_chart(
            fig, use_container_width=True, key=time.time())

    # Update
    df_previous = df
    time.sleep(5)  # Actualizar cada 5 segundos
