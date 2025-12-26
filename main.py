import streamlit as st
import os
from dotenv import load_dotenv

# Use Groq for 100% stability and speed
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# --- 1. Load Environment Variables ---
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

# --- 2. Page Configuration ---
st.set_page_config(page_title="AI Technical Mentor", page_icon="🎓", layout="wide")

# --- 3. Module & Topic Mapping ---
MODULE_MAP = {
    "Python": {"emoji": "🐍🔥", "topics": "Python syntax, libraries (Pandas, Numpy), scripts, and logic."},
    "SQL": {"emoji": "💾💎", "topics": "SQL queries, Joins, Databases, DDL, DML, and Schema design."},
    "Power BI": {"emoji": "📊⚡", "topics": "Power BI Desktop, DAX functions, Power Query, Modeling, and Visuals."},
    "EDA": {"emoji": "🔍📈", "topics": "Exploratory Data Analysis, Matplotlib, Seaborn, and data cleaning."},
    "Machine Learning": {"emoji": "🤖🧠", "topics": "Supervised, Unsupervised learning, Scikit-learn, and Algorithms."},
    "Deep Learning": {"emoji": "🕸️🧪", "topics": "Neural Networks, CNN, RNN, PyTorch, and TensorFlow."},
    "Gen AI": {"emoji": "🎨✨", "topics": "LLMs, Prompt Engineering, LangChain, and RAG."},
    "Agentic AI": {"emoji": "🦾🚀", "topics": "AI Agents, AutoGPT, CrewAI, and Tool Use."}
}

# --- 4. Session State ---
if "module" not in st.session_state:
    st.session_state.module = None
if "messages" not in st.session_state:
    st.session_state.messages = []

def reset_session():
    st.session_state.module = None
    st.session_state.messages = []

# --- 5. Download Dialog ---
@st.dialog("Session Finished")
def show_exit_dialog():
    st.write(f"Great session on *{st.session_state.module}*!")
    full_log = f"--- {st.session_state.module} SESSION LOG ---\n\n"
    for msg in st.session_state.messages:
        role = "USER" if isinstance(msg, HumanMessage) else "MENTOR"
        full_log += f"{role}: {msg.content}\n\n"
    
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("📥 Download Log", data=full_log, file_name=f"{st.session_state.module}_chat.txt", mime="text/plain", on_click=st.rerun)
    with col2:
        if st.button("New Subject"):
            reset_session(); st.rerun()

# --- 6. Selection Screen ---
if st.session_state.module is None:
    st.title(":rainbow[Welcome to your AI Mentor]")
    st.header("Select a module to begin", divider="rainbow")
    selected = st.selectbox("📌 Select your learning path:", list(MODULE_MAP.keys()))
    if st.button("Start Mentoring"):
        st.session_state.module = selected; st.rerun()

# --- 7. Chat Interface ---
else:
    module_name = st.session_state.module
    emoji = MODULE_MAP[module_name]["emoji"]
    allowed_topics = MODULE_MAP[module_name]["topics"]
    
    st.title(f":rainbow[{module_name} Mentor {emoji}]")
    st.divider()

    with st.sidebar:
        if st.button("⬅️ Change Subject"):
            reset_session(); st.rerun()

    for message in st.session_state.messages:
        role = "user" if isinstance(message, HumanMessage) else "assistant"
        with st.chat_message(role):
            st.markdown(message.content)

    if prompt := st.chat_input(f"Ask about {module_name}..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append(HumanMessage(content=prompt))

        if prompt.lower().strip() in ["bye", "goodbye", "exit"]:
            show_exit_dialog()
        else:
            try:
                # 🚀 Groq is much faster and more reliable
                chat_model = ChatGroq(
                    api_key=groq_key,
                    model_name="llama-3.3-70b-versatile",
                    temperature=0.4
                )

                prompt_template = ChatPromptTemplate.from_messages([
                    ("system", f"""You are a technical mentor for {module_name}.
                    Allowed Expertise: {allowed_topics}.
                    If the user asks about anything else, respond ONLY with: 
                    'I am not aware, please ask questions related to this module.'"""),
                    MessagesPlaceholder(variable_name="chat_history"),
                    ("human", "{input}")
                ])

                chain = prompt_template | chat_model
                
                with st.chat_message("assistant"):
                    with st.spinner("Mentor is thinking..."):
                        response = chain.invoke({
                            "input": prompt, 
                            "chat_history": st.session_state.messages[:-1]
                        })
                        st.markdown(response.content)
                        st.session_state.messages.append(AIMessage(content=response.content))
            except Exception as e:
                st.error(f"Error: {str(e)}")