# Excel-Payroll-filter
a simple filter of excel files 
# Payroll filter

Excel Filter for Lelchego Company Ltd

## Description

This project is a Flask-based web application that allows users to upload two Excel files, filter data based on a common column ("Sno"), and download the filtered data in a ZIP archive. The project is designed for Lelchego Company Ltd to manage payroll data, differentiating between payments made through Mpesa and cash.

## How to Use

1. Clone the repository:

  ```bash
   git clone https://github.com/kevinkip08/Excel-Payroll-filter
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

   Visit `http://localhost:5000` in your web browser.

4. Follow the instructions on the web page to upload Mpesa payment and payroll Excel files.

5. Click on the "Download Filtered Data" link to download the filtered data in a ZIP archive.

## Files and Structure

- **app.py**: Contains the Flask application code with routes for uploading files and downloading filtered data. The application uses the `pandas` library to process Excel files.

- **index.html**: HTML template for the web interface. Provides a form for file uploads and a link to download filtered data.

## Project Structure

- **uploads**: Folder where uploaded files are stored temporarily.

- **filtered_data.zip**: ZIP archive containing the filtered data in separate Excel files.

## Styling

The styling of the web interface is defined in the `style` section of the HTML file. The page includes a header, form for file uploads, and a link to download filtered data.

## Notes

- The project generates a random secret key for Flask sessions to enhance security.

- Ensure that you have the necessary dependencies installed before running the application.

Feel free to customize and adapt this project according to your needs. Happy coding!
