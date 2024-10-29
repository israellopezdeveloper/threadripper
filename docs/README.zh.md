# Threadripper - 实时日志监控应用

![Threadripper](https://raw.githubusercontent.com/israellopezdeveloper/threadripper/refs/heads/metadata-branch/logo.png)

**Threadripper** 是一款用于实时监控和可视化日志文件内容的应用程序。通过交互式图形界面，用户可以实时观察事件的发生，并随文件的每次更改更新图表。它是 **[Nanologger](https://github.com/israellopezdeveloper/nanologger)** 的完美补充，**[Nanologger](https://github.com/israellopezdeveloper/nanologger)** 是一种对代码影响极小的日志记录器，允许基于线程的日志跟踪，从而在并发执行环境中增强可追溯性和分析能力。

## 目录
- [系统需求](#系统需求)
- [安装](#安装)
- [使用方法](#使用方法)
- [注意事项](#注意事项)

## 系统需求

- **Python 3.8 或更高版本**

### Python 依赖
要运行该应用程序，需安装以下 Python 库：
- `streamlit`
- `plotly`
- `pandas`

## 安装

1. **克隆此存储库**：
   ```bash
   git clone git@gitlab.com:ILM-Investigaciones/threadripper.git
   cd threadripper
   ```

2. **安装 Python 依赖**：
   ```bash
   make check-dependencies
   ```

## 使用方法

要直接在 Python 环境中运行 **Threadripper**，请使用以下命令：

```bash
make run
```

此命令将启动 Streamlit 服务器，您可以在浏览器中查看应用程序，并读取 `logs.log` 文件中的日志。

## 注意事项

- **实时更新**：Threadripper 每隔 5 秒监控并更新图表。
- **图表最大化**：图形界面会自动调整以占用 Streamlit 中的全部可用空间。
- **兼容性**：该应用程序设计为在 Linux 系统上运行，但可能也适用于其他兼容 Python 和 Streamlit 的操作系统。
