# TradeLocker Bot

This repository contains a Python trading bot that implements various trading strategies using the TradeLocker API. The bot can be run locally using Docker Compose.

## Demo

A [demo](https://tradelocker-bot.onrender.com/) of the TradeLocker Bot is hosted on [Render](https://render.com/). You can access the demo and see the bot in action.

## Usage

To run the TradeLocker Bot locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ShazaGheiba/TradeLocker-Bot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd TradeLocker-Bot
   ```

3. Run the Docker containers:
   ```bash
   docker-compose up --build
   ```

4. Access the TradeLocker Bot interface in your web browser at `http://localhost:8000`.

5. Use the interface to manually initiate buy/sell orders or apply automatic trading strategies.

## TradeLocker Dashboard

You can access the [TradeLocker dashboard](https://demo.tradelocker.com) of the demo account on [OspreyFX](https://ospreyfx.com/) using the following credentials to check the orders you're creating:

- Email: shazagheiba@gmail.com
- Account Number: 641131
- Account Password: $FNRqxH8
- Server: OSP-DEMO

## Trading Strategies

The TradeLocker Bot implements the following trading strategies:

- **Moving Average Crossover Strategy**: This strategy involves using two moving averages of different time periods (e.g., 50-day and 200-day moving averages) to generate buy and sell signals. When the short-term moving average crosses above the long-term moving average, it generates a buy signal, and when the short-term moving average crosses below the long-term moving average, it generates a sell signal.

- **Bollinger Bands Strategy**: This strategy uses Bollinger Bands, which are volatility bands placed above and below a moving average. When the price touches the lower band, it may indicate an oversold condition, and when it touches the upper band, it may indicate an overbought condition.

- **Mean Reversion Strategy**: This strategy assumes that the price of an asset will eventually revert to its mean or average. It involves identifying periods of overbought or oversold conditions and taking positions to capitalize on the expected mean reversion.

- **Breakout Strategy**: This strategy aims to capitalize on the price breaking out of a defined range or level of support/resistance. It involves identifying consolidation periods and taking positions when the price breaks above or below the range.

For a detailed explanation of each strategy implementation, refer to the comments in the `trade_bot.py` file.

---
