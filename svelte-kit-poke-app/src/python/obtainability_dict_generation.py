with open('svelte-kit-poke-app/src/python/pokemon_obtainability_list.txt', 'r') as f:
    pokemon_info = f.readlines()   

pokemon_info = [i.split('],') for i in pokemon_info]
split_pokemon_info = []

for i in pokemon_info:
    for j in i:
        split_pokemon_info.append(j)

split_pokemon_info = [i.replace('{','')
                      .replace('[','')
                      .replace(".', '", ' , ')
                      .replace("'", '"')
                      .replace('}','')
                      .replace('"s', "'s") for i in split_pokemon_info]


string_pokemon_info = ''

for i in split_pokemon_info:
    string_pokemon_info += i+',\n'

string_pokemon_info = string_pokemon_info[:-2]



with open('svelte-kit-poke-app/src/lib/pokemon_obtainability_list.js', 'w') as f:
    f.write('let pokemon_info_dict = {'+string_pokemon_info+'}')
 



