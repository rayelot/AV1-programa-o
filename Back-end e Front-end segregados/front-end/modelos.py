from configuracoes import *

class Personagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    vida = db.Column(db.Integer)
    ataque = db.Column(db.Integer)
    defesa = db.Column(db.Integer)
    pacto = db.Column(db.String(254))

    def __str__(self):
        return str(self.id) + ") " + self.nome + ", " + str(self.vida) + ", " + str(self.ataque) + ", " + str(self.defesa) + ", " + self.pacto  + "."

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "vida": self.vida,
            "ataque": self.ataque,
            "defesa": self.defesa,
            "pacto": self.pacto
        }
