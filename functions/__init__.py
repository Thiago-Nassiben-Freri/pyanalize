
import statistics

def calcular_estatisticas(numeros):
    numeros = numeros.split(',')
    numeros = [float(numero.strip()) for numero in numeros if numero.strip()]
    
    if not numeros:
        return None, None, None
    
    media = statistics.mean(numeros)
    moda = statistics.mode(numeros)
    mediana = statistics.median(numeros)
    
    return media, moda, mediana
