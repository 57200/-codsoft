 🎥 Recommendation System
```markdown
# Movie Recommendation System 🎬

## 📌 Project Overview
This project implements a **movie recommendation system** using two approaches:
- **Collaborative Filtering** – based on user ratings similarity.
- **Content-Based Filtering** – based on movie genres similarity.

It demonstrates how recommendation engines are built in real-world systems (e.g., Netflix, Amazon).

---

## ✨ Features
- Collaborative filtering using **user-movie rating matrix**.  
- Content-based filtering using **TF-IDF + cosine similarity** on movie genres.  
- Suggests top-N recommended movies for a user or a given movie.  
- Simple Python scripts (can be extended into a web app).  

---

## 🛠️ Tech Stack
- **Python** – Core language.  
- **Pandas, NumPy** – Data handling.  
- **Scikit-learn** – TF-IDF, cosine similarity.  

---

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the script:

python recommendation_system.py


3. Example usage:

Collaborative filtering for user_id = 1.

Content-based filtering for "Toy Story (1995)".

📂 Folder Structure
recommendation_system/
├── recommendation_system.py  # Main logic
├── app.py                    # Additional helper functions
├── data/                     # Movie & ratings CSVs
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
