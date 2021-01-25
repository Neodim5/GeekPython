import requests


respons = requests.get("https://google.com", {"q": "neodim5"})
# https://google.com?q=neodim5
print(respons.status_code)
print(respons.content)

print(respons.text)

