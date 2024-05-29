<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'];
    if ($action == 'apply_strategy') {
        $strategy = $_POST['strategy'];
        $command = escapeshellcmd("python3 trade_bot.py strategy_$strategy");
    } else {
        $command = escapeshellcmd("python3 trade_bot.py $action");
    }
    $output = shell_exec($command);
    echo "<pre>$output</pre>";
}
?>
<a href="index.php">Go back</a>
