import subprocess
import time

# Start the PHP built-in server
php_server = subprocess.Popen(['php', '-S', 'localhost:8000'])

# Give the PHP server some time to start
time.sleep(2)

print("PHP server started at http://localhost:8000")

try:
    # Keep the script running to keep the PHP server alive
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the PHP server when the script is interrupted
    php_server.terminate()
    print("PHP server stopped.")
