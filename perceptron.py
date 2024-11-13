# -*- coding: utf-8 -*-
"""Perceptron.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10pnx_8l2KDKWXS7WMC3ckPXqu2mI4247

## **Codigo en general**
"""

import numpy as np

# Función de activación (Función escalón)
def funcion_activacion(x):
    return 1 if x >= 0 else 0

# Inicializar los pesos y el umbral
def inicializar_pesos(n_entradas):
    # Pesos inicializados entre -1 y 1
    pesos = np.random.uniform(-1, 1, n_entradas)
    umbral = np.random.uniform(-1, 1)
    return pesos, umbral

# Propagación hacia adelante
def propagacion(X, pesos, umbral):
    # Calcular y = X·W - θ
    suma = np.dot(X, pesos) - umbral
    return funcion_activacion(suma)

# Entrenamiento del perceptrón
def entrenar_perceptron(X, D, alfa, iteraciones):
    n_entradas = X.shape[1]
    pesos, umbral = inicializar_pesos(n_entradas)

    for _ in range(iteraciones):
        for i in range(len(X)):
            # Paso 1: Propagación
            y = propagacion(X[i], pesos, umbral)

            # Paso 2: Calcular el error
            error = D[i] - y

            # Paso 3: Retropropagación y actualización de pesos y umbral
            pesos += alfa * error * X[i]
            umbral -= alfa * error  # Actualizar umbral

    return pesos, umbral

# Probando el perceptrón
if __name__ == "__main__":
    # Datos de entrenamiento (X) y salidas deseadas (D)
    # Ejemplo simple con 2 entradas y salidas binarias
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    D = np.array([0, 0, 0, 1])  # Comportamiento de una puerta lógica AND

    # Parámetros de aprendizaje
    alfa = 0.1  # Tasa de aprendizaje
    iteraciones = 100  # Número de iteraciones

    # Entrenar el perceptrón
    pesos, umbral = entrenar_perceptron(X, D, alfa, iteraciones)

    # Imprimir resultados
    print("Pesos finales:", pesos)
    print("Umbral final:", umbral)

    # Evaluación del perceptrón
    for i in range(len(X)):
        y_pred = propagacion(X[i], pesos, umbral)
        print(f"Entrada: {X[i]}, Predicción: {y_pred}, Esperado: {D[i]}")

"""Función Escalón"""

import numpy as np

def funcion_escalon(x):
    return 1 if x >= 0 else 0

def inicializar_pesos(n_entradas):
    return np.random.uniform(-1, 1, n_entradas), np.random.uniform(-1, 1)

def propagacion(X, pesos, umbral):
    suma = np.dot(X, pesos) - umbral
    return funcion_escalon(suma)

def calcular_error(deseado, y):
    return deseado - y

def actualizar_pesos(pesos, umbral, alfa, error, X):
    return pesos + alfa * error * X, umbral - alfa * error

def entrenar_perceptron(X, D, alfa, iteraciones, umbral_error=0.01):
    pesos, umbral = inicializar_pesos(X.shape[1])
    for epoca in range(iteraciones):
        errores = []
        for i in range(len(X)):
            y = propagacion(X[i], pesos, umbral)
            error = calcular_error(D[i], y)
            errores.append(error ** 2)
            pesos, umbral = actualizar_pesos(pesos, umbral, alfa, error, X[i])
        mse = np.mean(errores)
        print(f"Época {epoca+1}, Error Promedio (MSE): {mse}")
        if mse < umbral_error:
            print("Error aceptable alcanzado.")
            break
    return pesos, umbral

# Datos de prueba
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
D = np.array([0, 0, 0, 1])
alfa = 0.1
iteraciones = 100
pesos, umbral = entrenar_perceptron(X, D, alfa, iteraciones)

"""Función Sigmoide"""

import numpy as np

def funcion_sigmoide(x):
    return 1 / (1 + np.exp(-x))

def inicializar_pesos(n_entradas):
    return np.random.uniform(-1, 1, n_entradas), np.random.uniform(-1, 1)

def propagacion(X, pesos, umbral):
    suma = np.dot(X, pesos) - umbral
    return funcion_sigmoide(suma)

def calcular_error(deseado, y):
    return deseado - y

def actualizar_pesos(pesos, umbral, alfa, error, X):
    return pesos + alfa * error * X, umbral - alfa * error

def entrenar_perceptron(X, D, alfa, iteraciones, umbral_error=0.01):
    pesos, umbral = inicializar_pesos(X.shape[1])
    for epoca in range(iteraciones):
        errores = []
        for i in range(len(X)):
            y = propagacion(X[i], pesos, umbral)
            error = calcular_error(D[i], y)
            errores.append(error ** 2)
            pesos, umbral = actualizar_pesos(pesos, umbral, alfa, error, X[i])
        mse = np.mean(errores)
        print(f"Época {epoca+1}, Error Promedio (MSE): {mse}")
        if mse < umbral_error:
            print("Error aceptable alcanzado.")
            break
    return pesos, umbral

# Datos de prueba
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
D = np.array([0, 0, 0, 1])
alfa = 0.1
iteraciones = 100
pesos, umbral = entrenar_perceptron(X, D, alfa, iteraciones)

"""Función Tanh"""

import numpy as np

def funcion_tanh(x):
    return np.tanh(x)

def inicializar_pesos(n_entradas):
    return np.random.uniform(-1, 1, n_entradas), np.random.uniform(-1, 1)

def propagacion(X, pesos, umbral):
    suma = np.dot(X, pesos) - umbral
    return funcion_tanh(suma)

def calcular_error(deseado, y):
    return deseado - y

def actualizar_pesos(pesos, umbral, alfa, error, X):
    return pesos + alfa * error * X, umbral - alfa * error

def entrenar_perceptron(X, D, alfa, iteraciones, umbral_error=0.01):
    pesos, umbral = inicializar_pesos(X.shape[1])
    for epoca in range(iteraciones):
        errores = []
        for i in range(len(X)):
            y = propagacion(X[i], pesos, umbral)
            error = calcular_error(D[i], y)
            errores.append(error ** 2)
            pesos, umbral = actualizar_pesos(pesos, umbral, alfa, error, X[i])
        mse = np.mean(errores)
        print(f"Época {epoca+1}, Error Promedio (MSE): {mse}")
        if mse < umbral_error:
            print("Error aceptable alcanzado.")
            break
    return pesos, umbral

# Datos de prueba
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
D = np.array([0, 0, 0, 1])
alfa = 0.1
iteraciones = 100
pesos, umbral = entrenar_perceptron(X, D, alfa, iteraciones)

"""Función ReLU"""

import numpy as np

def funcion_relu(x):
    return max(0, x)

def inicializar_pesos(n_entradas):
    return np.random.uniform(-1, 1, n_entradas), np.random.uniform(-1, 1)

def propagacion(X, pesos, umbral):
    suma = np.dot(X, pesos) - umbral
    return funcion_relu(suma)

def calcular_error(deseado, y):
    return deseado - y

def actualizar_pesos(pesos, umbral, alfa, error, X):
    return pesos + alfa * error * X, umbral - alfa * error

def entrenar_perceptron(X, D, alfa, iteraciones, umbral_error=0.01):
    pesos, umbral = inicializar_pesos(X.shape[1])
    for epoca in range(iteraciones):
        errores = []
        for i in range(len(X)):
            y = propagacion(X[i], pesos, umbral)
            error = calcular_error(D[i], y)
            errores.append(error ** 2)
            pesos, umbral = actualizar_pesos(pesos, umbral, alfa, error, X[i])
        mse = np.mean(errores)
        print(f"Época {epoca+1}, Error Promedio (MSE): {mse}")
        if mse < umbral_error:
            print("Error aceptable alcanzado.")
            break
    return pesos, umbral

# Datos de prueba
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
D = np.array([0, 0, 0, 1])
alfa = 0.1
iteraciones = 100
pesos, umbral = entrenar_perceptron(X, D, alfa, iteraciones)