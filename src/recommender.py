import pandas as pd
import numpy as np

def recommendation_system(title: str, df: pd.DataFrame, similaridades: np.ndarray):
    """
    Retorna uma lista com os 5 títulos mais semelhantes ao título fornecido.

    param title: Título da obra de interesse.
    param df: Dados vetorizados.
    param similaridades: Distâncias entre os vetores de cada título registrado nos dados.
    return: Lista com os 5 títulos mais semelhantes ao fornecido.
    """

    if title not in df['title'].values:
        return "Título não encontrado."

    # Obtém o índice do título passado como argumento
    index = df[df['title'] == title].index[0]
    
    # São verificado os títulos com vetores de menores distâncias em relação ao título passado como argumento
    distances = sorted(
        list(enumerate(similaridades[index])),
        reverse = True,
        key = lambda x: x[1]
    )
    
    # E então são considerados os 5 tírulos com menor distância, ou seja, com maior semelhança
    recommendations = []
    for i in distances[1:6]:
        recommendations.append(df.iloc[i[0]].title)
    
    return recommendations

