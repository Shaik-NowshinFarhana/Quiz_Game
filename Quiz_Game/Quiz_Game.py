# # # quiz_game_app.py
# # import streamlit as st
# # import random
# # import time
# # import json
# # from pymongo import MongoClient

# # # ✅ FIRST Streamlit command
# # st.set_page_config(page_title="Quiz Game", layout="centered")

# # # MongoDB Connection
# # @st.cache_resource
# # def get_db():
# #     client = MongoClient("mongodb://localhost:27017")  # Replace with Atlas URI if needed
# #     db = client["quiz_game"]
# #     return db

# # db = get_db()
# # leaderboard_collection = db["leaderboard"]

# # # Load Questions
# # @st.cache_data
# # def load_questions():
# #     with open("questions.json", "r") as f:
# #         return json.load(f)

# # questions_by_category = load_questions()

# # # App Layout - Neon Style Theme
# # st.markdown(
# #     """
# #     <style>
# #     body {
# #         background-color: #0d0d0d;
# #         color: #ffffff;
# #     }
# #     .stApp {
# #         background-color: #0d0d0d;
# #         color: #ffffff;
# #     }
# #     .stButton>button, .stSelectbox div, .stTextInput>div>input, .stRadio>div>label {
# #         background-color: #1e1e1e;
# #         color: #00ffcc;
# #         border: 1px solid #00ffcc;
# #         border-radius: 8px;
# #         padding: 8px;
# #     }
# #     .stButton>button:hover {
# #         background-color: #00ffcc;
# #         color: black;
# #         box-shadow: 0 0 15px #00ffcc;
# #     }
# #     .stRadio>div>label:hover {
# #         background-color: #2a2a2a;
# #     }
# #     .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
# #         color: #00ffcc;
# #     }
# #     .stExpanderHeader {
# #         color: #00ffcc;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )

# # st.title("🧠 Ultimate Quiz Game")
# # st.markdown("Start playing and get featured on the leaderboard!")

# # # Navigation: Leaderboard
# # page = st.sidebar.selectbox("Navigate", ["Play Quiz", "Leaderboard"])

# # if page == "Leaderboard":
# #     st.header("🏆 Leaderboard")
# #     category_filter = st.selectbox("Filter by Category", list(questions_by_category.keys()))
# #     top_scores = leaderboard_collection.find({"category": category_filter}).sort("score", -1).limit(10)
# #     for rank, entry in enumerate(top_scores, 1):
# #         st.markdown(f"{rank}. `{entry['name']}` - **{entry['score']} pts** in `{entry['time']}s`")

# # else:
# #     username = st.text_input("Enter your name")
# #     selected_category = st.selectbox("Choose a Category", list(questions_by_category.keys()))
# #     start = st.button("Submit")

# #     if start and username:
# #         questions = random.sample(questions_by_category[selected_category], k=min(5, len(questions_by_category[selected_category])))
# #         score = 0
# #         user_answers = []

# #         for i, q in enumerate(questions):
# #             st.markdown(f"### Q{i+1}: {q['question']}")
# #             start_time = time.time()
# #             answered = False
# #             answer = None

# #             while time.time() - start_time < 20:
# #                 option_selected = st.radio("Choose one:", q['options'], key=f"q{i}", index=None)
# #                 if st.button("Next", key=f"next_{i}"):
# #                     answer = option_selected
# #                     answered = True
# #                     break
# #                 time.sleep(1)
# #                 st.experimental_rerun()

# #             if not answered:
# #                 answer = "Timeout"

# #             correct = q['answer']
# #             if answer == correct:
# #                 score += 1

# #             user_answers.append((q['question'], answer, correct))

# #         st.header("✅ Quiz Completed")
# #         st.markdown(f"**Score:** `{score}/{len(questions)}`")

# #         leaderboard_collection.insert_one({
# #             "name": username,
# #             "score": score,
# #             "category": selected_category,
# #             "time": int(time.time() - start_time)
# #         })

# #         with st.expander("🔍 Review Your Answers"):
# #             for q, ua, ca in user_answers:
# #                 st.markdown(f"**Q:** {q}")
# #                 st.markdown(f"- Your Answer: `{ua}`")
# #                 st.markdown(f"- Correct Answer: `{ca}`")

# #     elif start:
# #         st.warning("⚠️ Please enter your name to begin!")





# # import streamlit as st
# # import time
# # import random
# # from pymongo import MongoClient
# # from datetime import datetime

# # # --- MongoDB Setup ---
# # client = MongoClient("mongodb://localhost:27017/")
# # db = client["quiz_db"]
# # scores_collection = db["leaderboard"]

# # # --- Questions Database ---
# # questions_db = {

# #     "General Knowledge": [
# #         {"question": "🌍 What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
# #         {"question": "🗓️ How many days are in a leap year?", "options": ["365", "366", "364", "367"], "answer": "366"},
# #         {"question": "🗼 Where is the Eiffel Tower located?", "options": ["Paris", "Tokyo", "New York", "Berlin"], "answer": "Paris"},
# #         {"question": "🌊 Which ocean is the largest?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
# #         {"question": "📚 Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Hemingway", "Tolstoy", "Twain"], "answer": "Shakespeare"},
# #         {"question": "🌌 What galaxy do we live in?", "options": ["Milky Way", "Andromeda", "Sombrero", "Whirlpool"], "answer": "Milky Way"},
# #         {"question": "🦁 Which is the king of the jungle?", "options": ["Lion", "Tiger", "Elephant", "Cheetah"], "answer": "Lion"},
# #         {"question": "🎨 Who painted the Mona Lisa?", "options": ["Da Vinci", "Picasso", "Van Gogh", "Rembrandt"], "answer": "Da Vinci"},
# #         {"question": "🚀 Who was the first person on the moon?", "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"], "answer": "Neil Armstrong"},
# #         {"question": "💡 Who invented the light bulb?", "options": ["Edison", "Newton", "Tesla", "Einstein"], "answer": "Edison"}
# #     ],
# #     "Science": [
# #         {"question": "🧪 What planet is known as the Red Planet?", "options": ["Mars", "Earth", "Venus", "Jupiter"], "answer": "Mars"},
# #         {"question": "🧬 What is the chemical symbol for water?", "options": ["O2", "CO2", "H2O", "HO2"], "answer": "H2O"},
# #         {"question": "⚡ What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s"], "answer": "300,000 km/s"},
# #         {"question": "🌡️ What is the boiling point of water?", "options": ["100°C", "90°C", "80°C", "70°C"], "answer": "100°C"},
# #         {"question": "🔬 What part of the cell contains DNA?", "options": ["Nucleus", "Cytoplasm", "Ribosome", "Cell wall"], "answer": "Nucleus"},
# #         {"question": "☄️ What are comets made of?", "options": ["Ice and dust", "Rock", "Gas", "Metal"], "answer": "Ice and dust"},
# #         {"question": "🌪️ What is the center of an atom called?", "options": ["Nucleus", "Electron", "Proton", "Neutron"], "answer": "Nucleus"},
# #         {"question": "🌋 Which gas do plants use for photosynthesis?", "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": "Carbon dioxide"},
# #         {"question": "🧲 Which is the strongest magnetic material?", "options": ["Iron", "Cobalt", "Nickel", "Neodymium"], "answer": "Neodymium"},
# #         {"question": "💥 What force keeps us on the ground?", "options": ["Gravity", "Friction", "Magnetism", "Air resistance"], "answer": "Gravity"}
# #     ],
# #     "Technology": [
# #         {"question": "💻 What does CPU stand for?", "options": ["Central Processing Unit", "Computer Personal Unit", "Central Programming Unit", "Central Processor Utility"], "answer": "Central Processing Unit"},
# #         {"question": "📱 Who founded Microsoft?", "options": ["Bill Gates", "Steve Jobs", "Elon Musk", "Mark Zuckerberg"], "answer": "Bill Gates"},
# #         {"question": "🌐 What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Hyperlink and Text Markup Language", "Home Tool Markup Language"], "answer": "Hyper Text Markup Language"},
# #         {"question": "🧠 What does AI stand for?", "options": ["Artificial Intelligence", "Automated Input", "Advanced Interface", "Artificial Input"], "answer": "Artificial Intelligence"},
# #         {"question": "🔒 What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "Hyper Technical Transfer Protocol", "High Transfer Text Protocol", "Hyper Transfer Text Protocol"], "answer": "HyperText Transfer Protocol"},
# #         {"question": "🖱️ What is used to navigate a computer screen?", "options": ["Mouse", "Keyboard", "Monitor", "Printer"], "answer": "Mouse"},
# #         {"question": "🧮 What is 101 in binary?", "options": ["5", "3", "4", "6"], "answer": "5"},
# #         {"question": "💾 What device stores data permanently?", "options": ["Hard Disk", "RAM", "Cache", "CPU"], "answer": "Hard Disk"},
# #         {"question": "🛰️ What tech allows global positioning?", "options": ["GPS", "WiFi", "Bluetooth", "NFC"], "answer": "GPS"},
# #         {"question": "🔧 Which language is used for web styling?", "options": ["CSS", "HTML", "Python", "Java"], "answer": "CSS"}
# #     ]
# # }



# # for category in questions_db.values():
# #     for q in category:
# #         random.shuffle(q["options"])

# # # --- Initialization ---
# # def init_session():
# #     keys_defaults = {
# #         "page": "start", "username": "", "category": None,
# #         "question_index": 0, "answers": {}, "score": 0,
# #         "start_time": time.time(), "selected_option": None
# #     }
# #     for key, value in keys_defaults.items():
# #         if key not in st.session_state:
# #             st.session_state[key] = value

# # # --- MongoDB Save & Fetch ---
# # def save_score_to_db(username, category, score, total):
# #     scores_collection.insert_one({
# #         "username": username,
# #         "category": category,
# #         "score": score,
# #         "total": total,
# #         "timestamp": datetime.utcnow()
# #     })

# # def get_leaderboard(category, limit=10):
# #     return list(scores_collection.find({"category": category}).sort("score", -1).limit(limit))

# # # --- UI Pages ---
# # def show_start_page():
# #     st.title("🎉 Welcome to the Quiz Game!")
# #     st.session_state.username = st.text_input("Enter your name:", st.session_state.username)
# #     categories = list(questions_db.keys())
# #     st.session_state.category = st.selectbox("Select a Category:", ["-- Select Category --"] + categories)

# #     if st.session_state.username and st.session_state.category != "-- Select Category --":
# #         if st.button("Start Quiz"):
# #             st.session_state.page = "quiz"
# #             st.session_state.question_index = 0
# #             st.session_state.answers = {}
# #             st.session_state.score = 0
# #             st.session_state.start_time = time.time()
# #             st.session_state.selected_option = None
# #             st.experimental_rerun()

# # def show_question_page():
# #     category = st.session_state.category
# #     questions = questions_db[category]
# #     index = st.session_state.question_index
# #     q = questions[index]

# #     st.markdown(f"### Category: **{category}**")
# #     st.markdown(f"#### Question {index + 1} of {len(questions)}")
# #     st.markdown(f"**{q['question']}**")

# #     elapsed = time.time() - st.session_state.start_time
# #     time_left = max(0, 20 - int(elapsed))
# #     st.progress(time_left / 20)
# #     st.write(f"⏳ Time left: **{time_left} seconds**")

# #     options = ["-- Select an option --"] + q["options"]
# #     current_index = options.index(st.session_state.selected_option) if st.session_state.selected_option in q["options"] else 0

# #     selected = st.selectbox("Choose your answer:", options=options, index=current_index, key="option_selectbox")
# #     st.session_state.selected_option = None if selected == options[0] else selected

# #     if index in st.session_state.answers:
# #         st.markdown("""
# #             <style>
# #             div[data-testid="stSelectbox"] > div {
# #                 pointer-events: none;
# #                 opacity: 0.6;
# #             }
# #             </style>
# #         """, unsafe_allow_html=True)

# #     if st.session_state.selected_option and index not in st.session_state.answers:
# #         st.session_state.answers[index] = st.session_state.selected_option
# #         if st.session_state.selected_option == q["answer"]:
# #             st.session_state.score += 1

# #     col1, col2 = st.columns([1, 1])

# #     with col1:
# #         if st.button("Next") and index < len(questions) - 1:
# #             if st.session_state.selected_option is None:
# #                 st.warning("Select an answer first.")
# #             else:
# #                 st.session_state.question_index += 1
# #                 st.session_state.selected_option = None
# #                 st.session_state.start_time = time.time()
# #                 st.experimental_rerun()

# #     with col2:
# #         if index == len(questions) - 1:
# #             if st.button("Submit Quiz"):
# #                 if st.session_state.selected_option is None:
# #                     st.warning("Select an answer first.")
# #                 else:
# #                     st.session_state.page = "results"
# #                     save_score_to_db(st.session_state.username, category, st.session_state.score, len(questions))
# #                     st.experimental_rerun()

# #     if time_left == 0:
# #         if index not in st.session_state.answers:
# #             st.session_state.answers[index] = "No answer"
# #         if index < len(questions) - 1:
# #             st.session_state.question_index += 1
# #             st.session_state.selected_option = None
# #             st.session_state.start_time = time.time()
# #             st.experimental_rerun()
# #         else:
# #             st.session_state.page = "results"
# #             save_score_to_db(st.session_state.username, category, st.session_state.score, len(questions))
# #             st.experimental_rerun()

# # def show_results_page():
# #     st.title("🏁 Quiz Completed!")
# #     st.write(f"**{st.session_state.username}**, your score is:")
# #     st.markdown(f"<h2 style='color: green;'>{st.session_state.score} / {len(questions_db[st.session_state.category])}</h2>", unsafe_allow_html=True)

# #     st.subheader("Review Answers:")
# #     questions = questions_db[st.session_state.category]
# #     for i, q in enumerate(questions):
# #         st.markdown(f"**Q{i+1}: {q['question']}**")
# #         user_answer = st.session_state.answers.get(i, "No answer")
# #         correct = q["answer"]
# #         if user_answer == correct:
# #             st.success(f"Your answer: {user_answer} (Correct)")
# #         else:
# #             st.error(f"Your answer: {user_answer} (Incorrect)")
# #             st.info(f"Correct answer: {correct}")

# #     col1, col2 = st.columns(2)
# #     with col1:
# #         if st.button("Play Again"):
# #             st.session_state.page = "start"
# #             st.session_state.selected_option = None
# #             st.experimental_rerun()
# #     with col2:
# #         if st.button("View Leaderboard"):
# #             st.session_state.page = "leaderboard"
# #             st.experimental_rerun()

# # def show_leaderboard_page():
# #     st.title("📊 Leaderboard")
# #     st.write(f"Category: **{st.session_state.category}**")

# #     leaderboard = get_leaderboard(st.session_state.category)
# #     if leaderboard:
# #         st.table([{"Name": x["username"], "Score": x["score"]} for x in leaderboard])
# #     else:
# #         st.info("No scores yet for this category.")

# #     if st.button("Back to Start"):
# #         st.session_state.page = "start"
# #         st.experimental_rerun()

# # # --- App Launch ---
# # init_session()

# # if st.session_state.page == "start":
# #     show_start_page()
# # elif st.session_state.page == "quiz":
# #     show_question_page()
# # elif st.session_state.page == "results":
# #     show_results_page()
# # elif st.session_state.page == "leaderboard":
# #     show_leaderboard_page()




# import streamlit as st
# import time
# import random
# import pymongo
# from datetime import datetime

# # MongoDB setup
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["quiz_app"]
# scores_collection = db["scores"]

# # Questions by category
# questions_by_category = {
#     "Python": [
#         {
#             "question": "What is the output of print(2 ** 3)?",
#             "options": ["6", "8", "9", "Error"],
#             "answer": "8"
#         },
#         {
#             "question": "Which of the following is a Python data type?",
#             "options": ["integer", "float", "string", "All of the above"],
#             "answer": "All of the above"
#         },
#         {
#             "question": "What keyword is used to define a function in Python?",
#             "options": ["function", "define", "def", "fun"],
#             "answer": "def"
#         },
#     ],
#     "JavaScript": [
#         {
#             "question": "Which company developed JavaScript?",
#             "options": ["Microsoft", "Netscape", "Google", "Apple"],
#             "answer": "Netscape"
#         },
#         {
#             "question": "What keyword is used to declare a variable in JavaScript?",
#             "options": ["var", "let", "const", "All of the above"],
#             "answer": "All of the above"
#         },
#         {
#             "question": "Which symbol is used for comments in JavaScript?",
#             "options": ["//", "<!-- -->", "#", "/* */"],
#             "answer": "//"
#         },
#     ],
#     "HTML": [
#         {
#             "question": "What does HTML stand for?",
#             "options": ["Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language", "None of the above"],
#             "answer": "Hyper Text Markup Language"
#         },
#         {
#             "question": "Which HTML tag is used to create a hyperlink?",
#             "options": ["<link>", "<a>", "<href>", "<url>"],
#             "answer": "<a>"
#         },
#         {
#             "question": "Which attribute is used to provide a unique name to an HTML element?",
#             "options": ["class", "id", "name", "key"],
#             "answer": "id"
#         },
#     ]
# }

# # Utility functions
# def save_score_to_db(username, category, score, total):
#     scores_collection.insert_one({
#         "username": username,
#         "category": category,
#         "score": score,
#         "total": total,
#         "timestamp": datetime.now()
#     })

# def get_leaderboard():
#     return list(scores_collection.find().sort("score", -1).limit(10))

# # Streamlit app setup
# st.set_page_config(page_title="Quiz Game", layout="centered")
# st.title("🚀 Quiz Game")

# # Initialize session state variables
# if "page" not in st.session_state:
#     st.session_state.page = "login"
# if "username" not in st.session_state:
#     st.session_state.username = ""
# if "category" not in st.session_state:
#     st.session_state.category = ""
# if "question_index" not in st.session_state:
#     st.session_state.question_index = 0
# if "score" not in st.session_state:
#     st.session_state.score = 0
# if "answers" not in st.session_state:
#     st.session_state.answers = {}
# if "start_time" not in st.session_state:
#     st.session_state.start_time = time.time()
# if "selected_option" not in st.session_state:
#     st.session_state.selected_option = None

# # Page navigation logic
# def show_login_page():
#     st.subheader("Enter your username to start")
#     username = st.text_input("Username")
#     if st.button("Continue") and username:
#         st.session_state.username = username
#         st.session_state.page = "category"
#         st.experimental_rerun()

# def show_category_page():
#     st.subheader("Choose a category")
#     category = st.selectbox("Select Category", list(questions_by_category.keys()))
#     if st.button("Start Quiz"):
#         st.session_state.category = category
#         st.session_state.page = "quiz"
#         st.session_state.question_index = 0
#         st.session_state.score = 0
#         st.session_state.answers = {}
#         st.session_state.start_time = time.time()
#         st.experimental_rerun()

# def show_question_page():
#     category = st.session_state.category
#     index = st.session_state.question_index
#     questions = questions_by_category[category]
#     question_data = questions[index]
#     question = question_data["question"]
#     options = question_data["options"]
#     answer = question_data["answer"]

#     st.subheader(f"Question {index + 1}/{len(questions)}")
#     st.write(question)

#     # Timer
#     time_limit = 20
#     elapsed_time = int(time.time() - st.session_state.start_time)
#     time_left = max(0, time_limit - elapsed_time)
#     st.progress((time_limit - time_left) / time_limit)
#     st.write(f"⏳ Time left: {time_left} seconds")

#     # Option selection
#     selected = st.radio("Select an option:", options, index=None, key=f"question_{index}")
#     st.session_state.selected_option = selected

#     # Timeout logic with check
#     if time_left == 0:
#         if index not in st.session_state.answers:
#             st.warning("⏰ Time is up! Please select an answer to proceed.")
#         else:
#             if index < len(questions) - 1:
#                 st.session_state.question_index += 1
#                 st.session_state.selected_option = None
#                 st.session_state.start_time = time.time()
#                 st.experimental_rerun()
#             else:
#                 st.session_state.page = "results"
#                 save_score_to_db(st.session_state.username, category, st.session_state.score, len(questions))
#                 st.experimental_rerun()

#     # Score update
#     if selected and index not in st.session_state.answers:
#         st.session_state.answers[index] = selected
#         if selected == answer:
#             st.session_state.score += 1

#     # Navigation
#     if st.button("Next") and index < len(questions) - 1:
#         if st.session_state.selected_option is None:
#             st.warning("❗Please select an option before proceeding.")
#         else:
#             st.session_state.question_index += 1
#             st.session_state.selected_option = None
#             st.session_state.start_time = time.time()
#             st.experimental_rerun()
#     elif st.button("Submit Quiz"):
#         if st.session_state.selected_option is None:
#             st.warning("❗Please select an option before submitting.")
#         else:
#             st.session_state.page = "results"
#             save_score_to_db(st.session_state.username, category, st.session_state.score, len(questions))
#             st.experimental_rerun()

# def show_results_page():
#     st.subheader("✅ Quiz Completed!")
#     st.write(f"**Name:** {st.session_state.username}")
#     st.write(f"**Category:** {st.session_state.category}")
#     st.write(f"**Score:** {st.session_state.score}/{len(questions_by_category[st.session_state.category])}")
#     st.write("---")
#     st.subheader("🏆 Leaderboard (Top 10 Scores)")
#     leaderboard = get_leaderboard()
#     for i, entry in enumerate(leaderboard, start=1):
#         st.write(f"{i}. {entry['username']} - {entry['score']} points ({entry['category']})")
#     if st.button("Play Again"):
#         for key in st.session_state.keys():
#             del st.session_state[key]
#         st.experimental_rerun()

# # Page routing
# if st.session_state.page == "login":
#     show_login_page()
# elif st.session_state.page == "category":
#     show_category_page()
# elif st.session_state.page == "quiz":
#     show_question_page()
# elif st.session_state.page == "results":
#     show_results_page()



import streamlit as st
import time
from datetime import datetime
from pymongo import MongoClient
import pandas as pd

# --- MongoDB setup ---
client = MongoClient("mongodb://localhost:27017/")
db = client["quiz_game_db"]
scores_collection = db["scores"]

# --- Sample Questions Database ---
questions_db = {
    "General Knowledge": [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
        {"question": "Who wrote '1984'?", "options": ["Orwell", "Shakespeare", "Hemingway", "Tolstoy"], "answer": "Orwell"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
        {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
        {"question": "In which year did WW2 end?", "options": ["1945", "1939", "1918", "1960"], "answer": "1945"},
        {"question": "Which element has the chemical symbol 'O'?", "options": ["Gold", "Oxygen", "Iron", "Silver"], "answer": "Oxygen"},
        {"question": "Who painted the Mona Lisa?", "options": ["Da Vinci", "Picasso", "Van Gogh", "Michelangelo"], "answer": "Da Vinci"},
        {"question": "What is the currency of Japan?", "options": ["Yen", "Dollar", "Euro", "Peso"], "answer": "Yen"},
        {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
        {"question": "Which gas do plants absorb?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"], "answer": "Carbon Dioxide"},
    ],
   
    "Science": [
        {"question": "🧪 What planet is known as the Red Planet?", "options": ["Mars", "Earth", "Venus", "Jupiter"], "answer": "Mars"},
        {"question": "🧬 What is the chemical symbol for water?", "options": ["O2", "CO2", "H2O", "HO2"], "answer": "H2O"},
        {"question": "⚡ What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s"], "answer": "300,000 km/s"},
        {"question": "🌡️ What is the boiling point of water?", "options": ["100°C", "90°C", "80°C", "70°C"], "answer": "100°C"},
        {"question": "🔬 What part of the cell contains DNA?", "options": ["Nucleus", "Cytoplasm", "Ribosome", "Cell wall"], "answer": "Nucleus"},
        {"question": "☄️ What are comets made of?", "options": ["Ice and dust", "Rock", "Gas", "Metal"], "answer": "Ice and dust"},
        {"question": "🌪️ What is the center of an atom called?", "options": ["Nucleus", "Electron", "Proton", "Neutron"], "answer": "Nucleus"},
        {"question": "🌋 Which gas do plants use for photosynthesis?", "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": "Carbon dioxide"},
        {"question": "🧲 Which is the strongest magnetic material?", "options": ["Iron", "Cobalt", "Nickel", "Neodymium"], "answer": "Neodymium"},
        {"question": "💥 What force keeps us on the ground?", "options": ["Gravity", "Friction", "Magnetism", "Air resistance"], "answer": "Gravity"}
    ],
    "Technology": [
        {"question": "💻 What does CPU stand for?", "options": ["Central Processing Unit", "Computer Personal Unit", "Central Programming Unit", "Central Processor Utility"], "answer": "Central Processing Unit"},
        {"question": "📱 Who founded Microsoft?", "options": ["Bill Gates", "Steve Jobs", "Elon Musk", "Mark Zuckerberg"], "answer": "Bill Gates"},
        {"question": "🌐 What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Hyperlink and Text Markup Language", "Home Tool Markup Language"], "answer": "Hyper Text Markup Language"},
        {"question": "🧠 What does AI stand for?", "options": ["Artificial Intelligence", "Automated Input", "Advanced Interface", "Artificial Input"], "answer": "Artificial Intelligence"},
        {"question": "🔒 What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "Hyper Technical Transfer Protocol", "High Transfer Text Protocol", "Hyper Transfer Text Protocol"], "answer": "HyperText Transfer Protocol"},
        {"question": "🖱️ What is used to navigate a computer screen?", "options": ["Mouse", "Keyboard", "Monitor", "Printer"], "answer": "Mouse"},
        {"question": "🧮 What is 101 in binary?", "options": ["5", "3", "4", "6"], "answer": "5"},
        {"question": "💾 What device stores data permanently?", "options": ["Hard Disk", "RAM", "Cache", "CPU"], "answer": "Hard Disk"},
        {"question": "🛰️ What tech allows global positioning?", "options": ["GPS", "WiFi", "Bluetooth", "NFC"], "answer": "GPS"},
        {"question": "🔧 Which language is used for web styling?", "options": ["CSS", "HTML", "Python", "Java"], "answer": "CSS"}
    ]
}

# --- Styling for Neon & Timer ---
st.markdown("""
<style>
body {
    background-color: #0e0e0e;
    color: #39ff14;
    font-family: 'Courier New', Courier, monospace;
}
h1, h2, h3, h4, h5, h6 {
    color: #39ff14;
    text-shadow: 0 0 10px #39ff14;
}
.timer {
    font-size: 18px;
    font-weight: bold;
    color: #ff073a;
    text-shadow: 0 0 8px #ff073a;
}
</style>
""", unsafe_allow_html=True)

# --- Helper Functions ---
def save_score_to_db(username, category, score, total):
    record = {
        "username": username,
        "category": category,
        "score": score,
        "total": total,
        "timestamp": datetime.now()
    }
    scores_collection.insert_one(record)

def get_leaderboard(category):
    cursor = scores_collection.find({"category": category}).sort("score", -1).limit(10)
    records = list(cursor)
    return pd.DataFrame([{
        "Rank": i+1,
        "Username": r["username"],
        "Score": f"{r['score']} / {r['total']}",
        "Date": r["timestamp"].strftime("%Y-%m-%d")
    } for i, r in enumerate(records)])

# --- Main App ---
def main():
    st.title("🌟Quiz Game 🌟")

    for key, default in {
        "started": False, "question_index": 0, "score": 0, "answers": [],
        "timer": 20, "review_mode": False, "username": "", "category": "",
        "selected_option": None, "quiz_completed": False, "saved_to_db": False
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

    if not st.session_state.started:
        st.session_state.username = st.text_input("Enter your name:", max_chars=20, key="username_input")
        st.session_state.category = st.selectbox("Choose Quiz Category:", list(questions_db.keys()), key="category_select")
        if st.button("Start Quiz", key="start_quiz_btn") and st.session_state.username.strip():
            st.session_state.started = True
            st.experimental_rerun()
        elif st.session_state.username.strip() == "":
            st.warning("Please enter your name to start!")

    else:
        questions = questions_db[st.session_state.category]
        q_idx = st.session_state.question_index

        if q_idx < len(questions):
            question = questions[q_idx]
            st.markdown(f"### Question {q_idx+1} / {len(questions)}")
            st.markdown(f"**{question['question']}**")

            if st.session_state.timer == 20:
                st.session_state.start_time = datetime.now()

            elapsed = (datetime.now() - st.session_state.start_time).seconds
            remaining = max(0, 20 - elapsed)
            st.markdown(f'<div class="timer">⏳ Time Left: {remaining} s</div>', unsafe_allow_html=True)

            selected = st.radio(
                "Choose your answer:",
                question["options"],
                index=0 if st.session_state.selected_option is None else question["options"].index(st.session_state.selected_option),
                key=f"radio_{q_idx}"
            )

            st.session_state.selected_option = selected

            if remaining == 0 or st.button("Next", key=f"next_btn_{q_idx}"):
                is_correct = selected == question["answer"]
                st.session_state.answers.append({
                    "question": question["question"],
                    "selected": selected,
                    "correct": question["answer"],
                    "is_correct": is_correct
                })
                if is_correct:
                    st.session_state.score += 1
                st.session_state.question_index += 1
                st.session_state.selected_option = None
                st.session_state.timer = 20
                st.experimental_rerun()

        else:
            st.session_state.quiz_completed = True

            if not st.session_state.saved_to_db:
                save_score_to_db(st.session_state.username, st.session_state.category, st.session_state.score, len(questions))
                st.session_state.saved_to_db = True

            leaderboard_df = get_leaderboard(st.session_state.category)
            st.markdown(f"## 🏆 Leaderboard - {st.session_state.category}")
            if not leaderboard_df.empty:
                st.dataframe(leaderboard_df, use_container_width=True)
            else:
                st.info("No scores available yet.")

            st.success(f"🎉 Quiz Completed, {st.session_state.username}!")
            st.markdown(f"Your Score: **{st.session_state.score} / {len(questions)}**")

            st.markdown("## 📘 Review Your Answers")
            for i, ans in enumerate(st.session_state.answers, 1):
                st.markdown(f"**Q{i}: {ans['question']}**")
                st.markdown(f"Your answer: {ans['selected']} {'✅' if ans['is_correct'] else '❌'}")
                st.markdown(f"Correct answer: {ans['correct']}")
                st.markdown("---")

if __name__ == "__main__":
    main()