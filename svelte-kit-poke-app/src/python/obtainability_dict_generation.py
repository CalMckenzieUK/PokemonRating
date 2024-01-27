with open('svelte-kit-poke-app/src/python/pokemon_obtainability_list.txt', 'r') as f:
    pokemon_info = f.read()

pokemon_info = pokemon_info[:-2]
pokemon_info = pokemon_info.replace(
                            "]", '').replace(
                            "[", '').replace(
                            " Size", '').replace(
                            'UnownA', 'Unown').replace(
                            'UnownB', 'Unown').replace(
                            'UnownC', 'Unown').replace(
                            'UnownD', 'Unown').replace(
                            'UnownE', 'Unown').replace(
                            'UnownF', 'Unown').replace(
                            'UnownG', 'Unown').replace(
                            'UnownH', 'Unown').replace(
                            'UnownI', 'Unown').replace(
                            'UnownJ', 'Unown').replace(
                            'UnownK', 'Unown').replace(
                            'UnownL', 'Unown').replace(
                            'UnownM', 'Unown').replace(
                            'UnownN', 'Unown').replace(
                            'UnownO', 'Unown').replace(
                            'UnownP', 'Unown').replace(
                            'UnownQ', 'Unown').replace(
                            'UnownR', 'Unown').replace(
                            'UnownS', 'Unown').replace(
                            'UnownT', 'Unown').replace(
                            'UnownU', 'Unown').replace(
                            'UnownV', 'Unown').replace(
                            'UnownW', 'Unown').replace(
                            'UnownX', 'Unown').replace(
                            'UnownY', 'Unown').replace(
                            'UnownZ', 'Unown').replace(
                            'Unown!', 'Unown').replace(
                            'Unown?', 'Unown').replace(
                            ' (Icy Snow)', '').replace(
                            ' (Archipelago)', '').replace(
                            ' (Sandstorm)', '').replace(
                            ' (River)', '').replace(
                            ' (Monsoon)', '').replace(
                            ' (Savannah)', '').replace(
                            ' (Sun)', '').replace(
                            ' (Ocean)', '').replace(
                            ' (Continental)', '').replace(
                            ' (Elegant)', '').replace(
                            ' (Highplains)', '').replace(
                            ' (Meadow)', '').replace(
                            ' (Modern)', '').replace(
                            ' (Marine)', '').replace(
                            ' (Tundra)', '').replace(
                            ' (Garden)', '').replace(
                            ' (Polar)', '').replace(
                            ' (Jungle)', '').replace(
                            ' (Fancy)', '').replace(
                            ' (Pokeball)', '')





opening = 'let info = {"":"",'
pokemon_info = opening+pokemon_info+'} \n export default info'


with open('svelte-kit-poke-app/src/lib/pokemon_obtainability_list.js', 'w') as f:
    f.write(pokemon_info)
 



