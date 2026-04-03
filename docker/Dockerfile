FROM apache/spark:3.5.1

USER root

RUN apt-get update && apt-get install -y \
    python3-pip \
    curl

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir -p /opt/spark/jars && \
    # JDBC SQL Server
    curl -L -o /opt/spark/jars/mssql-jdbc.jar \
    https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/12.6.1.jre11/mssql-jdbc-12.6.1.jre11.jar && \
    # Delta Lake
    curl -L -o /opt/spark/jars/delta-spark_2.12-3.1.0.jar \
    https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.1.0/delta-spark_2.12-3.1.0.jar && \
    curl -L -o /opt/spark/jars/delta-storage-3.1.0.jar \
    https://repo1.maven.org/maven2/io/delta/delta-storage/3.1.0/delta-storage-3.1.0.jar

WORKDIR /app

COPY . /app