questions = """Why?
How?
What time?
Where am I?
Who won?
Why not?
How much?
When is it?
What happened??
What for?
Where now?
Who's calling?
Why this?
How much?
When's dinner?
What time?
What else?
Where's home?
Who said?
Why ask?
How deep?
When will it?
How can this?
What went wrong?
Who can help?
What do you?
Where is that?
How should I?
Why can't I?
What's the problem?
What is reality?
How do I learn?
What is your capability?
Are you always correct?
How is this possible?
What's your main limitation?
Can you predict outcomes?
How do I build relationships?
Why do stars look distant?
Why care?"""

# Career and professional development questions
problems = """
I don’t know how to fix this broken relationship.
I’m struggling to pay my bills this month.
I can’t seem to lose weight no matter what I try.
I feel like I’m failing at my job.
I don’t know how to apologize without making it worse.
I can’t afford to fix my car right now.
I feel like I’m losing my best friend.
I don’t know how to deal with all this stress.
I can’t figure out how to meet new people.
I feel stuck in a dead-end career.
I don’t know how to study for this exam.
I can’t seem to get over my ex.
I feel like I’m constantly disappointing my family.
I can’t find a solution to this problem at work.
I don’t know how to manage my time better.
I can’t stop procrastinating, and it’s ruining everything.
I feel like I’m always misunderstood by others.
I don’t know how to confront my boss about this issue.
I can’t decide if I should stay in this relationship.
I feel like I’m not good enough for this role.
I don’t know how to explain my feelings to them.
I can’t stop feeling anxious about the future.
I don’t know how to balance work and school.
I feel like I’m running out of time to succeed.
I can’t figure out how to solve this technical issue.
I don’t know how to move past this failure.
I feel like I’m always overthinking everything.
I can’t seem to get along with my coworkers.
I don’t know how to say no without feeling guilty.
I can’t figure out what to do with my life.
I feel like I’m not learning anything new anymore.
I don’t know how to improve my communication skills.
I can’t stop comparing myself to others.
I don’t know how to fix my financial situation.
I feel like I’m constantly letting people down.
I can’t decide what’s best for my career.
I don’t know how to deal with rejection.
I feel like I’m wasting my potential.
I can’t figure out how to stop arguing with my partner.
I don’t know how to regain control of my life.
"""

# Relationship and social questions
statements = """
Hello
Goodbye
Yes
No
Thanks
Sorry
Night
Cheers
Congrats
You are right.
I don’t care.
That sounds great.
I feel fantastic.
I am ready.
I trust you.
That’s so funny.
It’s perfectly timed.
I’m very happy.
That was helpful.
Teach me something new.
Explain this step by step.
Help me make progress.
Bring this idea alive.
Focus my energy today.
Help me adapt faster.
Take me beyond basics.
This feels like real progress.
That’s absolutely true.
I’m connecting the dots now.
This opens up new possibilities.
I think we’re onto something.
	34.	I’m trying to figure out why we’re seeing this so differently.
	35.	It’s not that your idea won’t work—it’s that it might create other issues.
	43.	It’s not that I don’t trust you—it’s that I need to be sure.
	44.	I think we’re focusing too much on the details and not enough on the goal.
	45.	I understand your logic, but I don’t think it applies in this situation.
	71.	I’m trying to focus on the outcome, not just the process.
	83.	It’s not that I’m unwilling to compromise—I just think this is too important to overlook.
	87.	Even if we disagree, I still respect where you’re coming from.
	33.	Even if it seems like the right choice, there’s a risk we’re overlooking.
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
__all__ = ['questions', 'problems', 'statements', 'get_questions']