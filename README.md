# Book Recommendation System

## Summary
This project is a Book Recommendation System that suggests books on mindfulness and mental health based on user input. It utilizes the sentence-transformers/all-MiniLM-L6-v2 model to compute semantic similarities between input descriptions and book summaries.

## Dataset
The dataset used for this project consists of ~300 book summaries about mindfulness and mental health (Source: https://fourminutebooks.com/category/mindfulness/). It is stored as a CSV file (`data/mindfulness_books.csv`) with the following structure:

- `book_id`: ID of the book
- `book_name`: Title of the book
- `summaries`: Short descriptions of the book
- `categories`: Genres of the book

## Setup
### Requirements
- Python 3.8+
- Virtual environment (recommended)

### Installation
1. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Code
To run the recommendation system, execute the following command in your terminal:
```sh
python recommend.py
```
You will be prompted to enter a book description and the number of recommendations you want.

## Results
After running the script, the system will output a list of recommended books based on the input description. Example output:
```
Enter a book description: Guide to maintaining a good work/life balance
How many recommendations? 3

Top Book Recommendations:
1. The Burnout Fix
   Similarity: 0.7208
   Summary:  delivers practical advice on how to thrive in the dynamic working environment we revolve around every day by setting healthy boundaries, keeping a work-life balance, and prioritizing our well-being.

2. Designing Your Work Life
   Similarity: 0.5260
   Summary:  is a helpful guidebook for anyone who wants to create and maintain a work environment that is both happy and productive by working with what they already have, rather than keep on changing jobs in hope of finding better.

3. The 5 Choices
   Similarity: 0.5128
   Summary:  teaches us how to reach our highest potential in the workplace and achieve the top level of productivity through a series of tips and tricks and work habits that can change your life right away if you’re willing to give them a try.
```

## Notes
- Duplicate book titles are removed to improve recommendation diversity.
- Ensure your input description is clear and specific for better results.

---

I hope this helps you discover the perfect book! Prioritizing mental health and mindfulness is more important than ever in today's fast-paced world.

---
<sub>Considering my experience with Python and NLP, my desired salary range for this role is $24-$30. I am definitely open to negotiation though!</sub>