# CodeGrace

Hackathon Competition Project — a collaborative Django web application built by a team of 4.

## Features

- **Home page** with project listings and team member cards
- **Project management** — view projects and their tasks
- **Team page** — showcase all 4 team members with roles and bios
- **User authentication** — register, login, and logout
- **Django Admin** — manage projects, tasks, and team members

## Team

This project is developed by a team of 4 members collaborating on a hackathon competition.

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
# Clone the repository
git clone https://github.com/nextgeneratio/CodeGrace.git
cd CodeGrace

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# (Optional) Create a superuser for the admin panel
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Project Structure

```
CodeGrace/
├── codegrace/          # Django project settings & URL config
├── core/               # Main app (models, views, admin, URLs)
│   └── migrations/     # Database migrations
├── templates/          # HTML templates
│   ├── base.html
│   └── core/
│       ├── home.html
│       ├── login.html
│       ├── register.html
│       ├── project_list.html
│       ├── project_detail.html
│       └── team.html
├── manage.py
└── requirements.txt
```

## Models

- **TeamMember** — extends Django User with role, bio, and avatar
- **Project** — hackathon project with title, description, and members
- **Task** — task within a project, assignable to a team member with status tracking
