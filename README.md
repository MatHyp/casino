# Casino Web Application

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A containerized virtual casino web application built with Python Flask and PostgreSQL.

## Features

- User authentication system
- PostgreSQL database backend
- Docker containerization
- Flask web framework
- MVC architecture
- Ready-to-deploy configuration

## Prerequisites

- Docker 20.10+
- Docker Compose 1.29+
- Python 3.11 (included in container)

## Quick Start

```bash
# Clone the repository
git clone https://github.com/MatHyp/casino.git
cd casino

# Start the application
docker-compose up --build

The application will be available at: http://localhost:5000

Project Structure

.
├── app/                  # Application core
│   ├── controllers/      # Business logic
│   │   └── auth.py       # Authentication handlers
│   ├── models/           # Database models
│   │   └── User.py       # User model
│   ├── templates/        # HTML templates
│   ├── __init__.py       # App initialization
│   └── routes.py         # URL routing
├── venv/                 # Virtual environment
├── docker-compose.yml    # Multi-container setup
├── Dockerfile            # Web service configuration
├── docker_restart.sh     # Utility script
├── requirements.txt      # Python dependencies
└── run.py                # Application entry point
