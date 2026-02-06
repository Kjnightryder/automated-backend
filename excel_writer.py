import os
import pandas as pd
from datetime import datetime

FILE_PATH = "results.xlsx"

def append_result(data):
    row = {
        "candidate_id": data["candidate_id"],
        "score": data["score"],
        "time_taken": data["time_taken"],
        "violations": data["violations"],
        "decision": data["decision"],
        "timestamp": datetime.utcnow().isoformat()
    }

    if os.path.exists(FILE_PATH):
        df = pd.read_excel(FILE_PATH)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_excel(FILE_PATH, index=False)
