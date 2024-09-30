# lista
tarefas_diarias = []

#loop
while True:
#tratamento de excação
    try:
        #usuário insere nova tarefa
        nova_tarefas_diarias = input("Informe uma nova tarefa ou 'Enter' para exibir as tarefas cadastradas: ")

         #verifica se o usuário digitou uma nova tarefa                
        if nova_tarefas_diarias:
            #insere nova tarefa na lista
            tarefas_diarias.append(nova_tarefas_diarias) 
            print("{nova_tarefas_diarias} cadastrado com sucesso!") 
            continue
        else:
            break
        continue
    except Exception as e:
        print(f"Não foi possível cadastrar nova tarefa. {e}.")

# exibe a lista
for tarefa in tarefas_diarias:
    print(tarefa)