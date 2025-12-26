# 🤖 AI Chatbot Mentor  
### Domain-Specific Intelligent Learning Assistant

AI Chatbot Mentor is a **domain-restricted AI mentoring application** built with **Streamlit and LangChain**.  
It provides **focused, module-specific guidance** by answering questions **only within the selected learning domain**, avoiding irrelevant or hallucinated responses.

---

## 🚀 Key Features

### 🎯 Module-Based Mentoring  
Users select a learning module and receive guidance limited strictly to that domain.

### 🧠 Strict Domain Control  
Questions outside the selected module are rejected with a fixed response to ensure learning focus.

### 💬 Continuous Chat Experience  
Maintains session-based conversation history.

### 📥 Download Chat History  
Entire chat (user + AI responses) can be downloaded as a `.txt` file for revision or notes.

### 🧼 Simple & Clean UI  
Built using Streamlit’s chat interface for clarity and ease of use.

---

## 📚 Supported Modules

- Python  
- SQL  
- Power BI  
- Exploratory Data Analysis (EDA)  
- Machine Learning  
- Deep Learning  
- Generative AI  
- Agentic AI  

---

## ⚠️ Domain Restriction Logic

If a question is unrelated to the selected module, the chatbot responds **exactly** with:

Sorry, I don’t know about this question. Please ask something related to the selected module.

This ensures **accurate, distraction-free mentoring**.

---

## 🛠 Tech Stack

- **Frontend:** Streamlit  
- **AI Orchestration:** LangChain  
- **LLM:** Hugging Face Chat Models (DeepSeek / LLaMA-based)  
- **Language:** Python  
- **Export Format:** Text (.txt)

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/voonaanusha18/ai-chatbot-mentor.git
cd domain-specific-ai-mentor-chatbot

```
2️⃣ Install dependencies

```bash

pip install -r requirements.txt

```

3️⃣ Add environment variables

Create a .env file:

```bash

hf=YOUR_HUGGINGFACE_API_KEY

```

4️⃣ Run the app

```bash

streamlit run app.py

```

---

🎓 Learning Outcomes

This project demonstrates:

Designing domain-restricted AI systems

Prompt engineering for controlled responses

Using LangChain with chat models

Streamlit session management

Implementing chat export functionality

Structuring real-world AI applications



---

🏁 Conclusion

AI Chatbot Mentor bridges the gap between generic chatbots and focused educational AI systems by enforcing strict domain control and offering practical features like chat history downloads.

---