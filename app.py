from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def bmi():
    # get query args
    h = request.args['height']
    w = request.args['weight']

    # format string to int
    h = int(h)
    w = int(w)

    # rumus bmi
    bmi = round(float(w / (h/100)**2),2)

    # result logic label
    if bmi > 25.0:
        label = "overweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        label = "normal"
    else:
        label = "underweight"

    # data as dict
    data = {
        "bmi": bmi,
        "label": label
    }
    
    # return data
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0')
