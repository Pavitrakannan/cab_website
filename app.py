from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
app.secret_key = 'premium_cabs_secret'

# --- DATABASE OF VEHICLES (FIXED IMAGES) ---
cars = [
    {
        'id': 1,
        'name': 'Hatchback',
        'model': 'Maruti Swift / Celerio',
        # Using reliable Wikimedia/Public placeholder images
        'image': 'https://imgd.aeplcdn.com/600x337/n/cw/ec/102663/baleno-exterior-right-front-three-quarter-69.png?isig=0&q=80',
	'rate': '₹10',
        'capacity': '4 Seater',
        'features': ['AC', 'Compact', 'Budget Friendly']
    },
    {
        'id': 2,
        'name': 'Sedan Premium',
        'model': 'Swift Dzire / Etios',
        'image': 'https://www.timesbull.com/wp-content/uploads/2024/10/Exploring-the-Best-Sedan-Cars-in-India-Comfort-Performance-and-Affordability-jpg.webp',
        'rate': '₹12',
        'capacity': '4 Seater',
        'features': ['AC', 'Music System', 'Ample Boot Space']
    },
    {
        'id': 3,
        'name': 'SUV Comfort',
        'model': 'Maruti Ertiga / Kia Carens',
        'image': 'https://images.drivespark.com/webp/fit-in/510x383/car-image/car/1040807-hyundai_creta.jpg',
        'rate': '₹15',
        'capacity': '6 Seater',
        'features': ['AC', 'Reclining Seats', 'Extra Legroom']
    },
    {
        'id': 4,
        'name': 'SUV Luxury',
        'model': 'Toyota Innova Crysta',
        'image': 'https://imgd.aeplcdn.com/642x336/n/cw/ec/115025/innova-hycross-exterior-right-front-three-quarter-74.png?isig=0&q=80',
        'rate': '₹18',
        'capacity': '7 Seater',
        'features': ['Dual AC', 'Leather Seats', 'Premium Audio']
    }
]

# Helper function to save data to CSV
def save_to_csv(data):
    file_exists = os.path.isfile('bookings.csv')
    with open('bookings.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Updated Headers
            writer.writerow(['Trip Type', 'Name', 'Phone', 'Pickup State', 'Pickup Address', 'Drop State', 'Drop Address'])
        writer.writerow(data)

@app.route('/')
def home():
    return render_template('index.html', cars=cars)

@app.route('/book', methods=['POST'])
def book_cab():
    # Capture all new fields
    trip_type = request.form.get('trip_type')
    name = request.form.get('name')
    phone = request.form.get('phone')
    pickup_state = request.form.get('pickup_state')
    pickup_address = request.form.get('pickup_address')
    drop_state = request.form.get('drop_state')
    drop_address = request.form.get('drop_address')
    
    # Save to CSV
    save_to_csv([trip_type, name, phone, pickup_state, pickup_address, drop_state, drop_address])
    
    print(f"--- NEW BOOKING: {name} ({phone}) ---")
    
    flash('Booking request saved! Our agent will call you shortly.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
