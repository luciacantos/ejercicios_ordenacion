'''
B. Prevención de riegos
Hay n niños que quieren subir a una noria, y tu tarea es encontrar una góndola para cada
niño.
Cada góndola puede tener uno o dos niños, y además, el peso total en una góndola no
puede exceder x. Conoces el peso de cada niño.
¿Cuál es el número mínimo de góndolas necesarias para los niños?
'''

n, x = map(int, input().split())
pesos = list(map(int, input().split()))

pesos.sort()

izq = 0
dcha = n - 1
gondolas = 0
