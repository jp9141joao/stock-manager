# 🛒 **Gerenciador de Estoque Interativo** 📦

Um sistema interativo para gerenciar um estoque de produtos. Com ele, você pode adicionar, remover, visualizar e modificar produtos no estoque através de um menu simples e intuitivo no terminal.

---

## 🚀 **Visão Geral do Projeto**

O programa é um **Gerenciador de Estoque**, construído em Python, que permite ao usuário gerenciar uma lista de produtos com suas quantidades e atributos (preço, quantidade, nome, etc.) de forma simples e interativa.

Este projeto oferece a funcionalidade completa para:

- **Adicionar produtos ao estoque**
- **Remover produtos do estoque**
- **Modificar atributos específicos de um produto**
- **Visualizar estoque ativo**
- **Gerenciar entradas no estoque de forma intuitiva**

---

## 🛠️ **Recursos Principais**

### Funcionalidades Implementadas:
1. **Adicionar Produto ao Estoque**: Insere produtos no estoque com quantidade e preço.
2. **Remover Produtos do Estoque**: Remove um produto específico do estoque pelo código.
3. **Modificar Atributos de um Produto**: Altera atributos como nome, quantidade ou preço.
4. **Visualizar Estoque Ativo**: Lista todos os produtos em estoque com suas informações.
5. **Gerenciamento com códigos gerados automaticamente**: Evita duplicações ao adicionar produtos.
6. **Validação de entradas**: O sistema verifica entradas inválidas automaticamente.
7. **Menu intuitivo com opções claras** para navegação no programa.

---

## 💾 **Configuração**

### Pré-requisitos
- Python 3.x deve estar instalado no seu sistema.
- O ambiente deve permitir a execução de scripts Python.

---

## ▶️ **Como Executar**

1. Clone este repositório no seu ambiente local:
```bash
git clone https://github.com/seu-usuario/gerenciador-estoque.git
```

2. Navegue até a pasta do projeto:
```bash
cd gerenciador-estoque
```

3. Execute o código no terminal com:
```bash
python seu_arquivo.py
```

---

## 📚 **Funcionalidades por Menu**

Após iniciar o programa, você verá o seguinte menu no terminal:

```
* Gerenciador de Estoque *
-------------------------------------------
1- Adicionar Produto ao Estoque
2- Remover Produtos do Estoque
3- Mudar Atributos de um Item
4- Sair
```

### Opções:

1. **Adicionar Produto ao Estoque**
   - Insere um produto ao estoque com seu nome, quantidade e preço (opcional).
   
2. **Remover Produtos do Estoque**
   - Remove um produto do estoque através de seu código único gerado automaticamente.

3. **Mudar Atributos de um Item**
   - Modifica atributos específicos de um produto:
     - Nome
     - Preço
     - Quantidade

4. **Sair**
   - Encerra o programa.

---

## ⚙️ **Tecnologias Utilizadas**

- **Python 3.x**: Linguagem de programação principal.
- **Biblioteca `os`**: Para limpar a tela no console.
- **Gerenciamento de listas com dicionários**: Estrutura central de dados.

---

## 🎮 **Exemplo de Fluxo**

1. O programa exibe o menu principal.
2. O usuário escolhe **Adicionar Produto ao Estoque**.
3. O sistema solicita informações como:
   - Nome do produto
   - Quantidade disponível
   - Preço (opcional)
4. O produto é adicionado ao estoque com um código gerado automaticamente.
5. O usuário pode visualizar a lista de produtos no estoque.

---

Agora você tem um gerenciador de estoque funcional pronto para uso! 🚀 Boa sorte com seu gerenciamento! 🛒✨