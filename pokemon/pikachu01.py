#!/usr/bin/env python3

import requests

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main()

    # make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL wiht a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json

    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        # print(poke["name"])
        print(poke.get("name"))

    print(f"total number of Pokemon returned: {len(pokemon['results'])}")
if __name__ == "__main__":
    main()
