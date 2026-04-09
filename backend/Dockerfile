FROM python:3.11-slim

# не запускаемся от root
RUN useradd -m backendUser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN chown -R backendUser:backendUser /app

USER backendUser

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]