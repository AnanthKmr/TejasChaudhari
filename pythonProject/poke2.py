from Pokeapi import PokemonInfoRetriever


def main():
    while True:
        pokemon_name = input("Enter the name of the Pokémon (or type 'exit' to quit): ")

        if pokemon_name.lower() == 'exit':
            break

        if not pokemon_name:
            print("Please provide a Pokémon name.")
            continue

        pokemon_info_retriever = PokemonInfoRetriever(pokemon_name)
        response = pokemon_info_retriever.get_pokemon_info()

        if response.status_code == 200:
            pokemon_data = response.json()
            print("Pokemon Name:", pokemon_data['name'])
            print("Pokemon ID:", pokemon_data['id'])
            print("Height:", pokemon_data['height'])
            print("Weight:", pokemon_data['weight'])
            abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
            print("Abilities:", ', '.join(abilities))
        else:
            print(f"Failed to retrieve information for {pokemon_name}. Status Code: {response.status_code}")


if __name__ == "__main__":
    main()