import streamlit as st

st.set_page_config(
    page_title="Smart Student Brain",
    page_icon="🧠",
    layout="wide"
)

# SESSION DATA
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "notes" not in st.session_state:
    st.session_state.notes = ""

if "goals" not in st.session_state:
    st.session_state.goals = []

st.title("🧠 SMART STUDENT BRAIN")
st.subheader("Your Personal Smart Learning Assistant")
st.write("Learn smarter, plan better and improve every day!")

# NAVIGATION
st.sidebar.title("📚 Menu")

if st.sidebar.button("🏠 Dashboard"):
    st.session_state.page = "Dashboard"

if st.sidebar.button("📅 Study Planner"):
    st.session_state.page = "Planner"

if st.sidebar.button("📝 Smart Notes"):
    st.session_state.page = "Notes"

if st.sidebar.button("🎯 Quiz Practice"):
    st.session_state.page = "Quiz"

if st.sidebar.button("💡 Learning Goal"):
    st.session_state.page = "Goal"

if st.sidebar.button("🤖 AI Study Assistant"):
    st.session_state.page = "AI Assistant"

st.divider()

# DASHBOARD
if st.session_state.page == "Dashboard":

    st.header("🏠 Student Dashboard")

    name = st.text_input("Enter your name")

    if name:
        st.success(f"Welcome, {name}!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Study Tools", "5")
    col2.metric("Saved Goals", len(st.session_state.goals))
    col3.metric("Learning Platform", "Active")

    st.info("Choose a learning tool from the menu.")

# STUDY PLANNER
elif st.session_state.page == "Planner":

    st.header("📅 Smart Study Planner")

    subject = st.text_input("Enter Subject")
    topic = st.text_input("Enter Topic")

    hours = st.number_input(
        "Available Study Hours",
        min_value=1,
        max_value=12,
        value=2
    )

    if st.button("Create Study Plan"):

        if subject and topic:

            st.success("Your Study Plan is Ready!")

            st.write("Subject:", subject)
            st.write("Topic:", topic)
            st.write("Study Time:", hours, "hours")

            st.write("### Suggested Study Schedule")
            st.write(f"📖 Learn the topic: {hours * 30} minutes")
            st.write("✍️ Practice questions: 30 minutes")
            st.write("🔁 Revise important points: 15 minutes")

        else:
            st.warning("Please enter subject and topic.")

# SMART NOTES
elif st.session_state.page == "Notes":

    st.header("📝 Smart Notes")

    if "notes_input" not in st.session_state:
        st.session_state.notes_input = st.session_state.notes

    def update_notes():
        st.session_state.notes = st.session_state.notes_input

    st.text_area(
        "Write your study notes here",
        height=200,
        key="notes_input",
        on_change=update_notes
    )

    if st.button("Save Notes"):
        update_notes()
        st.success("Your notes are saved for this session!")

    if st.button("Clear Notes"):
        st.session_state.notes = ""
        st.session_state.notes_input = ""
        st.rerun()

# QUIZ
elif st.session_state.page == "Quiz":

    st.header("🎯 Quiz Practice")
    st.write("Test your basic Python knowledge!")

    question = st.radio(
        "Which keyword is used to define a function in Python?",
        ["for", "def", "if", "print"]
    )

    if st.button("Check Answer"):

        if question == "def":
            st.success("Correct Answer! 🎉")
        else:
            st.error("Try Again! The correct answer is def.")

# LEARNING GOAL
elif st.session_state.page == "Goal":

    st.header("💡 Your Learning Goal")

    goal = st.text_area("What do you want to learn today?")

    if st.button("Save Goal"):

        if goal.strip():
            st.session_state.goals.append(goal)
            st.success("Your learning goal has been saved!")
        else:
            st.warning("Please enter your goal.")

    st.subheader("Your Saved Goals")

    for i, saved_goal in enumerate(st.session_state.goals, 1):
        st.write(f"{i}. {saved_goal}")

# AI STUDY ASSISTANT
elif st.session_state.page == "AI Assistant":

    st.header("🤖 AI Study Assistant")

    st.write("Ask your study questions!")

    user_question = st.text_input(
        "Enter your question"
    )

    if st.button("Get Answer"):

        if user_question.strip():

            question = user_question.lower()

            if "python" in question:
                st.success(
                    "Python is a programming language "
                    "used to create applications."
                )

            elif "variable" in question:
                st.success(
                    "A variable is used to store data "
                    "in Python."
                )

            elif "loop" in question:
                st.success(
                    "A loop is used to repeat a set "
                    "of instructions."
                )

            elif "function" in question:
                st.success(
                    "A function is a reusable block "
                    "of code in Python."
                )

            elif "list" in question:
                st.success(
                    "A list is used to store multiple "
                    "items in Python."
                )

            else:
                st.info(
                    "Try asking about Python, variables, "
                    "loops, functions or lists."
                )

        else:
            st.warning("Please enter your question.")

st.divider()

st.caption(
    "Smart Student Brain | Student Learning Support Project"
)