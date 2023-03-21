import random
import os
mapa = ['-'] * random.randint(5, 10)
enemies =['/']* random.randint(1,3)
for i in enemies:
    mapa[random.randint(1, len(mapa))] = '/'
mapa[0] = '↓'
pontos = 0
vida = 10
ouro = 0
while True:
    print(len(mapa))
    if vida <=0:
        print('voce perdeu! pontos:', pontos,'\n \n \n \n')
        break
    
    if len(mapa) == 1:
        print('voce venceu! pontos:', pontos,'\n \n \n \n')
        break


    print((''.join(mapa)),'\n', 'esse é o mapa','\n','voce tem: ', pontos,' pontos','\n','voce tem: ', vida,' pontos de vida','\n','voce tem: ', ouro,' peças de ouro', '\n \n \n \n')
    if input('avançar 1 casa?(y/n)') == 'y':
        if mapa[1] == '-':
            mapa.pop(0)
            mapa[0] ='↓'
            pontos += 1
            print('sala vazia!')
        elif mapa[1] == '/':
            vida -= 5
            mapa.pop(0)
            mapa[0] ='↓'
            pontos += 3
            ouro += 100
            print('você mata o monstro!')
    else:
        break

    os.system('cls' if os.name == 'nt' else 'clear')
    
input('press any key to exit')
