from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def hello():
    return render_template('i.html')

# prediction function


@app.route('/', methods=['POST'])
def predict():
    if request.method == "POST":
        bloodPressure = int(request.form.get("HighChol2"))
        Cholesterol = int(request.form.get("HighChol"))
        BMI = int(request.form.get("bmi"))
        Smoke = int(request.form.get("smoke"))
        Stroke = int(request.form.get("stroke"))
        PhyActivity = int(request.form.get("phyact"))
        Alcho = int(request.form.get("Alcohol"))
        DiffWalking = int(request.form.get("DiffWalk"))
        Age = int(request.form.get("age"))
        Genhealth = int(request.form.get("Genhlt"))
        phyHealth = int(request.form.get("phyhlt"))
        menhealth = int(request.form.get("menhlt"))
        HeartProb = int(request.form.get("HeartAttack"))
        Education = int(request.form.get("education"))
        Income = int(request.form.get("income"))

        if (Age <= 24):
            Age = 1
        elif (Age >= 25 and Age <= 29):
            Age = 2
        elif (Age >= 30 and Age <= 34):
            Age = 3
        elif (Age >= 35 and Age <= 39):
            Age = 4
        elif (Age >= 40 and Age <= 44):
            Age = 5
        elif (Age >= 45 and Age <= 49):
            Age = 6
        elif (Age >= 50 and Age <= 54):
            Age = 7
        elif (Age >= 55 and Age <= 59):
            Age = 8
        elif (Age >= 60 and Age <= 64):
            Age = 9
        elif (Age >= 65 and Age <= 69):
            Age = 10
        elif (Age >= 70 and Age <= 74):
            Age = 11
        elif (Age >= 75 and Age <= 79):
            Age = 12
        else:
            Age = 13

        arr = np.array(
            [
                bloodPressure,
                Cholesterol,
                BMI,
                Smoke,
                Stroke,
                HeartProb,
                PhyActivity,
                Alcho,
                Genhealth,
                menhealth,
                phyHealth,
                DiffWalking,
                Age,
                Education,
                Income,

            ]
        ).reshape(1, -1)
        print(arr)

        result = model.predict(arr)
        if result[0] == 1:
            prediction = "Person is likely to have diabetes!"
        else:
            prediction = "Person is likely to NOT have diabetes!"
        print(prediction)
        model_probability = model.predict_proba(arr)
        predicp = "Probability of  this user having Diabetes is %0.4f" % model_probability[
            0][1]
        print(model_probability)
        return render_template('i.html', result=prediction, message=predicp)


if __name__ == "__main__":
    app.run(debug=True)
