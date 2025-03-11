from auth import authenticate
from read_cells import *
import random
from write_cells import *
from flask import Flask, render_template, request
from validate import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import smtplib
app = Flask(__name__)

@app.route("/")
def main():
    SAMPLE_SPREADSHEET_ID = "1V9mLaKA9WhsyA_qcEf0Uy6KB2fGLkKI8IzhtiVTVm8Y"
    SAMPLE_RANGE_NAME = "Sheet1!A2:A100"
    TARGET_CELL = "Sheet1!E2"
    
    # Authenticate once and pass the credentials to the functions
    creds = authenticate()
    
    # Read data from the sheet
    values = read_sheet(creds, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME)
    if values:
        flattened_values = [item for sublist in values for item in sublist]
        random_value = random.choice(flattened_values)
    else:
        return "No data found.", 404
    
    update_sheet(creds, SAMPLE_SPREADSHEET_ID, TARGET_CELL, [[random_value]])
    #return f"Updated cell {TARGET_CELL} with value: {random_value}", 200
    #return f"Your place to have dinner in Lisbon today: {random_value}", 200
    suggestion = request.args.get("suggestion")
    try:
        if suggestion is not None:
            result = validate(suggestion)
            print(result)
            
            subject = "User's suggestion"
            body = f"User's suggestion: {suggestion}"
            recipient = os.getenv('recipient')
            send_email(subject, body, recipient)
            return render_template('index.html', restaurant = random_value, result = result)
    except:
        pass
        
    return render_template('index.html', restaurant = random_value, result = "")

def send_email(subject, body, to_email):
    from_email = os.getenv('email')
    password = os.getenv('email_pass')
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to Gmail's SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
       
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())   

@app.route("/feedback", methods=["GET", "POST"])
def contact():
    confirmation = None
    if request.method == "POST":
        # Collect data from the form
        name = request.form["name"]
        email = request.form["email"]
        feedback = request.form["feedback"]
        
        # Format the email body
        subject = "Contact Form Submission"
        body = f"Name: {name}\nEmail: {email}\nMessage: {feedback}"
        recipient = os.getenv('recipient')
        # Send email 
        send_email(subject, body, recipient)
        
        # Return a confirmation message
        confirmation="Thank you for your message! We will get back to you soon."

    # For GET request, just render the contact form
    return render_template("feedback.html", confirmation = confirmation)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
