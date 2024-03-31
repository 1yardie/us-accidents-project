FROM apache/airflow:2.8.4

ENV AIRFLOW_HOME=/opt/airflow

# Set environment variables
# Set environment variables
ENV SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin
ENV PYTHONPATH=${SPARK_HOME}/python:${SPARK_HOME}/python/lib/py4j-0.10.9-src.zip:${PYTHONPATH}

USER root

RUN apt-get update -qq && \
    apt-get install vim -qqq -y wget && \
    apt-get clean

# git gcc g++ -qqq
COPY --chmod=600 --chown=airflow:airflow .kaggle/kaggle.json .kaggle/kaggle.json

USER airflow

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Ref: https://airflow.apache.org/docs/docker-stack/recipes.html


SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]


ARG CLOUD_SDK_VERSION=322.0.0
ENV GCLOUD_HOME=/home/google-cloud-sdk

USER root

ENV PATH="${GCLOUD_HOME}/bin/:${PATH}"

# Download and install OpenJDK 17.0.2
RUN mkdir -p /usr/lib/jvm && \
    cd /usr/lib/jvm && \
    wget -q https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/openjdk-17.0.2_linux-x64_bin.tar.gz && \
    tar -xf openjdk-17.0.2_linux-x64_bin.tar.gz && \
    rm openjdk-17.0.2_linux-x64_bin.tar.gz && \
    mv jdk-17.0.2 /usr/lib/jvm/java-17-openjdk-amd64

# Install Spark
RUN wget -qO- https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz | tar xz -C /opt/ && \
    ln -s /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} ${SPARK_HOME}

USER airflow

# Install PySpark dependencies
RUN pip install pyspark

USER root

RUN DOWNLOAD_URL="https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz" \
    && TMP_DIR="$(mktemp -d)" \
    && curl -fL "${DOWNLOAD_URL}" --output "${TMP_DIR}/google-cloud-sdk.tar.gz" \
    && mkdir -p "${GCLOUD_HOME}" \
    && tar xzf "${TMP_DIR}/google-cloud-sdk.tar.gz" -C "${GCLOUD_HOME}" --strip-components=1 \
    && "${GCLOUD_HOME}/install.sh" \
    --bash-completion=false \
    --path-update=false \
    --usage-reporting=false \
    --quiet \
    && rm -rf "${TMP_DIR}" \
    && gcloud --version

WORKDIR $AIRFLOW_HOME

COPY scripts scripts
RUN chmod +x scripts

USER $AIRFLOW_UID
