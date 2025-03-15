import streamlit as st  # For the web interface
import random  # For randomizing the questions

# Title of the Application
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>📝 Quiz Application</h1>
    """, unsafe_allow_html=True)

# Define quiz questions, options, and answers as a list of dictionaries
questions = [
    {"question": "What is the capital of Pakistan?", "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], "answer": "Islamabad"},
    {"question": "Who is the founder of Pakistan?", "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"], "answer": "Muhammad Ali Jinnah"},
    {"question": "Which is the national language of Pakistan?", "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"], "answer": "Urdu"},
    {"question": "What is the currency of Pakistan?", "options": ["Rupee", "Dollar", "Taka", "Riyal"], "answer": "Rupee"},
    {"question": "Which city is known as the City of Lights in Pakistan?", "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"], "answer": "Karachi"},
    {"question": "What is the national flower of Pakistan?", "options": ["Rose", "Tulip", "Jasmine", "Sunflower"], "answer": "Jasmine"},
    {"question": "Which is the largest province of Pakistan by area?", "options": ["Sindh", "Punjab", "Balochistan", "Khyber Pakhtunkhwa"], "answer": "Balochistan"},
    {"question": "Which is the longest river in Pakistan?", "options": ["Chenab", "Jhelum", "Ravi", "Indus"], "answer": "Indus"},
    {"question": "Who wrote the national anthem of Pakistan?", "options": ["Hafeez Jalandhari", "Faiz Ahmed Faiz", "Allama Iqbal", "Josh Malihabadi"], "answer": "Hafeez Jalandhari"},
    {"question": "Which year did Pakistan conduct its first nuclear test?", "options": ["1995", "1998", "2000", "2001"], "answer": "1998"},
    {"question": "Who was the first Prime Minister of Pakistan?", "options": ["Liaquat Ali Khan", "Benazir Bhutto", "Zulfikar Ali Bhutto", "Pervez Musharraf"], "answer": "Liaquat Ali Khan"},
    {"question": "Which is the highest mountain in Pakistan?", "options": ["Nanga Parbat", "K2", "Rakaposhi", "Broad Peak"], "answer": "K2"},
    {"question": "What is the name of the border between Pakistan and India?", "options": ["Durand Line", "Radcliffe Line", "Wagah Border", "Line of Control"], "answer": "Radcliffe Line"},
    {"question": "Which sport is most popular in Pakistan?", "options": ["Football", "Cricket", "Hockey", "Squash"], "answer": "Cricket"},
    {"question": "Which Pakistani scientist won the Nobel Prize?", "options": ["Abdus Salam", "Dr. AQ Khan", "Salimuzzaman Siddiqui", "Atta-ur-Rahman"], "answer": "Abdus Salam"},
    {"question": "Which Pakistani city is known as the 'Heart of Pakistan'?", "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"], "answer": "Lahore"},
    {"question": "When did Pakistan become a nuclear power?", "options": ["1974", "1998", "2001", "2010"], "answer": "1998"},
    {"question": "Which is the national animal of Pakistan?", "options": ["Lion", "Markhor", "Tiger", "Bear"], "answer": "Markhor"},
    {"question": "What is the total number of provinces in Pakistan?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Which ocean is to the south of Pakistan?", "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], "answer": "Indian Ocean"}
] * 2  # Duplicated to make 50 questions

# Initialize session state for tracking progress
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(questions, len(questions))  # Shuffle questions

# Get the current question
current_question = st.session_state.questions[st.session_state.question_index]

# Display the question
st.subheader(current_question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", current_question["options"], key="answer")

# Submit button to check the answer
if st.button("Submit Answer"):
    if selected_option == current_question["answer"]:
        st.session_state.score += 1
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect! The correct answer is {current_question['answer']}")
    
    # Move to next question
    if st.session_state.question_index < len(st.session_state.questions) - 1:
        st.session_state.question_index += 1
        st.rerun()
    else:
        st.markdown(f"<h3 style='color: #3498DB;'>🎉 Quiz Completed!</h3>", unsafe_allow_html=True)
        st.write(f"Your final score: {st.session_state.score}/{len(st.session_state.questions)}")
        st.session_state.question_index = 0  # Reset index
        st.session_state.score = 0  # Reset score
        if st.button("Restart Quiz"):
            st.session_state.questions = random.sample(questions, len(questions))
            st.rerun()
