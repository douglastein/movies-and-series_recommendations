from src.vectorizer import generate_similarity_matrix
from src.recommender import recommendation_system

if __name__ == "__main__":
    df, similaridades = generate_similarity_matrix(r"data/processed/netflix_titles_processed.csv")

    # titulo = "The Walking Dead"
    titulo = str(input("Digite o nome de um filme/série: ")).strip()

    recomendacoes = recommendation_system(titulo, df, similaridades)

    for recs in recomendacoes:
        print(recs)
    