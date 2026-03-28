import ssl
import logging
from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    logger.info('GET / called')
    return '<h1>Hellur...im working</h1>'

@app.route('/health')
def health():
    logger.info('GET /health called')
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('/certs/cert.pem', '/certs/key.pem')
    app.run(host='0.0.0.0', port=8443, ssl_context=context)