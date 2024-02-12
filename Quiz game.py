# Define the questions, options, and correct answers as lists
questions = [
    "What is the capital of India?",
    "Which of these is a odd number?",
    "Who is father of computer in india?",
    "what country has the most islands in the world?",
    "what is the national flower of india?",
]

options = [
    ["A) Delhi", "B) Mumbai", "C) Hyderabad", "D) Bengaluruss"],
    ["A) 12", "B) 17", "C) 20", "D) 28"],
       ["A) Dr.Ram", "B) Dr.Rajesh", "C) Dr.L.U.Vamshi",
               "D) Dr.Vijay Bhatkar" ],
           ["A) India", "B) Canada", "C) Andes", "D) Sweden"],
           ["A) Lotus", "B) Rose", "C) Sunflower", "D) Jasmine"],
]

answers = ["A","B", "D", "D", "A" ]

# Define a function to display a question and its options
def display_question(index):
    print(questions[index])
    for option in options[index]:
        print(option)

# Define a function to validate the user input and return True or False
def validate_input(answer):
    if answer.upper() in ["A", "B", "C", "D"]:
        return True
    else:
        return False

# Define a function to check the user answer and return True or False
def check_answer(index, answer):
    if answer.upper() == answers[index]:
        return True
    else:
        return False

# Define a variable to store the user score
score = 0

# Loop through the questions and ask the user for their answers
for i in range(len(questions)):
    # Display the question and options
    display_question(i)
    # Prompt the user for their answer
    user_answer = input("Enter your answer: ")
    # Validate the user input
    while not validate_input(user_answer):
        print("Invalid input. Please enter A, B, C, or D.")
        user_answer = input("Enter your answer: ")
    # Check the user answer and provide feedback
    if check_answer(i, user_answer):
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is " + answers[i])
    # Print a blank line for spacing
    print()

# Display the user's final score
print("You have completed the quiz.")
print("Your final score is " + str(score) + " out of " + str(len(questions)))
