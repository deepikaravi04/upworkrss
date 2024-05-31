from flask import Flask
import threading
import time


app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the application instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)



# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    


def background_task():
    while True:
        print("Background task is running...")
        time.sleep(10)

@app.route('/')
def index():
    users = User.query.all()
    return f"Users: {users}"


with app.app_context():
    db.create_all()

    
if __name__ == '__main__':
    # Start the background thread
    
    # thread = threading.Thread(target=background_task)
    # thread.daemon = True
    # thread.start()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
