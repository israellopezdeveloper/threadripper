# Threadripper - Real-Time Log Monitoring Application

![Threadripper](https://raw.githubusercontent.com/israellopezdeveloper/threadripper/refs/heads/metadata-branch/logo.png)

**Threadripper** is an application to monitor and visualize the contents of a log file in real time. Using an interactive graphical interface, it allows users to observe events as they occur, updating the chart in real time with each file change. It is the perfect complement to **[Nanologger](https://github.com/israellopezdeveloper/nanologger)**, a minimally intrusive logger that allows thread-based tracking of logs, enhancing traceability and analysis in concurrent execution environments.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Considerations](#considerations)

## Requirements

- **Python 3.8 or higher**

### Python Dependencies
To run the application, the following Python libraries are required:
- `streamlit`
- `plotly`
- `pandas`

## Installation

1. **Clone this repository**:
   ```bash
   git clone git@gitlab.com:ILM-Investigaciones/threadripper.git
   cd threadripper
   ```

2. **Install the Python dependencies**:
   ```bash
   make check-dependencies
   ```

## Usage

To run **Threadripper** directly with Python, use the following command:

```bash
make run
```

This command will start the Streamlit server, allowing you to view the application in your browser and read logs from the `logs.log` file.

## Considerations

- **Real-time Updates**: Threadripper monitors and updates the chart every 5 seconds.
- **Chart Maximization**: The graphical interface automatically adjusts to occupy the full available space in Streamlit.
- **Compatibility**: This application is designed to run on Linux systems but may work on other operating systems compatible with Python and Streamlit.
