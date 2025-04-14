import random as rd
class dadosFuncionais:
    @staticmethod
    def gerarNumeros():
        num1 = rd.randint(0,9)
        num2 = rd.randint(0,9)
        return num1, num2

    @staticmethod
    def selecionarOperador():
        return rd.choice(["+","-","/","*"])

    @staticmethod
    def calcularResultado(a,b,op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if(b==0):
                b==1
        return a / b
            
                

            