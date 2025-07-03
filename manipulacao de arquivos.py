tarefas = [

    def mostrar_menu():
        print("\n--- Menu ---")
        print =("1. adicionar tarefa")
        print("2. listar tarefas")
        print("3. remover tarefa")
        print("4. sair")
        
        def adicionar_tarefa():
            tarefa = input("digite a nova tarefa: ")
            tarefas.append(tarefa)
            print("tarefa adcionada com sucesso!")
            
            def listar_tarefas()
            if len(tarefas) -- 0:
            print("nenhuma tarefa cadastrada.")
            else:
            print("\n--- tarefas ---")
            for i, tarefa in enumerate(tarefas,1):
            print(f"{i}.{tarefa}")

            def remover_tarefa():
            listar tarefas()
            try:
            num - int(input("digite o numero da tarefa a remover:"))
            if 1 <= num <= len(tarefas):
            removida = tarefas.pop(num - 1)
            print(f"tarefa'{removida}'removida.")
            else:
            print("numero invalido.")
            except ValueError:
            print("digite um numero valido.")

            while True:
            mostrar_menu()
            opcao = input("escolha uma opcao:")
            
            if opcao =="1":
            adicionar tarefa()
            elif opcao == "2":
            listar tarefas()
            elif opcao == "3"
            remover tarefa()
            elif opcao == "4"
            print("saindo do programa...")
            break
            else:
            print("opcao invalcida.")
            

            