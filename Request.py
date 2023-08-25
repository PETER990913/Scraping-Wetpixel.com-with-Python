import requests
login_data = {
    'username': 'your_username',
    'password': 'your_password'
}
login_url = 'https://welcome.onelog.ch/'
response = requests.post(login_url, data=login_data)
if response.status_code == 200:
    # Login successful, handle the response data
    print("Login successful")
    print("Response content:", response.text)
else:
    # Login failed, handle the error
    print("Login failed")
    print("Error message:", response.text)