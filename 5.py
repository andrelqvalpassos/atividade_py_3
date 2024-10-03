def encontrar_pessoa_mais_alta():
    # Inicializa variáveis para armazenar os dados da pessoa mais alta
    nome_mais_alta = ""
    idade_mais_alta = 0
    altura_mais_alta = 0.0

    # Laço para ler os dados de 5 pessoas
    for i in range(1, 6):
        print(f"\nPessoa {i}:")
        
        # Lê o nome, idade e altura de cada pessoa
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura (em metros): "))

        # Verifica se a pessoa atual é mais alta do que a mais alta registrada até o momento
        if altura > altura_mais_alta:
            nome_mais_alta = nome
            idade_mais_alta = idade
            altura_mais_alta = altura

    # Exibe o nome, idade e altura da pessoa mais alta
    print("\nA pessoa mais alta é:")
    print(f"Nome: {nome_mais_alta}")
    print(f"Idade: {idade_mais_alta}")
    print(f"Altura: {altura_mais_alta:.2f} metros")

# Chama a função para executar o programa
encontrar_pessoa_mais_alta()
