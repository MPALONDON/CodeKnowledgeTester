# Code Knowledge Tester

A FastAPI + React application that tests coding knowledge using AI-generated multiple-choice questions. Users sign in via **Clerk authentication**, answer questions, and receive instant feedback with explanations. The app also keeps a history of previously generated questions for review and learning.

---

## Features

- AI-generated coding questions using **OpenAI API**.
- Multiple-choice answers with instant feedback and explanations.
- User authentication and management via **Clerk**.
- History of previously generated questions for review.
- Clean, modern interface with **React** frontend and **FastAPI** backend.

---

## Technologies Used

- **Backend:** FastAPI, Python  
- **Frontend:** React, JavaScript, HTML, CSS  
- **Authentication:** Clerk  
- **AI Integration:** OpenAI API  
- **Database:** SQLite / PostgreSQL (depending on setup)

---

## Environment Variables

### Frontend (`.env` in frontend folder)
```env
VITE_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key
VITE_BACKEND_URL=http://localhost:8000
VITE_FRONTEND_URL=http://localhost:5173
```
- `VITE_CLERK_PUBLISHABLE_KEY`: Public key for Clerk authentication.
- `VITE_BACKEND_URL`: URL of the backend API.
- `VITE_FRONTEND_URL`: URL of the frontend for redirects.

### Backend (`.env` in backend folder)
```env
CLERK_SECRET_KEY=your_clerk_secret_key
JWT_KEY=your_jwt_public_key
DATABASE=sqlite:///database.db
OPENAI_API_KEY=your_openai_api_key
CLERK_WEBHOOK_SECRET=your_clerk_webhook_secret
FRONTEND_URL=http://localhost:5173
PORT=8000
```
- `CLERK_SECRET_KEY`: Secret key for backend authentication.
- `JWT_KEY`: Public key for JWT verification.
- `DATABASE`: Database URL.
- `OPENAI_API_KEY`: API key for OpenAI.
- `CLERK_WEBHOOK_SECRET`: Secret to verify Clerk webhooks.
- `FRONTEND_URL`: URL of the frontend.
- `PORT`: Backend server port.

> **Important:** Do not commit `.env` files to version control. Use `.gitignore` and environment variables on deployment platforms.

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/MPALONDON/CodeKnowledgeTester.git
cd CodeKnowledgeTester
```

2. **Backend setup:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Frontend setup:**
```bash
cd ../frontend
npm install
```

4. **Add `.env` files** as described above.

---

## Running the Application

**Backend:**
```bash
cd backend
python server.py
```

**Frontend:**
```bash
cd frontend
npm start
```


---

## Usage

1. Sign in with **Clerk authentication**.
2. Generate coding questions via the AI-powered interface.
3. Answer multiple-choice questions and receive instant feedback with explanations.
4. Review your history of previously generated questions.

---

## Demo

Live demo: [https://codeknowledgetester-frontend.onrender.com/](https://codeknowledgetester-frontend.onrender.com/)

---



