from quay.io/centos/centos:stream9

RUN dnf install -y python-pip
COPY src/vault-api /app
WORKDIR /app
RUN pip install .

CMD ["tail", "-f", "/dev/null"]
