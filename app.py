from flask import Flask, request, render_template
from main import generate_recipe

app = Flask(__name__, template_folder='.')

@app.route('/')
@app.route('/index.html')
def show_index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    form_data = request.form
    recipe = generate_recipe(form_data)
    return render_template('recipePage.html', Recipe=recipe, Food=form_data["Food"].lower(), Calories=form_data["Calories"].lower(), Culture=form_data["Culture"].lower(), Meal = form_data["SelectedMeal"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
