from flask import Flask, render_template, request,flash
from form import StudentForm
import joblib
import pandas as pd

app = Flask(__name__)

# It's better practice to get secret keys from environment variables
app.config['SECRET_KEY'] = 'mysecretkey'


model = joblib.load('Student_exam_score_predictor.pkl')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = StudentForm()
    prediction = None
    input_data_readable = None  # for testing

    if form.validate_on_submit():

        input_df = pd.DataFrame({
            "gender": [form.gender.data],
            "course": [form.course.data],
            "study_hours": [form.study_hours.data],
            "class_attendance": [form.attendance.data],
            "internet_access": [form.internet_access.data],
            "sleep_hours": [form.sleep_hours.data],
            "sleep_quality": [form.sleep_quality.data],
            "study_method": [form.study_method.data],
            "facility_rating": [form.facility_rating.data],
            "exam_difficulty": [form.exam_difficulty.data]
        })

        try:
            prediction = round(model.predict(input_df)[0], 2)
            prediction = max(0, min(100, prediction))

        except Exception as e:
            prediction = f"Error: {e}"

        return render_template(
            "index.html",
            form=form,
            prediction=prediction
        )
    else:
        if request.method == "POST":

            study = form.study_hours.data
            sleep = form.sleep_hours.data
            attendance = form.attendance.data

            # 1️⃣ Empty check
            if not study or not sleep or not attendance:
                flash("All fields are required.", "danger")
                return render_template("index.html", form=form)

            # 2️⃣ Float check
            try:
                study = float(study)
                sleep = float(sleep)
                attendance = float(attendance)
            except:
                flash("Please enter valid numeric values.", "danger")
                return render_template("index.html", form=form)

            # 3️⃣ Range check
            if not (0.1 <= study <= 7.5):
                flash("Study Hours must be between 0.1 and 7.5.", "danger")
                return render_template("index.html", form=form)

            if not (4.5 <= sleep <= 9.5):
                flash("Sleep Hours must be between 4.5 and 9.5.", "danger")
                return render_template("index.html", form=form)

            if not (40 <= attendance <= 99):
                flash("Attendance % must be between 40 and 99.", "danger")
                return render_template("index.html", form=form)

    # Render initial form or if validation fails
    return render_template('index.html', form=form, prediction=prediction)


# Optional: Add the standard way to run the app if this is the main file
if __name__ == '__main__':
    app.run()
