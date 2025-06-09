from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import datetime
import socket
import logging
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Configura logging para arquivo visível ao Promtail
log_path = os.environ.get('LOG_PATH', '/var/log/flask/app.log')
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)

@app.route('/api/v1/info')
def info():
    log_msg = f"INFO endpoint called by host={socket.gethostname()}"
    app.logger.info(log_msg)
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great, little human! Clecio',
        'deployed_on': 'test',
        'env': os.environ.get('APP_ENV', 'unknown'),
        'app_name': os.environ.get('APP_NAME', 'unknown')
    })

@app.route('/api/v1/healthz')
def health():
    app.logger.info("Health check passed.")
    return jsonify({'status': 'up'}), 200

@app.route("/api/v1/error")
def generate_error():
    try:
        raise Exception("Erro forçado para teste de observabilidade.")
    except Exception as e:
        app.logger.error(f"[500] Erro interno: {str(e)}")
        return "Erro!", 500

# Prometheus metrics estarão em /metrics
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
