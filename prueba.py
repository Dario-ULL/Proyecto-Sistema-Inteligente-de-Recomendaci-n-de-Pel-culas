import pandas as pd

# Configurar Pandas para mostrar títulos completos
pd.set_option('display.max_colwidth', None)

# Cargar CSV
ratings = pd.read_csv("/home/alumnos.ull.es/43/alu0101408095/Desktop/SI/ml-32m/ratings.csv")
movies = pd.read_csv("/home/alumnos.ull.es/43/alu0101408095/Desktop/SI/ml-32m/movies.csv")

# Unir ratings y movies
df = ratings.merge(movies, on="movieId")

# Contar cuántos ratings tiene cada película y calcular promedio
conteo_ratings = df.groupby(["movieId", "title", "genres"])["rating"].agg(["count", "mean"]).reset_index()
conteo_ratings.rename(columns={"count":"num_ratings", "mean":"rating_promedio"}, inplace=True)

# Filtrar películas con al menos 100 votos
peliculas_filtradas = conteo_ratings[conteo_ratings["num_ratings"] >= 100].copy()  # copia explícita

# Asignar género principal
peliculas_filtradas.loc[:, "genre_principal"] = peliculas_filtradas["genres"].str.split("|").str[0]

# Obtener top 3 por género principal
top_por_genero = peliculas_filtradas.sort_values("rating_promedio", ascending=False).groupby("genre_principal").head(3)

# Ordenar por género alfabéticamente
top_por_genero = top_por_genero.sort_values("genre_principal").reset_index(drop=True)

# Mostrar resultados
print(top_por_genero[["movieId", "genre_principal", "title", "rating_promedio", "num_ratings"]])

# Guardar en JSON incluyendo movieId
top_por_genero[["movieId", "genre_principal", "title", "rating_promedio", "num_ratings"]].to_json(
    "/home/alumnos.ull.es/43/alu0101408095/Desktop/SI/top_por_genero.json",
    orient="records",
    force_ascii=False,
    indent=4
)
