def principal():
    print("Executando a função principal")
    def funcao_interna_1():
        print("Executando a função interna 1")
    def funcao_interna_2():
        print("Executando a função interna 2")
    
    funcao_interna_1()
    funcao_interna_2()

if __name__ == "__main__":
    principal()