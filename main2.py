from clases import *

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print("\n--------------------------------------")
print(f'\nDatos del Auto Particular: {particular}')
print(f'\nDatos del Auto Carga: {carga}')
print(f'\nDatos de la Bicicleta: {bicicleta}')
print(f'\nDatos de la Motocicleta: {motocicleta}')
print("\n--------------------------------------")
print("\nMotocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))
print("\n--------------------------------------")