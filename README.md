# Ubatuba Events API

A FastAPI backend application for managing local events in Ubatuba, São Paulo. This application provides a RESTful API for browsing, searching, and managing local events.

## Prerequisites

- Python 3.11
- pip (Python package installer)

##  Install Python 3.11 (using pyenv)

### macOS

If you don't have `pyenv` installed:

```bash
  brew install pyenv
  pyenv install 3.11.9
  pyenv local 3.11.9
```
### Ubuntu / Debian

```bash
    sudo apt update
    sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    
```

then install pyenv (via curl):

```bash
curl https://pyenv.run | bash
```

Add the following to your ~/.bashrc or ~/.zshrc:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

Restart your shell, then:

```bash
pyenv install 3.11.9
pyenv local 3.11.9
```

### Windows (via pyenv-win)


```bash
git clone https://github.com/pyenv-win/pyenv-win.git $HOME\.pyenv
setx PATH "$HOME\.pyenv\pyenv-win\bin;$HOME\.pyenv\pyenv-win\shims;%PATH%"
```


```bash
pyenv install 3.11.9
pyenv local 3.11.9
```

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


## Infrastructure

### Database
The application uses PostgreSQL hosted on Supabase for data persistence. The database connection is configured using connection pooling for better performance and scalability.

### Hosting
The API is currently hosted on Render.com, providing continuous deployment from the main branch.

### Environment Variables
The following environment variables are required for database connection:


```bash
SUPABASE_DB_USER=
SUPABASE_DB_PASSWORD=
SUPABASE_DB_HOST=
SUPABASE_DB_PORT=
SUPABASE_DB_NAME=
```
## Getting Started:

To run the app type the following commands:

```bash
python3.11 -m venv venv
source venv/bin/activate
pip3.11 install -r requirements.txt
python3.11 migrations.py
uvicorn app.main:app --reload
```

The API will be available at:
- API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative Documentation: http://localhost:8000/redoc
