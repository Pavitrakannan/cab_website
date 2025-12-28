from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
app.secret_key = 'premium_cabs_secret'

# --- DATABASE OF VEHICLES (DYNAMIC DATA) ---
cars = [
    {
        'id': 1,
        'name': 'Sedan Premium',
        'model': 'Swift Dzire / Etios',
        'image': 'https://imgd.aeplcdn.com/370x208/n/cw/ec/45691/swift-exterior-right-front-three-quarter-118.jpeg',
        'rate': '₹12',
        'capacity': '4 Seater',
        'features': ['AC', 'Music System', 'Ample Boot Space']
    },
    {
        'id': 2,
        'name': 'SUV Comfort',
        'model': 'Maruti Ertiga / Kia Carens',
        'image': 'https://imgd.aeplcdn.com/370x208/n/cw/ec/115457/ertiga-facelift-exterior-right-front-three-quarter.jpeg',
        'rate': '₹15',
        'capacity': '6 Seater',
        'features': ['AC', 'Reclining Seats', 'Extra Legroom']
    },
    {
        'id': 3,
        'name': 'SUV Luxury',
        'model': 'Toyota Innova Crysta',
        'image': 'https://imgd.aeplcdn.com/370x208/n/cw/ec/136217/innova-crysta-exterior-right-front-three-quarter-3.jpeg',
        'rate': '₹18',
        'capacity': '7 Seater',
        'features': ['Dual AC', 'Leather Seats', 'Premium Audio']
    },
    {
        'id': 4,
        'name': 'Tempo Traveller',
        'model': 'Force Traveller',
        'image': 'https://5.imimg.com/data5/SELLER/Default/2023/1/YI/IO/MI/23366886/17-seater-tempo-traveller-rental-service-500x500.png',
        'rate': '₹24',
        'capacity': '17 Seater',
        'features': ['Pushback Seats', 'Individual AC', 'Group Travel']
    }
]

# Helper function to save data to CSV
def save_to_csv(data):
    file_exists = os.path.isfile('bookings.csv')
    with open('bookings.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Add header if the file is being created for the first time
        if not file_exists:
            writer.writerow(['Phone', 'Pickup', 'Drop'])
        writer.writerow(data)

@app.route('/')
def home():
    return render_template('index.html', cars=cars)

@app.route('/book', methods=['POST'])
def book_cab():
    # 1. Capture data from the form
    phone = request.form.get('phone')
    pickup = request.form.get('pickup')
    drop = request.form.get('drop')
    
    # 2. Save data permanently to the CSV file
    save_to_csv([phone, pickup, drop])
    
    # 3. Print to console for immediate visibility
    print(f"--- NEW BOOKING SAVED ---")
    print(f"Phone: {phone} | Route: {pickup} to {drop}")
    
    # 4. Show success message
    flash('Booking request saved! Our agent will call you shortly.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
