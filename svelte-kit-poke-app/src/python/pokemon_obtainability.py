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
    pokemon_list = [i for i in pokemon_list if i != '']
    return pokemon_list

#pokemon_list is an array of all pokemon names as they appear on the 'Pokemon List' page of the wiki

def pokemon_page(pokemon_name):
    if pokemon_name != 'Mime Jr.':
        pokemon_page_url = f'https://wiki.tppc.info/{pokemon_name}'
    else:
        pokemon_page_url = f'https://wiki.tppc.info/Mime_Jr'
    pokemon_page_request = requests.get(pokemon_page_url)
    soup = bs4.BeautifulSoup(pokemon_page_request.text, 'lxml')
    pokemon_page_mw_content_text = soup.find('div', class_='mw-content-ltr')
    pokemon_page_types = pokemon_page_mw_content_text.text.split('id="Types"')
    try: pokemon_page_types = pokemon_page_types[0].split('Types')[2]
    except: pokemon_page_types = pokemon_page_types[0].split('Forms')[2]
    pokemon_page_types = pokemon_page_types.split('\n')
    pokemon_page_types = [i.strip() for i in pokemon_page_types if i != '']
    #drop last item from pokemon_page_types
    pokemon_page_types = pokemon_page_types[:-1]
    type_array = []
    type_headers = []
    for i in range(len(pokemon_page_types)):
        if 'Shiny:' in pokemon_page_types:
            variation = ''
            if pokemon_page_types[i] == 'Normal:':
                variation = pokemon_page_types[i-1]
                type_headers.append(variation)
                shiny_index = pokemon_page_types.index('Shiny:')
                type_array.append(pokemon_page_types[i+1:shiny_index])
                pokemon_page_types[i] = 'checked'
                # pokemon_page_types[shiny_index] = 'checked'
            elif pokemon_page_types[i] == 'Shiny:':
                dark_index = pokemon_page_types.index('Dark:')
                type_array.append(pokemon_page_types[i+1:dark_index])
                pokemon_page_types[i] = 'checked'
                # pokemon_page_types[dark_index] = 'checked'
            elif pokemon_page_types[i] == 'Dark:':
                golden_index = pokemon_page_types.index('Golden:')
                type_array.append(pokemon_page_types[i+1:golden_index])
                pokemon_page_types[i] = 'checked'
                # pokemon_page_types[golden_index] = 'checked'
            elif pokemon_page_types[i] == 'Golden:':
                type_array.append(pokemon_page_types[i+1])
                pokemon_page_types[i] = 'checked'
        else:
            variation = ''
            if pokemon_page_types[i] == 'Normal:':
                variation = pokemon_page_types[i-1]
                type_headers.append(variation)
                shiny_index = pokemon_page_types.index('Shiny')
                type_array.append(pokemon_page_types[i+1:shiny_index])
                pokemon_page_types[i] = 'checked'
                # pokemon_page_types[shiny_index] = 'checked'
            elif pokemon_page_types[i] == 'Shiny':
                dark_index = pokemon_page_types.index('Dark:')
                type_array.append(pokemon_page_types[i+1:dark_index])
                pokemon_page_types[i] = 'checked'
                # pokemon_page_types[dark_index] = 'checked'
            elif pokemon_page_types[i] == 'Dark:':
                golden_index = pokemon_page_types.index('Golden:')
                type_array.append(pokemon_page_types[i+1:golden_index])
                pokemon_page_types[i] = 'checked'
                # pokemon_page_types[golden_index] = 'checked'
            elif pokemon_page_types[i] == 'Golden:':
                type_array.append(pokemon_page_types[i+1])
                pokemon_page_types[i] = 'checked'
    type_dict = {}
    if len(type_headers) == 1:
        type_dict[pokemon_name] = type_array[0]
        type_dict['Shiny'+pokemon_name] = type_array[1]
        type_dict['Dark'+pokemon_name] = type_array[2]
        type_dict['Golden'+pokemon_name] = type_array[3]
    else:
        for i in range(len(type_headers)):
            base = i*4
            type_dict[pokemon_name+' ('+type_headers[i]+')'] = type_array[base]
            type_dict['Shiny'+pokemon_name+' ('+type_headers[i]+')'] = type_array[base+1]
            type_dict['Dark'+pokemon_name+' ('+type_headers[i]+')'] = type_array[base+2]
            type_dict['Golden'+pokemon_name+' ('+type_headers[i]+')'] = type_array[base+3]        
    
    # type_dict = {}
    # type_dict[pokemon_name+' ('+type_array[0]+')'] = type_array[1]
    # type_dict['Shiny'+pokemon_name+' ('+type_array[0]+')'] = type_array[2]
    # type_dict['Dark'+pokemon_name+' ('+type_array[0]+')'] = type_array[3]
    # type_dict['Golden'+pokemon_name+' ('+type_array[0]+')'] = type_array[4]
    # print(type_dict)
    return type_dict




def pokemon_page_from_table(pokemon_name):
    if pokemon_name != 'Mime Jr.':
        pokemon_page_url = f'https://wiki.tppc.info/{pokemon_name}'
    else:
        pokemon_page_url = f'https://wiki.tppc.info/Mime_Jr'
    pokemon_page_request = requests.get(pokemon_page_url)
    soup = bs4.BeautifulSoup(pokemon_page_request.text, 'lxml')
    pokemon_page_mw_content_text = soup.find('div', class_='mw-content-ltr')
    pokemon_page_mw_content_text = pokemon_page_mw_content_text.text.split('id=">Normal<"')
    #show pokemon_page_mw_content_text from the first occurance of 'Normal\n\n' to the end of the string
    # print(pokemon_page_mw_content_text)
    try: pokemon_page_mw_content_text = pokemon_page_mw_content_text[0].split('\n\nTypes\n\n')[1]
    except: pokemon_page_mw_content_text = pokemon_page_mw_content_text[0].split('\n\nTypes\n')[1]
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
    delimited_by_headers = []
    for i in range(len(type_headers)):
        if i == len(type_headers) - 1:
            delimited_by_headers.append(pokemon_page_types[pokemon_page_types.index(type_headers[i]):])
        else:
            delimited_by_headers.append(pokemon_page_types[pokemon_page_types.index(type_headers[i]):pokemon_page_types.index(type_headers[i+1])])


    for i in delimited_by_headers:
    
        for i in range(len(pokemon_page_types)):
            variation = ''
            if pokemon_page_types[i] == 'Normal:':
                variation = pokemon_page_types[i-1]
                try:
                    shiny_index = pokemon_page_types.index('Shiny:')
                except:
                    shiny_index = pokemon_page_types.index('Shiny')
                type_array.append(pokemon_page_types[i+1:shiny_index])
                pokemon_page_types[i] = 'checked'
            elif pokemon_page_types[i] == 'Shiny:':
                dark_index = pokemon_page_types.index('Dark:')
                type_array.append(pokemon_page_types[i+1:dark_index])
                pokemon_page_types[i] = 'checked'

            elif pokemon_page_types[i] == 'Dark:':
                golden_index = pokemon_page_types.index('Golden:')
                type_array.append(pokemon_page_types[i+1:golden_index])
                pokemon_page_types[i] = 'checked'
                # pokemon_page_types[golden_index] = 'checked'
            elif pokemon_page_types[i] == 'Golden:':
                type_array.append(pokemon_page_types[i+1])
                pokemon_page_types[i] = 'checked'
    type_dict = {}
    if len(type_headers) == 1:
        type_dict[pokemon_name] = type_array[0]
        type_dict['Shiny'+pokemon_name] = type_array[1]
        type_dict['Dark'+pokemon_name] = type_array[2]
        type_dict['Golden'+pokemon_name] = type_array[3]
    else:
        for i in range(len(type_headers)):
            base = i*4
            type_dict[pokemon_name+' ('+type_headers[i]+')'] = type_array[base]
            type_dict['Shiny'+pokemon_name+' ('+type_headers[i]+')'] = type_array[base+1]
            type_dict['Dark'+pokemon_name+' ('+type_headers[i]+')'] = type_array[base+2]
            type_dict['Golden'+pokemon_name+' ('+type_headers[i]+')'] = type_array[base+3]     
    # print(type_dict)
    return type_dict


def main():
    
    # print(pokemon_page('Pumpkaboo'))

    pokemon_list = get_pokemon_list()
    pokemon_list = [i.split('(')[0].strip() for i in pokemon_list]
    pokemon_list = list(dict.fromkeys(pokemon_list))
    pokemon_info = []
    for i in pokemon_list:
        print(i)
        try:
            type_dicts = pokemon_page(i)
            for key, value in type_dicts.items():
                if " (Normal)" in str(key):
                    key = str(key).replace(" (Normal)", "")
                    if '"' in str(value):
                        value = str(value).replace('"', '')
                        pokemon_info.append(f'"{str(key)}": "{value}",') 
                if '"' in str(value):
                        value = str(value).replace('"', '')
                        pokemon_info.append(f'"{str(key)}": "{value}",') 
                pokemon_info.append(f'"{str(key)}": "{str(value)}",')
            # print(1, type_dicts)
        except:
            type_dicts = pokemon_page_from_table(i)
            for key, value in type_dicts.items():
                if " (Normal)" in str(key):
                    key = str(key).replace(" (Normal)", "")
                    if '"' in str(value):
                        value = str(value).replace('"', '')
                        pokemon_info.append(f'"{str(key)}": "{value}",') 
                if '"' in str(value):
                        value = str(value).replace('"', '')
                        pokemon_info.append(f'"{str(key)}": "{value}",') 
                pokemon_info.append(f'"{str(key)}": "{str(value)}",')
            # print(2, type_dicts)
        # print(pokemon_info)

    with open('svelte-kit-poke-app/src/python/pokemon_obtainability_list.txt', 'w') as f:
        for i in pokemon_info:
            f.write(str(i)+'\n')



if __name__ == '__main__':
    main()