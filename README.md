# Ubatuba Events API

A FastAPI backend application for managing local events in Ubatuba, São Paulo. This application provides a RESTful API for browsing, searching, and managing local events.

## Prerequisites

- Python 3.11
- pip (Python package installer)

## Setting up Python 3.11

### macOS (using Homebrew) 

The API will be available at:
- API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative Documentation: http://localhost:8000/redoc

## API Endpoints

- `GET /events`: Retrieve all events
- `GET /events/{id}`: Retrieve specific event details
- `POST /events`: Create a new event
- `PUT /events/{id}`: Update an existing event
- `DELETE /events/{id}`: Delete an event

## Features

- RESTful API design
- Data validation using Pydantic
- SQLite database
- Automatic API documentation
- Error handling
- Event management (CRUD operations)

## Development

The application is built using:
- Python 3.11
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

## License

[Your License Here] 