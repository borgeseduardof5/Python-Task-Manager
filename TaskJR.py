import os

NOME_ARQUIVO = "tarefas.txt"

def carregar_tarefas():
    if not os.path.exists(NOME_ARQUIVO):
        return []
    tarefas = []
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            # Dividimos a linha pelo separador '|'
            partes = linha.strip().split(" | ")
            if len(partes) == 2:
                nome, status = partes
                # Convertemos a string 'True'/'False' de volta para booleano
                tarefas.append({"nome": nome, "concluida": status == "True"})
    return tarefas

def salvar_tarefas(tarefas):
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
        for t in tarefas:
            arquivo.write(f"{t['nome']} | {t['concluida']}\n")

def mostrar_tarefas(tarefas):
    if not tarefas:
        print("\nLista vazia.")
    else:
        print("\n--- SUAS TAREFAS ---")
        for i, t in enumerate(tarefas, 1):
            # Operador ternário para o ícone de status
            status = "[X]" if t['concluida'] else "[ ]"
            print(f"{i}. {status} {t['nome']}")

def gerenciar():
    tarefas = carregar_tarefas()
    
    while True:
        mostrar_tarefas(tarefas)
        print("\n1. Add | 2. Concluir/Desmarcar | 3. Remover | 4. Sair")
        escolha = input("Escolha: ")

        if escolha == '1':
            nome = input("Tarefa: ").strip()
            if nome:
                tarefas.append({"nome": nome, "concluida": False})
        
        elif escolha == '2':
            try:
                idx = int(input("Número da tarefa para alternar status: ")) - 1
                # Inverte o valor booleano (se True vira False e vice-versa)
                tarefas[idx]['concluida'] = not tarefas[idx]['concluida']
            except (ValueError, IndexError):
                print("Escolha inválida!")

        elif escolha == '3':
            try:
                idx = int(input("Remover qual número? ")) - 1
                tarefas.pop(idx)
            except (ValueError, IndexError):
                print("Erro ao remover.")

        elif escolha == '4':
            salvar_tarefas(tarefas)
            print("Salvo com sucesso!")
            break

if __name__ == "__main__":
    gerenciar()
