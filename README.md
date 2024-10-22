# Expenses_App

A simple expense management API built with FastAPI and PostgreSQL. This project allows you to track expenses, split amounts among participants, and manage expenses with ease.

# Features
Add expenses with descriptions and amounts

Split expenses among participants (e.g., equally or custom amounts)

Retrieve a list of all expenses

PostgreSQL integration for data persistence

# Prerequisites
Python 3.10+
PostgreSQL
Git
pip

# Installation 
1. Clone the repository
   git clone https://github.com/yourusername/expenses-app.git
   cd expenses-app

2. Create a virtual environment
   python -m venv venv

3. Activate the virtual environment
   Windows: venv\Scripts\activate
   Linux/Mac: source venv/bin/activate
   
4. Install dependencies
   pip install -r requirements.txt

# Running the Application
1. Start the FastAPI server
   python -m uvicorn app.main:app --reload

2. Check the logs: You should see the following message
   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

3. Access the API documentation: Open your browser and go to
   http://127.0.0.1:8000/docs

# API Endpoints
1. POST /expenses/ – Create a new expense
Request Body:

{
  "description": "Dinner with friends",
  "amount": 120.50,
  "split_method": "equally",
  "participants": [
    { "name": "Alice", "amount": 40.17 },
    { "name": "Bob", "amount": 40.17 },
    { "name": "Charlie", "amount": 40.16 }
  ]
}

2. GET /expenses/ – Retrieve all expenses


