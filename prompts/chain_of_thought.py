CHAIN_OF_THOUGHT_PROMPT = """
Let's break this down into steps to make a quiz on a topic.
The output should include a 'questions' key with a list of question objects.
Each question has a type, Each question has choices. Each choice has a "key" (a, b, c, or d) and a "value". i.e. "key": "A", value: "milk"
There is an answer is that corresponds to the choice "key".
Make 2 questions total.
Output in JSON format.
Let's make the quiz on {input} 
"""


