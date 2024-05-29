# Stage 1: Build the PHP application
FROM php:7.4-apache AS php-app
WORKDIR /var/www/html
COPY . /var/www/html
EXPOSE 80

# Stage 2: Build the Python trading bot
FROM python:3.9-slim AS python-app
WORKDIR /app
COPY trade_bot.py /app
RUN pip install pandas
CMD ["python", "trade_bot.py"]

# Combined image
FROM php:7.4-apache
WORKDIR /var/www/html
COPY --from=php-app /var/www/html /var/www/html
COPY --from=python-app /app/trade_bot.py /app/trade_bot.py
RUN apt-get update && apt-get install -y python3
RUN pip install pandas
EXPOSE 80
CMD ["apache2-foreground"]
