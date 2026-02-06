from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from excel_writer import append_result
import uuid
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/api/submit", methods=["POST"])
def submit_assessment():
    data = request.json

    result = {
        "candidate_id": f"CAND-{uuid.uuid4().hex[:8]}",
        "score": data.get("score"),
        "time_taken": data.get("time_taken"),
        "violations": data.get("violations"),
        "decision": data.get("decision")
    }

    append_result(result)

    return jsonify({
        "status": "success",
        "candidate_id": result["candidate_id"]
    })

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

