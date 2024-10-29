# Threadripper - Aplicación de Monitoreo de Logs en Tiempo Real

![Threadripper](https://raw.githubusercontent.com/israellopezdeveloper/threadripper/refs/heads/metadata-branch/logo.png)

**Threadripper** es una aplicación para monitorear y visualizar en tiempo real el contenido de un archivo de logs. Usando una interfaz gráfica interactiva, permite observar eventos a medida que ocurren, actualizando el gráfico en tiempo real con cada cambio en el archivo. Es el complemento perfecto para **[Nanologger](https://github.com/israellopezdeveloper/nanologger)**, un logger de intrusión mínima en el código que permite un seguimiento de logs optimizado por threads, mejorando la trazabilidad y el análisis en entornos de ejecución concurrente.

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Consideraciones](#consideraciones)

## Requisitos

- **Python 3.8 o superior**

### Dependencias de Python
Para ejecutar la aplicación, necesitas las siguientes bibliotecas de Python:
- `streamlit`
- `plotly`
- `pandas`

## Instalación

1. **Clona este repositorio**:
   ```bash
   git clone git@gitlab.com:ILM-Investigaciones/threadripper.git
   cd threadripper
   ```

2. **Instala las dependencias de Python**:
   ```bash
   make check-dependencies
   ```

## Uso

Para ejecutar **Threadripper** directamente con Python, usa el siguiente comando:

```bash
make run
```

Este comando iniciará el servidor de Streamlit y podrás visualizar la aplicación en tu navegador, leyendo los logs del archivo `logs.log`.

## Consideraciones

- **Actualización en tiempo real**: Threadripper monitorea y actualiza el gráfico en intervalos de 5 segundos.
- **Maximización del gráfico**: La interfaz gráfica se ajusta automáticamente para ocupar el espacio completo en Streamlit.
- **Compatibilidad**: La aplicación está diseñada para ejecutarse en sistemas Linux, pero puede funcionar en otros sistemas operativos compatibles con Python y Streamlit.

