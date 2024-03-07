def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    
    
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    
    if n in fib_sequence:
        return True
    else:
        return False


def verificar_fibonacci(numero):
    if fibonacci_sequence(numero):
        print(f"O número {numero} faz parte da sequência de Fibonacci.")
    else:
        print(f"O número {numero} não faz parte da sequência de Fibonacci.")


numero_informado = int(input("Informe um número: "))
verificar_fibonacci(numero_informado)
