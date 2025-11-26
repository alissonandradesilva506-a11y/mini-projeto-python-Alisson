produtos = []
codigos_produtos = set()
categorias =("Alimentos", "Bebidas", "Limpeza", "Utensílios Domésticos")
escolhas = ("Sair", "Cadastrar produto", "Listar produtos", "Buscar produto", "Atualizar produto", "Excluir produto")
atualizacoes =("Terminar", "Nome", "Preço", "Quantidade")
while True:
  print("//////MENU PRINCIPAL\\\\\\")
  for i, escolha in enumerate(escolhas):
    print(f"{i}. {escolha}")

  selecao = input("Escolha uma opção: ")

  if selecao == '1':
    while True:
      codigo = input("Digite o código do produto: ")
      if not codigo:
        print("Erro: Espaço do código não pode estar vazio. Por favor tente de novo.")
      elif codigo in codigos_produtos:
        print("Erro: Código já existe, por favor tente de novo.")
      else:
        break
       
    while True:
      nome = input("Digite o nome do produto: ")
      if not nome:
        print("Erro: Espaço do nome não pode estar vazio. Por favor tente de novo.")
      else:
        break
        
    while True:
      preco = float(input("Digite o preço do produto."))
      if not preco:
        print("Erro: Espaço do preço não pode estar vazio. Por favor tente de novo.")
      elif preco < 0:
        print("Erro: Preço não pode ser negativo. Por favor tente de novo")
      else:
        break
      
    while True:
      quantidade = int(input("Digite quantidade do produto: "))
      if not quantidade:
        print("Erro: Espaço de quantidade não pode estar vazio. Por favor tente de novo.")
      elif quantidade < 0:
        print("Erro: Quantidade não pode ser negativa. Por favor tente de novo.")
      else:
        break
        
    print("Categorias Disponíveis.")
    for i, categoria in enumerate(categorias):
      print(f"{i+1}. {categoria}")
    
    categoria_escolhida = None
    while True:
      opcao = int(input(f"Insira o número da categoria que deseja atribuir:(1-{len(categorias)}): "))
      if 1 <= opcao <= len(categorias):
        categoria_escolhida = categorias[opcao - 1]
        break
      else:
        print("Número de categoria inválido. Por favor digite um número da lista.")

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "categoria": categoria_escolhida
    }
    produtos.append(produto)
    codigos_produtos.add(codigo)
    print("Produto adicionado com sucesso!")
                 
  elif selecao == '2':
    if not produtos:
        print("Nenhum produto disponível.")
    else:
        print("\n--- Lista de Produtos ---")
        for produto in produtos:
            categoria = produto.get("categoria", "N/A") 
            print(f"Code: {produto['codigo']}, Name: {produto['nome']}, Price: {produto['preco']:.2f}, Quantity: {produto['quantidade']}, Category: {categoria}")
        print("--------------------\n")
      
  elif selecao == '3':
    while True:
        codigo_busca = input("Digite código de produto para procurar: ")
        if not codigo_busca:
            print("Erro: Espaço do código não pode estar vazio. Por favor tente de novo.")
        else:
            break

    found = False
    for produto in produtos:
        if produto["codigo"] == codigo_busca:
            print("\n--- Produto Encontrado ---")
            categoria = produto.get("categoria", "N/A")
            print(f"Code: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']:.2f}, Quantidade: {produto['quantidade']}, Categoria: {categoria}")
            print("---------------------\n")
            found = True
            break
    if not found:
        print("Produto não encontrado.")
      
  elif selecao == '4':
    while True:
        codigo_atualizar = input("Digite código de produto para atualizar: ")
        if not codigo_atualizar:
            print("Erro: Espaço do código não pode estar vazio. Por favor tente de novo.")
        else:
            break
    achado = False
    for produto in produtos:
        if produto["codigo"] == codigo_atualizar:
            print(f"Atualizando: {produto['nome']}")
            print("//////Escolha a Atualização\\\\\\")
            for i, atualizacao in enumerate(atualizacoes):
              print(f"{i}. {atualizacao}")
              
              alternativa = input("Escolha uma atualização: ")
              if alternativa == '1':
                while True:
                  nome = input("Digite novo nome: ")
                  if not nome:
                      print("Erro: Nome do produto não pode estar vazio. Por favor tente de novo.")
                  else:
                      break
                  produto["nome"] = nome
              elif alternativa == '2':
                while True:
                  preco = float(input("Digite o preço do produto."))
                  if not preco:
                    print("Erro: Espaço do preço não pode estar vazio. Por favor tente de novo.")
                  elif preco < 0:
                    print("Erro: Preço não pode ser negativo. Por favor tente de novo")
                  else:
                    break
                  produto["preco"] = preco
              elif alternativa == '3':
                while True:
                  quantidade = int(input("Digite quantidade do produto: "))
                  if not quantidade:
                    print("Erro: Espaço de quantidade não pode estar vazio. Por favor tente de novo.")
                  elif quantidade < 0:
                    print("Erro: Quantidade não pode ser negativa. Por favor tente de novo.")
                  else:
                    break
                  produto["quantidade"] = quantidade
              elif alternativa == '0':
                print("Product updated successfully!")
                achado = True
                break
              else:
                print("Por favor insira um número disponível")
    if not achado:
      print("Produto não encontrado.")
          
  elif selecao == '5':
    while True:
        codigo_deletar = input("Digite código de produto para deletar: ")
        if not codigo_deletar:
            print("Erro: Espaço do código não pode estar vazio. Por favor tente de novo.")
        else:
            break

    achado = False
    for i, produto in enumerate(produtos):
        if produto["codigo"] == codigo_deletar:
            del produtos[i]
            codigos_produtos.remove(codigo_deletar)
            print("Product deleted successfully!")
            achado = True
            break
    if not achado:
        print("Produto não foi encontrado.")
      
  elif selecao == '0':
   print("Desligando o programa.")
   break
    
  else:
    print("Opção inválida, por favor, tente novamente.")
