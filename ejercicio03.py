'''
C. SSIFF
Se está dando lugar el Festival de Cine de San Sebastián. Tienes el abono completo y
quieres ver tantas películas como puedas.
Dispones de todos los horarios con la hora a la que empieza y acaba cada película.
¿Cuántas películas puedes ver como máximo?
'''

n = int(input())
horarios = []

for _ in range (n):
    a,b = map(int, input().split())
    horarios.append((a,b))

horarios.sort(key=lambda x: x[1])

total = 0
ultima_pelicula = 0

for inicio, final in horarios:
    if inicio >= ultima_pelicula:
        total += 1
        ultima_pelicula = final
