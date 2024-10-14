tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)

def listar_tarefas():
    for i, tarefa in enumerate(tarefas):
        print(f"{i+1}. {tarefa}")

def remover_itens_lista(lista):
    """
    Função para remover itens de uma lista de forma interativa.

    Args:
        lista: A lista de itens.
    """

    while True:

        print("Itens da lista:")
        for i, item in enumerate(lista):
            print(f"{i+1}. {item}")


        indice = input("Digite o número do item que deseja remover (ou 0 para sair): ")


        if indice == '0':
            break


        try:
            indice = int(indice) - 1
            if 0 <= indice < len(lista):
                del lista[indice]
                print("Item removido com sucesso!")
            else:
                print("Índice inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

while True:
    print("\nOpções:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4 Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == '2':
        listar_tarefas()
    elif opcao == '3':
        remover_itens_lista(tarefas)
    elif opcao == '4':
        break
    else:
        print("Opção inválida.")


