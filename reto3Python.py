#Juan Felipe Quintero

#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “admin” y la contraseña es “admin123*”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente es

def login(username, password):
    if(username == 'admin' and password == 'admin123*'):
        return(f'Verdadero. El usuario es {username} y la contraseña es {password}')
    
username = ''
password = ''

contador = 1

while contador != 0:
    print(f'Veces que intentadas {contador - 1}')
    print(f'**Estas ingresando a la app**')
    username = input('Digite el nombre de usuario: ')
    password = input('Digite la contraseña: ')

    validar = login(username, password)
    if(validar):
        print(validar)
        contador = 0
    else:
        contador = contador + 1