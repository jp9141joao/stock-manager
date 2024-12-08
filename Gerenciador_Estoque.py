from os import system
from random import randint
from math import inf


def Input_Verificador_Digito(Pergunta,Tipo,Parametros=[0]):
    
    if Tipo == 'Float':
        while True:
            system('cls')
            Verificador = input(Pergunta)
            
            Verificador = Verificador.replace(',','.')
            Resposta = None
            
            if Verificador.isdigit() or Verificador.replace('.','').isdigit():
                Resposta = float(Verificador)
                
            if Resposta is not None:
                return Resposta
                
    elif Tipo == 'Int':
        while True:
            system('cls')
            Verificador = input(Pergunta)
            
            Resposta = None
            
            if Verificador.isdigit():
                Resposta = int(Verificador)
                
            if len(Parametros) > 1:
                if Resposta is not None and Resposta > Parametros[0] and Resposta <= Parametros[1]:
                    return Resposta
            else:
                if Resposta is not None:
                    return Resposta
  
        
def Input_Verificador_Codigo(Pergunta,Estoque):
    while True:
        system('cls')
        Verificador = input(Pergunta)
        
        Codigo = None

        if Verificador.isdigit():
            Codigo = int(Verificador)
        
        if Codigo is not None and Codigo == -1:
            return -1
            
        if any(Item['Codigo'] == Codigo for Item in Estoque) and Codigo is not None:
            return Codigo
        else:
            Opcao_Invalida()
            

def Opcao_Invalida():
     while True:
        system('cls')
        Verificador = input('Opção Invalida!\nDigite "1" para voltar\nR: ')
        
        Opcao_Invalida = None

        if Verificador.isdigit():
            Opcao_Invalida = int(Opcao_Invalida)
            
        if Opcao_Invalida == 1:
            break
        

def Voltar(Mensagem):
    while True:
        Verificador = input(f'\n{Mensagem}\nDigite "1" para voltar\nR: ')
        
        Voltar = None
        
        if Verificador.isdigit():
            Voltar = int(Verificador)
            
        if Voltar == 1 and Voltar is not None:
            break


def Excluir_Estoque(Codigo,Estoque):
    
    for Item in Estoque:
        if Item['Codigo'] == Codigo:
            Indice = Estoque.index(Item)
            Estoque.pop(Indice)
            break
        
    
def Adicionar_Estoque(Nome,Qntd,Estoque,Preco=0):
    
    while True:
        Codigo = randint(10000,99999)
        Cont = 0
        
        for Item in Estoque:
            if Item['Codigo'] == Codigo:
                Cont += 1
        
        if Cont == 0:
            break
    
    if Preco > 0:
        Produto = {
            'Nome': Nome,
            'Preco': Preco,
            'Qntd': Qntd,
            'Codigo': Codigo
        }
    else:
        Produto = {
            'Nome': Nome,
            'Qntd': Qntd,
            'Codigo': Codigo
        }
        
    Estoque.append(Produto)
    
    
def Mudar_Atributos(Codigo,Atributo,Novo_Valor,Estoque):
    for Item in Estoque:
        if Item['Codigo'] == Codigo:
            Item[Atributo] = Novo_Valor
            break
    
    
def Main():
    Estoque = []
    
    while True:
        while True:
            system('cls')
            if len(Estoque) == 0:
                print('\n* Estoque *\n\nVAZIO')
            else:
                print('\n* Estoque *')
                for Item in Estoque:
                    try:
                        print(f"\nNome: {Item['Nome']}\nPreço: {Item['Preco']}\nQuantidade: {Item['Qntd']}\nCodigo: {Item['Codigo']}")
                    except:
                        print(f"\nNome: {Item['Nome']}\nQuantidade: {Item['Qntd']}\nCodigo: {Item['Codigo']}")
                        
            print('\n-------------------------------------------')
                        
            Verificador = input(f'\n* Gerenciador de Estoque *\n\n1- Adicionar Produto ao Estoque\n2- Remover Produtos do Estoque\n3- Mudar Atributos de um Item\n4- Sair\n\nR: ')            
            
            Menu = None
            
            if Verificador.isdigit():
                Menu = int(Verificador)
                
            if Menu is not None and Menu > 0 and Menu <= 4:
                break

            
        if Menu == 4:
            system('cls')
            print('\nPrograma Encerrado!')
            break
        
        elif Menu == 1:
            system('cls')
            Nome = str(input('\nDigite o nome do item\nR: '))
            
            Incluir_Preco = Input_Verificador_Digito('\nDeseja informar o preço do produto\n\n1- Sim\n2- Não\nR: ','Int',[0,2])
            
            if Incluir_Preco == 1:
                Preco = Input_Verificador_Digito(f'\nDigite o nome do item\nR: {Nome}\n\nDigite o preço do item\nR: ','Float',[0,inf])
                Qntd = Input_Verificador_Digito(f'\nDigite o nome do item\nR: {Nome}\n\nDigite o preço do item\nR: {Preco}\n\nDigite a quantidade de produtos em estoque deste item\nR: ','Int',[0,inf])
            else:
                Qntd = Input_Verificador_Digito(f'\nDigite o nome do item\nR: {Nome}\n\nDigite a quantidade de produtos em estoque deste item\nR: ','Int',[0,inf])
                Preco = 0
                
            Adicionar_Estoque(Nome,Qntd,Estoque,Preco)
            Voltar('\nItem adiconado com sucesso!')
        
        elif Menu == 2:
            if len(Estoque) == 0:
                Voltar('Adicione um produto primeiro antes de excluir!')
            else:
                Codigo = Input_Verificador_Codigo('\nDigite o codigo do produto que deseja excluir ou digite "-1" para voltar\nR: ',Estoque)
                if Codigo != -1:
                    Excluir_Estoque(Codigo,Estoque)
                    Voltar('Item excluido com sucesso!')
        
        elif Menu == 3:
            if len(Estoque) == 0:
                Voltar('Adicione um produto primeiro antes de mudar o atributo!')
            else:
                Codigo = Input_Verificador_Codigo('\nDigite o codigo do produto que deseja mudar o atributo ou digite "-1" para voltar\nR: ',Estoque)
            
                for i, Item in enumerate(Estoque):
                    if Item['Codigo'] == Codigo:
                        Indice = i
                        break
                        
                
                if Codigo != -1:
                    
                    while True:
                        if 'Preco' in Estoque[Indice]:
                            Atributo = Input_Verificador_Digito(f"Nome: {Estoque[Indice]['Nome']}\nPreço: {Estoque[Indice]['Preco']}\nQuantidade: {Estoque[Indice]['Qntd']}\nCodigo: {Estoque[Indice]['Codigo']}\n\nQual atributo você deseja mudar\n\n1- Nome\n2- Preço\n3- Quantidade\n4- Sair\nR: ",'Int',Parametros=[0,4])
                        else:
                            Atributo = Input_Verificador_Digito(f"Nome: {Estoque[Indice]['Nome']}\nQuantidade: {Estoque[Indice]['Qntd']}\nCodigo: {Estoque[Indice]['Codigo']}\n\nQual atributo você deseja mudar\n\n1- Nome\n2- Preço\n3- Quantidade\n4- Sair\nR: ",'Int',Parametros=[0,4])
                        
                        if Atributo == 1:
                            Atributo = 'Nome'
                            Novo_Valor = str(input('\nDigite o novo nome do item\nR: '))
                            
                        elif Atributo == 2:
                            Atributo = 'Preço'
                            Verificador = False
                            
                            for Item in Estoque:
                                if 'Preco' in Item and Item['Codigo'] == Codigo:
                                    Verificador = True
                                    break
                                
                            if Verificador == False:
                                Voltar('Este item não possui preço nos atributos!')
                                break
                                
                        elif Atributo == 3:
                            Atributo = 'Quantidade'
                            Novo_Valor = Input_Verificador_Digito('\nDigite a nova quantidade do item\nR: ','Int')
                        else:
                            break
                        
                        Mudar_Atributos(Codigo,Atributo,Novo_Valor,Estoque)
                        Voltar('Atributo mudado com sucesso!')

                             
Main()