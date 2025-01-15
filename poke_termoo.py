from colorama import Fore, Style
import random
from Nomes_Pokemon import palavras

palavra_secreta = random.choice(palavras)
tentativas = 6 

print("Bem vindo ao Pokérmoo!")
print(f"O pokémon em questão tem {len(palavra_secreta)} letras em seu nome")

for tentativa in range(tentativas):

    palpite = input(f"Tentativa {tentativa + 1}/{tentativas}: ").lower()

    if len(palpite) != len(palavra_secreta):
        print(f"Seu palpite precisa ter {len(palavra_secreta)} letras!")
        continue

    resultado = ""
    for posicao_letra in range(len(palavra_secreta)):
        if palpite[posicao_letra] == palavra_secreta[posicao_letra]:
            resultado += Fore.GREEN + palpite[posicao_letra] + Style.RESET_ALL
        elif palpite[posicao_letra] in palavra_secreta:
            resultado += Fore.YELLOW + palpite[posicao_letra] + Style.RESET_ALL
        else:
            resultado += Fore.RED + palpite[posicao_letra] + Style.RESET_ALL

    print ("Resultado: ", resultado)

    if palpite == palavra_secreta:
        print(Fore.GREEN + "Parabéns, você acertou!" + Style.RESET_ALL)
        break

else:
      print(Fore.RED + f"Que pena, você perdeu! A palavra secreta era: {palavra_secreta}!" + Style.RESET_ALL)
      