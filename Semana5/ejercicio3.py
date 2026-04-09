"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    resultado=1
    for i in range(1,n+1):
        resultado=*i
return resultado
print(factorial_ciclo(6))


def factorial_recursivo(n):
    if n==1
    return 1
    return n * factorial_recursivo(n-1)
print (factorial_recursivo(8))
