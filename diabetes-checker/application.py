# import dependencies
import urllib.request
import json

try: 
    from flask import Flask, render_template, request
except ImportError: 
	print("Error importing dependencies")

# create an instance of the Flask class
app = Flask(__name__)

# '/process' triggers this function
@app.route('/process', methods=['POST'])
def process():
    # recieve input from browser
    # store each input in respective variable
    PatientID = request.form['PatientID']
    Pregnancies = request.form['Pregnancies']
    PlasmaGlucose = request.form['PlasmaGlucose']
    DiastolicBloodPressure = request.form['DiastolicBloodPressure']
    TricepsThickness = request.form['TricepsThickness']
    SerumInsulin = request.form['SerumInsulin']
    BMI = request.form['BMI']
    DiabetesPedigree = request.form['DiabetesPedigree']
    Age = request.form['Age']

    # start request-response code
    data = {
        "Inputs": {
                "input1":
                [
                    {
                        'PatientID': PatientID,   
                        'Pregnancies': Pregnancies,   
                        'PlasmaGlucose': PlasmaGlucose,   
                        'DiastolicBloodPressure': DiastolicBloodPressure,   
                        'TricepsThickness': TricepsThickness,   
                        'SerumInsulin': SerumInsulin,   
                        'BMI': BMI,   
                        'DiabetesPedigree': DiabetesPedigree,   
                        'Age': Age,   
                    }
                ],
        },
        "GlobalParameters":  {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://europewest.services.azureml.net/subscriptions/ad700fbcaa0d4ac9ae3054a95ad1eb0f/services/e37b7f3ccad245f9bf217119bc44294a/execute?api-version=2.0&format=swagger'
    api_key = 'ZLZVVqXvXWUOW5x0Axf5vf9G/wp19RZT6xAbHTOcwrxEJZhlGzkhB/58PcsvhruP/7jKSS2M7rY1oJ2WaotY/Q=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
    # end request-response code

    # return result --> convert result from bytes to string 
    return render_template("index.html", result=result.decode())

# '/' triggers this function
@app.route("/")
def output():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

