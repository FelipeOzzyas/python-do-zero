import random

palavras = ["amada", "bucha", "durma", "ungir", "cueca"]

palavra_secreta = random.choice(palavras)

print("Bem vindo ao jogo de adivinhação!")

palpite = input(f"Adivinhe uma palavra com {len(palavra_secreta)} letras: ")

while len(palpite) != len(palavra_secreta):
    print("Seu palpite não tem o número de letras correto!")
    palpite = input(f"Adivinhe uma palavra com {len(palavra_secreta)} letras: ")

while palpite != palavra_secreta:
    resultado = ""
    for posicao_letra in range(len(palavra_secreta)):
        if palpite[posicao_letra] == palavra_secreta[posicao_letra]:
            resultado += f"[{palpite[posicao_letra]}]"
        elif palpite[posicao_letra] in palavra_secreta:
            resultado += "[?]"
        else:
            resultado += "[ ]"
    print ("Resultado: ", resultado)
    palpite = input(f"Adivinhe uma palavra com {len(palavra_secreta)} letras: ")

print("Parabéns, você acertou!")