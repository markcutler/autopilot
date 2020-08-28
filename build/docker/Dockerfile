FROM ubuntu:20.04

RUN apt update \
  && apt install -y --no-install-recommends \
      ansible \
  && apt clean \
  && rm -rf /var/lib/apt/lists/*

COPY *.yaml /tmp

RUN ansible-playbook /tmp/playbook.yaml