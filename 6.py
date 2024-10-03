def encontrar_maior_par():
    # Inicializa uma variável para armazenar o maior número par
    maior_par = None

    # Laço para solicitar 10 números do usuário
    for i in range(1, 11):
        numero = int(input(f"Digite o {i}º número: "))

        # Verifica se o número é par
        if numero % 2 == 0:
            # Se for o primeiro par ou maior que o par registrado, atualiza o maior par
            if maior_par is None or numero > maior_par:
                maior_par = numero

    # Verifica se foi encontrado algum número par
    if maior_par is not None:
        print(f"\nO maior número par digitado foi: {maior_par}")
    else:
        print("\nNenhum número par foi digitado.")

# Chama a função para executar o programa
encontrar_maior_par()
