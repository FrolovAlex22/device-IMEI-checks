FROM python:3.12.0-slim

WORKDIR /device-IMEI-checks

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
