🚀 AI Yes/No Quiz Generator
A fast, fun, OpenAI‑powered quiz game built with Python + Tkinter!
This project is a lightweight desktop app that generates hard yes/no questions about smartphones using the OpenAI API. Players answer using big friendly buttons, earn points, and get instant feedback — all wrapped in a clean themed UI.
Perfect for students, tech lovers, or anyone who wants to test their smartphone knowledge with AI‑generated challenges.

🎮 Features
- 🤖 AI‑generated questions using GPT‑3.5 Turbo
- 📱 Smartphone‑themed yes/no trivia
- 🎯 Real‑time scoring
- 🎨 Modern UI with ttkthemes
- ⚡ Instant feedback (“Right Answer” / “Wrong Answer”)
- 🔄 New question after every click

🧠 How It Works
The app sends a prompt to OpenAI asking for:
- A hard difficulty yes/no question
- A clear correct answer
- A strict format:
Question: <question> | Answer: <yes/no>


The program then:
- Splits the response into question + answer
- Displays the question in the GUI
- Checks the user’s answer
- Updates the score
- Generates a new question
Simple, fast, addictive.

🛠️ Installation
1. Clone the repo
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo


2. Install dependencies
pip install openai tkinter ttkthemes


Note: tkinter is included with most Python installations.

3. Add your OpenAI API key
Inside the script, replace:
client = openai.OpenAI(api_key="write your own")


with your actual key.

▶️ Run the App
python main.py


A window will pop up with:
- A question
- Two big buttons: Yes and No
- Your score
- Feedback text

📸 Screenshot (Optional)
You can add one here later:
![App Screenshot](screenshot.png)



📂 Project Structure
📁 project-folder
 ├── main.py
 ├── README.md
 └── (optional) screenshot.png



🧩 Code Overview
Main components:
- generate_question()
Calls OpenAI, parses the response, updates the label.
- check(reply)
Compares user input with the correct answer and updates score.
- Tkinter UI
Buttons, labels, and a themed window.

⚠️ Requirements
- Python 3.8+
- OpenAI API key
- Internet connection

📜 License
MIT License — feel free to use, modify, and share.


