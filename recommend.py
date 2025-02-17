import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load HuggingFace model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Load/process dataset and precompute embeddings
def process_dataset(csv_path):
    df = pd.read_csv(csv_path).fillna('') 
    df = df.drop_duplicates(subset=['book_name'], keep='first')  
    # Precompute embeddings
    df['embeddings'] = list(model.encode(df['summaries'].tolist(), convert_to_numpy=True))  

    return df

# Compute similarity and get recommendations
def get_recommendations(user_query, dataset, top_n):
    query_embedding = model.encode([user_query], convert_to_numpy=True)
    similarities = cosine_similarity(query_embedding, np.stack(dataset['embeddings']))[0]
    top_indices = np.argsort(similarities)[::-1][:top_n]
    return [(dataset['book_name'].iloc[i], dataset['summaries'].iloc[i], similarities[i]) for i in top_indices]

if __name__ == "__main__":
    dataset = process_dataset("data/mindfulness_books.csv")

    # Prompt user for input and handle errors
    user_query = input("Enter a book description: ").strip()
    if not user_query:
        print("Invalid input. Please enter a valid book description.")
        exit()

    # Prompt user for number of recommendations and handle errors
    try:
        top_n = int(input("How many recommendations? ").strip())
        if top_n <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number. Please enter a positive integer.")
        exit()

    recommendations = get_recommendations(user_query, dataset, top_n)

    # Unpack recommendations tuple and display to user
    print("\nTop Book Recommendations:")
    for i, rec in enumerate(recommendations, 1):
        title, summary, similarity = rec  
        print(f"{i}. {title}")
        print(f"   Similarity: {similarity:.4f}")
        print(f"   Summary: {summary}\n")
