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

if __name__=="__main__":
    if os.path.exists(arquivo_bd):
        os.remove(arquivo_bd)

    db.create_all()

    p1 = Personagem(nome="Andre", vida=20, ataque=5, 
    defesa=13,pacto="N/D")

    p2 = Personagem(nome="Siegward", vida=50, ataque=10, 
    defesa=15, pacto="pacto de catarina")

    p3 = Personagem(nome="Lautrec", vida=15, ataque=35,
    defesa=0, pacto="Ordem dos assassinos")

    p4 = Personagem(nome="Logan", vida=7, ataque=60,
    defesa=0, pacto="Ordem da magia")

    p5 = Personagem(nome="Queelag", vida=160, ataque=40,
    defesa=30, pacto="Bruxas do caos")

    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.commit()

    print(p2)
    print(p1.json())
    print(p2.json())