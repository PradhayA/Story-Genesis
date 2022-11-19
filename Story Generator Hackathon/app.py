from flask import Flask, render_template, request

app = Flask(__name__)
import markovify
import sys
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function

@app.route('/')
def home():
    return render_template('index.html')


# retrievs the comment from web app and renders predicted value in web page
@app.route('/success', methods=['POST'])
def print_data():
    msg = request.form['message']
    text = msg
    # Train model
    text_model = markovify.Text(text)
    res = str("")
    # Generate sentences
    for i in range(20):
        lisadd = str((text_model.make_sentence()))
        res = res + lisadd
    res = res.replace("None", "")

    return render_template('result.html', prediction=res)


if __name__ == '__main__':
    app.run()