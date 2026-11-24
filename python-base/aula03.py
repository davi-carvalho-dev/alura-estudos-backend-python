# Exercícios aula 03

import os

# Exercicio 1
decimais = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Helena', 'Davi', 'Lucas', 'Juliana']
anos = [2002, 2026]

# Exercicio 2
def main():
    os.system('clear')
    print('Teste de Lista\n')

    numero = int(input('Digite um valor (0/10): '))

    if numero in decimais:
        print(f'Número válido encontrado na lista: {numero}')
    else:
        print('Valor inesperado, tente novamente\n')
        input('Pressione Enter para continuar...')
        main()

if __name__ == '__main__' :
    main()

# Exercicio 3
impares = [n + n  for n in decimais if n %2 == 0]
print(impares)

# Exercicio 4
decimais.reverse()
print(decimais)

# Exercicio 5
numero = int(input('Digite um número: '))

tabuada = [n * numero for n in decimais] 
print(tabuada)

# Exercicio 6
numeros = [10, 20, 30, 40, 50]

try:
    soma = 0
    for n in numeros:
        soma += n
    print(f"Soma: {soma}")
except TypeError:
    print("Erro: a lista contém um elemento que não é número.")
except Exception as e:
    print(f"Erro inesperado: {e}")


# Exercicio 7
valores = [8, 7.5, 9, 6]
# valores = []  # teste com lista vazia

try:
    media = sum(valores) / len(valores)
    print(f"Média: {media}")
except ZeroDivisionError:
    print("Erro: não é possível calcular a média de uma lista vazia.")