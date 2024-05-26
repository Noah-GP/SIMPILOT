from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Addon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Addon {self.name}>"

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    kind = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Event {self.name}>"

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

@app.route('/schedule_event', methods=['GET', 'POST'])  
def schedule_event():
    if request.method == 'POST':
        # Handle event scheduling
        return redirect(url_for('events'))  
    return render_template('schedule_event.html')

@app.route('/browse_addons', methods=['GET', 'POST'])
def browse_addons():
    search_query = request.form.get('search_query', '')
    if search_query:
        addons = Addon.query.filter(
            or_(
                Addon.name.ilike(f'%{search_query}%'),
                Addon.category.ilike(f'%{search_query}%'),
                Addon.description.ilike(f'%{search_query}%')
            )
        ).all()
    else:
        addons = Addon.query.all()
    return render_template('browse_addons.html', addons=addons, search_query=search_query)

@app.route('/upload_addon', methods=['GET', 'POST'])
def upload_addon():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        link = request.form['link']
        new_addon = Addon(name=name, category=category, description=description, link=link)
        db.session.add(new_addon)
        db.session.commit()
        return redirect(url_for('browse_addons'))  # Redirect after uploading addon
    return render_template('upload_addon.html')

@app.route('/browse_events', methods=['GET', 'POST'])
def browse_events():
    search_query = request.form.get('search_query', '')
    if search_query:
        events = Event.query.filter(
            or_(
                Event.name.ilike(f'%{search_query}%'),
                Event.kind.ilike(f'%{search_query}%'),
                Event.description.ilike(f'%{search_query}%')
            )
        ).all()
    else:
        events = Event.query.all()
    return render_template('browse_events.html', events=events, search_query=search_query)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
