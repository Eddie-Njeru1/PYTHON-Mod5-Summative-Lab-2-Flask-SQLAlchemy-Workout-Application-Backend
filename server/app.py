# Entry point for configuring flask app and starting the server as well as defining API routes 

#Import dependencies 
from flask import Flask,request, make_response
from flask_migrate import Migrate
from models import *
from schemas import *

# Create the flask app
app = Flask(__name__) 
# Set up SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Connect the database and migration tool to the app
migrate = Migrate(app, db)
db.init_app(app)

@app.route ('/workouts', methods=['GET']) # Retrieve all workouts
def get_workouts():
    return workouts_schema.dump(Workout.query.all())

@app.route ('/workouts/<int:id>', methods=['GET']) #Get workout by id
def get_workout_by_id(id):
    workout = db.session.get(Workout, id)
    return workout_detail_schema.dump(workout)

@app.route ('/workouts', methods=['POST']) # Create a new workout
def create_workout():
    data = workout_schema.load(request.get_json())
    workout = Workout(**data)
    db.session.add(workout)
    db.session.commit()
    return workout_schema.dump(workout), 201

@app.route ('/workouts/<int:id>', methods=['DELETE']) # Delete a workout by id
def delete_workout(id):
    workout = db.session.get(Workout, id)
    db.session.delete(workout)
    db.session.commit()
    return {}, 204

@app.route ('/exercises', methods=['GET']) # Get all exercises
def get_exercises():
    return exercises_schema.dump(Exercise.query.all())

@app.route ('/exercises/<int:id>', methods=['GET']) # Get exercise by id
def get_exercise_by_id(id):
    exercise = db.session.get(exercise, id)
    return exercise_detail_schema.dump(exercise)

@app.route ('/exercises', methods=['POST']) #Create a new exercise 
def create_exercise():
    data = exercise_schema.load(request.get_json())
    exercise = Exercise(**data)
    db.session.add(exercise)
    db.session.commit()
    return exercise_schema.dump(exercise), 201

@app.route ('/exercises/<int:id>', methods=['DELETE']) # Delete exercise by id
def delete_exercise(id):
    exercise = db.session.get(Exercise, id)
    db.session.delete(exercise)
    db.session.commit()
    return {}, 204

# Add exercise to specific workout
@app.route ('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    data = request.get_json() or {}
    data['workout_id'] = workout_id
    data['exercise_id'] = exercise_id
    validated = workout_exercise_schema.load(data)
    workout_exercise = WorkoutExercise(**validated)
    db.session.add(workout_exercise)
    db.session.commit()
    return workout_exercise_schema.dump(workout_exercise), 201

# Start the Flask server 
if __name__ == '__main__':
    app.run(port=5555, debug=True) 

