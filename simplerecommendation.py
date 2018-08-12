import pandas as pd
metadata = pd.read_csv('movies_metadata.csv', low_memory=False)


C = metadata['vote_average'].mean()

m = metadata['vote_count'].quantile(0.90)

q_movies = metadata.copy().loc[metadata['vote_count']>=m]


def weighted_rating(a, m=m, C=C):

    v = a['vote_count']
    R = a['vote_average']

    return (v/(m+v)*R) + (m/(m+v)*C)


q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)

print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(20))
print(q_movies.shape)
