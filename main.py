'''
Daniel Felipe Villa Rengifo
Lenguaje: Python
Tema: Atributos de clases y de instancias, métodos de clase
Links de referencia
1. https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/
2. https://stackoverflow.com/questions/35520251/difference-between-class-attributes-instance-attributes-and-instance-methods-i
'''
# Ejemplo 1 de Atributos de clase:
print('-------------------------------------------------')
print('\n# Ejemplo 1 de Atributos de clase e Instancia:')

## Definimos una clase:
print('\n## Definimos una clase:')

print('\n<class contador>')

class contador:
  '''
  Un contador,
  empieza desde 1 (tecnicamente desde 0, si no se llama la clase)
  donde utiliza un metodo incremento que aumenta de 1 a 1.
  '''
  c = 0
  # Se defeine el metodo incremento:
  def incremento(self):
    '''
    Este metodo permite ir añadiendo a la variable c
    el valor de 1, es decir aumenta de uno en uno 
    cada vez que se llama incremento.
    '''
    # Se llma a la clase, para que le agrege un valor nuevo a "c" (cada ves que se necesario)
    contador.c += 1

## Llamamos al objeto incremento():
print('\n## Llamamos al objeto incremento():')

print('\nc1 = contador()')
c1 = contador()

c1.incremento()
print('\nc1.incremento()')

print('\nValor de c1.c', '=>', c1.c)

## Una más lo intentamos, pero ahora con un siclo for:
print('\nUna más lo intentamos, pero ahora con un siclo for')

print('\ncn = contador()', '<=', 'Un Numero n definido por el usuario')
cn = contador()

print('\nNumeros desde el 0 al nuemro dado n, trate que sea mayor a 100')
n = int(input('Un Numero n (# Entero <=> Int): '))

'''
Con el while le decimos qu esi el valor de n es menor estrictamente que 100, se repita infinitamente
hasta cumplir la condición
'''
while n < 100:
  n = int(input('Un Numero n (# Entero <=> Int) mayor o igual a 100: '))
else:
  pass
  
## Entrmaos en el ciclo for para tener un c >= 2:
print("\ncn.incremento()")
print('\nVeamos como aumenta el contador y en que valor termina')
print('\nEmpieza el for desde 2 porque ya teniamos valores anteriormente agregador, es decir, c guarda los valores en la clase contador()')
for x in range(n):
  cn.incremento()
  print(cn.c)

# Fin del Ejemplo
print('\n# Fin del Ejemplo')
print('\n-------------------------------------------------')

# Ejemplo 2:
print('\n-------------------------------------------------')
print('\n# Ejemplo 2 Atributos de Instancia/Objeto:')

'''
Demostraremos los atributos de instancia:
Explicados en el Markdown.
'''

## Definimos una clase:
print('\n## Definimos una clase:')
print('\n<class empleado>')

class empleado:
  '''
  Esta clase define:
  el nombre de un empleado y su respectivo salario
  '''
  def __init__(self, nombre, salario):
    '''
    con el metodo constructor
    definimos el nombre y el salario de una persona x
    '''
    self.nombre = nombre
    self.salario = salario
  
  def exponer(self):
    '''
    Aqui como un revelado fotografico,
    revelamos con el print el nombre y salario de una persona x
    '''
    print(self.name)
    print(self.salario)

## ahora definimos el nombre de una persona y su respectivo salario:
print('\n## ahora definimos el nombre de una persona (str) y su respectivo salario:')
print('\nIngrese solo su primer nombre y su salario como un numero float: ')

nom = input('Ingrese su nombre (o su primer nombre): ')
sal = float(input('Ingrese su salario (Numero decimal): '))

empleado_1 = empleado(nom, sal)

# Creamos un diccionario con los metodos y sus respectivos valores definidos en empleado_1:
print('\n# Creamos un diccionario con los metodos y sus respectivos valores definidos en empleado_1:')
print('\nCreando Diccionario con "var()": ', vars(empleado_1))

# Imprime el catalogo de de los atributos de su clase y sus antecesoras:
print('\n# Imprime el catalogo de de los atributos de su clase y sus antecesoras:')
print(dir(empleado_1))

# Fin del Ejemplo
print('\n# Fin del Ejemplo')
print('\n-------------------------------------------------')