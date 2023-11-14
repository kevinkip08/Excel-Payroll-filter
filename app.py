from flask import Flask, request, render_template, send_file, flash
import pandas as pd
import os
import zipfile
import secrets

app = Flask(__name__)

def generate_secret_key():
    return secrets.token_hex(16)

SECRET_KEY = generate_secret_key()
print(SECRET_KEY)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if the post request has the file part
    if 'file1' not in request.files or 'file2' not in request.files:
        return "No file part"

    file1 = request.files['file1']
    file2 = request.files['file2']

    # If user does not select file, browser also submits an empty part without filename
    if file1.filename == '' or file2.filename == '':
        return "No selected file"

    # Save the uploaded files to the 'uploads' folder
    file1_path = os.path.join(app.config['UPLOAD_FOLDER'], 'mpesa_payment.xlsx')
    file2_path = os.path.join(app.config['UPLOAD_FOLDER'], 'cash_payment.xlsx')
    file1.save(file1_path)
    file2.save(file2_path)

    #return render_template('succes.html')
    
    return "Files uploaded successfully!"

@app.route('/download_filtered_data', methods=['GET'])
def download_filtered_data():
    # Process the data and create two separate Excel files

    # Read the uploaded data from the 'uploads' folder
    file1_path = os.path.join(app.config['UPLOAD_FOLDER'], 'mpesa_payment.xlsx')
    file2_path = os.path.join(app.config['UPLOAD_FOLDER'], 'cash_payment.xlsx')

    mpesa_payment_requests = pd.read_excel(file1_path, engine='openpyxl')
    payroll_data = pd.read_excel(file2_path, engine='openpyxl')

    mpesaPayment = payroll_data[~payroll_data['Sno'].isin(mpesa_payment_requests['Sno'])]
    cash_payment_data = payroll_data[payroll_data['Sno'].isin(mpesa_payment_requests['Sno'])]

    # Save the filtered data back to new Excel files
    cash_payment_data.to_excel('mpesa_payment_data.xlsx', index=False)
    mpesaPayment.to_excel('cash_payment_data.xlsx', index=False)

    # Create a ZIP archive and add the Excel files to it
    with zipfile.ZipFile('filtered_data.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.write('mpesa_payment_data.xlsx', 'mpesa_payment_data.xlsx')
        archive.write('cash_payment_data.xlsx', 'cash_payment_data.xlsx')

    # Define the path to the ZIP archive+p0[]
    filtered_data_zip = 'filtered_data.zip'

    return send_file(filtered_data_zip, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
