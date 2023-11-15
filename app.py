from flask import Flask, request, render_template
import requests
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

# debug = DebugToolbarExtension(app)

base_url = "http://api.exchangerate.host"
# endpoint = "/live"
endpoint = "/convert"

@app.route("/")
def show_homepage():
    
    return render_template("home.html")


@app.route("/complete", methods= ["POST", "GET"])
def show_conversion():
    if request.method == "POST":
        base_currency = request.form.get("confrom")
        target_currency = request.form.get("conto")
        amount = request.form.get("amount")

        if not base_currency or not target_currency or not amount:
            error_message = "Please fill in all fields!"
            return render_template("error.html", error_message = error_message)
        
        if not amount:
            error_message = "Please enter a valid number for the amount."
            return render_template("error.html", error_message=error_message)
        
        try:
            amount = float(amount)
        except ValueError:
            error_message = "Please enter a valid number for the amount."
            return render_template("error.html", error_message=error_message)

        params = {
            "access_key": "db0ce6e0415d2bbd4b82b4e9d08b713e",
            "from": base_currency,
            "to": target_currency,
            "amount": amount,
            "format": "json",
        }
        
        response = requests.get(base_url + endpoint, params=params)
        
        if response.status_code == 200:
            data = response.json()

            if 'error' in data:
                error_message = data['error']['info']
                return render_template("error.html", error_message = error_message)

            res = data["result"]
            result = round(res, 2)
            return render_template("complete.html", result=result, base_currency=base_currency, target_currency=target_currency, amount=amount)
            
        else:
            return "API request failed with status code: " + str(response.status_code)

