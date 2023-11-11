# syntax=docker/dockerfile:1.2
FROM python:3.9
# put you docker configuration here

RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt

ENV APP_HOME /root
WORKDIR $APP_HOME
COPY /challenge $APP_HOME/challenge

EXPOSE 8000
CMD ["uvicorn", "challenge:app", "--host", "0.0.0.0", "--port", "8000"]