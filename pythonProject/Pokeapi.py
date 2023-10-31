# import requests
#
#
# def get_pokemon_info(pokemon_name):
#     url= f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         pokemon_data = response.json()
#
#     # Extract and print information
#         print("Name:", pokemon_data["name"])
#         print("ID:", pokemon_data["id"])
#         print("Height:", pokemon_data["height"])
#         print("Weight:", pokemon_data["weight"])
#         print("Abilities:")
#         for ability in pokemon_data["abilities"]:
#             print("- " + ability["ability"]["name"])
#     else:
#         print("Failed to retrieve Pokemon information. Status code:", response.status_code)
#
# if __name__ == "__main__":
#     pokemon_name = input("Enter a Pokémon name: ")
#     get_pokemon_info(pokemon_name)

#
import requests


def get_pokemon_info(pokemon_name):
    if not pokemon_name:
        print("Pokemon name cannot be empty.")
        return


    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        pokemon_data = response.json()
        # print(pokemon_data)
        print(f"Name: {pokemon_data['name']}")
        print(f"ID: {pokemon_data['id']}")
        print(f"Height: {pokemon_data['height']}")
        print(f"Weight: {pokemon_data['weight']}")
        abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
        print("Abilities:")
        for ability in abilities:
            print(f"- {ability}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve Pokemon information. {e}")

if __name__ == "__main__":
    get_pokemon_info("pikachu")
