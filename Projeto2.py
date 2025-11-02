dados_estudantes = {}
alunos_registrados = set()

while True:
  print("////////MENU PRINCIPAL\\\\\\\\")
  print("1- Cadastrar alunos")
  print("2- Registrar notas")
  print("3- listar alunos e médias")
  print("4- Buscar aluno")
  print("5- Mostrar aprovados e reprovados")
  print("6- Relatórios")
  print("0- Sair")

  selecao = input("Escolha uma opção: ")

  if selecao == '1':
    nome_aluno = input("Insira o nome do novo aluno: ")
    if nome_aluno in alunos_registrados:
      print(f"O aluno '{nome_aluno}' já está cadastrado.")
      continue

    matricula_estudante = input("Insira a matrícula do estudante.")
    if matricula_estudante in dados_estudantes:
      print(f"A matrícula '{matricula_estudante}' já está cadastrada")
      continue

    alunos_registrados.add(nome_aluno)
    dados_estudantes[matricula_estudante] = []
    print(f"Aluno {nome_aluno} com matrícula {matricula_estudante} cadastrado com sucesso.")
   
  elif selecao == '2':
    select_matricula = input("Digite a matricula do aluno para registrar suas notas: ")
    if select_matricula not in dados_estudantes:
      print("Matrícula não encontrada.")
      continue

    insere_nota = input("Digite as notas separadas por vìrgulas: ")
    try:
      notas= [float(nota.strip()) for nota in insere_nota.split(',')]
      dados_estudantes[select_matricula].extend(notas)
      print(f"Notas registradas na matricula '{select_matricula}' com sucesso.")
    except Erro:
      print("Entrada inválida. Certifique-se de inserir números separados por vírgulas.")

  elif selecao == '3':
    if not dados_estudantes:
      print("Nenhum estudante registrado.")
      continue

    print("Lista de Estudantes e Médias")
    for matricula, notas in dados_estudantes.items():
      if notas:
        media = sum(notas) / len(notas)
        print(f"Matrícula: {matricula}, Média: {media:.2f}")
      else:
        print(f"Matrícula: {matricula}, Sem notas registradas")

  elif selecao == '4':
    matricula = input("Insira a matrícula do aluno que está procurando: ")

    if matricula in dados_estudantes:
      notas = dados_estudantes[matricula]
      print(f"Informações do Estudante com Matrícula: {matricula}")
      print(f"Notas: {notas}")
      if notas:
        media = sum(notas) / len(notas)
        print(f"Média: {media:.2f}")
      else:
        print("Não tem notas registradas")
    else:
      print(f"Matrícula '{matricula}' não encontrada.")

  elif selecao == '5':
    if not dados_estudantes:
      print("Nenhum aluno registrado.")
      continue

    alunos_aprovados = []
    alunos_reprovados = []
    for matricula, notas in dados_estudantes.items():
      if notas:
        media = sum(notas) / len(notas)
        if media >=7.0:
          alunos_aprovados.append((matricula, media))
        else:
          alunos_reprovados.append((matricula, media))
      else:
        alunos_reprovados.append((matricula, "Sem notas registradas."))
    print("////Alunos aprovados\\\\")
    if alunos_aprovados:
      for matricula, media in alunos_aprovados:
        print(f"Matrícula: {matricula}, Média: {media:.2f}")
    else:
      print("Nenhum estudante aprovado.")

    print("////Alunos reprovados\\\\")
    if alunos_reprovados:
      for matricula, media in alunos_reprovados:
        print(f"Matrícula: {matricula}, Média: {media:.2f}")
    else:
      print("Nenhum estudante reprovado.")
      
  elif selecao == '6':
    while True:
      print("///////////////SUB-MENU\\\\\\\\\\")
      print("1- Alunos Cadastrados")
      print("2- Médias individuais")
      print("3- Aprovados e reprovados")
      print("0- Retornar ao menu principal")

      selecao_relatorio = input("Qual relatório quer ver? ")

      if selecao_relatorio == '1':
        print("////Alunos Cadastrados\\\\")
        if alunos_registrados:
          for nome in alunos_registrados:
            print(nome)
        else:
          print("Nenhum estudante cadastrado.")
      elif selecao_relatorio == '2':
        if not dados_estudantes:
          print("Nenhum estudante registrado.")
          continue
        print("Lista de Estudantes e Médias Individuais")
        for matricula, notas in dados_estudantes.items():
            if notas:
                media = sum(notas) / len(notas)
                print(f"Matrícula: {matricula}, Média: {media:.2f}")
            else:
                print(f"Matrícula: {matricula}, Sem notas registradas")

      elif selecao_relatorio == '3':
        if not dados_estudantes:
            print("Nenhum aluno registrado.")
            continue

        alunos_aprovados = []
        alunos_reprovados = []
        for matricula, notas in dados_estudantes.items():
            if notas:
                media = sum(notas) / len(notas)
                if media >= 7.0:
                    alunos_aprovados.append((matricula, media))
                else:
                    alunos_reprovados.append((matricula, media))
            else:
                alunos_reprovados.append((matricula, "Sem notas registradas."))

        print("////Alunos aprovados\\\\")
        if alunos_aprovados:
            for matricula, media in alunos_aprovados:
                print(f"Matrícula: {matricula}, Média: {media:.2f}")
        else:
            print("Nenhum estudante aprovado.")

        print("////Alunos reprovados\\\\")
        if alunos_reprovados:
            for matricula, media in alunos_reprovados:
                print(f"Matrícula: {matricula}, Média: {media:.2f}")
        else:
            print("Nenhum estudante reprovado.")
      elif selecao_relatorio == '0':
        break
      else:
        print("Opção inválida. Tente novamente.")  
      
  elif selecao == '0':
    print("Desligando o programa.")
    break
  else:
    print("Seleção inválida. Tente novamente.")
