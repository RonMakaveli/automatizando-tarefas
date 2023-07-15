import random

# Função para gerar um número aleatório
def gerar_numero_aleatorio():
    return random.randint(1, 100)

# Função para validar a entrada do usuário
def validar_entrada_usuario(entrada):
    if not entrada.isdigit():
        print("Por favor, insira um número válido.")
        return False
    return True

# Função principal do jogo
def jogar_adivinhacao():
    print("Bem-vindo ao jogo de Adivinhação!")
    nome = input("Por favor, digite o seu nome: ")
    pontuacao = 0
    jogando = True

    while jogando:
        numero_secreto = gerar_numero_aleatorio()
        tentativas = 0
        chute = None
        acertou = False

        while chute != numero_secreto and tentativas < 5:
            chute = input("Olá, {}! Tente adivinhar o número secreto (entre 1 e 100): ".format(nome))
            
            if validar_entrada_usuario(chute):
                chute = int(chute)
                tentativas += 1
                
                if chute < numero_secreto:
                    print("Tente novamente! O número é maior.")
                elif chute > numero_secreto:
                    print("Tente novamente! O número é menor.")
                else:
                    print("Parabéns, você acertou o número secreto {} em {} tentativa(s)!".format(numero_secreto, tentativas))
                    acertou = True
                    pontuacao += 1
                    break

        if not acertou:
            print("Você atingiu o número máximo de tentativas. O número secreto era {}.".format(numero_secreto))
            pontuacao -= 1

        opcao = input("Deseja jogar novamente? (S/N): ").lower()
        if opcao != 's':
            jogando = False

    print("Obrigado por jogar! Sua pontuação final é {}.".format(pontuacao))

# Iniciar o jogo
jogar_adivinhacao()
