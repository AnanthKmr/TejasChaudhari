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
# import requests
#
#
# def get_pokemon_info(pokemon_name):
#     if not pokemon_name:
#         print("Pokemon name cannot be empty.")
#         return
#
#
#     url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         pokemon_data = response.json()
#         # print(pokemon_data)
#         print(f"Name: {pokemon_data['name']}")
#         print(f"ID: {pokemon_data['id']}")
#         print(f"Height: {pokemon_data['height']}")
#         print(f"Weight: {pokemon_data['weight']}")
#         abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
#         print("Abilities:")
#         for ability in abilities:
#             print(f"- {ability}")
#     except requests.exceptions.RequestException as e:
#         print(f"Failed to retrieve Pokemon information. {e}")
#
# if __name__ == "__main__":
#     get_pokemon_info("pikachu")

# import requests
#
#
# class PokemonInfoRetriever:
#     API_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
#
#
#     def __init__(self):
#         self.pokemon_name = ""
#
#
#     def set_pokemon_name(self, name):
#         self.pokemon_name = name
#
#
#     def get_pokemon_info(self):
#         if not self.pokemon_name:
#             print("Pokemon name cannot be empty.")
#             return
#
#         try:
#             url = f"{self.API_BASE_URL}{self.pokemon_name}"
#             response = requests.get(url)
#             response.raise_for_status()
#             pokemon_data = response.json()
#             self.display_info(pokemon_data)
#         except requests.exceptions.RequestException as e:
#             print(f"Failed to retrieve Pokemon information. {e}")
#
#
#     @staticmethod
#     def display_info(data):
#         print(f"Name: {data['name']}")
#         print(f"ID: {data['id']}")
#         print(f"Height: {data['height']}")
#         print(f"Weight: {data['weight']}")
#         abilities = [ability['ability']['name'] for ability in data['abilities']]
#         print("Abilities:")
#         for ability in abilities:
#             print(f"- {ability}")
#
#
# if __name__ == "__main__":
#     pokemon_retriever = PokemonInfoRetriever()
#
#     while True:
#         user_input = input("Enter a Pokemon name (or 'exit' to quit): ").lower()
#         if user_input == "exit":
#             break
#         pokemon_retriever.set_pokemon_name(user_input)
#         pokemon_retriever.get_pokemon_info()


import requests


class PokemonInfoRetriever:
    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name

    def get_pokemon_info(self):
        api_url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_name}"
        response = requests.get(api_url)
        return response