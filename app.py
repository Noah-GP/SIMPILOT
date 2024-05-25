from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/checklist')
def checklist():
    return render_template('checklist.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/add_on')
def add_on():
    return render_template('add_on.html')

if __name__ == '__main__':
    app.run(debug=True)