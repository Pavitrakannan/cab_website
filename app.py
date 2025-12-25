from flask import Flask, render_template, request

app = Flask(__name__)

# 1. Route for the Home Page
@app.route('/')
def home():
    return render_template('index.html')

# 2. Route to handle the "Search" button
@app.route('/search', methods=['POST'])
def search_cabs():
    # Get data from the form
    pickup = request.form.get('pickup')
    drop = request.form.get('drop')
    date = request.form.get('date')
    
    # In a real app, you would query a database here.
    # For now, we print to the console and return a success message.
    print(f"New Search Request: From {pickup} to {drop} on {date}")
    
    # You could render a 'results.html' here, but we will just reload home for now
    return render_template('index.html', message=f"Searching cabs for {pickup} to {drop}...")

if __name__ == '__main__':
    # Debug mode allows the server to auto-reload when you change code
    app.run(debug=True)