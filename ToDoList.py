import json

# Modelo de uma Tarefa
class Tarefa:
    def __init__(self, nome, concluida=False):
        self.nome = nome
        self.concluida = concluida

    def __repr__(self):
        status = "✅ Concluída" if self.concluida else "🕒 Pendente"
        return f"Tarefa: {self.nome} | Status: {status}"

# Gerenciador de Tarefas
class GerenciadorDeTarefas:
    def __init__(self, arquivo='tarefas.json'):
        self.tarefas = []
        self.arquivo = arquivo
        self.carregar_tarefas()

    # Adicionar uma nova tarefa
    def adicionar_tarefa(self, nome_tarefa):
        nova_tarefa = Tarefa(nome_tarefa)
        self.tarefas.append(nova_tarefa)
        print(f"🎉 Tarefa '{nome_tarefa}' adicionada com sucesso!")

    # Listar todas as tarefas
    def listar_tarefas(self):
        if not self.tarefas:
            print("🚫 Nenhuma tarefa encontrada.")
        else:
            for index, tarefa in enumerate(self.tarefas, start=1):
                print(f"{index}. {tarefa}")

    # Remover uma tarefa pelo índice
    def remover_tarefa(self, indice):
        try:
            tarefa_removida = self.tarefas.pop(indice - 1)
            print(f"🗑️ Tarefa '{tarefa_removida.nome}' removida com sucesso!")
        except IndexError:
            print("⚠️ Índice inválido. Nenhuma tarefa removida.")

    # Marcar uma tarefa como concluída
    def marcar_como_concluida(self, indice):
        try:
            self.tarefas[indice - 1].concluida = True
            print(f"✅ Tarefa '{self.tarefas[indice - 1].nome}' marcada como concluída!")
        except IndexError:
            print("⚠️ Índice inválido. Nenhuma tarefa foi marcada.")

    # Salvar tarefas no arquivo JSON
    def salvar_tarefas(self):
        with open(self.arquivo, 'w') as f:
            json.dump([tarefa.__dict__ for tarefa in self.tarefas], f, indent=4)
        print("💾 Tarefas salvas com sucesso!")

    # Carregar tarefas do arquivo JSON
    def carregar_tarefas(self):
        try:
            with open(self.arquivo, 'r') as f:
                tarefas_carregadas = json.load(f)
                self.tarefas = [Tarefa(**dados) for dados in tarefas_carregadas]
            print("📥 Tarefas carregadas com sucesso!")
        except (FileNotFoundError, json.JSONDecodeError):
            print("📋 Nenhum arquivo de tarefas encontrado, começando uma nova lista.")
            
# Menu de opções
def menu():
    print("\n==============================")
    print("Escolha uma opção:")
    print("1. ➕ Adicionar Tarefa")
    print("2. 📜 Listar Tarefas")
    print("3. ❌ Remover Tarefa")
    print("4. ✅ Marcar Tarefa como Concluída")
    print("5. 🚪 Sair")
    print("==============================")
# Programa principal
if __name__ == "__main__":
    gerenciador = GerenciadorDeTarefas()

    while True:
        menu()
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            nome_tarefa = input("📝 Digite o nome da tarefa: ")
            gerenciador.adicionar_tarefa(nome_tarefa)
            gerenciador.salvar_tarefas()

        elif escolha == '2':
            gerenciador.listar_tarefas()

        elif escolha == '3':
            gerenciador.listar_tarefas()
            indice = int(input("📉 Digite o número da tarefa que deseja remover: "))
            gerenciador.remover_tarefa(indice)
            gerenciador.salvar_tarefas()

        elif escolha == '4':
            gerenciador.listar_tarefas()
            indice = int(input("✔️ Digite o número da tarefa que deseja marcar como concluída: "))
            gerenciador.marcar_como_concluida(indice)
            gerenciador.salvar_tarefas()

        elif escolha == '5':
            print("👋 Saindo...")
            break

        else:
            print("❌ Opção inválida! Tente novamente.")
