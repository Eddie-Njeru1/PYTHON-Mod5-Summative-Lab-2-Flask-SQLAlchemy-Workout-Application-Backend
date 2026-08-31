# Sample data for the database 

from datetime import date 
from app import app
from models import db, Exercise, Workout, WorkoutExercise

with app.app_context(): # Opens app database
    WorkoutExercise.query.delete() # Removes existing records before adding sample data
    Workout.query.delete()
    Exercise.query.delete()

    # Sample exercises
    pushup = Exercise(name="Push-up", category="strength", equipment_needed=False)
    squat = Exercise(name="Squat", category="strength", equipment_needed=False)
    plank = Exercise(name="Plank", category="core", equipment_needed=False)
    db.session.add_all([pushup, squat, plank]) #Adds exercises to the database

     # Sample worouts
    workout1 = Workout(date=date(2026, 1, 1), duration_minutes=30, notes="Upper body")
    workout2 = Workout(date=date(2026, 1, 1), duration_minutes=45, notes="Full body")
    db.session.add_all([workout1, workout2]) # Add workouts to database

    db.session.commit() #Save exercises and workouts 

   # Link exercises to workouts
    we1 = WorkoutExercise(workout=workout1, exercise=pushup, reps=10, sets=3, duration_seconds=None)
    we2 = WorkoutExercise(workout=workout1, exercise=plank, reps=1, sets=3, duration_seconds=60)
    we3 = WorkoutExercise(workout=workout2, exercise=squat, reps=10, sets=4, duration_seconds=None)
    db.session.add_all([we1, we2, we3]) # Add workout exercises to databases 

    db.session.commit() # Save workout exercise relationships
    print("Seeded 3 exercises, 2 workouts, 3 workout_exercise links.")
