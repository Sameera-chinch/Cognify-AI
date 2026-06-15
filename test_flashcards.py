from app.ai_utils import generate_flashcards

sample_text = """
Machine Learning is a branch of Artificial Intelligence.
Supervised learning uses labeled data.
Unsupervised learning uses unlabeled data.
"""

flashcards = generate_flashcards(sample_text)

print(flashcards)