from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Create an uploads folder to store images temporarily
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Render the form page (you can serve the HTML directly or integrate it here)
    return "Loan Application Form"

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        customer_name = request.form['name']
        mobile = request.form['mobile']
        address = request.form['address']
        village_town = request.form['village_town']
        residence_type = request.form['residence_type']
        income = request.form['income']
        vehicle_model = request.form['vehicle_model']
        finance_amount = request.form['finance_amount']
        emi = request.form['emi']
        tenure = request.form['tenure']
        agent = request.form['agent']

        # Process customer photo
        customer_photo = request.files['customer_photo']
        customer_photo_path = os.path.join(app.config['UPLOAD_FOLDER'], customer_photo.filename)
        customer_photo.save(customer_photo_path)

        # Process KYC document
        kyc = request.files['kyc']
        kyc_path = os.path.join(app.config['UPLOAD_FOLDER'], kyc.filename)
        kyc.save(kyc_path)

        # Optional: Process any other document
        other_document = request.files.get('other_document')
        if other_document:
            other_document_path = os.path.join(app.config['UPLOAD_FOLDER'], other_document.filename)
            other_document.save(other_document_path)
        else:
            other_document_path = None

        # Print collected data (later, this can be stored in a database)
        print(f"Customer Name: {customer_name}")
        print(f"Mobile: {mobile}")
        print(f"Address: {address}")
        print(f"Village/Town: {village_town}")
        print(f"Residence Type: {residence_type}")
        print(f"Monthly Income: {income}")
        print(f"Vehicle Model: {vehicle_model}")
        print(f"Finance Amount: {finance_amount}")
        print(f"EMI: {emi}")
        print(f"Tenure: {tenure} months")
        print(f"Agent: {agent}")
        print(f"Customer Photo saved at: {customer_photo_path}")
        print(f"KYC Document saved at: {kyc_path}")
        if other_document_path:
            print(f"Other Document saved at: {other_document_path}")

        return 'Loan Application Submitted Successfully!'
    return 'Invalid request', 400

if __name__ == '__main__':
    app.run(debug=True)

