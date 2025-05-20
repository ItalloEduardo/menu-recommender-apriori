from collections import defaultdict
from itertools import count
import random
import csv

# Produtos do menu fictício
produtos = [
    (1, "Neural Smash", "Hamburguer", 26.90),
    (2, "AI Bacon Boost", "Hamburguer", 28.90),
    (3, "Deep Learning Double", "Hamburguer", 32.90),
    (4, "Quantum Blend", "Hamburguer", 34.90),
    (5, "Cyber Classic", "Hamburguer", 30.90),
    (6, "Data Crunch", "Hamburguer", 33.90),
    (7, "Machine Melt", "Hamburguer", 31.90),
    (8, "Batata Frita Clássica", "Acompanhamento", 12.90),
    (9, "Batata Frita com Cheddar e Bacon", "Acompanhamento", 19.90),
    (10, "Onion Rings", "Acompanhamento", 14.90),
    (11, "Extra Queijo", "Adicional", 4.00),
    (12, "Extra Bacon", "Adicional", 4.00),
    (13, "Ovo Frito", "Adicional", 4.00),
    (14, "Maionese Trufada ou Defumada", "Adicional", 4.00),
    (15, "Refrigerante Lata", "Bebida", 6.90),
    (16, "Suco Natural", "Bebida", 8.90),
    (17, "Milkshake", "Bebida", 14.90),
    (18, "Água Mineral", "Bebida", 4.90),
]

# Mapeamento de personas (cliente_id: lista de ids de produtos mais frequentes)
personas = {
    1: [3, 9, 15, 12],           # Rafael
    2: [1, 8, 16],               # Larissa
    3: [4, 10, 14, 18],          # Marcos
    4: [2, 9, 12, 15],           # Vinícius
    5: [5, 16, 13],              # Amanda
    6: [7, 1, 8, 8, 17, 11, 15]  # Carlos
}

# Contadores e acumuladores
transacoes = []
transacao_id_counter = count(1)

# Geração das transações baseadas nas personas
for _ in range(1000):
    id_cliente = random.randint(1, 6)
    favoritos = personas[id_cliente]
    num_itens = random.randint(2, min(5, len(favoritos)))
    itens = random.sample(favoritos, num_itens)
    id_transacao = next(transacao_id_counter)
    for id_produto in itens:
        transacoes.append((id_transacao, id_cliente, id_produto))

# Geração de transações aleatórias
todos_ids_produtos = [p[0] for p in produtos]
for _ in range(1000):
    num_itens = random.randint(2, 5)
    itens = random.sample(todos_ids_produtos, num_itens)
    id_transacao = next(transacao_id_counter)
    for id_produto in itens:
        transacoes.append((id_transacao, 0, id_produto))  # cliente 0 = aleatório

# Salvar produtos.csv
produtos_path = "data/produtos.csv"
with open(produtos_path, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["id_produto", "nome_produto", "categoria", "preco"])
    writer.writerows(produtos)

# Salvar transacoes.csv
transacoes_path = "data/transacoes.csv"
with open(transacoes_path, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["id_transacao", "id_cliente", "id_produto"])
    writer.writerows(transacoes)

produtos_path, transacoes_path