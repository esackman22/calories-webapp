from flask.views import MethodView
from wtforms import From, StringField, SubmitField
from flask import Flask, render_template, request
from calculator import Calorie, Temperature


app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html', caloriesform=calories_form)


class CaloriesForm(Form):
    weight = StringField("Weight in lbs: ")
    height = StringField("Height in feet/inches: ")
    age = StringField("Age: ")

    city = StringField("City: ")
    country = StringField("Country: ")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories', view_func=CaloriesFormPage.as_view('calories_form_page'))