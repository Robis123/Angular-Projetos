from flask_restful import Resource, reqparse
from flask import jsonify
from flask_marshmallow import Marshmallow
from dao import dao

mar = Marshmallow()
dao = dao.ClienteDAO()

class ClienteSchema(mar.SQLAlchemyAutoSchema):
    class Meta:
        model = dao.tb_cliente

class ClienteRest(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('idt_cliente', type=int)
        self.parser.add_argument('nme_cliente', type=str)
        self.parser.add_argument('end_cliente', type=str)
        self.parser.add_argument('tel_cliente', type=str)

    def get(self):
        args = self.parser.parse_args()
        if args['idt_cliente'] is not None:
            obj = dao.readByIdt(args['idt_cliente'])
            sch = ClienteSchema()
            return jsonify(sch.dump(obj))
        elif args['nme_cliente'] is not None:
            lista = dao.readByNme(args['nme_cliente'])
            sch = ClienteSchema(many=True)
            return jsonify(sch.dump(lista))
        else:
            lista = dao.readAll()
            sch = ClienteSchema(many=True)
            return jsonify(sch.dump(lista))

    def post(self):
        args = self.parser.parse_args()
        obj = dao.tb_cliente()
        for a in args:
            exec('obj.{}=args["{}"]'.format(a, a))
        dao.create(obj)
        return jsonify({'insert': obj.idt_cliente})

    def put(self):
        args = self.parser.parse_args()
        obj = dao.readByIdt(args['idt_cliente'])
        if obj is None:
            return jsonify({'update': 0})
        else:
            for a in args:
                if args[a] is not None:
                    exec('obj.{}=args["{}"]'.format(a, a))
            dao.update()
            return jsonify({'update': obj.idt_cliente})

    def delete(self):
        args = self.parser.parse_args()
        idt = args['idt_cliente']
        obj = dao.readByIdt(idt)
        if obj is None:
            return jsonify({'delete': 0})
        else:
            dao.delete(obj)
            return jsonify({'delete': idt})
