def recommend_content_based(movie_title, num_recommendations=5):
    # Find movies that contain the input text (case-insensitive)
    matches = movies[movies['title'].str.contains(movie_title, case=False, regex=False)]
    if matches.empty:
        return ["Movie not found!"]
    idx = matches.index[0]
    sim_scores = list(enumerate(cosine_sim_content[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    recommended_movies = [movies['title'][i[0]] for i in sim_scores[1:num_recommendations+1]]
    return recommended_movies
