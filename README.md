## Fundamentação Matemática
Este projeto foi desenvolvido com o objetivo de aplicar conceitos matemáticos revisados na pós-graduação, especialmente no que diz respeito à representação vetorial de dados e cálculo de similaridade.

Ao representar descrições textuais como vetores em um espaço vetorial, cada filme/série passa a ocupar uma posição geométrica. A recomendação emerge da proximidade angular entre esses vetores. Dessa forma, foi desenvolvido um sistema de recomendação que explora diretamente propriedades geométricas do espaço vetorial para medir proximidade entre diferentes filmes e séries presentes no catálogo da Netflix.

## Dados
Os dados se encontram em [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download).

## Estrutura do Projeto
- data/: dados brutos e processados
- notebooks/: exploração inicial
- src/: módulos do projeto
- main.py: script principal

## Tecnologias Utilizadas
- Python
- Pandas
- Numpy
- NLTK
- Scikit-learn
- Git

## Como Executar
1. Clone o repositório:

git clone <https://github.com/douglastein/movies-and-series_recommendations>

2. Crie e ative um ambiente virtual:

python -m venv .venv

Windows:
.venv\Scripts\activate

Linux/Mac:
source .venv/bin/activate

3. Instale as dependências:

pip install -r requirements.txt

Após instalar as dependências, execute uma vez:

python -m nltk.downloader stopwords

4. Execute o projeto:

python -m main