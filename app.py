import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load API key
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(page_title="MEC AI Assistant")
with st.sidebar:
    st.title("📋 About This Assistant")
    
    st.info(
        "This AI Assistant is here to help you with information about "
        "Muthayammal Engineering College!"
    )
    
    st.subheader("✨ What I Can Help You With:")
    
    help_topics = [
        "🎯 Admissions - Entrance requirements, application process",
        "🏫 Departments - Available programs and specializations",
        "💼 Placements - Recruitment drives, companies, salary stats",
        "🏠 Hostel - Facilities, accommodation details",
        "🚌 Transport - Campus shuttle, routes, schedules",
        "📚 Library - Resources, opening hours, services",
        "🎓 Courses - Curriculum, subjects, course structure",
        "👨‍🏫 Faculty - Department heads, professor info",
        "🎪 Student Activities - Clubs, events, competitions",
        "🏛️ Campus - Infrastructure, facilities"
    ]
    for topic in help_topics:
        st.write(f"• {topic}")
    
    st.divider()
    
    st.subheader("🔧 Chat Controls")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.success("Chat history cleared!")
        st.rerun()
    
    st.divider()
    
    st.caption("💡 Tip: Ask specific questions for better answers!")

st.title("🎓 Muthayammal Engineering College AI Assistant")

st.write("Ask me anything about Muthayammal Engineering College.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Type your question here...")

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # System prompt
    system_prompt = """
You are the official AI Assistant for Muthayammal Engineering College.

Answer only questions related to:
- Admissions
- Departments
- Placements
- Hostel
- Transport
- Library
- Campus
- Faculty
- Courses
- Student Activities

If the user asks something unrelated to the college,
politely say:
'I am designed to answer only Muthayammal Engineering College related questions.'

Keep answers short and friendly.
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(st.session_state.messages)

    # AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.5,
                max_tokens=400
            )

            reply = response.choices[0].message.content

            st.write(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    ) 