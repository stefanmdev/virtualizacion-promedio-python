FROM python:3.11-slim
WORKDIR /app
COPY promedio.py .
CMD ["python", "promedio.py"]
