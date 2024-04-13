import requests

# Define the API endpoint URL
url = "https://so-epic-right-now.kintone.com/k/v1/record.json?app=3&id=2"

# Set the API token in the headers
headers = {
    "X-Cybozu-API-Token": "Dzg8sZPBnT5qaEYvb2rWxciDkazzm08vOL39qVW8"
}

# Send HTTP GET request to the API endpoint
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the values for 'coolname' and 'soawesome' from the 'record' dictionary
    coolname_value = data['record']['username']['value']
    soawesome_value = data['record']['password']['value']

    # Print the extracted values
    print("Username:", coolname_value)
    print("Password:", soawesome_value)

    with open('name.txt', 'w') as file:
        file.write(coolname_value, soawesome_value)

else:
    # Print error message if the request was not successful
    print("Error:", response.text)


# curl -X POST 'https://so-epic-right-now.kintone.com/k/v1/record.json' \
#   -H 'X-Cybozu-API-Token: Dzg8sZPBnT5qaEYvb2rWxciDkazzm08vOL39qVW8' \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "app": 3,
#     "record": {
#       "coolname": {
#         "value": "Donna"
#       },
#       "soawesome": {
#         "value": "420"
#       }
#     }
#   }'
