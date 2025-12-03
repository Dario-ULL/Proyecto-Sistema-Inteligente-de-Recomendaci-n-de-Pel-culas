import json
import os

# Función para cargar los usuarios desde el archivo JSON, si existe
def load_users():
    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r') as json_file:
            try:
                # Intentamos cargar el archivo JSON
                return json.load(json_file)
            except json.JSONDecodeError:
                # Si el archivo está vacío o es inválido, devolvemos una lista vacía
                print("El archivo está vacío o no contiene datos válidos.")
                return []
    else:
        return []

# Función para guardar usuarios en el archivo JSON
def save_users(users):
    with open('usuarios.json', 'w') as json_file:
        json.dump(users, json_file, indent=4)

# Función para registrar un nuevo usuario
def sign_up_users():
    users = load_users()

    # Asignar un ID al nuevo usuario: el siguiente ID es uno mayor que el último existente
    if users:
        new_id = users[-1]["id"] + 1  # El último ID + 1
    else:
        new_id = 200949  # Si no hay usuarios, el primer ID será 200949

    name = input("Introduce el nombre: ")
    email = input("Introduce el email: ")
    password = input("Introduce la contraseña: ")
    peliculas_votadas = [{}]

    user = {
        "id" : new_id,
        "nombre": name,
        "email": email,
        "password": password,
        "peliculas_votadas": peliculas_votadas
        #"peliculas_votadas": [
        #    {
        #        "nombre": N
        #        "votacion": NULLL
        #    }
        #]
    }

    # Agregar el nuevo usuario a la lista de usuarios
    users.append(user)

    # Escribir en el archivo JSON
    save_users(users)

    print(f"Usuario registrado con éxito. El ID asignado es: {new_id}")

if __name__ == "__main__":
    sign_up_users()
