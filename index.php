<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeLocker Bot</title>
    <style>
        .section {
            margin-bottom: 20px;
        }
        .label {
            font-weight: bold;
            display: block;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>TradeLocker Bot</h1>

    <form method="POST" action="trade.php">
        <div class="section">
            <span class="label">Manual Sell/Buy</span>
            <button type="submit" name="action" value="buy">Buy</button>
            <button type="submit" name="action" value="sell">Sell</button>
        </div>

        <div class="section">
            <span class="label">Automatic Sell/Buy Strategies</span>
            <label for="strategy">Select Strategy:</label>
            <select name="strategy" id="strategy">
                <option value="moving_average_crossover">Moving Average Crossover</option>
                <option value="bollinger_bands">Bollinger Bands</option>
                <option value="mean_reversion">Mean Reversion</option>
                <option value="breakout">Breakout</option>
            </select>
            <button type="submit" name="action" value="apply_strategy">Apply Strategy</button>
        </div>
    </form>
</body>
</html>
