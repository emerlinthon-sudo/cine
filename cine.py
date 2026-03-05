# Programa: Reserva de asiento en cine (3x4)

# Crear matriz de 3 filas x 4 columnas con asientos libres (0)
asientos = [[0 for j in range(4)] for i in range(3)]

# Pedir fila y columna
f = int(input("Ingrese fila (0 a 2): "))
c = int(input("Ingrese columna (0 a 3): "))

# Reservar asiento
asientos[f][c] = 1

# Mostrar estado de la sala
print("Estado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
cd C:\Users\emerl\Documents
python cine.py
Ingrese fila (0 a 2): 1
Ingrese columna (0 a 3): 2
Estado de la sala:
0 0 0 0
0 0 1 0
0 0 0 0
