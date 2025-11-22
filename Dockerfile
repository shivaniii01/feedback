FROM python:3.8-slim
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
ExPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]