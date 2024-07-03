def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Oi {nome}, tudo bem?"

def executar(funcao, nome):
    print('executando executar')
    return funcao(nome)

if __name__ == "__main__":
    print(executar(mensagem, 'Tiago'))
    print(executar(mensagem_longa, 'Tiago'))
