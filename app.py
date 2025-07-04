# app.py
from flask import Flask, request, jsonify
import sqlite3 
import os

from flask import render_template
import config
from models import Person

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'people.db')  # adjust if it's in a subfolder
db_path = './oral_cancer_app/sqlite_backup/people.db'

def get_db_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
        return None

@app.route("/")
def home():
    return '✅ FLask SQLite Web API for Oral Cancer App is running locally. Go to /schema or /data for API calls.'

@app.route("/schema")
def get_schema():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(person)")
        columns = cursor.fetchall()
        return {"schema": schema}
    return {"error": "Database connection failed"}

@app.route("/PatientNames",methods=["GET"])
def get_PatientNames():
    conn = get_db_connection()
    cursor = conn.cursor()
    n = request.args.get("n", default=5, type=int)
    cursor.execute("SELECT uid,patientName FROM person LIMIT?",(n,))
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)
    #return jsonify([dict(row) for row in rows])




@app.route("/PatientNames_forAge",methods=["GET"])
def filterPatientName_forAge():
    age = request.args.get("age", type=int)
    print(f"Filtering patient names for age: {age}")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT patientName FROM person WHERE patientAge = ?",(age,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return jsonify([row[0] for row in rows])




@app.route("/patientcount_forAge",methods=["GET"])
def get_patientcount_forAge():
    age = request.args.get("age", type=int)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count(patientName) FROM person WHERE patientAge = ?",(age,))
    row = cursor.fetchone()
    return jsonify(row)



@app.route('/Agewisepatients',methods=["GET"])
def getAgewisepatients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT patientAge,count(patientName) FROM person GROUP BY patientAge")
    rows = cursor.fetchall()    
    #return jsonify([(row[0],row[1]) for row in rows])
    return jsonify([{"age":row[0],"count":row[1]} for row in rows])



@app.route('/Genderwisepatients',methods=["GET"])
def get_GenderwisePatients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count(patientName),patientGender FROM person GROUP BY patientGender")
    rows = cursor.fetchall()
    return jsonify([{"gender":row[0],"count":row[1]} for row in rows])


@app.route('/risk_factors',methods=["GET"])
def get_riskfactors():
    conn = get_db_connection()
    cursor = conn.cursor()

    #cursor.execute("SELECT COUNT(*) AS total,paan, alcoholIntake, smoking, tobaccoChewing FROM person GROUP BY paan, alcoholIntake, smoking, tobaccoChewing ORDER BY total DESC LIMIT 10")
    habits = ["alcoholIntake", "paan", "smoking", "tobaccoChewing"]
    results = []

    for habit in habits:
        query = f"""
        SELECT patientAge, COUNT({habit})
        FROM person
        WHERE {habit} = 'No'
        GROUP BY patientAge
        """
    cursor.execute(query)
    rows = cursor.fetchall()
    results.append([
        {"patientAge": row[0], f"count({habit})": row[1]} for row in rows
    ])

    return jsonify(results)





'''connect to the database
conn = get_db_connection()
cursor = conn.cursor()'''

'''get_schema()
filterPatientName_forAge()
get_patientcount_forAge()
get_GenderwisePatients()'''

#conn.close()


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)