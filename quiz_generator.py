import random
import spotipy
import json
import os

# Load JSON question_templates into object
with open("question_templates.json", "r") as json_file:
    question_templates = json.load(json_file)
    
def generate_quiz(length):
    quiz = []
    # Create a pool of possible IDs (assuming IDs range from 1 to 12)
    id_pool = list(range(1, 13))
    
    # Select 'length' number of unique IDs from the pool
    selected_ids = random.sample(id_pool, length)
    
    # Construct questions with selected IDs
    for question_id in selected_ids:
        question = {"id": question_id}
        quiz.append(question)
        
    print(quiz)

def generate_answer(id):
    return

generate_quiz(5)