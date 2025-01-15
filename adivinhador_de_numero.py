import random

numero_secreto = random.randint(1, 10)

tentativas_restantes = 5

print (f"Você tem {tentativas_restantes} chances para adivinhar um número entre 1 e 10")

while tentativas_restantes > 0:
    tentativa = int(input("Qual seu chute? "))

    if tentativa == numero_secreto:
        print("Boa, você acertou!")
        break
    elif tentativa > numero_secreto:
        print(f"Não era esse, o número secreto é MENOR que {tentativa}")
    else:
        print(f"Osso, você errou! O número secreto é MAIOR que {tentativa}.")

    tentativas_restantes -= 1
    print(f"Você ainda tem {tentativas_restantes} tentativas pra tentar acertar, acerta aí pelo amor de Deus! ")

    if tentativas_restantes == 0:
        print(f"Puuutz, deu mole nessa, hein!? o número certo era {numero_secreto}, quero ver mandar melhor na próxima!")