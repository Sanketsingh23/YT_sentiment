# Sentimental Analysis

A small Streamlit app for sentiment analysis using Hugging Face Transformers and PyTorch.

This repository contains the app code (`streamlit_app.py`) and a `requirements.txt` listing runtime dependencies.

## What this repo does

- Runs a Streamlit UI to enter text and get a sentiment prediction using a pretrained transformer model.

## Prerequisites

- Windows, macOS, or Linux
- Python 3.10+ (this project used Python 3.13 in the development environment)
- Git (optional)

## Commands

Below are the exact commands for PowerShell to create a virtual environment, install the requirements, and run the Streamlit app. Replace the path with your project path if different.

PowerShell (recommended):

```powershell
cd "d:\projects\python\sentimental analysis"

# Create and activate a virtual environment
python -m venv .venv
. .venv\Scripts\Activate.ps1

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Run the Streamlit app (opens browser)
streamlit run streamlit_app.py
```

If you prefer not to activate the venv, use the venv Python directly (works on any shell):

```powershell
cd "d:\projects\python\sentimental analysis"
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run streamlit_app.py --server.port 8501 --server.headless true
```

Quick smoke-test (prints installed package versions):

```powershell
.venv\Scripts\python.exe -c "import streamlit as st, transformers, torch; print('streamlit', st.__version__); print('transformers', transformers.__version__); print('torch', torch.__version__)"
```

## Quick setup (PowerShell)

Open PowerShell in the project root (where `requirements.txt` and `streamlit_app.py` live) and run:

```powershell
cd "d:\projects\python\sentimental analysis"

# Create virtual environment
python -m venv .venv

# Activate the venv (PowerShell)
. .venv\Scripts\Activate.ps1

# Upgrade pip, then install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

If you prefer not to activate, you can use the venv Python directly:

```powershell
cd "d:\projects\python\sentimental analysis"
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run the Streamlit app

With the venv activated:

```powershell
streamlit run streamlit_app.py
```

Or explicitly via the venv Python (headless on port 8501):

```powershell
.venv\Scripts\python.exe -m streamlit run streamlit_app.py --server.port 8501 --server.headless true
```

Open http://localhost:8501 in your browser to view the app.

To stop the server: press Ctrl+C in the terminal where Streamlit is running, or close the terminal.

## Verify installation (quick smoke test)

Run this to confirm key packages import and to print their versions:

```powershell
.venv\Scripts\python.exe -c "import streamlit as st, transformers, torch; print('streamlit', st.__version__); print('transformers', transformers.__version__); print('torch', torch.__version__)"
```

## Notes / Troubleshooting

- PyTorch wheels can be platform- and CUDA-specific. If `pip install -r requirements.txt` fails on the `torch` package, visit https://pytorch.org and follow the selector to get the correct install command for your Python version and CUDA (or CPU-only) configuration. Example CPU-only install:

```powershell
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

- If the app fails to start because port 8501 is in use, start Streamlit on a different port:

```powershell
streamlit run streamlit_app.py --server.port 8502
```

- If you see long model download times at first run, the Transformers model is being cached by Hugging Face in `~/.cache/huggingface` (or the OS equivalent). Ensure you have network access and disk space.

## Where to go next

- Add tests that verify imports and a minimal app smoke test.
- Pin package versions in `requirements.txt` if you need reproducible installs across machines.

## License

This project is provided without an explicit license. Add a LICENSE file if you wish to set terms.
