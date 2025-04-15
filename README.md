
# Projeto: Estrutura de Dados com Árvores Binária de Busca (BST) e AVL

Este projeto tem como objetivo implementar, comparar e analisar o desempenho das estruturas de dados **Árvore Binária de Busca (BST)** e **Árvore AVL**, utilizando a base pública `dados_abertos_ogu_2024122.csv`, referente ao Programa Minha Casa, Minha Vida (MCMV).

---

## 🔍 Sobre o Conjunto de Dados

A base de dados disponibilizada pelo Ministério das Cidades contém informações sobre os empreendimentos e unidades habitacionais contratadas pelo Programa Minha Casa, Minha Vida com recursos do **Orçamento Geral da União (OGU)**. Os dados abrangem:

- Identificação do município (UF, código IBGE)
- Código e nome do empreendimento (`cod_operacao`)
- Modalidade de financiamento (como FAR – Fundo de Arrendamento Residencial)
- Nome do agente financeiro
- Data de assinatura e situação
- Região geográfica

Esta base é atualizada periodicamente e tem como objetivo permitir análises relacionadas à habitação de interesse social no Brasil.

---

## 📁 Estrutura dos Dados (Exemplo)

| data_referencia | cod_ibge | txt_nome_municipio | txt_sigla_uf | txt_regiao   | dt_assinatura | cod_operacao | txt_nome_empreendimento           | txt_nome_agente_financeiro | txt_modalidade |
|-----------------|----------|--------------------|---------------|--------------|----------------|---------------|----------------------------------|-----------------------------|----------------|
| 31/12/2024      | 520.140  | Aparecida de Goiânia | GO           | Centro-Oeste | 05/08/2009     | 16517361      | RES AGUAS CLARAS                | CAIXA                       | FAR            |
| 31/12/2024      | 330.330  | Niterói             | RJ           | Sudeste       | 23/07/2007     | 18283735      | VARZEA DAS MOCAS I. RESIDENCIAL | CAIXA                       | FAR            |
| 31/12/2024      | 330.455  | Rio de Janeiro      | RJ           | Sudeste       | 22/06/2007     | 19095100      | VIVENDAS DAS ANDORINHAS         | CAIXA                       | FAR            |

A coluna **`cod_operacao`** foi escolhida como chave para as árvores.

---

## 🔍 Base de Dados

A base utilizada é composta por **18.532 registros únicos** de operações governamentais, identificadas pela coluna `cod_operacao`, utilizada como **chave** para a construção das árvores.

- Total de elementos únicos: `18.532`
- Coluna utilizada como chave: `cod_operacao`
- Arquivo: `dados_abertos_ogu_2024122.csv`

---

---

## ⚙️ Implementação

Foram implementadas duas estruturas:
- `BST` (Árvore Binária de Busca comum, sem balanceamento)
- `AVLTree` (Árvore Binária de Busca auto-balanceada)

A linguagem utilizada foi **Python**, e as árvores foram construídas com classes personalizadas que suportam inserção, busca e cálculo de altura.

---

## 📊 Resultados Comparativos

| Métrica                 | BST        | AVL        |
|-------------------------|------------|------------|
| Elementos inseridos     | 18.532     | 18.532     |
| Tempo de inserção       | 5.55 s     | 1.90 s     |
| Tempo de busca (100)    | 0.016 s    | 0.000 s    |
| Altura da árvore        | 1761       | 17         |

---

### 📈 Gráficos

#### Tempo de Inserção + Busca
![Gráfico de Tempo](grafico_tempo_insercao_busca.png)

#### Altura das Árvores
![Gráfico de Altura](grafico_altura_arvores.png)

---

## 📚 Documentação Técnica

### i) Método

- **Equipamento Utilizado:**  
  Notebook com processador Ryzen 7 2700 com de 32GB RAM.

- **Massa de Dados:**  
  Arquivo `dados_abertos_ogu_2024122.csv`, contendo 18.532 registros únicos.

- **Chave Utilizada:**  
  `cod_operacao` – um identificador textual de cada operação.

- **Algoritmos Utilizados:**  
  - Árvore Binária de Busca (BST)
  - Árvore AVL (balanceada automaticamente)

- **Linguagem de Programação:**  
  Python 3.11  
  Bibliotecas: `pandas`, `matplotlib`, `time`, `random`

---

### ii) Gráficos de Comparação de Tempos de Busca

Os gráficos apresentados mostram claramente a superioridade da AVL em termos de altura e tempo de execução.

---

### iii) Análise Crítica da Eficiência

- A AVL foi mais eficiente em **tempo de busca** e **estrutura balanceada**.
- A BST apresentou comportamento próximo ao **pior caso** com altura de 1761, prejudicando buscas.
- A AVL manteve altura próxima a `log₂(18532) ≈ 14.2`.

---

### iv) Análise Assintótica vs Tempos Obtidos

| Estrutura | Complexidade Inserção | Complexidade Busca | Tempo Real de Busca |
|-----------|------------------------|---------------------|----------------------|
| **BST**   | O(log n) média / O(n) pior caso | O(log n) média / O(n) pior caso | 0.0167 s |
| **AVL**   | O(log n)               | O(log n)            | 0.0000 s |

---

### v) Discussão: Alterando a Chave de Busca / Como buscar por outros campos além da chave?

Como as Árvores BST e AVL são organizadas em torno de uma **chave primária específica** (`cod_operacao`), buscas por outros campos exigem abordagens alternativas:

### 1. Busca Linear na Árvore
Percorrer todos os nós da árvore verificando o campo desejado:

```python
def buscar_por_estado(node, estado, resultados):
    if node is None:
        return
    if node.data['txt_sigla_uf'] == estado:
        resultados.append(node.data)
    buscar_por_estado(node.left, estado, resultados)
    buscar_por_estado(node.right, estado, resultados)
```

Essa abordagem é O(n), pois percorre todos os nós — mas é funcional.

### 2. Nova Árvore com Outra Chave
Criar uma nova árvore AVL ou BST com outra coluna como chave, caso buscas por esse campo sejam frequentes.

Caso a chave utilizada não fosse `cod_operacao`, mas sim:

- `orgao_superior`: exigiria tratamento de valores repetidos.
- `valor_pago`: possível desbalanceamento com dados ordenados.
- `funcao`: ideal para agrupamentos e análise temática.

Cada tipo de dado afetaria diretamente:
- A **ordenação interna** das árvores
- O **balanceamento natural**
- A **eficiência na busca**

Conclusão: **a escolha da chave é decisiva** para a performance das estruturas de dados.

---

## 🛠️ Ambiente e Execução

- **Linguagem:** Python 3.11
- **Bibliotecas:** pandas, matplotlib
- **Ambiente de teste:** CPU AMD Ryzen 7 2700, 32GB RAM
- **Execução local com arquivo `.csv` contendo os dados**

---
