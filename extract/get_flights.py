# To run this script, you should run the python file from the root by doing:
#   python3 -m flights.get_flights
# If you run it directly, the imports will not work.

from api.apiclient import ApiClient
import extract.constants as c

def get_flights():
    while True:
        # Set the url to the specified limit and offset
        extended_relative_url = f"{c.relative_url}?limit={c.limit}&offset={c.offset}"

        # Create the ApiClient instance
        api_request = ApiClient(c.base_url)

        # Make the GET-request, the class method already makes it a JSON string
        response = api_request.get(
            extended_relative_url,
            c.headers
            )

        # Extract the flights data by navigating through the JSON string
        flights_data = response["flights"].get("id", [])
        
        # Append flights list to result
        c.result.extend(flights_data)

        # Stop if there are no more flights
        if not flights_data:
            break

        # Get total available records
        total_records = int(response["flights"].get("total", "0"))

        # Stop if we have retrieved all records
        if c.offset + c.limit >= total_records:
            break

        # Move to the next page
        c.offset += c.limit

    print(c.result, f"\nThe result yields {total_records} total records.")