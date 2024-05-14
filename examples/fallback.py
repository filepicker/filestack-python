from filestack import Client, Security

# create security object
json_policy = {"call":["pick","read","stat","write","writeUrl","store","convert"],"expiry":1717099200}
security = Security(json_policy, '<YOUR_APP_SECRET>')
APIKEY = '<YOUR_API_KEY>'

client = Client(apikey=APIKEY, security=security)
transform = client.transform_external('/')
transform.fallback(file='HANDLER', cache=12)
print(transform.url)
