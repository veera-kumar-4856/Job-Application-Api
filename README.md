# Job Application API

A RESTful Job Application Management API built using **Python, Flask, and MySQL**.
The API allows users to create, view, update, delete, search, and filter job application records.

## Features

* Create a new job application
* Get all job applications
* Get a single job application by ID
* Update an existing job application
* Delete a job application
* Search jobs by company
* Search jobs by role
* Filter jobs by application status
* Advanced filtering using company, role, and status
* Input validation
* Error handling
* MySQL database integration
* Environment variables using `.env`
* API testing using Postman

## Technologies Used

* Python
* Flask
* MySQL
* MySQL Connector/Python
* python-dotenv
* Postman
* Git
* GitHub

## Project Structure

```text
Job-Application-Api-Test/
│
├── app.py
├── test_db.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
└── venv/
```

## Database

The project uses a MySQL database with a `job_applications` table.

### Table Structure

| Column  | Description                      |
| ------- | -------------------------------- |
| id      | Unique ID of the job application |
| company | Company name                     |
| role    | Job role                         |
| status  | Application status               |

Example data:

```text
TCS        | Python Developer | Interview
Zoho       | Developer        | Interview
Infosys    | Python Developer | Applied
HCL        | Backend Developer| Applied
Accenture  | Python Developer | Interview
```

## Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
```

The `.env` file should not be committed to GitHub.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/veera-kumar-4856/Job-Application-Api.git
```

### 2. Open the project

```bash
cd Job-Application-Api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Create the required database and `job_applications` table in MySQL.

### 7. Configure `.env`

Add your MySQL credentials to the `.env` file.

### 8. Run the Flask application

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

---

# API Endpoints

## 1. Home

**GET**

```text
/
```

Example:

```text
GET http://127.0.0.1:5000/
```

Response:

```text
Job Application API is running!
```

---

## 2. Get All Job Applications

**GET**

```text
/api/jobs
```

Example:

```text
GET http://127.0.0.1:5000/api/jobs
```

Returns all job applications.

---

## 3. Get a Job Application by ID

**GET**

```text
/api/jobs/<job_id>
```

Example:

```text
GET http://127.0.0.1:5000/api/jobs/6
```

Example response:

```json
{
    "company": "Accenture",
    "id": 6,
    "role": "Python Developer",
    "status": "Interview"
}
```

If the ID does not exist:

```json
{
    "message": "Job application not found"
}
```

---

## 4. Add a Job Application

**POST**

```text
/api/jobs
```

Example:

```text
POST http://127.0.0.1:5000/api/jobs
```

Request body:

```json
{
    "company": "Wipro",
    "role": "Python Developer",
    "status": "Applied"
}
```

Successful response:

```json
{
    "id": 8,
    "message": "Job application added successfully"
}
```

### Required Fields

* `company`
* `role`
* `status`

Example validation response:

```json
{
    "error": "Company is required"
}
```

---

## 5. Update a Job Application

**PUT**

```text
/api/jobs/<job_id>
```

Example:

```text
PUT http://127.0.0.1:5000/api/jobs/6
```

Request body:

```json
{
    "company": "Accenture",
    "role": "Python Developer",
    "status": "Interview"
}
```

Successful response:

```json
{
    "message": "Job application updated successfully"
}
```

If the job ID does not exist:

```json
{
    "message": "Job application not found"
}
```

---

## 6. Delete a Job Application

**DELETE**

```text
/api/jobs/<job_id>
```

Example:

```text
DELETE http://127.0.0.1:5000/api/jobs/8
```

Successful response:

```json
{
    "message": "Job application deleted successfully"
}
```

If the job ID does not exist:

```json
{
    "message": "Job application not found"
}
```

---

# Search and Filtering

## 7. Search by Company

**GET**

```text
/api/jobs/search?company=<company>
```

Example:

```text
GET http://127.0.0.1:5000/api/jobs/search?company=TCS
```

Returns job applications matching the company.

---

## 8. Search by Role

**GET**

```text
/api/jobs/search/role?role=<role>
```

Example:

```text
GET http://127.0.0.1:5000/api/jobs/search/role?role=Python%20Developer
```

Returns job applications matching the specified role.

---

## 9. Filter by Status

**GET**

```text
/api/jobs/filter?status=<status>
```

Example:

```text
GET http://127.0.0.1:5000/api/jobs/filter?status=Interview
```

Possible status values used in the project include:

```text
Applied
Interview
```

---

## 10. Advanced Filtering

**GET**

```text
/api/jobs/advanced-filter
```

The endpoint supports:

* Company
* Role
* Status
* Multiple filters together

### Company

```text
GET http://127.0.0.1:5000/api/jobs/advanced-filter?company=Accenture
```

### Status

```text
GET http://127.0.0.1:5000/api/jobs/advanced-filter?status=Interview
```

### Company + Status

```text
GET http://127.0.0.1:5000/api/jobs/advanced-filter?company=Accenture&status=Interview
```

### Role + Status

```text
GET http://127.0.0.1:5000/api/jobs/advanced-filter?role=Python%20Developer&status=Interview
```

### Company + Role + Status

```text
GET http://127.0.0.1:5000/api/jobs/advanced-filter?company=Accenture&role=Python%20Developer&status=Interview
```

If no filter is provided:

```json
{
    "message": "At least one filter parameter is required"
}
```

---

# Error Handling

The API validates incoming requests and returns appropriate error responses.

### Empty Request Body

```json
{
    "error": "Request body is required"
}
```

### Missing Company

```json
{
    "error": "Company is required"
}
```

### Missing Role

```json
{
    "error": "Role is required"
}
```

### Missing Status

```json
{
    "error": "Status is required"
}
```

### Job Not Found

```json
{
    "message": "Job application not found"
}
```

---

# Testing

The API was tested using **Postman**.

The following operations were tested:

* GET all jobs
* GET job by ID
* POST job application
* POST validation
* PUT job application
* PUT validation
* DELETE existing job
* DELETE non-existing job
* Search by company
* Search by role
* Filter by status
* Advanced filtering
* Missing parameter validation

Successful responses and error responses were verified using Postman.

# Project Purpose

This project was developed to practice:

* REST API development
* Flask
* CRUD operations
* MySQL database connectivity
* SQL queries
* API validation
* HTTP status codes
* Query parameters
* Error handling
* Postman API testing
* Git and GitHub workflow

# Author

**Veera Kumar M M**

B.Tech Information Technology
