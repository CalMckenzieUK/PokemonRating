import requests
import pandas
import bs4

def get_pokemon_list():
    pokemon_list_wiki_url = 'https://wiki.tppc.info/Pok%C3%A9mon'
    pokemon_list_wiki_request = requests.get(pokemon_list_wiki_url)
    soup = bs4.BeautifulSoup(pokemon_list_wiki_request.text, 'lxml')   
    pokemon_list_wiki_table = soup.find_all('tr')
    pokemon_list = []
    for i in pokemon_list_wiki_table[1:]:
        pokemon_list.append(i.text.split('\n')[2].strip())

#pokemon_list is an array of all pokemon names as they appear on the 'Pokemon List' page of the wiki

def pokemon_page(pokemon_name):
    pokemon_page_url = f'https://wiki.tppc.info/{pokemon_name}'
    pokemon_page_request = requests.get(pokemon_page_url)
    soup = bs4.BeautifulSoup(pokemon_page_request.text, 'lxml')
    pokemon_page_mw_content_text = soup.find('div', class_='mw-content-ltr')
    pokemon_page_types = pokemon_page_mw_content_text.text.split('id="Types"')
    pokemon_page_types = pokemon_page_types[0].split('Types')[2]
    pokemon_page_types = pokemon_page_types.split('\n')
    pokemon_page_types = [i.strip() for i in pokemon_page_types if i != '']
    #drop last item from pokemon_page_types
    pokemon_page_types = pokemon_page_types[:-1]
    type_array = []
    for i in range(len(pokemon_page_types)):
        if pokemon_page_types[i] == 'Normal:':
            shiny_index = pokemon_page_types.index('Shiny:')
            type_array.append(pokemon_page_types[i+1:shiny_index])
        elif pokemon_page_types[i] == 'Shiny:':
            dark_index = pokemon_page_types.index('Dark:')
            type_array.append(pokemon_page_types[i+1:dark_index])
        elif pokemon_page_types[i] == 'Dark:':
            golden_index = pokemon_page_types.index('Golden:')
            type_array.append(pokemon_page_types[i+1:golden_index])
        elif pokemon_page_types[i] == 'Golden:':
            type_array.append(pokemon_page_types[i+1])
    type_dict = {}
    type_dict['Normal'] = type_array[0]
    type_dict['Shiny'] = type_array[1]
    type_dict['Dark'] = type_array[2]
    type_dict['Golden'] = type_array[3]
    print(type_dict)



def pokemon_page_from_table(pokemon_name):
    print('lol')
    pokemon_page_url = f'https://wiki.tppc.info/{pokemon_name}'
    pokemon_page_request = requests.get(pokemon_page_url)
    soup = bs4.BeautifulSoup(pokemon_page_request.text, 'lxml')
    pokemon_page_mw_content_text = soup.find('div', class_='mw-content-ltr')
    pokemon_page_mw_content_text = pokemon_page_mw_content_text.text.split('id=">Normal<"')
    #show pokemon_page_mw_content_text from the first occurance of 'Normal\n\n' to the end of the string
    pokemon_page_mw_content_text = pokemon_page_mw_content_text[0].split('\n\nTypes\n\n')[1]
    pokemon_page_types = pokemon_page_mw_content_text.split('\n')
    pokemon_page_types = [i.strip() for i in pokemon_page_types if i != '']
    #drop last item from pokemon_page_types
    pokemon_page_types = pokemon_page_types[:-1]
    type_headers = []
    for i in range(len(pokemon_page_types)):
        if pokemon_page_types[i] == 'Normal:':
            type_headers.append(pokemon_page_types[i-1])
    type_array = []

    #split pokemon_page_types into arrays of types for each header
    

    for i in range(len(pokemon_page_types)):
        if pokemon_page_types[i] == 'Normal:':
            shiny_index = pokemon_page_types.index('Shiny:')
            type_array.append(pokemon_page_types[i+1:shiny_index])
        elif pokemon_page_types[i] == 'Shiny:':
            dark_index = pokemon_page_types.index('Dark:')
            type_array.append(pokemon_page_types[i+1:dark_index])
        elif pokemon_page_types[i] == 'Dark:':
            golden_index = pokemon_page_types.index('Golden:')
            type_array.append(pokemon_page_types[i+1:golden_index])
        elif pokemon_page_types[i] == 'Golden:':
            type_array.append(pokemon_page_types[i+1])
    print(type_array)
        


    # print(type_headers)

def main():
    # pokemon_list = get_pokemon_list()
    
    pokemon_page_from_table('Burmy')
    
    # pokemon_info = []
    # for i in pokemon_list:
    #     pokemon_info.append(pokemon_page(i))

    # with open('pokemon_obtainability_list.txt', 'w') as f:
    #     for i in pokemon_list:
    #         f.write(i + '\n')


if __name__ == '__main__':
    main()