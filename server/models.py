# Defines the database SQLAlchemy models, relationships, constraints and validations

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy() # Creates the database for the app

class Exercise(db.Model): # Stores info about an exercise in the database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)
    workout_exercise = db.relationship('WorkoutExercise', back_populates='exercise') # Connects exercise to a worout
    @validates('name') # Ensures the exercise has a valid name 
    def validate_name(self, key, name):
        if not name or not isinstance(name, str):
            raise ValueError("Exercise name must be a non-empty string")
        return name 

class Workout(db.Model): # Stores info about a workout in the database
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)
    __table_args__ = ( # Sets the time duration of the workout 
        db.CheckConstraint('duration_Minutes > 0', name='check_duration_positive'),
    )
    workout_exercise = db.relationship('WorkoutExercise', back_populates='workout') # Connects workout to an exercise 
    

class WorkoutExercise(db.Model): # Stores info about exercises done during a workout
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id')) # Connects each exercise to a specific workout
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    __table_args__ = ( # Sets number of reps 
            db.CheckConstraint('reps > 0', name='check_reps_positive'),
        )
    workout = db.relationship('Workout', back_populates='workout_exercises') # Link table to the workout and exercise tables
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

    @validates('sets') # Allocate number of sets 
    def validate_sets(self, key, sets):
        if sets is None or sets <= 0:
            raise ValueError("Sets must have a positive integer")
        return sets 
    

                    