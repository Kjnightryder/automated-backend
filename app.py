from flask import Flask, request, jsonify
from excel_writer import append_result
import uuid

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/api/submit", methods=["POST"])
def submit_assessment():
    data = request.json

    result = {
        "candidate_id": f"CAND-{uuid.uuid4().hex[:6]}",
        "score": data.get("score", 0),
        "time_taken": data.get("time_taken", 0),
        "violations": data.get("violations", 0),
        "decision": data.get("decision", "Pending")
    }

    append_result(result)

    return jsonify({
        "status": "success",
        "candidate_id": result["candidate_id"]
    })
from flask import send_file

from flask import send_file, jsonify
import os

@app.route("/api/download/excel", methods=["GET"])
def download_excel():
    if not os.path.exists("results.xlsx"):
        return jsonify({
            "error": "No results yet. Please submit at least one assessment first."
        }), 400

    return send_file(
        "results.xlsx",
        as_attachment=True,
        download_name="assessment_results.xlsx"
    )


