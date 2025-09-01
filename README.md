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
