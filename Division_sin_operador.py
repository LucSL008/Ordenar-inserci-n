def dividir(a, b):
    if b == 0:
        return "Error (Division con 0)"
    cociente = 0
    while a >= b:
        a -= b
        cociente += 1
    return cociente
