from database import init_db, add_pet, add_adopter

init_db()

add_pet("Luna", "Perro", 2, "Ansiedad leve")
add_pet("Milo", "Gato", 1, "Muy sociable")

add_adopter("Sofía Martínez", "Madrid", "Primerizo")
add_adopter("Carlos Pérez", "Barcelona", "Intermedio")

print("Datos demo creados")
