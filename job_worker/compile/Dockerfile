FROM openjdk:11-jdk

RUN apt-get update && \
    apt-get install -y python3.10 python3-pip && \
    wget https://services.gradle.org/distributions/gradle-8.8-bin.zip -P /tmp && \
    unzip -d /opt/gradle /tmp/gradle-8.8-bin.zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install --upgrade pip

ENV PATH $PATH:/opt/gradle/gradle-8.8/bin

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "compile_worker.py"]