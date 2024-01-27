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
        individual_pokemon.append(f'{i[1]} M: {i[2]}')
    if int(i[3]) > 0:
        individual_pokemon.append(f'{i[1]} F: {i[3]}')
    if int(i[4]) > 0:
        individual_pokemon.append(f'{i[1]} G: {i[4]}')
    if int(i[5]) > 0:
        individual_pokemon.append(f'{i[1]} U: {i[5]}')

individual_pokemon = str(individual_pokemon).replace(']','').replace('[','').replace(',',',\n').replace("'",'"').replace(':','":"')

output_start = 'let rarity = {'
output = output_start + individual_pokemon + '} \n export default rarity'

with open('/workspaces/PokemonRating/svelte-kit-poke-app/src/lib/rarity.js', 'w') as f:
    f.write(output)

