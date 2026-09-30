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


# GET - Search jobs by company
@app.route("/api/jobs/search", methods=["GET"])
def search_jobs():
    company = request.args.get("company")

    if not company:
        return jsonify({
            "message": "Company parameter is required"
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT * FROM job_applications WHERE company = %s"
    cursor.execute(sql, (company,))

    jobs = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(jobs)

# GET - Search jobs by role
@app.route("/api/jobs/search/role", methods=["GET"])
def search_jobs_by_role():

    role = request.args.get("role")

    if not role:
        return jsonify({
            "message": "Role parameter is required"
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT * FROM job_applications WHERE role = %s"
    cursor.execute(sql, (role,))

    jobs = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(jobs)

# GET - Filter jobs by status
@app.route("/api/jobs/filter", methods=["GET"])
def filter_jobs():

    status = request.args.get("status")

    if not status:
        return jsonify({
            "message": "Status parameter is required"
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT * FROM job_applications WHERE status = %s"
    cursor.execute(sql, (status,))

    jobs = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(jobs)

# GET - Filter jobs by multiple conditions
@app.route("/api/jobs/advanced-filter", methods=["GET"])
def advanced_filter():

    company = request.args.get("company")
    role = request.args.get("role")
    status = request.args.get("status")

    if not company and not role and not status:
        return jsonify({
            "message": "At least one filter parameter is required"
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM job_applications WHERE 1=1"
    values = []

    if company:
        query += " AND company = %s"
        values.append(company)

    if role:
        query += " AND role = %s"
        values.append(role)

    if status:
        query += " AND status = %s"
        values.append(status)

    cursor.execute(query, tuple(values))

    jobs = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(jobs)

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