##
# This program shows a simple quiz with one question.
#
from class_questions import Question
# Create the question and expected answer.
q = Question()
q.setText("Who is the inventor of Python?")
q.setAnswer("Guido van Rossum")
# Display the question and obtain user’s response.
q.display()
response = input("Your answer: ")
print(q.checkAnswer(response))