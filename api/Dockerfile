FROM python:alpine
EXPOSE 5000
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY hello.py /app
ENTRYPOINT [ "python", "hello.py" ]