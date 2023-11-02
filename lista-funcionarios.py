import sqlite3

def criar_tabela():
    conn = sqlite3.connect('funcionario.db')
    cursor = conn.cursor()

    cursor.execute('''
      CREATE TABLE IF NOT EXISTS funcionario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()  

def criar_funcionario(nome,cargo,salario):
  conn = sqlite3.connect('funcionario.db')
  cursor = conn.cursor()
 
  cursor.execute('''INSERT INTO funcionario (nome, cargo,
  salario) VALUES (?, ?, ?)''', (nome,cargo,salario))
  conn.commit()
  conn.close()

def listar_funcionarios():
  conn = sqlite3.connect('funcionario.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM funcionario')
  funcionario = cursor.fetchall()
 
  if len(funcionario) > 0:
      print("Lista dos Funcionários:")
      for funcionarios in funcionario:
        print(f"ID: {funcionarios[0]}")
        print(f"Nome: {funcionarios[1]}")
        print(f"Cargo: {funcionarios[2]}")
        print(f"Salário: {funcionarios[3]}")
  else:
      print("Não há funcionários cadastrados")
  conn.close()

def atualizar_funcionario(funcionario_id, nome, cargo, salario):
  conn = sqlite3.connect('funcionario.db')
  cursor = conn.cursor()
  cursor.execute('''UPDATE funcionario SET nome = ?, cargo = ?, salario = ?
  WHERE id = ?''', (nome, cargo, salario, funcionario_id))
  conn.commit()
  conn.close()

def excluir_funcionario(funcionario_id):
  conn = sqlite3.connect('funcionario.db')
  cursor = conn.cursor()
  cursor.execute('''DELETE FROM funcionario WHERE id = ?''', (funcionario_id,))
  conn.commit()
  conn.close()

criar_tabela()

criar_funcionario('João', 'Analista', 3000)
criar_funcionario('Maria', 'Analista', 3000)

print("Listar Funcionários após a Criação:")
listar_funcionarios()

atualizar_funcionario(1, 'João Paulo', 'Analista', 84000)

print("\nListar Funcionários após a Atualização:")
listar_funcionarios()

excluir_funcionario(2)
print("\nListar Funcionários após a Exclusão:")
listar_funcionarios()  

def menu():
  print("\n---------------------------------------\n")
  print("1 - Cadastrar Funcionário")
  print("2 - Listar Funcionários")
  print("3 - Atualizar Funcionário")
  print("4 - Excluir Funcionário")
  print("5 - Sair")
  opcao = int(input("Digite a opção desejada: "))
  return opcao

def main():
  criar_tabela()
  while True:
    opcao = menu()
    if opcao == 1:
      nome = input("Digite o nome do funcionário: ")
      cargo = input("Digite o cargo do funcionário: ")
      salario = float(input("Digite o salário do funcionário: "))
      criar_funcionario(nome, cargo, salario)
    elif opcao == 2:
      listar_funcionarios()
      input("\nPressione Enter para continuar...")
     # os.system('clear')
      continue
     
    elif opcao == 3:
      funcionario_id = int(input("Digite o ID do funcionário: "))
      nome = input("Digite o nome do funcionário: ")
      cargo = input("Digite o cargo do funcionário: ")
      salario = float(input("Digite o salário do funcionário: "))
      atualizar_funcionario(funcionario_id, nome, cargo, salario)
     
    elif opcao == 4:
      funcionario_id = int(input("Digite o ID do funcionário: "))
      excluir_funcionario(funcionario_id)
     
    elif opcao == 5:
      print("\nObrigado por ter utilizado nosso sistema!\n")
      break
    else:
      print("Opção inválida!")
      input("\nPressione Enter para continuar...")
      os.system('clear')
      continue
     
if __name__ == '__main__':
  main()