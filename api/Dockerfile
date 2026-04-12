FROM python:3.10-slim

WORKDIR /app

# evita cache e melhora performance
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# instala libs
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia código
COPY . .

# expõe porta
EXPOSE 8000

# roda com múltiplos workers (produção)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]