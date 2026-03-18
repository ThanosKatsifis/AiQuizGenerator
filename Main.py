import openai
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter as tk
window = ThemedTk(theme="yaru")
window.configure(themebg="yaru")
window.resizable(False, False)
window.title("AI Quiz Generator")
window.geometry('600x500')
score=0


client = openai.OpenAI(api_key = "ADD YOUR OWN HERE")

def check(reply):
    global score
    global scoretex
    global wrong
    if answer == reply:
        wrong.configure(text="Right Answer")
        score+=1
        scoretext.configure(text="Score :" + str(score))

    elif answer != reply:
        wrong.configure(text="Wrong Answer")

    generate_question()
def generate_question():
    global lblq
    global answer
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Generate a hard difficulty yes/no question in English about smartphones, suitable for students up to 18 years old, with a clear correct answer. Return the format: 'Question: <question> | Answer: <yes/no>'"},
            {"role": "user", "content": "Generate a simple yes/no question"}
        ]

    )
    print(response)
    result= response.choices[0].message.content.strip()
    print(result)
    question_part, answer_part = result.split(" | ")
    print(question_part)
    print(answer_part)
    question = question_part.replace("Question: ", "").strip()
    answer= answer_part.replace("Answer: ", "").strip().lower()
    print(question)
    print(answer)
    lblq.configure(text=question)


lblq=ttk.Label(window, text="")
lblq.place(x=180,y=50)
buttonyes=ttk.Button(window,text="Yes",width=10 ,command=lambda:check("yes"))
buttonyes.place(x=200,y=150)
buttonno = ttk.Button(window, text="No",width=10,command=lambda:check("no"))
buttonno.place(x=300, y=150)
wrong=ttk.Label(window,text="")
wrong.place(x=250,y=300)
scoretext = ttk.Label(window, text="Score: " + str(score))
scoretext.place(x=270,y=400)


generate_question()
window.mainloop()