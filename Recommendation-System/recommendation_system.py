
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')

movie_data = pd.merge(ratings, movies, on='movieId')

user_movie_ratings = movie_data.pivot_table(index='userId', columns='title', values='rating').fillna(0)
cosine_sim = cosine_similarity(user_movie_ratings)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
cosine_sim_content = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_collaborative(user_id, num_recommendations=5):
    similar_users = cosine_sim[user_id - 1]
    similar_users_ratings = user_movie_ratings.iloc[similar_users.argsort()[-num_recommendations:]]
    recommended_movies = similar_users_ratings.mean(axis=0).sort_values(ascending=False).index.tolist()
    return recommended_movies

def recommend_content_based(movie_title, num_recommendations=5):
    idx = movies.index[movies['title'] == movie_title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim_content[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    recommended_movies = [movies['title'][i[0]] for i in sim_scores[1:num_recommendations+1]]
    return recommended_movies

if __name__ == "__main__":
    user_id = 1
    print("Collaborative Filtering Recommendations:")
    print(recommend_collaborative(user_id))
    movie_title = "Toy Story (1995)"
    print(f"\nContent-Based Filtering Recommendations for '{movie_title}':")
    print(recommend_content_based(movie_title))
