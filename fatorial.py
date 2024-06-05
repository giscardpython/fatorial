def calcular_fatorial(n):
    if n == 0:
        return 1
    else: 
        return n * calcular_fatorial (n -1)

n = int(input('Informe um número inteiro: '))

print(f'Fatorial de {n}: {calcular_fatorial(n)}')