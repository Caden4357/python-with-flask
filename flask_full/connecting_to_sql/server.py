from flask_app import app
from flask_app.controllers import owners, animals, doctors

if __name__ == "__main__":
    app.run(debug=True)