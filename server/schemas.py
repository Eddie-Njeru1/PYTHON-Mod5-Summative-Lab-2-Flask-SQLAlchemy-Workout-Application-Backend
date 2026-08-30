# Defines the schemas used to convert database data to JSON

from marshmallow import Schema, fields, validates, ValidationError

class ExerciseSchema(Schema): # Defines data used for an exercise
    id = fields.Int(dump_only=True) 
    name = fields.Str(required=True)
    category = fields.Str()
    equipment_needed = fields.Bool()

    @validates('name') # ensures exercise name isn't blank
    def validate_name(self, value):
        if not value.strip():
            raise ValidationError("Name must not be blank")

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
    workout = fields.Nested(WorkoutSchema, dump_only=True)

    @validates('sets') # ensure number of sets is more than zero
    def validate_sets(self, value):
        if value <= 0:
            raise ValidationError("Sets must be a positive integer.")

class WorkoutDetailSchema(WorkoutSchema):
    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True, dump_only=True, exclude=('workout',))

class ExerciseDetailSchema(ExerciseSchema):
    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True, dump_only=True, exclude=('exercise',))
    
# Schema objects to handle single records and lists 
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
exercise_detail_schema = ExerciseDetailSchema()

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
workout_detail_schema = WorkoutDetailSchema()
workout_exercise_schema = WorkoutExerciseSchema()


