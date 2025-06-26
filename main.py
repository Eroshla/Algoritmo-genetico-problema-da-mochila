from funcoes import *
from matplotlib import pyplot as plt

itens = [
    {"nome": "Notebook", "peso": 3, "valor": 2000},
    {"nome": "Livro", "peso": 1, "valor": 300},
    {"nome": "Garrafa de água", "peso": 2, "valor": 150},
    {"nome": "Fone de ouvido", "peso": 0.5, "valor": 500},
    {"nome": "Câmera", "peso": 2.5, "valor": 1500},
    {"nome": "Carregador", "peso": 0.7, "valor": 200},
    {"nome": "Jaqueta", "peso": 1.8, "valor": 800},
    {"nome": "Lanche", "peso": 1.2, "valor": 250}
]

capacidade_maxima = 7
max_geracoes = 100
max_populacao = 100
taxa_mutacao = 0.02
num_elites = 5

populacao = criar_populacao(max_populacao)
fitness = [calcular_fitness(ind, itens, capacidade_maxima) for ind in populacao]

fitness_por_geracao = []

for i in range(max_geracoes):
    print(f"\nGeração {i + 1}:")
    for j, individuo in enumerate(populacao):
        print(f"Indivíduo {j + 1}: {individuo}, Fitness: {fitness[j]}")

    fitness_por_geracao.append(fitness.copy())

    elite = selecionar_melhores(populacao, fitness, num_elites)

    casais = formar_casais(populacao, itens, capacidade_maxima)
    nova_populacao = []
    for casal in casais:
        filhos = cruzar(casal)
        nova_populacao.extend(filhos)

    nova_populacao = [mutar(ind, taxa_mutacao) for ind in nova_populacao]
    nova_fitness = [calcular_fitness(ind, itens, capacidade_maxima) for ind in nova_populacao]

    melhores = selecionar_melhores(nova_populacao, nova_fitness, max_populacao - num_elites)
    populacao = elite + melhores
    fitness = [calcular_fitness(ind, itens, capacidade_maxima) for ind in populacao]

print("\nMelhor solução encontrada:")
melhor_individuo = max(populacao, key=lambda ind: calcular_fitness(ind, itens, capacidade_maxima))
melhor_fitness = calcular_fitness(melhor_individuo, itens, capacidade_maxima)
print(f"Indivíduo: {melhor_individuo}, Fitness: {melhor_fitness}")
print("Itens selecionados:")
for i, item in enumerate(itens):
    if melhor_individuo[i] == 1:
        print(f" - {item['nome']} (Peso: {item['peso']}, Valor: {item['valor']})")


geracoes = list(range(1, max_geracoes + 1))
fitness_melhores = [max(f) for f in fitness_por_geracao]
fitness_medios = [sum(f)/len(f) for f in fitness_por_geracao]

plt.plot(geracoes, fitness_melhores, label="Melhor", marker='o')
plt.plot(geracoes, fitness_medios, label="Média", linestyle='--', marker='x')
plt.title("Evolução da Fitness")
plt.xlabel("Gerações")
plt.ylabel("Fitness")
plt.legend()
plt.grid(True)
plt.show()
