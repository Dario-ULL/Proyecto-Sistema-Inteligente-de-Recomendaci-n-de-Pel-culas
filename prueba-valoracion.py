import json 
import os
import time
import csv

def read_movies():
    if os.path.exists('top_por_genero.json'):
        with open('top_por_genero.json', 'r') as archivo_json:
            try:
                # Intentamos cargar el archivo JSON
                return json.load(archivo_json)
            except json.JSONDecodeError:
                # Si el archivo está vacío o es inválido, devolvemos una lista vacía
                print("El archivo está vacío o no contiene datos válidos.")
                return []
    else:
        return []
    
def select_genres():
    existing_genres = ["Action", "Adventure", "Animation", "Children", "Comedy",
                       "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", 
                       "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", 
                       "Thriller", "War", "Western"]
    
    genres_index = 1
    for genre in existing_genres:
        print("Genero[%d] : %s" %(genres_index, genre))
        genres_index += 1

    print("\n")

    favourite_genres = []
    while len(favourite_genres) < 3 :
        try: 
            selected = int(input("Introduce el genero (numero): "))
            if 1 <= selected <= len(existing_genres):
                if existing_genres[selected - 1] not in favourite_genres:
                    favourite_genres.append(existing_genres[selected - 1])
                else:
                    print("Ya has seleccionado ese género. Prueba otra vez")
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Debes introducir un número válido.")

    print("\n")
          
    return favourite_genres
        
def insert_in_ratings_new_movie(userID, movieID, rating):
    timestamp = int(time.time())

    with open("/Trainsets-20251202T111802Z-1-001/Trainsets/trainset_32m_raw_ratings.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([userID, movieID, rating, timestamp])



def rate_movie(movieId):
    while True:
        try:
            num = float(input("Valore la siguiente película del 0 al 5 en intervalos de 0,5: "))
            if 0.5 <= num <= 5 and (num * 10) % 5 == 0:
                return num
            else:
                print("Debe estar entre 0.5 y 5 y de 0.5.")
        except ValueError:
            print("Entrada inválida.")
    

def show_movies():
    movies = read_movies()
    favourite_genres = select_genres()
    rating
    for genre in favourite_genres: 
        print("Peliculas del genero {genre}")
        for movie in movies:
            if genre == movie["genre_principal"]:
                print ("%s[%d]" %(movie["title"], movie["movieId"]))
                rating = rate_movie(movie["movieId"])         
                print("\n")
    return [movie["movieId"], rating]
    

if __name__ == "__main__":
    show_movies()