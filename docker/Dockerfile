# build final container

FROM python:3.9.1-alpine3.12

WORKDIR /src
COPY . /src/rmeta

RUN apk update \
    && apk add --no-cache --virtual .build-deps build-base libffi-dev openssl-dev \
    && apk add --no-cache git squashfs-tools libseccomp sudo coreutils \
    && pip3 install -U pip \
    && pip3 install ./rmeta \
    && rm -rf /src/* \
    && rm -rf /root/.cache/pip/* \
    && apk del .build-deps
    
# install requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# CMD ["python"]