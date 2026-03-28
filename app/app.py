from flask import Flask, jsonify # imported Flask

app = Flask(__name__) # craeted app instance 

@app.route('/')
def index():
    return '<h1>Hello from nucleus-service</h1>'

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443) # Port were running on