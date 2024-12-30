ZERO_SHOT_PROMPT = """
Generate a quiz on {input} with one multiple choice question (4 choices).
The output should include a 'questions' key with a list of question objects.
Each question object should have 'question', 'choices', and 'answer' keys. The choices key should be in "key": "A", "value": "value" format
"""
