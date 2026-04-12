FROM apache/spark:3.5.1

USER root

RUN apt-get update && apt-get install -y \
    python3-pip \
    curl

COPY pipeline_spark/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# jars do Spark / JDBC
COPY pipeline_spark/jars/ /opt/spark/jars/

WORKDIR /app
COPY pipeline_spark/ /app