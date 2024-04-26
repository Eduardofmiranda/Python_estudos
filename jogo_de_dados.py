
import random

def play_dice(num_rolls,qtd_dice):
    total = 0
    for i in range(num_rolls):        
        result = sum(random.randint(1, 6) for _ in range(qtd_dice))
        print('Resultado do lançamento: ', result)
        total += result
    print('Total dos lançamentos: ', total)
    
if __name__== "__main__":
    num_rolls = int(input('Quantas vezes deseja jogar o dado?: '))        
    num_dice = int(input('Quantos dados voce deseja jogar? '))
    play_dice(num_rolls, num_dice)
        

