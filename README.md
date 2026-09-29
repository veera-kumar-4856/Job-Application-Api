# Job Application REST API

A backend REST API for managing job applications using Python, Flask, and MySQL.

## Features

- View all job applications
- View a single job application by ID
- Add a new job application
- Update an existing job application
- Delete a job application
- Request validation
- 400 Bad Request handling
- 404 Not Found handling
- Environment-based database configuration

## Technologies Used

- Python
- Flask
- MySQL
- MySQL Connector/Python
- REST API
- Postman
- python-dotenv

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/jobs` | Get all job applications |
| GET | `/api/jobs/<id>` | Get a job application by ID |
| POST | `/api/jobs` | Add a new job application |
| PUT | `/api/jobs/<id>` | Update a job application |
| DELETE | `/api/jobs/<id>` | Delete a job application |

## Example Job Data

```json
{
    "company": "TCS",
    "role": "Python Developer",
    "status": "Applied"
}