from flask import Flask
from prometheus_client import start_http_server, Counter
import time
app = Flask(__name__)
REQUEST_COUNT = Counter('app_request_total', 'Total App Requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Cloud Service Running"

if __name__ == '__main__':
    start_http_server(8000)  # Start Prometheus metrics server on port 8000
    app.run(host='0.0.0.0', port=5000)  # Start Flask app on port 5000