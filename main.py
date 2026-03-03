from src.vectorizer import generate_similarity_matrix
from src.recommender import recommendation_system

def main():
    print("Sistema de Recomendação de filmes e séries")
    print("Digite 'sair' para encerrar.\n")

    df, similarity = generate_similarity_matrix(
        "data/processed/netflix_titles_processed.csv"
    )

    while True:
        titulo = input("Digite o nome de um filme ou série: ")

        if titulo.lower() == "sair":
            print("\nEncerrando sistema.")
            break

        recommendations = recommendation_system(titulo, df, similarity)
        print("\nRecomendações:")
        for r in recommendations:
            print(f"- {r}")
        print()


if __name__ == "__main__":
    main()
