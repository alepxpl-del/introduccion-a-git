def factorial(n):
    resultado = 1
    breakpoint
    if n > 1:
        resultado = n * factorial(n - 1)
    return resultado

num = int(input())
fact = factorial(num)
breakpoint
print(fact)