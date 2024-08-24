from auth import authenticate
from read_cells import *
import random
from write_cells import *
from flask import Flask, render_template, request
from validate import *
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
            return render_template('index.html', restaurant = random_value, result = result)
    except:
        pass
        
    return render_template('index.html', restaurant = random_value, result = "")
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
