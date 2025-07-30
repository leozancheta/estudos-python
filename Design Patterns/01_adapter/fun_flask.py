from flask import Flask, jsonify, request
from adapter import request_adapter

app = Flask(__name__)

@app.route('/usuario/<user>', methods=['POST'])
def receber_mensagem(user):
    http_request = request_adapter(request)

    print(http_request)

    return jsonify({'resposta': f'Olá {user}, sua mensagem foi recebida!'}), 200

if __name__ == '__main__':
    app.run(debug=True)