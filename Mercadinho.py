#CRUD em python - mercadinho


#Listagem de produtos

produtos = []

#Localizar pelo ID

proximo_id = 1


#Função para cadastrar os produtos com o return pra não deixar avançar com nome vazio
#Funções pra colocar o preço e a quantidade usando a mesma logica

def cadastrar_produto (produtos, proximo_id):
    nome = input ("Digite o nome do produto: ")
    if nome == "":
        print("O nome não pode ficar vazio")
        return proximo_id

    preco = float(input("Digite o preço, apenas números: "))
    if preco < 0:
        print("O preço não pode ser menor que 0")
        return proximo_id

    quantidade = int(input ("Digite a quantidade do produto, apenas número inteiro: "))
    if quantidade < 0:
        print("A quantidade não pode ser menor que 0")
        return proximo_id


    produto = {
        "id": proximo_id,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)
    return proximo_id + 1


#Função de definir listagem de produtos

def listar_produtos(produtos):
    print("Lista de Produtos")
    if not produtos:
        print("Não encontrado produtos")
        return
    for listagem_prod in produtos:
        print(f"ID: {listagem_prod['id']} | Nome: {listagem_prod['nome']} | Preço: R${listagem_prod['preco']:.2f} | Quantidade: {listagem_prod['quantidade']}")


#Função de remover produtos

def remover_produto(produtos):
    print("Remover Produto")
    id_exluir = int(input("Digite o ID do produto que deseja excluir, apenas números: "))


    for produto in produtos:
        if produto["id"] == id_exluir:
            produtos.remove(produto)
            print("Produto removido com sucesso")
            return
    print("Produto não encontrado")


#Criando o menu com o While True para apresentar as opções

while True:
    print("MENU")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Remover Produto")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        proximo_id = cadastrar_produto(produtos, proximo_id)

    if opcao == "2":
        listar_produtos(produtos)

    if opcao == "3":
        remover_produto(produtos)

    if opcao == "4":
        print("Encerrando o sistema...")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção não disponivel! Tente novamente.")
