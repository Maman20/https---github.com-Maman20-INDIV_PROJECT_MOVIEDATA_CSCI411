from flask import Flask, render_template

app = Flask(__name__)
#hello world
@app.route('/')
def home():
    return render_template('gitassignment.html')  # Ensure your HTML file is named index.html or update this line accordingly.

if __name__ == '__main__':
    app.run(debug=True)
