base_url = "https://api.schiphol.nl"
relative_url = "/public-flights/flights"
limit = 20
offset = 0
spl_app_id = dbutils.secrets.get(scope="scope-ennatuurlijk",key="schiphol-app-id")
spl_app_key = dbutils.secrets.get(scope="scope-ennatuurlijk",key="schiphol-app-key")
headers = {
  'Accept': 'application/json',
  'app_id': spl_app_id,
  'app_key': spl_app_key,
  'ResourceVersion': 'v4'
}
result = []