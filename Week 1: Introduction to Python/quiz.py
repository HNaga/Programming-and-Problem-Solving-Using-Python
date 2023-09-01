# This program creates a quiz and calculates the total and average score,
# with an option to display the correct answers.

# Import the random module.
import random

# Create a list of questions and answers.
questions = [
    ["What is the capital of Japan?", "Tokyo"],
    ["What is the largest ocean in the world?", "Pacific Ocean"],
    ["What is the chemical formula for water?", "H2O"],
    ["What is the square root of 25?", "5"],
    ["What is the sum of 10 and 15?", "25"],
    ["What is the difference between 20 and 10?", "10"],
    ["What is the product of 2 and 3?", "6"],
    ["What is the quotient of 10 and 5?", "2"],
    ["What is the remainder of 10 divided by 5?", "0"],
    ["What is the first 10 prime numbers?", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]],
]

# Generate a random number for the number of questions to ask.
number_of_questions = random.randint(1, len(questions))

# Get the user's answers to the questions.
answers = []
wrong_answers = []
for i, question in enumerate(questions[:number_of_questions]):
    answer = input(question[0] + ": ")
    answers.append(answer)
    if answer != question[1]:
        wrong_answers.append([question[0], answer, question[1]])

# Calculate the total score.
total_score = 0
for i in range(number_of_questions):
    if answers[i] == questions[i][1]:
        total_score += 1

# Calculate the average score.
average_score = total_score / number_of_questions

# Display the results.
print("Your total score is", total_score)
print("Your average score is", average_score)

# Display the correct answers, if desired.
print("The correct answers are:")
for question, answer in questions[:number_of_questions]:
    print(question, ":", answer)

# Display the wrong answers.
print("The wrong answers are:")
for question, wrong_answer, correct_answer in wrong_answers:
    print(question, ":", wrong_answer, "(correct answer:", correct_answer, ")")