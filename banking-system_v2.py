import os #Serve para importar a biblioteca OS (Usada para limpar o terminal)!

saldo = 0 #É o saldo do usuário, que será manipulado por todo o processo!
limite = 500 #É o valor máximo que o usuário pode sacar por vez!
numero_saques = 0 #É a variável que será manipulada toda vez que o usuário fizer um saque!
id_operacao = 0 #É a variável que terá como valor "O número da operação"!
LIMITE_SAQUES = 3 #É o número máximo de vezes que o usuário pode sacar dinheiro!

operacoes = { #Serve para definir o dicionário "operacoes"!
    "depositos": {}, #Vai receber todos os valores pertinentes às operações de Depósito.
    "saques": {}, #Vai receber todos os valores pertinentes às operações de Saque.
}

def exibir_opcoes (): #Essa função serve para exibir para o usuário as opções de operações!
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    """
    print(menu)

def match_opcao(): #Essa função serve para verificar a operação escolhida pelo usuário!

    while True:
        exibir_opcoes()
        opcao = input("=> ").upper() #Caso o usuário digite a letra D minúscula, o sistema transforma ela em maiúscula.

        if opcao in ['D', 'S', 'E', 'Q']: #Serve para verificar se o usuário escolheu alguma das opções!
            match opcao:
                case "D":
                    op_deposito() #Serve para chamar a função de Depósito!
                case "S":
                    op_saque() #Serve para chamar a função de Saque!
                case "E":
                    op_extrato() #Serve para chamar a função de Extrato!
                case "Q":
                    print("Saindo do Programa")
                    break #Serve para encerrar o programa!
        else: #Caso o usuário não escolha nenhuma das opções acima, vamos exibir a mensagem abaixo para ele!
            print("Por favor, escolha uma opção válida.")
        
def op_deposito(): #Essa função serve para realizar a operação de Depósito!
    #Para alterar o valor de uma variável fora da função, precisamos declarar ela como Global!
    global operacoes # Declarando o dicionário "operacoes" como global.
    global saldo  # Declarando a variável "saldo" como global.
    global id_operacao # Declarando a variável "id_operacao" como global.
    os.system('cls') #Serve para limpar o terminal.
    print("Depósito")
    valor_dep = float(input("Digite o valor que deseja Depositar: "))
    if valor_dep > 0: #Serve para verificar se o valor digitado pelo usuário é maior que 0!
        id_operacao += 1 #Serve para aumentar o valor da variável "id_operacao" (Simular uma sequência de operações)!
        saldo = saldo + valor_dep #Serve para somar o valor do saldo + o valor digitado pelo usuário!
        resumo_dep = f"R$ {valor_dep}" #Serve para definir a variável que será enviada para o "Extrato de operações" (dicionário "operacoes")!
        operacoes["depositos"][f"{id_operacao}"] = resumo_dep #Serve para criar dentro do dicionário "operacoes", um dicionário que tem como nome o "id_operacao" e como valor o "resumo_dep" (O valor digitado pelo usuário)
        print(f"Foi depositado o valor de R$ {valor_dep}")
    else: #Caso o valor que o digite seja menor que 0, vamos exibir a mensagem abaixo para ele!
        print("O valor precisa ser maior do que 0!")

def op_saque(): #Essa função serve para realizar a operação de Saque!
    #Para alterar o valor de uma variável fora da função, precisamos declarar ela como Global!
    global operacoes # Declarando o dicionário "operacoes" como global
    global saldo  # Declarando a variável saldo como global
    global numero_saques #Declarando a variável numero_saques como global
    global id_operacao # Declarando a variável "id_operacao" como global
    print("Saque")
    if numero_saques < LIMITE_SAQUES: #Serve para verificar se o usuário já atingiu o número máximo de Saques (LIMITE_SAQUES)!
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        if valor_saque > 0: #Serve para verificar se o valor digitado pelo usuário é maior que 0!
            if valor_saque <= saldo: #Serve para verificar se o valor digitado pelo usuário é menor ou igual ao saldo!
                if valor_saque <= limite: #Serve para verificar se o valor digitado pelo usuário é menor ou igual ao limite máximo de saque por operação (limite)!
                    id_operacao += 1 #Serve para aumentar o valor da variável "id_operacao" (Simular uma sequência de operações)!
                    saldo = saldo - valor_saque #Serve para diminuir do saldo, o valor digitado pelo usuário!
                    resumo_saque = f"R$ {valor_saque}" #Serve para definir a variável que será enviada para o "Extrato de operações" (dicionário "operacoes")!
                    operacoes["saques"][f"{id_operacao}"] = resumo_saque #Serve para criar dentro do dicionário "operacoes", um dicionário que tem como nome o "id_operacao" e como valor o "resumo_saque" (O valor digitado pelo usuário)
                    numero_saques += 1 #Serve para aumentar o valor da variável "numero_saques" (Para registrar o saque feito pelo usuário)!
                    print(f"Foi feito um saque de R$ {valor_saque}")
                else: #Caso o valor digitado pelo usuário seja maior do que o valor limite por saque (limite), vamos exibir a mensagem abaixo para ele!
                    print("O valor excede o limite por saque!")
            else: #Caso o valor digitado pelo usuário seja maior do que o saldo, vamos exibir a mensagem abaixo para ele!
                print("O seu saldo é inferior ao valor que deseja sacar!")
        else: #Caso o valor digitado pelo usuário seja menor que 0, vamos exibir a mensagem abaixo para ele!
            print("O valor precisa ser maior que 0!")
    else: #Caso a variável "numero_saques" seja maior ou igual a 3, o processo não será feito e vamos exibir a mensagem abaixo para ele!
        print("Você excedeu o limite de 3 saques diários!")

def op_extrato(): #Essa função serve para realizar a operação de Extrato!
    os.system('cls') #Serve para limpar o terminal
    ext_depositos = operacoes["depositos"] #Serve para atribuir à variável "ext_depositos", todos os "depósitos" que foram incluídos no dicionário "operacoes"!
    ext_saques = operacoes["saques"] #Serve para atribuir à variável "ext_saques", todos os "saques" que foram incluídos no dicionário "operacoes"!
    print("================== Extrato ==================")
    print("Depósitos")
    if ext_depositos != {}: #Serve para verificar se a variável "ext_depositos" está retornando um valor diferente de vazio (Se houveram depósitos cadastrados nela)!
        for depositos in ext_depositos: #Serve para percorrer cada item inserido na variável "ext_depositos" (Percorrer cada um dos depósitos existentes)!
            ext_operacao = operacoes["depositos"][f"{depositos}"] #Serve para acessar cada um dos "depositos" feitos pelo usuário, e exibir na tela com o print abaixo!
            print(ext_operacao)
    else: #Se o usuário não tiver feito nenhum depósito, vamos exibir a mensagem abaixo para ele!
        print("Não houveram Depósitos!")
    print("=============================================")
    print("Saques")
    if ext_saques != {}: #Serve para verificar se a variável "ext_saques" está retornando um valor diferente de vazio (Se houveram saques cadastrados nela)!
        for saques in ext_saques: #Serve para percorrer cada item inserido na variável "ext_depositos" (Percorrer cada um dos depósitos existentes)!
            ext_operacao = operacoes["saques"][f"{saques}"] #Serve para acessar cada um dos "saques" feitos pelo usuário, e exibir na tela com o print abaixo!
            print(ext_operacao)
    else: #Se o usuário não tiver feito nenhum saque, vamos exibir a mensagem abaixo para ele!
        print("Não houveram Saques!")
    print("=============================================")
    print(f"\nO seu saldo atual é de R${saldo}") #Serve para exibir o saldo do usuário!

def main(): #Serve para organizarmos as etapas do programa (a ordem em que as funções seram exibidas e executadas)
    os.system('cls') #Serve para limpar o terminal
    match_opcao() #Serve para executar a função "match_opcao()"

if __name__ == '__main__': #Serve para informar ao terminal, que a página que estamos executando é a principal!
    main() #Serve para executar a função "main()", que irá organizar as etapas do programa!