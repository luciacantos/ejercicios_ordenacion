'''
A. Pasando lista
Eres profesor de una clase de la que te piden que pases asistencia. Cada alumno, según
llega a clase, confirma su asistencia y en la lista aparece su número identificador como un
entero. Sin embargo, el sistema es algo nuevo y a ratos vuelve a aparecer por error en la
lista un alumno ya registrado.
Tu objetivo es, dada la lista de identificadores A con longitud n, obtener el número de
identificadores únicos en ella sin hacer uso de estructuras adicionales (sets, listas, etc).
'''

t = int(input()) # nº casos

for _ in range (t):
    n = int(input())
    A = list(map(int, input().split()))

