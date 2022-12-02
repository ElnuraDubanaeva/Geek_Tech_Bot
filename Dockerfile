FROM python:3.10

EXPOSE 4554

RUN mkdir -p /opt/services/bot1
WORKDIR /opt/services/bot1

COPY . /opt/services/bot1

RUN pip install -r requirements.txt
CMD ["python", "/opt/services/bot/main.py"]