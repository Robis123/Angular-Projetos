from flask_restful import Resource, reqparse
from flask import jsonify
from flask_marshmallow import Marshmallow
from dao import dao

mar = Marshmallow()
dao = dao.ServicoDAO()

class ServicoSchema(mar.SQLAlchemyAutoSchema):
    class Meta:
        model = dao.tb_servico

class ServicoRest(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('idt_servico', type=int)
        self.parser.add_argument('dsc_servico', type=str)
        self.parser.add_argument('vlr_servico', type=float)
        self.parser.add_argument('tmp_servico', type=int)

    def get(self):
        args = self.parser.parse_args()
        if args['idt_servico'] is not None:
            obj = dao.readByIdt(args['idt_servico'])
            sch = ServicoSchema()
            return jsonify(sch.dump(obj))
        elif args['dsc_servico'] is not None:
            lista = dao.readByDsc(args['dsc_servico'])
            sch = ServicoSchema(many=True)
            return jsonify(sch.dump(lista))
        else:
            lista = dao.readAll()
            sch = ServicoSchema(many=True)
            return jsonify(sch.dump(lista))

    def post(self):
        args = self.parser.parse_args()
        obj = dao.tb_servico()
        for a in args:
            exec('obj.{}=args["{}"]'.format(a, a))
        dao.create(obj)
        return jsonify({'insert': obj.idt_servico})

    def put(self):
        args = self.parser.parse_args()
        obj = dao.readByIdt(args['idt_servico'])
        if obj is None:
            return jsonify({'update': 0})
        else:
            for a in args:
                if args[a] is not None:
                    exec('obj.{}=args["{}"]'.format(a, a))
            dao.update()
            return jsonify({'update': obj.idt_servico})

    def delete(self):
        args = self.parser.parse_args()
        idt = args['idt_servico']
        obj = dao.readByIdt(idt)
        if obj is None:
            return jsonify({'delete': 0})
        else:
            dao.delete(obj)
            return jsonify({'delete': idt})
