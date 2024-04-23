import requests

# URL of your Flask server
url = "http://127.0.0.1:5000/predict"

# Example data in the user-friendly format (this is the raw data before one-hot encoding)
test_data = {
    "school": "GP",
    "sex": "F",
    "age": 17,
    "address": "U",
    "famsize": "LE3",
    "Pstatus": "T",
    "Medu": 4,
    "Fedu": 3,
    "Mjob": "health",
    "Fjob": "services",
    "reason": "course",
    "guardian": "mother",
    "traveltime": 1,
    "studytime": 2,
    "failures": 0,
    "schoolsup": "no",
    "famsup": "yes",
    "paid": "no",
    "activities": "yes",
    "nursery": "yes",
    "higher": "yes",
    "internet": "yes",
    "romantic": "no",
    "famrel": 4,
    "freetime": 3,
    "goout": 3,
    "Dalc": 1,
    "Walc": 2,
    "health": 5,
    "absences": 4,
    "G1": 14,
    "G2": 15
}

# Convert the data to JSON
json_data = test_data

# Send a POST request to the Flask server
response = requests.post(url, json=json_data)

# Print the response from the server
print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")
