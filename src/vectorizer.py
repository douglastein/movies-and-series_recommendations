import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def custom_analyzer(text):
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [ps.stem(word) for word in tokens]
    return tokens

def generate_similarity_matrix(path_to_data):

    df = pd.read_csv(path_to_data)

    cv = CountVectorizer(max_features=5000, analyzer=custom_analyzer)
    vectors = cv.fit_transform(df['tags']).toarray()

    similarity = cosine_similarity(vectors)

    return df, similarity
