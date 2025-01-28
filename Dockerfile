FROM python:3.12-slim

WORKDIR /app

# COPY requirements.txt /app
RUN pip install  flask

COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]

