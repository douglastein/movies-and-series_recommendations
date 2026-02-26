def recommendation_system(title, df, similaridades):

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

