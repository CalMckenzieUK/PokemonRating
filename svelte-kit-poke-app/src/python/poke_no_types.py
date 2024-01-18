import requests
import pandas
import bs4

pokemon_list_wiki_url = 'https://wiki.tppc.info/Pok%C3%A9mon'

pokemon_list_wiki_request = requests.get(pokemon_list_wiki_url)
soup = bs4.BeautifulSoup(pokemon_list_wiki_request.text, 'lxml')   
pokemon_list_wiki_table = soup.find_all('tr')
pokemon_list = []
for i in pokemon_list_wiki_table[1:]:
    pokemon_list.append(i.text.split('\n')[2].strip())





def pokemon_page(pokemon_name):
    pokemon_page_url = f'https://wiki.tppc.info/{pokemon_name}'
    pokemon_page_request = requests.get(pokemon_page_url)
    soup = bs4.BeautifulSoup(pokemon_page_request.text, 'lxml')
    pokemon_page_table = soup.find_all('td')
    print(pokemon_page_table)

pokemon_page('Bulbasaur')