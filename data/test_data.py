questions = """Can you explain quantum mechanics?
How do plants make oxygen?
Where is it?
How do we?
What is life?
Where at?
Who's next?
How bad?
When again?
What?"""

problems = """
I don’t know how to stay consistent with my goals.
I can’t seem to connect with people around me.
I don’t know how to fix this mistake I made.
I feel like I’m not achieving anything meaningful.
I can’t find the motivation to keep going.
I don’t know how to overcome my fear of failure.
I feel like my efforts never pay off.
I can’t stop worrying about what others think of me.
I don’t know how to handle this conflict.
I can’t figure out why I’m so unhappy.
"""

statements = """
I’m seeing things more clearly.
Every step teaches me something.
I’m realizing how this matters.
I keep losing track of myself.
My dreams feel further away fuck.
	14.	I just don’t see how this could work out the way you’re suggesting.
Welcome
This is amazing.
I totally agree.
It’s all good.
"""

# Add more categories as needed...

def get_questions(category):
    """
    Retrieve questions for a specific category.
    
    Args:
        category (str): The category of questions to retrieve
        
    Returns:
        str: The questions string for the specified category
    """
    categories = {
        'questions': questions,
        'problems': problems,
        'statements': statements
    }
    
    return categories.get(category, "Category not found")

# Export all categories
__all__ = ['testing_questions', 'testing_problems', 'testing_statements', 'get_questions']