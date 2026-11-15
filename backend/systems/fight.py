from models.personagem import *



def battle():
    if marcelo_dragon.attributes['hp'] > 0 and protagonist.attributes['hp'] > 0:
        if protagonist.attributes['speed'] > marcelo_dragon.attributes['speed']:
            turno = True
            while turno:
                dano_causado = (marcelo_dragon.attributes['hp'] + marcelo_dragon.attributes['defense']) - protagonist.attributes['attack']
                if dano_causado > 0:
                    marcelo_dragon.attributes['hp'] = dano_causado
                else:
                    marcelo_dragon.attributes['hp'] = 0

                turno = False
        else:
            dano_causado = (protagonist.attributes['hp'] + protagonist.attributes['defense']) - marcelo_dragon.attributes['attack']
            if dano_causado > 0:
                protagonist.attributes['hp'] = dano_causado
            else:
                protagonist.attributes['hp'] = 0


    else:
        print('Já um ganhador')