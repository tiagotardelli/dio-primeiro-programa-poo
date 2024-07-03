## Factory
def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return subtrair
        case "*":
            return multiplicar
        case "/":
            return dividir

if __name__ == "__main__":
   op = calculadora("+")
   print(op(2, 2))
   op = calculadora("-")
   print(op(2, 2))
   op = calculadora("*")
   print(op(2, 2))
   op = calculadora("/")
   print(op(2, 2))