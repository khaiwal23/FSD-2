# Experiment 16 – Full Stack Testing with GitHub Actions

## 📌 Objective
To test backend and frontend using pytest and vitest and automate using GitHub Actions.

---

## 🖥️ Backend Setup

```bash
cd Experiment-16/backend
pip install flask pytest requests
python app.py

#Backend Testing
pytest

#Frontend Setup
cd Experiment-16/frontend/frontend-app
npm install
npm run dev

#Frontend Testing
npx vitest

#CI/CD (GitHub Actions)
GitHub Actions runs tests automatically on every push
Backend and frontend both are tested

#Screenshots
GitHub Actions PASS
Backend running
Frontend running
Test results

#Technologies Used
Flask (Backend)
React + Vite (Frontend)
Pytest (Backend testing)
Vitest (Frontend testing)
GitHub Actions (CI/CD)


---

# 🚀 After creating README

Run this:

```bash id="2v4gcs"
git add .
git commit -m "added README for experiment 16"
git push