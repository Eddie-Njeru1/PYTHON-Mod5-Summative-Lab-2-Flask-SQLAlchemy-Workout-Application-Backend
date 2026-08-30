# Defines the schemas used to convert database data to JSON

from marshmallow import Schema, fields

class ExerciseSchema(Schema): # Defines data used for an exercise
    id = fields.Int(dump_only=True) 
    name = fields.Str(required=True)
    category = fields.Str()
    equipment_needed = fields.Bool()

class WorkoutSchema(Schema):# Defines data used for a workout
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

class WorkoutExerciseSchema(Schema): # Defines data used for an exercise added to a workout
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int()
    sets = fields.Int(required=True)
    duration_seconds = fields.Int()
    exercise = fields.Nested(ExerciseSchema, dump_only=True) # Includes exercise details when returning workout data

# Schema objects to handle single records and lists 
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema


