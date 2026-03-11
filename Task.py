# Criar lista de tarefas vazia

list_task = []

while True:

    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. Show Task")
    print ("3. remove Task")
    print ("4. Exit the program")  

    choice = input("Choice: ")

    if choice == '1':
         task = input("New task: ")
         list_task.append(task)
    elif choice == '2':
         print ("n--- Tasks ---")
         for i, t in enumerate(list_task, 1):
              print(f"{i}. {t}")
    elif choice == '3':
         if not list_task:
              print("Empty List!")
              continue
         for i, t in enumerate(list_task, 1): print(f"{i}. {t}")
         indice = int(input("Número da tarefa a remover: ")) - 1
         if 0 <= indice < len(list_task):
              list_task.pop(indice)
         else:
              print("Number Invalid.")
    elif choice == '4':
         break
    else:
         print("Option Invalid.")