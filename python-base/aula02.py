
# Aula 2 - Estruturas Condicionais

# Exercício 1

numero = int(input('Digite um número: '))

if numero %2 == 0:
    print(f'O número {numero} é par')
else: 
    print(f'O número {numero} é impar')

# Exercício 2

idade = int(input('Qual a sua idade: '))

if 0 < idade <= 12:
    print('Você é uma criança!')
elif 12 < idade < 18:
    print('Você é um adolescente!')
elif idade >=18:
    print('Você é um adulto!')
else: 
    print('Valor inválido!')

# Exercício 3
usuario_correto = "Helena"
senha_correta = "davilindo"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")

# Exercício 4

x = int(input('Dê a coordenada de X: '))
y = int(input('Dê a coordenada de Y: '))

if x > 0 and y > 0:
    print('Você está no primeiro quadrante!')
elif x < 0 and y > 0:
    print('Você está no segundo quadrante!')
elif x < 0 and y < 0:
    print('Você está no terceiro quadrante!')
elif x > 0 and y < 0:
    print('Você está no quarto quadrante!')
else: 
    print('o ponto está localizado no eixo ou origem.')