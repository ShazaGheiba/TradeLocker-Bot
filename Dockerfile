FROM python:3.12

WORKDIR /app

# Install PHP
RUN apt-get update && apt-get install -y php

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["php", "-S", "0.0.0.0:8000"]
