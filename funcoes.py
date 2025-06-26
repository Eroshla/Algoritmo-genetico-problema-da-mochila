from random import randint, choice

def criar_populacao(tamanho_populacao):
    return [[randint(0, 1) for _ in range(8)] for _ in range(tamanho_populacao)]

def calcular_fitness(individuo, itens, capacidade_maxima):
    peso_total = sum(item['peso'] for i, item in enumerate(itens) if individuo[i] == 1)
    valor_total = sum(item['valor'] for i, item in enumerate(itens) if individuo[i] == 1)

    if peso_total > capacidade_maxima:
        return 0 

    return valor_total

def formar_casais(populacao, itens, capacidade_maxima):
    casais = []
    while len(casais) < len(populacao) // 2:
        a, b = choice(populacao), choice(populacao)
        c, d = choice(populacao), choice(populacao)

        pai = a if calcular_fitness(a, itens, capacidade_maxima) > calcular_fitness(b, itens, capacidade_maxima) else b
        mae = c if calcular_fitness(c, itens, capacidade_maxima) > calcular_fitness(d, itens, capacidade_maxima) else d

        casais.append((pai, mae))
    return casais

def cruzar(casal):
    ponto_cruzamento = randint(1, len(casal[0]) - 1)
    filho1 = casal[0][:ponto_cruzamento] + casal[1][ponto_cruzamento:]
    filho2 = casal[1][:ponto_cruzamento] + casal[0][ponto_cruzamento:]
    return filho1, filho2

def mutar(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if randint(0, 100) < taxa_mutacao * 100:
            individuo[i] = 1 - individuo[i] 
    return individuo

def selecionar_melhores(populacao, fitness, n):
    indices = sorted(range(len(fitness)), key=lambda i: fitness[i], reverse=True)
    return [populacao[i] for i in indices[:n]]
