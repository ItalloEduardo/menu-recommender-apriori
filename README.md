# 🍽️ IntelliMenu: Recomendador de Cardápio com IA

Este projeto aplica o algoritmo **Apriori** para recomendar itens de cardápio com base em pedidos anteriores. Ele foi desenvolvido como parte de um trabalho acadêmico e simula um sistema de **recomendações inteligentes** utilizando regras de associação em Python, via Google Colab.

---

## 📌 Objetivo

O objetivo é treinar uma IA que sugira produtos frequentemente comprados em conjunto com outros, como em sistemas de "clientes que compraram x também compraram y". Isso ajuda a melhorar a experiência do cliente e aumenta o ticket médio de pedidos, potencializando vendas.

---

## 🧠 Algoritmo Utilizado

- **Apriori** (via `apyori`)
- Geração de **regras de associação** com suporte, confiança e lift

---

## 📁 Estrutura do Projeto
📂 intellimenu/
├── recomenda_lanches.ipynb # Notebook principal com todo o processamento
├── gerar_csv.py # Função que gera a tabela de pedidos para uso como Base de Dados 
├── README.md # Documentação do projeto
├── 📂 tabelas/
    ├── pedidos.csv # Histórico de 2000 pedidos anteriores
    ├── cardapio.csv # Catálogo completo de produtos disponíveis


---

## 🚀 Como Executar

1. Faça upload do notebook no [Google Colab](https://colab.research.google.com)
2. Faça upload dos arquivos `pedidos.csv` e `cardapio.csv` no ambiente Colab
3. Execute as células em sequência
4. Insira produtos de entrada e veja as recomendações geradas pela IA

---

## 📊 Exemplo de Saída

Se o carrinho contém: `[2, 12]`  # ['AI Bacon Boost', 'Extra Bacon']
A IA pode recomendar: `[9, 3, 15]`  # ['Batata Frita com Cheddar e Bacon', 'Deep Learning Double', 'Refrigerante Lata']

> *Analisando recomendações para o carrinho: [2, 12]
>    Recomendação potencial adicionada: 9 (Lift: 1.6593)
>    Recomendação potencial adicionada: 3 (Lift: 1.8593)
>    Recomendação potencial adicionada: 9 (Lift: 2.1312)
>    Recomendação potencial adicionada: 15 (Lift: 1.7910)
>    Recomendação potencial adicionada: 9 (Lift: 2.9939)*
> *Recomendações para [2, 12]: [9, 3, 15]*

> *Com base em compras anteriores que frequentemente associaram esses itens.*

---

## 📦 Bibliotecas Utilizadas

- `pandas`
- `apyori`
- `numpy`

---

## 🧪 Dataset

- `pedidos.csv`: Cada linha representa um pedido (uma transação).
- `cardapio.csv`: Contém o nome dos produtos e suas categorias (opcional para visualização adicional).
