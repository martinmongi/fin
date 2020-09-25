
def valor_presente(precio, cuotas, inflacion):
    inflacion_mensual = 1. / (inflacion / 100. + 1.)**(1. / 12.)
    return (precio/cuotas) * (1-inflacion_mensual**cuotas)/(1-inflacion_mensual)

precio = float(input("Precio: "))
cuotas = int(input("Cuotas sin interés: "))
inflacion = float(input("Inflación esperada mientras pagás las cuotas: "))
valor = valor_presente(precio, cuotas, inflacion)

print("Con esa inflación, ese plan de pagos es equivalente a pagar $" + \
    str(round(valor,2)) + " al contado.")

precio_contado = float(input("Precio al contado: "))

print("Te conviene pagarlo " + \
    ("al contado." if precio_contado < valor else "en cuotas."))
print("Te ahorrás $" + str(round(abs(precio_contado-valor),2)))

from scipy import optimize

def dif_contado(infla):
    return valor_presente(precio, cuotas, infla) - precio_contado

inflacion_equivalente = optimize.newton(dif_contado, .99)

print("Para que las dos formas de pago sean igualmente convenientes, la " + \
    "inflación debería ser de " + str(round(inflacion_equivalente,2)) + "%")
print("Si esperás que la inflación sea mayor, te conviene pagarlo en " + \
    "cuotas. Si no, al contado.")
