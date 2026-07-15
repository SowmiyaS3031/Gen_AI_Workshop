# 🎓 MEC AI Chatbot

**Muthayammal Engineering College AI Assistant** - Powered by Streamlit & Groq API

An intelligent chatbot designed to answer student queries about Muthayammal Engineering College. Get instant information about admissions, placements, courses, hostel facilities, and more!

---

## ✨ Features

- 🤖 **AI-Powered Chat** - Uses Groq's LLaMA 3.3 70B model for intelligent responses
- 📋 **Comprehensive Sidebar** - Lists all topics the bot can help with
- 💬 **Chat History** - Maintains conversation context
- 🗑️ **Clear Chat** - Easy button to reset conversation
- 🎯 **Smart Filtering** - Only answers college-related questions
- 📱 **Responsive UI** - Works on desktop and mobile

---

## 🎯 What This Bot Can Help With

| Category | Details |
|----------|---------|
| 🎯 **Admissions** | Entrance requirements, application process, cut-off marks |
| 🏫 **Departments** | CS, IT, ECE, Mechanical, Civil, and specializations |
| 💼 **Placements** | Recruitment drives, companies, salary statistics |
| 🏠 **Hostel** | Accommodation facilities, rules, mess services |
| 🚌 **Transport** | Shuttle routes, timings, transport facilities |
| 📚 **Library** | Resources, opening hours, database access |
| 🎓 **Courses** | Curriculum, subjects, semester structure |
| 👨‍🏫 **Faculty** | Department heads, professor information |
| 🎪 **Student Activities** | Clubs, events, competitions, fests |
| 🏛️ **Campus** | Infrastructure, facilities, locations |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API Key (Get free from [console.groq.com](https://console.groq.com))

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/SowmiyaS3031/Gen_AI_Workshop.git
cd Gen_AI_Workshop
```

2. **Create Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup Environment Variables**
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_api_key_here
```

5. **Run the Application**
```bash
streamlit run app.py
```

6. **Access the App**
Open your browser and go to: `http://localhost:8501`

---

## 📦 Requirements

```
streamlit==1.28.0
groq==0.4.1
python-dotenv==1.0.0
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
MEC-CHATBOT/
│
├── app.py                 # Main Streamlit application
├── .env                   # API keys (Don't commit this!)
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🎮 How to Use

1. **Open the Chat Interface**
   - Type your question in the input box at the bottom
   - Press Enter or click the send button

2. **Explore Topics**
   - Check the sidebar to see what topics are supported
   - Ask specific questions for better answers

3. **View History**
   - All your chat messages are displayed above
   - Scroll up to see previous messages

4. **Clear Chat**
   - Click the "🗑️ Clear Chat History" button in the sidebar
   - This resets the conversation

### Example Questions
- "What are the admission requirements for CSE?"
- "Which companies visited campus last year?"
- "Tell me about hostel facilities"
- "What are the timings of the library?"
- "When is the next techfest?"

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Streamlit** | Web UI framework for Python |
| **Groq API** | LLM inference (LLaMA 3.3 70B) |
| **Python** | Backend logic |
| **python-dotenv** | Environment variable management |

---

## 🔐 Security Notes

⚠️ **Never commit `.env` file!** It contains sensitive API keys.

The `.gitignore` file already includes `.env`, so it won't be pushed to GitHub.

---

## 🐛 Troubleshooting

### `streamlit: command not found`
```bash
python -m streamlit run app.py
```

### `GROQ_API_KEY not found`
- Make sure `.env` file exists in the project root
- Check that the API key is correctly set
- Restart the application

### Port 8501 already in use
```bash
streamlit run app.py --server.port 8000
```

### Module import errors
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📈 Future Enhancements

- [ ] Add database to store college information
- [ ] Implement file uploads for documents
- [ ] Add multi-language support
- [ ] Create admin panel for updating college info
- [ ] Add voice input/output
- [ ] Implement user authentication
- [ ] Add analytics and chat logs

---

## 👨‍💻 Development

### Add New Features
1. Modify `app.py`
2. Test locally with `streamlit run app.py`
3. Commit changes: `git commit -m "Feature description"`
4. Push to GitHub: `git push`

### Modify System Prompt
Edit the `system_prompt` variable in `app.py` to change bot behavior.

---

## 🤝 Contributing

Want to improve this project?

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the MIT License.

---

## 📞 Support & Contact

For issues or suggestions:
- Create an issue on GitHub
- Contact Muthayammal Engineering College official channels
- Reach out to the developer

---

## 🎓 About Muthayammal Engineering College

This chatbot is designed to assist students and visitors with information about:
- **Institution**: Muthayammal Engineering College
- **Mission**: To provide quality education and career development
- **Focus Areas**: Engineering education, placements, student development

*Note: For official college inquiries, please contact the college directly.*

---

## 📊 Stats

- **Model**: Groq LLaMA 3.3 70B
- **Response Time**: < 2 seconds
- **Supported Topics**: 10+ categories
- **Max Response Length**: 400 tokens

---

## 🎉 Acknowledgments

- **Groq** - For fast and efficient LLM inference
- **Streamlit** - For easy web app development
- **Muthayammal Engineering College** - For the inspiration

---

## 📅 Last Updated

July 15, 2026

---

<div align="center">

**Made with ❤️ for MEC Students**

[GitHub](https://github.com/SowmiyaS3031/Gen_AI_Workshop) | [Groq API](https://console.groq.com) | [Streamlit Docs](https://docs.streamlit.io/)

</div>
