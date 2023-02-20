from flask import Flask
from flask_restful import Api
from api.clienteRest import ClienteRest
from api.servicoRest import ServicoRest
from api.agendamentoRest import AgendamentoRest

app = Flask(__name__)
api = Api(app)

api.add_resource(ClienteRest, '/clientes')
api.add_resource(ServicoRest, '/servicos')
api.add_resource(AgendamentoRest, '/agendamentos')

if __name__ == '__main__':
    app.run(debug=True)
