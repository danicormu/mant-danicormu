# mant-danicormu

# Proyecto de Mantenimiento

En este proyecto se va desarrollar una función en Python que genera contraseñas entre 4 y 16 caracteres que contengan letras mayúsculas, minúsculas, numeros y caracteres especiales.

# Modulos Utilizados

* String

De este módulo se utilizó:

String.ascii_letters - Concatenación de las letras ascii (mayúsculas y minúsculas).
Ej: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

String.digits - Contiene todos los numeros. 
Ej: 0123456789

String.punctuation - Contiene la cadena de caracteres ASCII que se consideran caracteres de puntuación.
Ej: (!"#$%&'()*+,-./:;<=>?@[]^_`{|}~)



* Secrets

Este módulo secrets es utilizado para generar números aleatorios de manera criptográfica sadecuados para administrar datos como contraseñas, autenticación de cuentas y tokens de seguridad.

De este modulo se utilizó choice(secuencia). El cual devuelve un elemento elegido al azar de una secuencia de caracteres no vacía.

* Random

Este módulo random proporciona un generador de números aleatorios, por lo que es adecuado para una gran gama de aplicaciones.

De este modulo se utilizó randint() el cual recibe dos numeros enteros como parametros. La función randint(a, b) genera un número entero entre a y b, ambos incluidos. a debe ser inferior o igual a b.
