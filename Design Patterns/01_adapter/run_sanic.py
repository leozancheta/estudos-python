from sanic import Sanic, response
from sanic.request import Request
from adapter import request_adapter

app = Sanic(__name__)

@app.route('/usuario/<user>')
async def receber_mensagem(request: Request, user: str):
    http_request =await request_adapter(request, user)


    return response.json({'resposta': f'Olá {user}, sua mensagem foi recebida!'}, status=200)

if __name__ == '__main__':
    app.run(
            host='0.0.0.0',
            debug=True,
            port=8000,
            auto_reload=True
            )  # Sanic runs on port 8000 by default

