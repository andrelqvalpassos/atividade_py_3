# Função para analisar o desempenho de vendas
def analisar_vendas():
    # Lista para armazenar as vendas de cada mês
    vendas_mensais = []
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    # Entrada dos valores de vendas mensais
    for i in range( 12):
        venda = float(input(f"Digite o valor de vendas para {meses[i]}: "))
        vendas_mensais.append(venda)

    # Cálculo do total de vendas no ano
    total_vendas = sum(vendas_mensais)

    # Cálculo da média de vendas no ano
    media_vendas = total_vendas / 12

    # Encontrando o mês com a maior e a menor venda
    maior_venda = max(vendas_mensais)
    menor_venda = min(vendas_mensais)
    mes_maior_venda = meses[vendas_mensais.index(maior_venda)]
    mes_menor_venda = meses[vendas_mensais.index(menor_venda)]

    # Exibição dos resultados
    print("\nAnálise do desempenho de vendas:")
    print(f"Total de vendas no ano: R$ {total_vendas:.2f}")
    print(f"Média de vendas mensais: R$ {media_vendas:.2f}")
    print(f"O mês com a maior venda foi {mes_maior_venda} com R$ {maior_venda:.2f}")
    print(f"O mês com a menor venda foi {mes_menor_venda} com R$ {menor_venda:.2f}")

# Chamada da função para executar o programa
analisar_vendas()
