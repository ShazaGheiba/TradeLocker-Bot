# trade_bot.py
from tradelocker import TLAPI
import pandas as pd
import sys
import time


def moving_average_crossover_strategy(data, short_window, long_window):
    data['short_ma'] = data['close'].rolling(window=short_window).mean()
    data['long_ma'] = data['close'].rolling(window=long_window).mean()
    data['signal'] = 0
    data.loc[data['short_ma'] > data['long_ma'], 'signal'] = 1
    data.loc[data['short_ma'] < data['long_ma'], 'signal'] = -1

    print("\n=== Moving Average Crossover Strategy Debug Info ===")
    print("\nShort-Term Moving Average:")
    print(list(data['short_ma'].tail()))
    print("\nLong-Term Moving Average:")
    print(list(data['long_ma'].tail()))
    print("\nClose Prices:")
    print(list(data['close'].tail()))
    print("\nSignals:")
    print(list(data['signal'].tail()))
    print("===============================================\n")

    return data


def bollinger_bands_strategy(data, window, num_std):
    data['rolling_mean'] = data['close'].rolling(window=window).mean()
    data['rolling_std'] = data['close'].rolling(window=window).std()
    data['upper_band'] = data['rolling_mean'] + (data['rolling_std'] * num_std)
    data['lower_band'] = data['rolling_mean'] - (data['rolling_std'] * num_std)
    data['signal'] = 0
    data.loc[data['close'] < data['lower_band'], 'signal'] = 1
    data.loc[data['close'] > data['upper_band'], 'signal'] = -1

    print("\n=== Bollinger Bands Strategy Debug Info ===")
    print("\nRolling Mean:")
    print(list(data['rolling_mean'].tail()))
    print("\nRolling Std Dev:")
    print(list(data['rolling_std'].tail()))
    print("\nUpper Band:")
    print(list(data['upper_band'].tail()))
    print("\nLower Band:")
    print(list(data['lower_band'].tail()))
    print("\nClose Prices:")
    print(list(data['close'].tail()))
    print("\nSignals:")
    print(list(data['signal'].tail()))
    print("==========================================\n")

    return data


def mean_reversion_strategy(data, window, num_std):
    data['rolling_mean'] = data['close'].rolling(window=window).mean()
    data['rolling_std'] = data['close'].rolling(window=window).std()
    data['upper_bound'] = data['rolling_mean'] + (data['rolling_std'] * num_std)
    data['lower_bound'] = data['rolling_mean'] - (data['rolling_std'] * num_std)
    data['signal'] = 0
    data.loc[data['close'] > data['upper_bound'], 'signal'] = -1
    data.loc[data['close'] < data['lower_bound'], 'signal'] = 1

    print("\n=== Mean Reversion Strategy Debug Info ===")
    print("\nRolling Mean:")
    print(list(data['rolling_mean'].tail()))
    print("\nRolling Std Dev:")
    print(list(data['rolling_std'].tail()))
    print("\nUpper Bound:")
    print(list(data['upper_bound'].tail()))
    print("\nLower Bound:")
    print(list(data['lower_bound'].tail()))
    print("\nClose Prices:")
    print(list(data['close'].tail()))
    print("\nSignals:")
    print(list(data['signal'].tail()))
    print("==========================================\n")

    return data


def breakout_strategy(data, window):
    data['rolling_high'] = data['high'].rolling(window=window).max()
    data['rolling_low'] = data['low'].rolling(window=window).min()
    data['signal'] = 0
    data.loc[data['close'] > data['rolling_high'], 'signal'] = 1
    data.loc[data['close'] < data['rolling_low'], 'signal'] = -1

    print("\n=== Breakout Strategy Debug Info ===")
    print("\nRolling High:")
    print(list(data['rolling_high'].tail()))
    print("\nRolling Low:")
    print(list(data['rolling_low'].tail()))
    print("\nClose Prices:")
    print(list(data['close'].tail()))
    print("\nSignals:")
    print(list(data['signal'].tail()))
    print("==========================================\n")

    return data


def execute_trade(action):
    tl = TLAPI(environment="https://demo.tradelocker.com", username="shazagheiba@gmail.com", password="$FNRqxH8",
               server="OSP-DEMO")
    symbol_name = "BTCUSD"

    instrument_id = tl.get_instrument_id_from_symbol_name(symbol_name)
    side = "buy" if action == "buy" else "sell"

    order_id = tl.create_order(instrument_id, quantity=0.01, side=side, type_="market")
    if order_id:
        print(f"Placed {side} order with id {order_id}, sleeping for 2 seconds.")
        time.sleep(2)
        tl.close_position(order_id)
        print(f"Closed {side} order with id {order_id}.")
    else:
        print(f"Failed to place {side} order.")


def apply_strategy(strategy):
    tl = TLAPI(environment="https://demo.tradelocker.com", username="shazagheiba@gmail.com", password="$FNRqxH8",
               server="OSP-DEMO")
    symbol_name = "BTCUSD"

    instrument_id = tl.get_instrument_id_from_symbol_name(symbol_name)
    price_history = tl.get_price_history(instrument_id, resolution="1D", start_timestamp=0, end_timestamp=0,
                                         lookback_period="1Y")
    data = pd.DataFrame(price_history)
    data.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']

    if strategy == "moving_average_crossover":
        strategy_data = moving_average_crossover_strategy(data, short_window=50, long_window=200)
        explanation = ("A buy signal is generated when the short-term moving average crosses above the long-term "
                       "moving average, indicating a bullish trend.\nA sell signal is generated when the short-term "
                       "moving average crosses below the long-term moving average, indicating a bearish trend.")
    elif strategy == "bollinger_bands":
        strategy_data = bollinger_bands_strategy(data, window=20, num_std=2)
        explanation = ("A buy signal is generated when the closing price falls below the lower Bollinger Band, "
                       "indicating an oversold condition.\nA sell signal is generated when the closing price rises "
                       "above the upper Bollinger Band, indicating an overbought condition.")
    elif strategy == "mean_reversion":
        strategy_data = mean_reversion_strategy(data, window=20, num_std=1.5)
        explanation = ("A buy signal is generated when the closing price falls below the lower bound, indicating that "
                       "the price may revert to the mean.\nA sell signal is generated when the closing price rises "
                       "above the upper bound, indicating that the price may revert to the mean.")
    elif strategy == "breakout":
        strategy_data = breakout_strategy(data, window=20)
        explanation = ("A buy signal is generated when the closing price rises above the rolling high, indicating a "
                       "breakout to the upside.\nA sell signal is generated when the closing price falls below the "
                       "rolling low, indicating a breakout to the downside.")
    else:
        print("Unknown strategy:", strategy)
        return

    latest_signal = strategy_data['signal'].iloc[-1]

    print(f"Latest signal for {strategy}: {latest_signal}")
    print("\nStrategy Explanation:")
    print(explanation)

    if latest_signal == 1:
        execute_trade('buy')
    elif latest_signal == -1:
        execute_trade('sell')
    else:
        print("No trade signal generated.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action in ["buy", "sell"]:
            execute_trade(action)
        elif action.startswith("strategy_"):
            strategy = "_".join(action.split("_")[1:])
            apply_strategy(strategy)
        else:
            print("Unknown action:", action)
    else:
        print("No action provided.")
