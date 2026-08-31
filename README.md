# Flask SQLAlchemy Workout Application Backend

This is backend API for a workout tracking application used by personal trainers built with Flask, SQLAlchemy, and Marshmallow. It allows personal trainers to create exercises, build workouts, and link exercises to a workout with specific reps, sets, and duration.

# Features

* Create, view, and delete workouts via REST API.
* Create, view, and delete exercises via REST API.
* Link an existing exercise to an existing workout, recording reps, sets, and duration for that pairing.
* View a single workout together with its associated exercises, or a single exercise together with the workouts it's used in.
* Validation enforced at three layers: database table constraints, model-level validation, and API schema validation.

# Project Structure

```
PYTHON-Mod5-Summative-Lab-2-Flask-SQLAlchemy-Workout-Application-Backend/
├── server/
│   ├── app.py           # Has the Flask REST API routes
│   ├── models.py        # Defines the database SQLAlchemy models, relationships, constraints and validations
│   ├── schemas.py        # Defines the Marshmallow schemas used to convert database data to JSON for serialization and validation
│   └── seed.py           # Has sample data for the database 
├── migrations/            # Flask-Migrate/Alembic migration scripts
├── Pipfile
├── Pipfile.lock
└── README.md
```

## Data Model

* **Exercise** — id, name, category, equipment_needed
* **Workout** — id, date, duration_minutes, notes
* **WorkoutExercise** — join table linking a Workout and an Exercise, with reps, sets, and duration_seconds for that specific pairing
* A Workout and an Exercise have a many-to-many relationship through WorkoutExercise.
* Data is persisted in a SQLite database (`server/instance/app.db`), not held in memory thus it survives server restarts.

## Prerequisites

Before running the project, ensure you have the following installed:

* Python 3.x
* Pipenv

## Installation and Dependencies

Clone the repository and set up the environment:

```bash
git clone https://github.com/Eddie-Njeru1/PYTHON-Mod5-Summative-Lab-2-Flask-SQLAlchemy-Workout-Application-Backend.git
cd PYTHON-Mod5-Summative-Lab-2-Flask-SQLAlchemy-Workout-Application-Backend
pipenv install       # installs all project dependencies and creates the virtual environment
pipenv shell          # launches the virtual environment
```

The Pipfile defines the project's dependencies, while Pipfile.lock ensures consistent package versions across different development environments.

* **flask** — powers the REST API and routing.
* **flask-sqlalchemy** — ORM layer connecting Flask to the SQLite database.
* **flask-migrate** — manages database schema migrations.
* **marshmallow** — serializes model data to JSON and validates incoming request data.

Set up and seed the database:

```bash
cd server
flask db init        # first-time only
flask db migrate -m "initial migration"
flask db upgrade
python seed.py
```

## Running the Application

Start the Flask server from the `server/` directory:

```bash
python app.py
```

The API runs at `http://localhost:5555`.

* **View All Workouts**
   * `curl http://localhost:5555/workouts`
* **View a Single Workout** (includes its associated exercises)
   * `curl http://localhost:5555/workouts/1`
* **Create a Workout**
   * `curl -X POST http://localhost:5555/workouts -H "Content-Type: application/json" -d '{"date": "2026-03-01", "duration_minutes": 30, "notes": "Upper body"}'`
* **Delete a Workout**
   * `curl -X DELETE http://localhost:5555/workouts/1`
* **View All Exercises**
   * `curl http://localhost:5555/exercises`
* **View a Single Exercise** (includes the workouts it's used in)
   * `curl http://localhost:5555/exercises/1`
* **Create an Exercise**
   * `curl -X POST http://localhost:5555/exercises -H "Content-Type: application/json" -d '{"name": "Push-up", "category": "strength", "equipment_needed": false}'`
* **Delete an Exercise**
   * `curl -X DELETE http://localhost:5555/exercises/1`
* **Add an Exercise to a Workout**
   * `curl -X POST http://localhost:5555/workouts/1/exercises/1/workout_exercises -H "Content-Type: application/json" -d '{"reps": 10, "sets": 3}'`
      * Note: both the workout and exercise must already exist. If either id can't be found, the API returns an error response instead of crashing.

## Validations

* **Table constraints (database level):** `Workout.duration_minutes` and `WorkoutExercise.reps` must be greater than 0.
* **Model validations (Python level):** `Exercise.name` must be a non-empty string; `WorkoutExercise.sets` must be a positive integer.
* **Schema validations (API level):** `ExerciseSchema` rejects a blank/whitespace-only name; `WorkoutExerciseSchema` rejects a non-positive `sets` value.

## Current Limitations

The current version intentionally keeps the feature set to what's required.

* There are no update endpoints — a workout, exercise, or workout_exercise link can only be created or deleted, not edited in place.
* Deleting a workout or exercise does not cascade to remove its associated WorkoutExercise links.
* No automated test suite is included.