menu = """

[c] Criar conta
[v] Ver contas
[p] Pegar uma conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def molde(nro: int):
    return {
        "cliente": 
        {
            "nome": "",
            "data": "",
            "cpf": 0,
            "endereco": {
                "logradouro": "",
                "numero": 0,
                "bairro": "",
                "cidade": "",
                "siglaDoEstado": "",
            }
        },
        "info": 
        {
            "saldo" : 0,
            "limite" : 500,
            "extrato" : "",
            "numero_saques" : 0,
            "LIMITE_SAQUES" : 3
    },
        "ag": "0001",
        "nro": nro
    }

contaBancaria = []
aux = -1

def depositar(valor, info):
    if valor > 0:
        info['info']["saldo"] += valor
        info['info']["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        return info
    else:
        print("Operação falhou! O valor informado é inválido.")
        return info

def sacar(valor, info):
    if(valor > info['info']["saldo"]):
        print("Operação falhou! Você não tem saldo suficiente.")
    elif(valor > info['info']["limite"]):
        print("Operação falhou! O valor do saque excede o limite.")
    elif(info['info']["numero_saques"] >= info['info']["LIMITE_SAQUES"]):
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        info['info']["saldo"] -= valor
        info['info']["extrato"] += f"Saque: R$ {valor:.2f}\n"
        info['info']["numero_saques"] += 1
    
    return info

def extrato(info):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not info['info']["extrato"] else info['info']["extrato"])
    print(f"\nSaldo: R$ {info['info']['saldo']}")
    print("==========================================")

while True:

    opcao = input(menu)

    if opcao == "d":
        if(aux > -1):
            valor = float(input("Informe o valor do depósito: "))
            contaBancaria[aux] = depositar(valor, contaBancaria[aux])
        else:
            print("Não foi ninguém selecionado.")

    elif opcao == "s":
        if(aux > -1):
            valor = float(input("Informe o valor do saque: "))
            contaBancaria[aux] = sacar(valor, contaBancaria[aux])
        else:
            print("Não foi ninguém selecionado.")

    elif opcao == "e":
        if(aux > -1):
            extrato(contaBancaria[aux])
        else:
            print("Não foi ninguém selecionado.")

    elif opcao == "c":
        try:
            cliente = molde(len(contaBancaria))

            cliente["cliente"]["nome"] = input("Qual é o nome? \n")
            cliente["cliente"]["data"] = input("Data de nascimento? \n")
            cliente["cliente"]["cpf"] = int(input("Qual o cpf (somente números)? \n"))
            cliente["cliente"]["endereco"]["logradouro"] = input("Qual é a rua?\n")
            cliente["cliente"]["endereco"]["numero"] = int(input("Qual é o número?\n"))
            cliente["cliente"]["endereco"]["bairro"] = input("Qual é o bairro?\n")
            cliente["cliente"]["endereco"]["cidade"] = input("Qual é a cidade?\n")
            cliente["cliente"]["endereco"]["siglaDoEstado"] = input("Qual é a sigla do estado?\n")

            contaBancaria.append(cliente)

            print("Adicionado com sucesso!!!\n")
        except:
            print("Erro!!!\n")

    elif opcao == "v":
        for i in contaBancaria:
            print(f"Nome: {i['cliente']['nome']}\n")
            print(f"CPF: {i['cliente']['cpf']}\n")
            print(f"Número de conta: {i['nro']}\n\n")
            
    elif opcao == "p":
        aux = int(input("\nQual o número da conta: "))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")