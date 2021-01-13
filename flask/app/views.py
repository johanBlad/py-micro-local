from app import app

@app.route('/')
@app.route('/fl/')
def index():
    return 'Hello from containered flask\n'