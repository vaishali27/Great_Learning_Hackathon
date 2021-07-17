from flask_ngrok import run_with_ngrok
from flask import Flask
import requests
from flask import request,render_template

from utils.ml_utils import CreditScoreModel

import traceback

app = Flask(__name__, template_folder='templates')
run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def home():
    return """
 <html>
    <body>
    <h2>Predict Credit score</h2>
    <div>
  <form action="/predict" method="POST">
    <label for="input">Status of existing checking account</label>
    <input type="text" id="inputStatus" name="Status_of_existing_checking_account">
    <br>
    <label for="input">Duration in month</label>
    <input type="int" id="inputDur" name="Duration_in_month">
    <br>
    <label for="input">Credit history</label>
    <input type="text" id="inputHis" name="Credit_history">
    <br>
    <label for="input">Purpose</label>
    <input type="text" id="inputPurpose" name="Purpose">
    <br>
    <label for="input">Credit amount</label>
    <input type="text" id="inputAmt" name="Credit_amount">
    <br>
    <label for="input">Savings account/bonds</label>
    <input type="text" id="inputSavings" name="Savings_account_bonds">
    <br>
    <label for="input">Present employment since</label>
    <input type="text" id="inputEmp" name="Present_employment_since">
    <br>
    <label for="input">Installment rate in percentage of disposable income</label>
    <input type="text" id="inputInstallment" name="Installment_rate_in_percentage_of_disposable_income">
    <br>
    <label for="input">Personal status and sex</label>
    <input type="text" id="inputPersonalStatus" name="Personal_status_and_sex">
    <br>
    <label for="input">Other debtors / guarantors</label>
    <input type="text" id="inputGuarantors" name="Other_debtors_guarantors">
    <br>
    <label for="input">Present residence since</label>
    <input type="text" id="inputResidenceSince" name="Present_residence_since">
    <br>
    <label for="input">Property</label>
    <input type="text" id="inputProperty" name="Property">
    <br>
    <label for="input">Age in years</label>
    <input type="text" id="inputAge" name="Age_in_years">
    <br>
    <label for="input">Other installment plans</label>
    <input type="text" id="inputOtherInstallment" name="Other_installment_plans">
    <br>
    <label for="input">Housing</label>
    <input type="text" id="inputHousing" name="Housing">
    <br>
    <label for="input">Number of existing credits at this bank</label>
    <input type="text" id="inputExistingCredit" name="Number_of_existing_credits_at_this_bank">
    <br>
    <label for="input">Job</label>
    <input type="text" id="inputJob" name="Job">
    <br>
    <label for="input">Number of people being liable to provide maintenance for</label>
    <input type="text" id="inputPeopleLiable" name="Number_of_people_being_liable_to_provide_maintenance_for">
    <br>
    <label for="input">Telephone</label>
    <input type="text" id="inputTel" name="Telephone">
    <br>
    <label for="input">foreign worker</label>
    <input type="text" id="inputForeign" name="foreign_worker">
    <br>
    <div class="container">
    <form method="post">
        <input type="submit" value="Predict" >
    </form>
</div>
</div>
</body>
</html>"""

@app.route('/predict/', methods=["POST"])
def predictApi():
    result = None
    errors = []
    if request.method == "POST":
        # get url that the user has entered
        try:
            model = CreditScoreModel()
            data = request.form.to_dict()
            print(data)
            result = {"credit_risk": model.predict(data)}
        except Exception as error:
            errors.append(traceback.format_exc())
            errors.append(str(error))
            errors.append(
                "Unable to get the prediction. Please make sure to enter the data and try again."
            )

    return {'result': result if result else errors}
app.run()