from quay.io/centos/centos:stream9

RUN dnf install -y python-pip
COPY src /app
WORKDIR /app
RUN pip install .

CMD ["tail", "-f", "/dev/null"]
