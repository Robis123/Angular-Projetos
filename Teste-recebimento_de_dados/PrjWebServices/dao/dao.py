from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

class ClienteDAO:

   def __init__(self):
       # Ligação com o esquema de banco de dados
       engine = create_engine("mysql+mysqlconnector://root:hiragi7@localhost/db_work?charset=utf8mb4")

       # Mapeamento Objeto Relacional com o SQLAlchemy
       DB = automap_base()
       DB.prepare(engine, reflect=True)
       self.tb_cliente = DB.classes.tb_cliente
       self.tb_servico = DB.classes.tb_servico
       self.ta_agendamento = DB.classes.ta_agendamento

       # Trabalho com sessões da base agora Objeto-Relacional
       session_factory = sessionmaker(bind=engine)
       self.ses = session_factory()
       # -------------------------------------------------------------------------------------------------

   def create(self, obj):
       self.ses.add(obj)
       self.ses.commit()

   def readAll(self):
       objs = self.ses.query(self.tb_cliente).all()
       return objs

   def readByIdt(self, idt):
       obj = self.ses.query(self.tb_cliente).filter_by(idt_cliente=idt).first()
       return obj

   def readByNme(self, nme):
       objs = self.ses.query(self.tb_cliente).filter(self.tb_cliente.nme_cliente.ilike('%' + nme + '%')).all()
       return objs

   def update(self):
       self.ses.commit()

   def delete(self, obj):
       self.ses.delete(obj)
       self.ses.commit()

   def getSessao(self):
       return self.ses

   def __del__(self):
       self.ses.close()



class ServicoDAO:

   def __init__(self):
       # Ligação com o esquema de banco de dados
       engine = create_engine("mysql+mysqlconnector://root:hiragi7@localhost/db_work?charset=utf8mb4")

       # Mapeamento Objeto Relacional com o SQLAlchemy
       DB = automap_base()
       DB.prepare(engine, reflect=True)
       self.tb_cliente = DB.classes.tb_cliente
       self.tb_servico = DB.classes.tb_servico
       self.ta_agendamento = DB.classes.ta_agendamento

       # Trabalho com sessões da base agora Objeto-Relacional
       session_factory = sessionmaker(bind=engine)
       self.ses = session_factory()
       # -------------------------------------------------------------------------------------------------

   def create(self, obj):
       self.ses.add(obj)
       self.ses.commit()

   def readAll(self):
       objs = self.ses.query(self.tb_servico).all()
       return objs

   def readByIdt(self, idt):
       obj = self.ses.query(self.tb_servico).filter_by(idt_servico=idt).first()
       return obj

   def readByDsc(self, dsc):
       objs = self.ses.query(self.tb_servico).filter(self.tb_servico.dsc_servico.ilike('%' + dsc + '%')).all()
       return objs

   def update(self):
       self.ses.commit()

   def delete(self, obj):
       self.ses.delete(obj)
       self.ses.commit()

   def getSessao(self):
       return self.ses

   def __del__(self):
       self.ses.close()


class AgendamentoDAO:

   def __init__(self):
       # Ligação com o esquema de banco de dados
       engine = create_engine("mysql+mysqlconnector://root:hiragi7@localhost/db_work?charset=utf8mb4")

       # Mapeamento Objeto Relacional com o SQLAlchemy
       DB = automap_base()
       DB.prepare(engine, reflect=True)
       self.tb_cliente = DB.classes.tb_cliente
       self.tb_servico = DB.classes.tb_servico
       self.ta_agendamento = DB.classes.ta_agendamento

       # Trabalho com sessões da base agora Objeto-Relacional
       session_factory = sessionmaker(bind=engine)
       self.ses = session_factory()
       # -------------------------------------------------------------------------------------------------

   def create(self, obj):
       self.ses.add(obj)
       self.ses.commit()

   def readAll(self):
       objs = self.ses.query(self.ta_agendamento).all()
       return objs

   def readByIdt(self, idt):
       obj = self.ses.query(self.ta_agendamento).filter_by(idt_agendamento=idt).first()
       return obj

   def readByCliente(self, cod):
       objs = self.ses.query(self.ta_agendamento).filter_by(cod_cliente=cod).all()
       return objs

   def readByServico(self, cod):
       objs = self.ses.query(self.ta_agendamento).filter_by(cod_servico=cod).all()
       return objs

   def update(self):
       self.ses.commit()

   def delete(self, obj):
       self.ses.delete(obj)
       self.ses.commit()

   def getSessao(self):
       return self.ses

   def __del__(self):
       self.ses.close()
