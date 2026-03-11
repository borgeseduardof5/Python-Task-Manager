import os

NOME_ARQUIVO = "tarefas.txt"

def carregar_tarefas():
    """Lê as tarefas do arquivo .txt ao iniciar o programa."""
    if not os.path.exists(NOME_ARQUIVO):
        return []
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
        # .strip() remove a quebra de linha (\n) ao ler
        return [linha.strip() for linha in arquivo.readlines()]

def salvar_tarefas(tarefas):
    """Salva a lista atual no arquivo .txt."""
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa}\n")

def gerenciar_tarefas():
    tarefas = carregar_tarefas()
    
    while True:
        print(f"\n--- TODO LIST ({len(tarefas)} tarefas) ---")
        print("1. Adicionar | 2. Mostrar | 3. Remover | 4. Sair")
        
        escolha = input("Escolha: ")

        if escolha == '1':
            nova = input("Digite a tarefa: ").strip()
            if nova:
                tarefas.append(nova)
                print("Adicionada!")

        elif escolha == '2':
            if not tarefas:
                print("Lista vazia.")
            else:
                for i, t in enumerate(tarefas, 1):
                    print(f"{i}. {t}")

        elif escolha == '3':
            if not tarefas:
                print("Nada para remover.")
                continue
            
            # VALIDAÇÃO COM TRY/EXCEPT
            try:
                indice = int(input("Número da tarefa para remover: ")) - 1
                removida = tarefas.pop(indice)
                print(f"Removido: {removida}")
            except ValueError:
                print("Erro: Digite apenas números inteiros!")
            except IndexError:
                print(f"Erro: Escolha um número entre 1 e {len(tarefas)}.")

        elif escolha == '4':
            salvar_tarefas(tarefas)
            print("Dados salvos. Até logo!")
            break

if __name__ == "__main__":
    gerenciar_tarefas()
