listaprodutos = [[],[],[],[],[]]#matrizes de cadastramentos dos dados.
from time import sleep as s
from os import system 
nome = fabricante = ""
def input_int(alert):#Funcao para retorno de erros das variaveis do tipo int
    while True:
        try:
            return int(input(alert))
        except ValueError:
            print("Valor Inserido Invalido")
            print(26*"=")

def input_float(alert):#Funcao para retorno de erros das variaveis do tipo int
    while True:
        try:
            return float(input(alert))
        except ValueError:
            print("Valor Inserido Invalido")

def cadastrar():#Função para cadastraro usuario.
    while True:
        nome = str(input("Nome do Produto:")).strip().lower()
        fabricante = str(input("Nome do Fabricante:")).strip()
        if nome.isalnum() and fabricante.isalnum():
            print("Analisando Nome e Fabricante")
            s(1.2)
            break
            
        else:
            print("Apenas letras e numeros\nou Apenas letras")
            continue
            
    valor = input_float("Valor do Produto:")
    
    while True:
        quantidade = input_int("Quantidade do Produto:")
        
        if quantidade >= 1:#Se na quantidade o valor for maior ou igual a 1 quebra o laco.
            break
            
        else:#condicao que testa se o usuario digitar um valor inferior a 1.
            print("Valor incorreto")
            
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
            
        elif checkprod != ("s","n"):
            print("Resposta invalida")
            continue

def consultar():#Função para consultar o usuario.
    if listaprodutos[0] == []:#Caso o usuario consulte e nao tenha nada cadastrado
        print("Sem Produtos")
        print(15*"=")
        
    else:#caso tenha algo ele mostra "codigo e produto" e mostra suas informacoes
        for cod,itens in enumerate(listaprodutos[0]):
            print(f"{cod}.....{itens}")
            
        check = str(input("Nome do Produto:")).strip().lower()
        
        if check in listaprodutos[0]:#Condicao que checa se o produto digitado esta na lista e exibe suas informacoes.
            print(f"Produto:{check}")
            print(f"Valor:{listaprodutos[1][listaprodutos[0].index(check)]}")
            print(f"Fabricante:{listaprodutos[2][listaprodutos[0].index(check)]}")
            print(f"Quantidade:{listaprodutos[3][listaprodutos[0].index(check)]}")
            print(f"Total:{listaprodutos[4][listaprodutos[0].index(check)]}")
            
        else:#caso o produto digitado nao tiver nao lista aparece esse mensagem.
            print("produto nao cadastrado.")
            
def remover():#Função para remover o usuario
    remove = str(input("Nome do Produto:")).strip().lower()
    
    idx = listaprodutos[0].index(remove)
    del listaprodutos[0][idx]
    del listaprodutos[1][idx]
    del listaprodutos[2][idx]
    del listaprodutos[3][idx]
    del listaprodutos[4][idx]
    print("Excluindo Dados")
    s(2)
    print("Dados Excluidos")
    print(15*"=")
    
   
while True:#laço com tartamento de erros para as opçoes
    opcao = input_int("""[1]Cadastrar
[2]Consultar
[3]Remover\nDigite uma Opcao:""")#variavel para as opções

    if opcao not in range(1,4):
        print("opcao invalida.")
        print(20*"=")
        continue
        
    else:
    
        if (opcao == 1):#condição caso o usuario digite 1
            cadastrar()
            
        elif (opcao == 2):#condição caso o usuario digite 2
            consultar()
            
        elif (opcao == 3):#condição caso o usuario digite 3
            if (listaprodutos[0] == []):
                print("Nada ha excluir")
                print(15*"=")
                
            else:
                remover()
    
    
    
    
    
