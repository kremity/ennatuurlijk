import requests
import json

# Dit Script maakt een parent class met functies die hergebruikt kunnen worden voor een specifike API request.
# Het script geeft het resultaat terug in een pretty printed JSON format.

class ApiClient:
    
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, relative_url, headers=None):
        # Set full URL
        url = self.base_url + relative_url
        # Do a get request
        response = requests.request("GET", url, headers=headers)
        # Parse the response
        parsed_response = json.loads(response)
        # Return the result
        return json.dumps(parsed_response, indent=4)

    