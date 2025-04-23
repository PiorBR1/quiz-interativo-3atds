def executar_quiz(perguntas):
    # Executa o quiz com as perguntas fornecidas, permitindo que o usuário escolha a dificuldade.
    print("Seja Bem-Vindo ao nosso quiz de Futebol, sera que você sabe realmente tudo?!")

    # Exibe as opções de dificuldade para o usuário escolher
    print("Primeiramente escolha a dificuldade do quiz:")
    print("1. Fácil")
    print("2. Médio")
    print("3. Difícil")
    
    # ele coleta a entrada do usuário para a dificuldade
    dificuldade = input("Digite o número da dificuldade (1-3): ")
    
    # Mapeia a entrada do usuário para o nível correspondente
    if dificuldade == "1":
        nivel = "facil"
    elif dificuldade == "2":
        nivel = "medio"
    elif dificuldade == "3":
        nivel = "dificil"  
    else:
        # Informa que a dificuldade é inválida e encerra a função
        print("Dificuldade inválida")
        return

    pontuacao = 0  # Inicializa a pontuação do usuário
    perguntas_nivel = perguntas[nivel]  # Seleciona as perguntas com base na dificuldade escolhida

    # Itera sobre cada pergunta na lista de perguntas do nível escolhido
    for pergunta in perguntas_nivel:
        print(pergunta["pergunta"])  # Exibe a pergunta
        
        
        # Exibe as opções de resposta numeradas
        for i, opcao in enumerate(pergunta["opcoes"], start=1):
            print(f"{i}. {opcao}")
        
        # Solicita a resposta do usuário
        resposta_usuario = input("Escolha a opção correta (1-4): ")
        
        # Validação da resposta
        if resposta_usuario.isdigit() and 1 <= int(resposta_usuario) <= 4:
            # Obtém a resposta do usuário com base na opção escolhida
            resposta_usuario = pergunta["opcoes"][int(resposta_usuario) - 1]
            # Verifica se a resposta do usuário está correta
            if resposta_usuario == pergunta["resposta"]:
                print("Acertou, Bora pra próxima!")  # Informa que a resposta está correta
                pontuacao += 1  # Incrementa a pontuação
            else:
                # Informa que a resposta está incorreta e exibe a resposta correta
                print(f"Putz, infelizmente você errou, A resposta correta era: {pergunta['resposta']}")
        else:
            # Informa que a opção escolhida é inválida
            print("Opção inválida! Por favor, escolha um número entre 1 e 4.")
            
    # Exibe a pontuação final do usuário
    print(f"Sua pontuação final é: {pontuacao} de {len(perguntas_nivel)}")
