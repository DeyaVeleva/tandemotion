# TandeMotion

**A Django web application for organizing sports training, managing athlete and coach profiles, and reflecting on training progress.**

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation Instructions](#installation-instructions)
3. [Usage Examples](#usage-examples)
4. [Features/Functionality](#featuresfunctionality)
5. [Future Improvements](#future-improvements)

## 1. Project Overview

TandeMotion is a web application developed as an individual project for the SoftUni Django Basics course. Its purpose is to provide a centralized place for managing sports training activities and related information.

The application allows users to manage coach and athlete profiles, organize training sessions, maintain competition information, and create athlete reflections about their training experiences.

The project is built with Django and follows the Model-View-Template (MVT) architectural pattern. It uses Django models to represent application data, forms to handle user input, views to manage application logic, and templates to render the user interface.

### Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Django Template Language

## 2. Installation Instructions

### Prerequisites

- Python installed on your system
- pip package manager
- Git

### Step 1: Clone the repository

```bash
git clone https://github.com/DeyaVeleva/tandemotion.git
cd tandemotion
```

### Step 2: Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install dependencies

If the repository includes a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

### Step 4: Configure environment variables

If environment variables are required, create a local `.env` file based on `.env.example` and configure the required values.

Do not publish secret keys or other private credentials.

### Step 5: Apply database migrations

```bash
python manage.py migrate
```

### Step 6: Run the development server

```bash
python manage.py runserver
```

Open the address displayed in the terminal, usually:

`http://127.0.0.1:8000/`

## 3. Usage Examples

After starting the application, use the navigation menu to access the available sections.

### Managing Profiles

Navigate to the profiles section to view and manage coach and athlete information.

### Organizing Training Sessions

Open the training section to create a training session and provide information such as its title, date, time, location, description, coaches, and athletes.

### Managing Competitions

Navigate to the competitions section to view and manage competition information.

### Creating Athlete Reflections

Open a training session's reflection section to add a reflection. Depending on the available fields, a reflection can include a rating, main goals, and personal observations.

### Running Project Checks

To check the Django project for common configuration problems, run:

```bash
python manage.py check
```

## 4. Features/Functionality

- **Profile Management:** Organize information about coaches and athletes.
- **Training Management:** Create, view, update, and delete training sessions.
- **Participant Organization:** Associate coaches and athletes with training sessions.
- **Competition Management:** Maintain competition-related information.
- **Athlete Reflections:** Record and review reflections associated with training sessions.
- **Form Validation:** Validate submitted information and display appropriate error messages.
- **Reusable Templates:** Use template inheritance and shared components for a consistent interface.
- **Database Integration:** Store application data using Django models and SQLite.
- **Navigation:** Access application sections through the site's navigation.

## 5. Future Improvements

Possible future improvements for TandeMotion include:

- Expanding training organization and categorization.
- Adding more structured assignment and coach feedback functionality.
- Improving athlete progress tracking over time.
- Enhancing filtering and sorting options for training sessions and competitions.
- Improving the presentation of training history and athlete reflections.
- Expanding the interface and adding further usability improvements.

