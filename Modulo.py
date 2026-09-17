def modulo(a, b):
    #en español, sin usar el operador de módulo
    division = a // b
    producto = division * b
    resto = a - producto
    return resto
