import time

# matrizes de cadastramentos dos dados
listaprodutos = [[],[],[],[],[]]

# Função para cadastrar o usuario
def cadastrar():
    while True:
        try:
            nome = str(input("Nome do Produto:")).strip().lower()
            fabricante = str(input("Nome do Fabricante:")).strip()
            assert nome.isalnum()
            assert fabricante.isalnum()
            valor = float(input("Valor do Produto:"))
            quantidade = int(input("Quantidade do Produto:"))
            
            if quantidade < 1:
                raise ValueError
            break
        
        except ValueError:
            print("Valor Inserido Invalido")
            continue
        
        except Exception:
            print("Apenas letras e numeros\nou Apenas letras")
            continue
            
    total = quantidade * valor
    
    print(f"Nome:{nome}\nValor:{valor}\nfabricante:{fabricante}\nQuantidade:{quantidade}\nTotal:{total}")
    
    while True:
        checkprod = str(input("Os dados estao corretos:")).strip().lower()[0]
        if checkprod == "s":
            listaprodutos[0].append(nome)
            listaprodutos[1].append(valor)
            listaprodutos[2].append(fabricante)
            listaprodutos[3].append(quantidade)
            listaprodutos[4].append(total)
            print("Produtos cadastrados")
            break
        
        elif checkprod == "n":
            print("Dados Nao cadastrados")
            
        else:
            print("Resposta invalida")
            continue

# Função para consultar o usuario
def consultar():
    # Caso o usuario consulte e nao tenha nada cadastrado
    if listaprodutos[0] == []:
        print("Sem Produtos")
        print(15*"=")
    
    # Caso tenha algo ele mostra "codigo e produto" e mostra suas informacoes
    else:
        for cod, itens in enumerate(listaprodutos[0]):
            print(f"{cod}.....{itens}")
            
        check = str(input("Nome do Produto:")).strip().lower()
        
        # Condicao que checa se o produto digitado esta na lista e exibe suas informacoes
        if check in listaprodutos[0]:
            print(f"Produto: {check}")
            print(f"Valor: {listaprodutos[1][listaprodutos[0].index(check)]}")
            print(f"Fabricante: {listaprodutos[2][listaprodutos[0].index(check)]}")
            print(f"Quantidade: {listaprodutos[3][listaprodutos[0].index(check)]}")
            print(f"Total: {listaprodutos[4][listaprodutos[0].index(check)]}")
        
        # Caso o produto digitado nao tiver nao lista aparece esse mensagem
        else:
            print("produto nao cadastrado.")

# Função para remover o usuario
def remover():
    remove = str(input("Nome do Produto:")).strip().lower()
    
    idx = listaprodutos[0].index(remove)
    del listaprodutos[0][idx]
    del listaprodutos[1][idx]
    del listaprodutos[2][idx]
    del listaprodutos[3][idx]
    del listaprodutos[4][idx]
    print("Excluindo Dados")
    time.sleep(2)
    print("Dados Excluidos")
    print(15*"=")
    

# laço com tartamento de erros para as opçoes
while True:
    # Variavel para as opções
    opcao = int(input("""
[1] Cadastrar
[2] Consultar
[3] Remover
[4] Sair
Digite uma Opcao:"""))
        
    # Condição caso o usuario digite 1
    if opcao == 1:
        cadastrar()
    
    # Condição caso o usuario digite 2
    elif opcao == 2:
        consultar()
        
    # Condição caso o usuario digite 3
    elif opcao == 3:
        if listaprodutos[0] == []:
            print("Nada ha excluir")
            print(15*"=")
                
        else:
            remover()

    elif opcao == 4:
        break

    else:
        print("opcao invalida.")
        print(20*"=")
