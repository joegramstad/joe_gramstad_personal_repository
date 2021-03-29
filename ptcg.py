import requests
import json

def main():
    response = requests.get("https://api.pokemontcg.io/v2/cards?q=supertype:pokemon set.id:sm1").text
    response_info = json.loads(response)
    if 
    print(response_info)

main()    