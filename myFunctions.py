def operAritmetic(val1, val2, operator):
    try:
        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        elif operator == '*':
            return val1 * val2
        elif operator == '/':
            if val2 == 0:
                return "Error: Divisón por cero, no es posible"
            else:
                return val1 / val2
        else:
            return "Error: Opración invalida"
    except Exception as e:
        print (f"Error: {e}")
        
        
def calcIva(cifra):
    return cifra * 19/100

#Serie Fibonacci
def fibonacci(n):
    num=int(input('Cuántos valores de la sucesión de Fibonacci deseas?: ' ))
    a=0
    b=1
    c=1
    print ('0 \n1' ) 
    for i in range (num):
          print (c) 
          a=b
          b=c
          c=a+b
       
    return c

    