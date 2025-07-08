tarefas = []

def mostrar_menu():
    print("\n--- Menu ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefa():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\n--- Tarefas ---")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def remover_tarefa():
    listar_tarefa()
    try:
        num = int(input("Digite o numero da tarefa a remover: "))
        if 1 <= num <= len(tarefas):
            removida = tarefas.pop(num - 1)
            print(f"Tarefa '{removida}' removida.")
        else:
            print("Numero invalido.")
    except ValueError:
        print("Digite um numero valido.")

while True:
    mostrar_menu()
    opcao = input("Escolher uma opcao: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefa()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opcao invalida.")



    

    
    