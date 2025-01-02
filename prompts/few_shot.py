FEW_SHOT_PROMPT = """
Generate a quiz on {input} with one multiple choice question (5 choices).
The output should be in JSON.

Example output for a quiz is: questions=[Question(question='What is the primary leavening agent in most traditional sponge cakes?', choices=[Choice(key='A', value='Baking soda'), Choice(key='B', value='Baking powder'), Choice(key='C', value='Yeast'), Choice(key='D', value='Air beaten into the eggs')], answer='D')])
"""
