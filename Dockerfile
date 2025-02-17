FROM apache/airflow:2.10.5

USER airflow

WORKDIR /opt/airflow

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt