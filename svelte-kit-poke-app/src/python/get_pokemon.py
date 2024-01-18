import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

with requests.session() as s:
    rarity_retrieve = s.get('https://www.tppcrpg.net/rarity.html')
rarity_scrape = bs(rarity_retrieve.text, 'lxml')
rarity_table = rarity_scrape.find_all('tr')
array = []

for i in rarity_table:
    row = str(i).replace('<tr class="row0"><td>','').replace('</td><td>',':').replace('</td></tr>','')
    row = str(row).replace('<tr class="row1"><td>','').replace('</td><td>',':').replace('</td></tr>','')
    split_row = row.split(':')
    split_row = [i.replace('Flabéb&amp;eacute','Flabébé') for i in split_row]
    array.append(split_row)
    if len(split_row) > 7:
        print(split_row)
        print(i)

individual_pokemon = []
for i in array[1:]:
    if int(i[2]) > 0:
        individual_pokemon.append([i[1], 'M'])
    if int(i[3]) > 0:
        individual_pokemon.append([i[1], 'F'])
    if int(i[4]) > 0:
        individual_pokemon.append([i[1], 'G'])
    if int(i[5]) > 0:
        individual_pokemon.append([i[1], 'U'])

with open('/workspaces/PokemonRating/svelte-kit-poke-app/src/dex.txt', 'w') as f:
    pokedex = f.read().splitlines()
    pokedex = [i.replace('\t','').replace('\xa0',' ') for i in pokedex]
    pokedex = [i.split(',') for i in pokedex]

pokedex_dict = {}

for i in pokedex:
    pokedex_dict[i[1]] = i[0]

pokemon_link_dict = {}


for i in individual_pokemon:
    gender = i[1]
    if gender == 'U':
        gender = 'M'
    if gender == 'G':
        gender = 'M'
    if "Golden" in i[0]:
        type_strip = i[0].replace('Golden','')
        dex_no_and_form = pokedex_dict[type_strip].split('-')
        try: 
            form = dex_no_and_form[1]
            dex_no = dex_no_and_form[0]
            if len(dex_no) == 1:
                dex_no = '00' + dex_no
            if len(dex_no) == 2:
                dex_no = '0' + dex_no
            link = f'https://graphics.tppcrpg.net/xy/golden/{dex_no}{gender}-{dex_no_and_form[1]}.gif'
            pokemon_link_dict[str(i[0]+' '+i[1])] = link
        except:
            dex_no = dex_no_and_form[0]
            if len(dex_no) == 1:
                dex_no = '00' + dex_no
            if len(dex_no) == 2:
                dex_no = '0' + dex_no
            link = f'https://graphics.tppcrpg.net/xy/golden/{dex_no}{gender}.gif'
            pokemon_link_dict[str(i[0]+' '+i[1])] = link
    elif "Shiny" in i[0]:
        type_strip = i[0].replace('Shiny','')
        dex_no_and_form = pokedex_dict[type_strip].split('-')
        try: 
            form = dex_no_and_form[1]
            dex_no = dex_no_and_form[0]
            if len(dex_no) == 1:
                dex_no = '00' + dex_no
            if len(dex_no) == 2:
                dex_no = '0' + dex_no
            link = f'https://graphics.tppcrpg.net/xy/shiny/{dex_no}{gender}-{dex_no_and_form[1]}.gif'
            pokemon_link_dict[str(i[0]+' '+i[1])] = link
        except:
            dex_no = dex_no_and_form[0]
            if len(dex_no) == 1:
                dex_no = '00' + dex_no
            if len(dex_no) == 2:
                dex_no = '0' + dex_no
            link = f'https://graphics.tppcrpg.net/xy/shiny/{dex_no}{gender}.gif'
            pokemon_link_dict[str(i[0]+' '+i[1])] = link
    elif "Dark" in i[0] and i[0][0:7] != 'Darkrai':
        type_strip = ''
        if i[0] == 'DarkDarkrai':
            type_strip = "Darkrai"
        else:
            type_strip = i[0].replace('Dark','')
        dex_no_and_form = pokedex_dict[type_strip].split('-')
        try: 
            form = dex_no_and_form[1]
            dex_no = dex_no_and_form[0]
            if len(dex_no) == 1:
                dex_no = '00' + dex_no
            if len(dex_no) == 2:
                dex_no = '0' + dex_no
            link = f'https://graphics.tppcrpg.net/xy/dark/{dex_no}{gender}-{dex_no_and_form[1]}.gif'
            pokemon_link_dict[str(i[0]+' '+i[1])] = link
        except:
            dex_no = dex_no_and_form[0]
            if len(dex_no) == 1:
                dex_no = '00' + dex_no
            if len(dex_no) == 2:
                dex_no = '0' + dex_no
            link = f'https://graphics.tppcrpg.net/xy/dark/{dex_no}{gender}.gif'
            pokemon_link_dict[str(i[0]+' '+i[1])] = link
    else:
        type_strip = i[0]
        dex_no_and_form = pokedex_dict[type_strip].split('-')
        try: 
            form = dex_no_and_form[1]
            dex_no = dex_no_and_form[0]
            if len(dex_no) == 1:
                dex_no = '00' + dex_no
            if len(dex_no) == 2:
                dex_no = '0' + dex_no
            link = f'https://graphics.tppcrpg.net/xy/normal/{dex_no}{gender}-{dex_no_and_form[1]}.gif'
            pokemon_link_dict[str(i[0]+' '+i[1])] = link
        except:
            dex_no = dex_no_and_form[0]
            if len(dex_no) == 1:
                dex_no = '00' + dex_no
            if len(dex_no) == 2:
                dex_no = '0' + dex_no
            link = f'https://graphics.tppcrpg.net/xy/normal/{dex_no}{gender}.gif'
            pokemon_link_dict[str(i[0]+' '+i[1])] = link


# with open('/workspaces/PokemonRating/poke-app/src/pokemon_links.txt', 'w') as f:
#     for i in pokemon_link_dict:
#         f.write(str(i+', '+pokemon_link_dict[i])+'\n')

with open('/workspaces/PokemonRating/svelte-kit-poke-app/src/individual_pokemon.txt', 'w') as f:
    for i in individual_pokemon:
        f.write(str("'"+i[0]+' '+i[1])+"',\n")

#     pokemon_link_dict[i] = 'https://www.tppcrpg.net/' + i.replace(' ','').lower() + '.html'


# df = pd.DataFrame(array[1:], columns = ['Rank', 'Pokémon', 'Male', 'Female', 'Genderless', 'Ungendered', 'Total'])
# print(df)