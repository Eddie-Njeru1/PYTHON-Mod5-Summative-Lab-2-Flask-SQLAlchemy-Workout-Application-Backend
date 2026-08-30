# Entry point for confiuring flask app and starting the server as well as defining API routes 

#Import dependencies 
from flask import Flask, make_response
from flask_migrate import Migrate
from models import *

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
    pass

@app.route ('/workouts/<int:id>', methods=['GET']) #Get workout by id
def get_workout_by_id(id):
    pass

@app.route ('/workouts', methods=['POST']) # Create a new workout
def create_workout():
    pass

@app.route ('/workouts/<int:id>', methods=['DELETE']) # Delete a workout by id
def delete_workout(id):
    pass

@app.route ('/exercises', methods=['GET']) # Get all exercises
def get_exercises():
    pass

@app.route ('/exercises/<int:id>', methods=['GET']) # Get exercise by id
def get_exercise_by_id(id):
    pass

@app.route ('/exercises', methods=['POST']) #Create a new exercise 
def create_exercise():
    pass

@app.route ('/exercises/<int:id>', methods=['DELETE']) # Delete exercise by id
def delete_exercise(id):
    pass

# Add exercise to specific workout
@app.route ('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    pass
# Start the Flask server 
if __name__ == '__main__':
    app.run(port=5555, debug=True) 

