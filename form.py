from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired,NumberRange

class StudentForm(FlaskForm):

    # Numeric inputs
    name = StringField("Name", validators=[DataRequired()])
    study_hours = FloatField("Study Hours", validators=[ NumberRange(min=0, max=7.5)])
    sleep_hours = FloatField("Sleep Hours", validators=[DataRequired(), NumberRange(min=4, max=9.5)])
    attendance = FloatField("Attendance %", validators=[DataRequired(), NumberRange(min=40, max=99)])
    internet_access = SelectField(
        "Internet Access",
    )


    # Categorical inputs (order & names match training)
    gender = SelectField(
        "Gender",
        choices=[
            ("female", "Female"),    # note: order same as model_columns
            ("male", "Male"),
            ("other", "Other")
        ]
    )

    course = SelectField(
        "Course",
        choices=[
            ("b.com", "B.Com"),
            ("b.sc", "B.Sc"),
            ("b.tech", "B.Tech"),
            ("ba", "BA"),
            ("bba", "BBA"),
            ("bca", "BCA"),
            ("diploma", "Diploma")
        ]
    )

    internet_access = SelectField(
        "Internet Access",
        choices=[
            ("no", "No"),
            ("yes", "Yes")
        ]
    )

    sleep_quality = SelectField(
        "Sleep Quality",
        choices=[
            ("average", "Average"),
            ("good", "Good"),
            ("poor", "Poor")
        ]
    )

    study_method = SelectField(
        "Study Method",
        choices=[
            ("coaching", "Coaching"),
            ("group study", "Group Study"),
            ("mixed", "Mixed"),
            ("online videos", "Online Videos"),
            ("self-study", "Self Study")
        ]
    )

    facility_rating = SelectField(
        "Facility Rating",
        choices=[
            ("high", "High"),
            ("low", "Low"),
            ("medium", "Medium")
        ]
    )

    exam_difficulty = SelectField(
        "Exam Difficulty",
        choices=[
            ("easy", "Easy"),
            ("hard", "Hard"),
            ("moderate", "Moderate")
        ]
    )

    submit = SubmitField("Predict Marks")

