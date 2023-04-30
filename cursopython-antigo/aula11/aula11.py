
user = input('Digite seu usuário: ')
password = input('Digite sua senha: ')

user_db = 'g_gusmao'
password_db = '123456'

if user_db == user and password_db == password:
    print('Login efetuado com sucesso!')
else:
    print('Login ou senha inválidos.')