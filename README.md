## Flashcard Quiz Generator

A simple web app that takes in user-provided text (notes, study material, etc.), sends it to a Hugging Face model to generate quiz questions, and stores the flashcards in a MySQL database.

## Features

Accepts text input from a frontend (via REST API).

Calls Hugging Face’s T5-base Question Generation model to generate quiz questions.

Stores questions (and answers, if extended) in a MySQL database.

Provides JSON responses for frontend integration.

## Tech Stack

Backend: Flask (Python)

Database: MySQL

API: Hugging Face Inference API

Environment Variables: python-dotenv

## Setup & Installation
1. Clone the repositor
   git clone https://github.com/kal576/hugging_face_api
   cd hugging_face_api

3. Create a virtual environment (optional but recommended)
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows

5. Install dependencies
   pip install -r requirements.txt

7. Set up .env file
   Create a file called .env in the project root and add:
   DB_USERNAME=your_mysql_username_here
   DB_PASSWORD=your_mysql_password_here
   HF_API_KEY=your_huggingface_api_key_here

9. Configure MySQL
    Make sure you have a MySQL database set up:
   CREATE DATABASE hugging_face_db;
   USE hugging_face_db;

   CREATE TABLE flashcards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    answer TEXT
);

6. Run the app
   python app.py


The Flask server will start at http://127.0.0.1:5000
