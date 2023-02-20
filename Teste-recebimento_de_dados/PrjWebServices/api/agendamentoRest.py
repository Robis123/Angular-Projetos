from flask_restful import Resource, reqparse
from flask import jsonify
from flask_marshmallow import Marshmallow
from dao import dao

mar = Marshmallow()
dao = dao.AgendamentoDAO()

class AgendamentoSchema(mar.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('idt_agendamento', 'dti_agendamento', 'cod_servico', 'cod_cliente')

class AgendamentoRest(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('idt_agendamento', type=int)
        self.parser.add_argument('dti_agendamento')
        self.parser.add_argument('cod_servico', type=int)
        self.parser.add_argument('cod_cliente', type=int)

    def get(self):
        args = self.parser.parse_args()
        if args['idt_agendamento'] is not None:
            obj = dao.readByIdt(args['idt_agendamento'])
            sch = AgendamentoSchema()
            return jsonify(sch.dump(obj))
        elif args['cod_cliente'] is not None:
            lista = dao.readByCliente(args['cod_cliente'])
            sch = AgendamentoSchema(many=True)
            return jsonify(sch.dump(lista))
        elif args['cod_servico'] is not None:
            lista = dao.readByServico(args['cod_servico'])
            sch = AgendamentoSchema(many=True)
            return jsonify(sch.dump(lista))
        else:
            lista = dao.readAll()
            sch = AgendamentoSchema(many=True)
            return jsonify(sch.dump(lista))

    def post(self):
        args = self.parser.parse_args()
        obj = dao.ta_agendamento()
        for a in args:
            exec('obj.{}=args["{}"]'.format(a, a))
        dao.create(obj)
        return jsonify({'insert': obj.idt_agendamento})

    def put(self):
        args = self.parser.parse_args()
        obj = dao.readByIdt(args['idt_agendamento'])
        if obj is None:
            return jsonify({'update': 0})
        else:
            for a in args:
                if args[a] is not None:
                    exec('obj.{}=args["{}"]'.format(a, a))
            dao.update()
            return jsonify({'update': obj.idt_agendamento})

    def delete(self):
        args = self.parser.parse_args()
        idt = args['idt_agendamento']
        obj = dao.readByIdt(idt)
        if obj is None:
            return jsonify({'delete': 0})
        else:
            dao.delete(obj)
            return jsonify({'delete': idt})

