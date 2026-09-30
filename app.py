from flask import Flask, jsonify, request
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


@app.route("/")
def home():
    return "Job Application API is running!"


# GET - Get all job applications
@app.route("/api/jobs", methods=["GET"])
def get_jobs():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM job_applications")
    jobs = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(jobs)


# GET - Get a single job application
@app.route("/api/jobs/<int:job_id>", methods=["GET"])
def get_job(job_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM job_applications WHERE id = %s",
        (job_id,)
    )

    job = cursor.fetchone()

    if not job:
        cursor.close()
        connection.close()
        return jsonify({
            "message": "Job application not found"
        }), 404

    cursor.close()
    connection.close()

    return jsonify(job)


# POST - Add a new job application
@app.route("/api/jobs", methods=["POST"])
def add_job():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    if not data.get("company"):
        return jsonify({
            "error": "Company is required"
        }), 400

    if not data.get("role"):
        return jsonify({
            "error": "Role is required"
        }), 400

    if not data.get("status"):
        return jsonify({
            "error": "Status is required"
        }), 400

    company = data["company"]
    role = data["role"]
    status = data["status"]

    connection = get_db_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO job_applications (company, role, status)
        VALUES (%s, %s, %s)
    """
    values = (company, role, status)

    cursor.execute(sql, values)
    connection.commit()

    new_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Job application added successfully",
        "id": new_id
    }), 201


# PUT - Update a job application
@app.route("/api/jobs/<int:job_id>", methods=["PUT"])
def update_job(job_id):
    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Request body is required"
        }), 400

    required_fields = ["company", "role", "status"]

    for field in required_fields:
        if field not in data or not isinstance(data[field], str) or not data[field].strip():
            return jsonify({
                "message": f"{field} is required"
            }), 400

    company = data["company"].strip()
    role = data["role"].strip()
    status = data["status"].strip()

    connection = get_db_connection()
    cursor = connection.cursor()

    sql = """
        UPDATE job_applications
        SET company = %s, role = %s, status = %s
        WHERE id = %s
    """
    values = (company, role, status, job_id)

    cursor.execute(sql, values)

    if cursor.rowcount == 0:
        cursor.close()
        connection.close()
        return jsonify({
            "message": "Job application not found"
        }), 404

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Job application updated successfully"
    }), 200


# DELETE - Delete a job application
@app.route("/api/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "DELETE FROM job_applications WHERE id = %s"
    values = (job_id,)

    cursor.execute(sql, values)

    if cursor.rowcount == 0:
        cursor.close()
        connection.close()
        return jsonify({
            "message": "Job application not found"
        }), 404

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Job application deleted successfully"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)