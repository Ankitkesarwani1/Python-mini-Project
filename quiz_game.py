import tkinter as tk
from tkinter import messagebox

#Sample Quiz Question and Answer
quiz_data=[
    {
        "question":"Which is the largest planent in the solar system?",
        "choices":["Earth","Jupiter","Saturn","Mars"],
        "answer":"Jupiter"
    },
    {
        "question":"What is the capital of India?",
        "choices":["Delhi","Mumbai","UttarPradesh","Lacknow"],
        "answer":"Delhi"
    },
    {
        "question":"What is the chemical symbol of gold?",
        "choices":["Go","Au","Ag","Gd"],
        "answer":"Au"
    },
    {
        "question":"Which country is known as the 'Land of the Rising Sun?",
        "choices":["China","Japan","Thialand","South Korea"],
        "answer":"Japan"
    },
    {
        "question":"What is the capital of Maharashtra?",
        "choices":["Pune","Mumbai","Nashik","Thane"],
        "answer":"Mumbai"
    }
]
#Function to check the answer
def check_answer(selected_choice):
    global current_question, score
    if selected_choice == quiz_data[current_question]["answer"]:
        score += 1

    current_question += 1
    if current_question < len(quiz_data):
        update_question()
    else:
        show_final_score()

#Function to update the question
def update_question():
    question_label.config(text=quiz_data[current_question]["question"])
    for i, choice in enumerate(quiz_data[current_question]["choices"]):
        buttons[i].config(text=choice, command=lambda c=choice: check_answer(c))

#Function to show the final score
def show_final_score():
    messagebox.showinfo("Quiz Completed" , f"You Scored {score} out of {len(quiz_data)}")
    root.quit()

#Setting up the GUI
root=tk.Tk()
root.title("General Knowlege Quiz Game")

current_question = 0
score = 0

question_label = tk.Label(root, text=quiz_data[current_question]["question"], font=("Arial", 14))
question_label.pack(pady=20)

buttons =[]
for i in range(5):
    btn=tk.Button(root, text="", font=("Arial", 14))
    btn.pack(pady=5, fill=tk.X)
    buttons.append(btn)

update_question()

root.mainloop()
