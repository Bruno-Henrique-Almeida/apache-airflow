# Airflow and Airbyte Setup Guide

## Part 1: Setting Up Airflow

### 1. Launch Airflow Services with Docker
To start Airflow services using Docker, run:
```sh
docker-compose up
```
For more details, check the official Airflow documentation:
[Apache Airflow Quick Start (Docker)](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)

### 2. Launch Airflow Locally for Development (Windows)

#### Install Python (Windows)
Download and install Python 3.9:
[Python 3.9 Download](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)

#### Install Rust
Download and install Rust:
[Install Rust](https://win.rustup.rs/x86_64)

If the Rust/Cargo path is not found, add it manually:
```powershell
$env:Path += ";$env:USERPROFILE\.cargo\bin"
```
Set Rust to the stable version:
```sh
rustup default stable-x86_64-pc-windows-msvc
```

#### Setup Python Virtual Environment
```sh
py -3.9 -m venv venv
.\venv\Scripts\activate
py -m pip install --upgrade pip
pip install -r requirements_dev.txt
pip install -r requirements.txt
```
For more details, refer to the official Airflow local installation guide:
[Apache Airflow Quick Start (Local)](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html)

## Part 2: Setting Up Airbyte

### 1. Setup and Launch Airbyte with Docker
Follow the Airbyte quickstart guide:
[Airbyte OSS Quickstart](https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart)

### 2. Choose the Correct Airbyte Binary for Your Windows Architecture
Download the appropriate version from:
[Airbyte Control Tool (abctl)](https://github.com/airbytehq/abctl/releases/download/v0.24.0/abctl-v0.24.0-windows-amd64.zip)

Unzip the file and install using PowerShell (for low-resource systems, enable low-resource mode):
```powershell
.\abctl.exe local install --low-resource-mode
```

### 3. Retrieve Local Credentials
For authentication details, refer to:
[Airbyte Authentication Docs](https://docs.airbyte.com/deploying-airbyte/integrations/authentication)

To fetch credentials locally:
```sh
.\abctl.exe local credentials
```

### 4. Configure Airbyte in Airflow
To integrate Airbyte with Airflow, follow the connection setup guide:
[Airflow Airbyte Provider Connection](https://airflow.apache.org/docs/apache-airflow-providers-airbyte/stable/connections.html)
