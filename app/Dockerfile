FROM python:3.8
WORKDIR /tg_bot
COPY . /tg_bot
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
#CMD ["python3", "-m", "http.server", "-d", "/tg_bot", "80"]


