# Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.
def imc(altura, peso):
    'Calcular el indice de masa corporal: '
    return (peso/altura**2)

peso = float(input('Ingresar tu peso en kg: '))
altura = float(input('Ingresar tu altura en metros: '))
indice= imc(altura, peso)
print('Tu indice de masa corporal es :  {:.2f}'.format(indice))