class Personagem:
    def __init__(self,name,attack,defense,hp,speed):
        self.attributes = {
            "name": name,
            "attack": attack,
            "defense": defense,
            "hp": hp,
            "speed": speed
        }
        

protagonist = Personagem('José', 10, 10, 20, 5)
marcelo_dragon = Personagem('MarceloDragon', 20, 20,20, 10)