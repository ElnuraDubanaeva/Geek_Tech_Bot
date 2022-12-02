FROM python:3.10

EXPOSE 4554

RUN mkdir -p /opt/services/bot
WORKDIR /opt/services/bot

COPY . /opt/services/bot

RUN pip install -r req.txt
CMD ["python", "/opt/services/bot/main.py"]