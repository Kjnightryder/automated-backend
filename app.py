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
