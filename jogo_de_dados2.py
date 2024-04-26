import random

def roll_dice(num_dice, num_rolls):
    total_score = 0
    for _ in range(num_rolls):
        roll_result = sum(random.randint(1, 6) for _ in range(num_dice))
        total_score += roll_result
        print(f"Resultado do lançamento: {roll_result}")
    print(f"Total dos lançamentos: {total_score}")

if __name__ == "__main__":
    num_rolls = int(input('Quantas vezes deseja jogar o dado?: '))
    while num_rolls <= 0:
        print("Por favor, insira um número válido maior que zero.")
        num_rolls = int(input('Quantas vezes deseja jogar o dado?: '))

    num_dice = int(input('Quantos dados você deseja jogar? '))
    while num_dice <= 0:
        print("Por favor, insira um número válido maior que zero.")
        num_dice = int(input('Quantos dados você deseja jogar? '))

    roll_dice(num_dice, num_rolls)
