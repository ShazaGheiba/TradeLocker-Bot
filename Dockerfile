# Stage 1: Build the PHP application
FROM php:7.4-cli AS php-app
WORKDIR /var/www/html
COPY . /var/www/html

# Stage 2: Build the Python trading bot
FROM python:3.12-slim AS python-app
WORKDIR /app
COPY trade_bot.py /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install tradelocker

# Combined image
FROM php:7.4-cli
WORKDIR /var/www/html

# Copy PHP application
COPY --from=php-app /var/www/html /var/www/html

# Install Python and required packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy Python application and dependencies from the python-app stage
COPY --from=python-app /app /app

# Ensure the trading bot dependencies are installed
RUN pip3 install --no-cache-dir -r /app/requirements.txt
RUN pip3 install tradelocker

EXPOSE 8000

# Start PHP built-in server and the trading bot
CMD ["sh", "-c", "php -S 0.0.0.0:8000 -t /var/www/html & python3 /app/trade_bot.py"]
