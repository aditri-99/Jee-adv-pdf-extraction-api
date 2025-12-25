from flask import Flask,request,jsonify
from extract import get_random_question
import json
import random

app = Flask(__name__)

with open("data/all_questions.json", "r", encoding="utf-8") as f:
    all_questions = json.load(f)


@app.route("/get_question")
def get_question_api():
    year=int(request.args.get("year"))      
    subject=request.args.get("subject")     

    question=get_random_question(year, subject)

    if question is None:
        return jsonify({"error": "No question found"}), 404

    return jsonify(question)


if __name__=="__main__":
    app.run(debug=True)



