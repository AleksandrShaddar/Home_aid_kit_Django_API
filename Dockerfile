FROM python:3.12-slim

WORKDIR /usr/scr/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY docker-entrypoint.sh /usr/local/bin

COPY . .

ENTRYPOINT ["docker-entrypoint.sh"]