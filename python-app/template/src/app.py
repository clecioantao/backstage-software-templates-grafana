from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import datetime
import socket

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/api/v1/info')
def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great, little human! Clecio',
        'deployed_on': 'kubernetes',
        'env': '${{values.app_env}}',
        'app_name': '${{values.app_name}}'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status': 'up'}), 200

@app.route("/api/v1/error")
def generate_error():
    return "Erro!", 500

# Prometheus metrics estarão em /metrics
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
