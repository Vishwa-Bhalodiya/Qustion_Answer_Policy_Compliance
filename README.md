# Policy Compliance Using LLM (Question & Answer Based)

An AI-powered system that analyzes and aligns policy documents using a **Question-Answer based approach** insted of traditional paragraph matching. This improves contextual understanding and accuracy in compliance detection.

---

## Features
- Upload and process policy documents
- Text exxtraction and preprocessing
- Question-based policy evaluation
- AI-generated answers using LLMs
- Compliance detection (Match / Partial / Gap)
- Structured compliance report generation
- RESTful API for scalable integration

---

## Tech Stack
- Python - Core programming language
- FastAPI - Backend API framework
- Mistral / Gemini (LLMs) - Question answring & reasoning
- NLP Techniques - Text processing
- Postman - API Testing
- Git & Github - Version control

---

## Project Structure

```bash
QA_Compliance/
│── main.py
│── compare_service.py
│── mistral_service.py
│── text_utils.py
│── requirements.txt
│── .gitignore
```

---

## Setup Instructions

### 1. Clone Repo
```bash
git clone https://github.com/Vishwa-Bhalodiya/Qustion_Answer_Policy_Compliance.git
cd Question_Answer_Policy_Compliance
```

### 2. Create Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables

create a .env file in the root directory:
```bash
MISTRAL_API_KEY=your_api_key
```
OR
```bash
GEMINI_API_KEY=your_api_key
```

### 5. Run Project
```bash
uvicorn main:app --reload
```

### 6. API Testing

Use Postman to test:
- Document upload
- Question-based policy evaluation
- Compliance result generation
---

## How it Works

1. Upload policy documents
2. Extract and preprocess text
3. Generate compliance-related questions from client side policy
4. Use LLM to generate answers from documents (client & vendor)
5. Compare answers between policies
6. Determine compliance (Mtch / Partial / Gap)
7. Generate final compliance report

---

## Use Cases

- Policy compliance verification
- Regulatory requirement validation
- Vendr policy evaluation
- AI-based legal analysis





