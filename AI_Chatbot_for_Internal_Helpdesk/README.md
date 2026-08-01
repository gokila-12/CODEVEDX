# 🤖 AI Internal Helpdesk Chatbot

An AI-powered **Internal Helpdesk Chatbot** built using **Python, Flask, HTML, CSS, JavaScript, and Scikit-learn**. This chatbot assists employees by answering common HR and IT-related queries such as leave policy, password reset, office timings, attendance, VPN issues, Wi-Fi support, salary details, and more.

---
## DEMO VIDEO

https://github.com/user-attachments/assets/c7abf322-cba8-415f-b501-c27cf0d6bf44

## 📌 Features

- 🤖 AI-powered chatbot
- 🧠 Intent recognition using Machine Learning
- 💬 Interactive chat interface
- 🏢 HR and IT Helpdesk support
- 🔑 Password reset assistance
- 🌐 Wi-Fi & VPN support
- 💰 Salary information
- 📅 Leave policy assistance
- 🕒 Attendance information
- 💻 Software and laptop support
- 🍽️ Cafeteria & Transport information
- 📱 Responsive web interface
- ⚡ Fast Flask backend

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- CountVectorizer
- Multinomial Naive Bayes
- Joblib

### Database
- SQLite

---

## 📂 Project Structure

```
AI_Chatbot_for_Internal_Helpdesk/
│
├── app.py
├── chatbot.py
├── train.py
├── database.py
├── helpdesk.db
│
├── data/
│ └── intents.json
│
├── models/
│   ├── chatbot_model.pkl
│   └── vectorizer.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/gokila-12/AI_Chatbot_for_Internal_Helpdesk.git
```

```bash
cd AI_Chatbot_for_Internal_Helpdesk
```

---

### Install dependencies

```bash
pip install flask scikit-learn pandas joblib nltk
```

---

## ▶️ Train the Model

Whenever you update **intents.json**, retrain the chatbot.

```bash
python train.py
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 💬 Sample Questions

Try asking:

- Hello
- Good Morning
- What is the leave policy?
- How do I reset my password?
- What are the office timings?
- Attendance details
- Salary date
- Wi-Fi is not working
- VPN not working
- Printer issue
- Email not working
- I lost my ID card
- Work from home policy
- Medical insurance
- Where is the cafeteria?
- Thank you

---

## ⚙️ How It Works

1. User enters a question.
2. The message is sent to the Flask backend.
3. The trained Machine Learning model predicts the user's intent.
4. The chatbot fetches the corresponding response.
5. The response is displayed in the chat interface.

---

## 🧠 Machine Learning Workflow

```
User Query
     │
     ▼
Text Preprocessing
     │
     ▼
CountVectorizer
     │
     ▼
Multinomial Naive Bayes
     │
     ▼
Intent Prediction
     │
     ▼
Chatbot Response
```

---

## 📋 Supported Modules

### HR Support
- Leave Policy
- Casual Leave
- Sick Leave
- Salary Information
- Attendance
- Office Timings
- Work From Home
- Company Holidays
- Medical Insurance
- Employee ID
- Notice Period
- Resignation Process

### IT Support
- Password Reset
- Wi-Fi Issues
- VPN Issues
- Email Issues
- Printer Support
- Laptop Support
- Software Installation

### Office Facilities
- Cafeteria
- Parking
- Transport

### General
- Greetings
- Thank You
- Goodbye

---

## 📈 Future Enhancements

- User Login Authentication
- Admin Dashboard
- Chat History
- Voice Assistant
- OpenAI/Gemini API Integration
- Multi-language Support
- Dark Mode
- Email Notifications
- Ticket Generation System
- Analytics Dashboard

---

## 📚 Learning Outcomes

This project demonstrates:

- Natural Language Processing (NLP)
- Intent Classification
- Machine Learning
- Flask Web Development
- Frontend & Backend Integration
- JSON Dataset Management
- REST API Development
- Git & GitHub Version Control

---

## 👨‍💻 Author

**Gokila Krishna B**

AI & ML INTERN
---

## 📜 License

This project is developed for **educational and internship purposes**. You are free to use and modify it for learning and academic projects.

---

⭐ If you found this project useful, don't forget to **Star** the repository!
