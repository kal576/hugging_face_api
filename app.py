from flask import Flask, request, jsonify
import mysql.connector
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

#sql connection
db = mysql.connector.connect(
            host="localhost",
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            database="your_database_name"
            )

cursor = db.cursor()

#api to hugging face
HF_API_TOKEN = os.getenv("HF_API_KEY")
HF_URL = "https://api-inference.huggingface.co/models/valhalla/t5-base-e2e-qg"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

#routes
@app.route("/generate-quiz", methods=["POST"])
def gen_quiz():
    """
    Generates questions when requested by frontend
    """
    data = request.get_json()
    context = data.get("context", "").strip()

    if not context:
        return jsonify({"error": "Context is required"}), 400

    # call Hugging Face API tp generate questions
    try:
        response = requests.post(
                HF_URL,
                headers=headers,
                json={"inputs": context}
                )

        response.raise_for_status()
        result = response.json()

        # check if there is an error in generating the question
        if "error" in result:
            print("Model error:", result["error"])

        # check if the result is a list
        elif isinstance(result, list) and "generated_text" in result:
            questions = [item["generated_text"]for item in result]

        # check if it's a dict
        elif isinstance(result, dict) and "generated_text" in result:
            questions = [result["generated_text"]]

        else:
            questions = []

        # save to MySql
        cursor = db.cursor()
        insert_query = "INSERT INTO flashcards (question, answer) VALUES (%s, %s)"

        for q in questions:
            cursor.execute(insert_query, (q, "N/A"))

        db.commit()
        
        return jsonify({'success': True, 'flashcards': questions})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
