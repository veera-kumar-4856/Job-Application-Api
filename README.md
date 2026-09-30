# Job Application API

A RESTful Job Application Management API built using **Python, Flask, and MySQL**.

This API allows users to create, view, update, and delete job application records.

## Technologies Used

* Python
* Flask
* MySQL
* MySQL Connector/Python
* python-dotenv
* Postman
* Git & GitHub

## Project Structure

```text
Job-Application-Api-Test/
│
├── app.py
├── test_db.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── venv/
```

## Database

The project uses a MySQL database named:

```text
job_tracker
```

The main table is:

```text
job_applications
```

The table contains:

| Column  | Description               |
| ------- | ------------------------- |
| id      | Unique job application ID |
| company | Company name              |
| role    | Job role                  |
| status  | Application status        |

## Environment Variables

Database credentials are stored in a `.env` file.

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=job_tracker
```

**Note:** The `.env` file should not be uploaded to GitHub.

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/veera-kumar-4856/Job-Application-Api.git
```

### 2. Open the project

```bash
cd Job-Application-Api
```

### 3. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure `.env`

Create a `.env` file in the project root and add your MySQL credentials.

### 6. Run the Flask application

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### 1. Get All Job Applications

```http
GET /api/jobs
```

Example:

```text
http://127.0.0.1:5000/api/jobs
```

### 2. Get a Single Job Application

```http
GET /api/jobs/<id>
```

Example:

```text
http://127.0.0.1:5000/api/jobs/6
```

### 3. Add a Job Application

```http
POST /api/jobs
```

Request body:

```json
{
    "company": "Wipro",
    "role": "Python Developer",
    "status": "Applied"
}
```

### 4. Update a Job Application

```http
PUT /api/jobs/<id>
```

Request body:

```json
{
    "company": "Accenture",
    "role": "Python Developer",
    "status": "Interview"
}
```

### 5. Delete a Job Application

```http
DELETE /api/jobs/<id>
```

Example:

```text
http://127.0.0.1:5000/api/jobs/8
```

## Validation

The API validates required fields when creating or updating a job application.

For example:

```json
{
    "error": "Company is required"
}
```

Other validation messages include:

```json
{
    "error": "Role is required"
}
```

```json
{
    "error": "Status is required"
}
```

The API also handles requests for job IDs that do not exist:

```json
{
    "message": "Job application not found"
}
```

## Testing

The API was tested using **Postman**.

Tested operations include:

* GET all jobs
* GET a single job
* POST a new job
* PUT/update a job
* DELETE a job
* Required-field validation
* Non-existent job ID handling

## Author

Veera Kumar M M
