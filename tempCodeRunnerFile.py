from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb+srv://obisikemercy09:LlP0UUqCyZWcFFuo@cluster0.qpt7u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        income = request.form.get("income")
        
        expenses = {
            "utilities": request.form.get("utilities", "0"),
            "entertainment": request.form.get("entertainment", "0"),
            "school_fees": request.form.get("school_fees", "0"),
            "shopping": request.form.get("shopping", "0"),
            "healthcare": request.form.get("healthcare", "0")
        }

        user_data = {
            "name": name,
            "age": age,
            "gender": gender,
            "income": income,
            "expenses": expenses
        }

        # Insert data into MongoDB
        mongo.db.users.insert_one(user_data)
        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
     app.run(debug=True)
