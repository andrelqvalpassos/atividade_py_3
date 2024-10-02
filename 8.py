# Função para calcular o bônus de natal dos clientes
def calcular_bonus():
    # Entrada: número de clientes
    num_clientes = int(input("Digite o número de clientes na loja: "))
    
    # Inicializando contadores
    clientes_aptos = 0
    total_bonus = 0

    # Loop para processar cada cliente
    for i in range(1, num_clientes + 1):
        print(f"\nCliente {i}:")
        nome = input("Digite o nome do cliente: ")
        valor_compras = float(input("Digite o valor total das compras no ano (R$): "))

        # Verificação se o cliente tem direito ao bônus
        if valor_compras >= 2000.00:
            bonus = valor_compras * 0.15  # 15% de bônus
            clientes_aptos += 1
            total_bonus += bonus
            print(f"{nome} é apto para receber o bônus de R$ {bonus:.2f}.")
        else:
            print(f"{nome} não é apto para receber o bônus.")
    
    # Exibição do resultado final
    print(f"\nTotal de clientes que ganharam o bônus: {clientes_aptos}")
    print(f"Total em bônus pagos: R$ {total_bonus:.2f}")

# Chamada da função para executar o programa
calcular_bonus()
