from database_connection import database_query
import os 
import pandas as pd

def get_battles():
    battle_df = pd.DataFrame(database_query('select * from pokemon_rating order by datetime_created asc'), columns=('battle_id', 'left_pokemon', 'right_pokemon', 'result', 'datetime_of_battle')) 
    return battle_df


def create_elo_table():
    database_query('create table if not exists elo_table (pokemon varchar(50), elo int, battles int, wins int, losses int, draws int, win_rate float)')

def create_historical_battles():
    database_query('create table if not exists historical_battles (battle_id int, left_pokemon varchar(50), right_pokemon varchar(50), result varchar(1), datetime_of_battle datetime)')

def battles_to_elo():
    elo_table = pd.DataFrame(database_query('select * from elo_table'), columns=('pokemon', 'elo', 'battles', 'wins', 'losses', 'draws', 'win_rate'))
    battle_df = get_battles()
    elo_array = []
    elo_dict = {}
    elo_table['pokemon'] = elo_table['pokemon'].str.replace('%20',' ')
    battle_df['left_pokemon'] = battle_df['left_pokemon'].str.replace('%20',' ')
    battle_df['right_pokemon'] = battle_df['right_pokemon'].str.replace('%20',' ')
    for i in battle_df['left_pokemon'].unique():
        if i not in elo_array:
            if i not in elo_table['pokemon'].unique():
                elo_dict[i] = {'elo': 1000, 'battles': 0, 'wins': 0, 'losses': 0, 'draws': 0, 'win_rate': 0}
                elo_array.append(i)
            else:
                elo_dict[i] = {'elo': elo_table[elo_table['pokemon'] == i]['elo'].values[0], 
                               'battles': elo_table[elo_table['pokemon'] == i]['battles'].values[0], 
                               'wins': elo_table[elo_table['pokemon'] == i]['wins'].values[0], 
                               'losses': elo_table[elo_table['pokemon'] == i]['losses'].values[0], 
                               'draws': elo_table[elo_table['pokemon'] == i]['draws'].values[0], 
                               'win_rate': elo_table[elo_table['pokemon'] == i]['win_rate'].values[0]}
                elo_array.append(i)
    for i in battle_df['right_pokemon'].unique():
        if i not in elo_array:
            if i not in elo_table['pokemon'].unique():
                elo_dict[i] = {'elo': 1000, 'battles': 0, 'wins': 0, 'losses': 0, 'draws': 0, 'win_rate': 0}
                elo_array.append(i)
            else:
                elo_dict[i] = {'elo': elo_table[elo_table['pokemon'] == i]['elo'].values[0], 
                               'battles': elo_table[elo_table['pokemon'] == i]['battles'].values[0], 
                               'wins': elo_table[elo_table['pokemon'] == i]['wins'].values[0], 
                               'losses': elo_table[elo_table['pokemon'] == i]['losses'].values[0], 
                               'draws': elo_table[elo_table['pokemon'] == i]['draws'].values[0], 
                               'win_rate': elo_table[elo_table['pokemon'] == i]['win_rate'].values[0]}
    for i in range(len(battle_df)):
        left_pokemon = battle_df['left_pokemon'][i]
        right_pokemon = battle_df['right_pokemon'][i]
        result = battle_df['result'][i]
        if result == '1':
            elo_dict[left_pokemon]['elo'] = elo_dict[left_pokemon]['elo'] + 32 * (1 - (1 / (1 + 10 ** ((elo_dict[right_pokemon]['elo'] - elo_dict[left_pokemon]['elo']) / 400))))
            elo_dict[right_pokemon]['elo'] = elo_dict[right_pokemon]['elo'] + 32 * (0 - (1 / (1 + 10 ** ((elo_dict[left_pokemon]['elo'] - elo_dict[right_pokemon]['elo']) / 400))))
            elo_dict[left_pokemon]['battles'] = elo_dict[left_pokemon]['battles'] + 1
            elo_dict[left_pokemon]['wins'] = elo_dict[left_pokemon]['wins'] + 1
            elo_dict[right_pokemon]['battles'] = elo_dict[right_pokemon]['battles'] + 1
            elo_dict[right_pokemon]['losses'] = elo_dict[right_pokemon]['losses'] + 1
            elo_dict[left_pokemon]['win_rate'] = elo_dict[left_pokemon]['wins'] / elo_dict[left_pokemon]['battles']
            elo_dict[right_pokemon]['win_rate'] = elo_dict[right_pokemon]['wins'] / elo_dict[right_pokemon]['battles']

        if result == '2':
            elo_dict[left_pokemon]['elo'] = elo_dict[left_pokemon]['elo'] + 32 * (0 - (1 / (1 + 10 ** ((elo_dict[right_pokemon]['elo'] - elo_dict[left_pokemon]['elo']) / 400))))
            elo_dict[right_pokemon]['elo'] = elo_dict[right_pokemon]['elo'] + 32 * (1 - (1 / (1 + 10 ** ((elo_dict[left_pokemon]['elo'] - elo_dict[right_pokemon]['elo']) / 400))))
            elo_dict[left_pokemon]['battles'] = elo_dict[left_pokemon]['battles'] + 1
            elo_dict[left_pokemon]['losses'] = elo_dict[left_pokemon]['losses'] + 1
            elo_dict[right_pokemon]['battles'] = elo_dict[right_pokemon]['battles'] + 1
            elo_dict[right_pokemon]['wins'] = elo_dict[right_pokemon]['wins'] + 1
            elo_dict[left_pokemon]['win_rate'] = elo_dict[left_pokemon]['wins'] / elo_dict[left_pokemon]['battles']
            elo_dict[right_pokemon]['win_rate'] = elo_dict[right_pokemon]['wins'] / elo_dict[right_pokemon]['battles']

        if result == '0':
            elo_dict[left_pokemon]['elo'] = elo_dict[left_pokemon]['elo'] + 32 * (0.5 - (1 / (1 + 10 ** ((elo_dict[right_pokemon]['elo'] - elo_dict[left_pokemon]['elo']) / 400))))
            elo_dict[right_pokemon]['elo'] = elo_dict[right_pokemon]['elo'] + 32 * (0.5 - (1 / (1 + 10 ** ((elo_dict[left_pokemon]['elo'] - elo_dict[right_pokemon]['elo']) / 400))))
            elo_dict[left_pokemon]['draws'] = elo_dict[left_pokemon]['draws'] + 1
            elo_dict[right_pokemon]['draws'] = elo_dict[right_pokemon]['draws'] + 1
            elo_dict[left_pokemon]['battles'] = elo_dict[left_pokemon]['battles'] + 1
            elo_dict[right_pokemon]['battles'] = elo_dict[right_pokemon]['battles'] + 1
            elo_dict[left_pokemon]['win_rate'] = elo_dict[left_pokemon]['wins'] / elo_dict[left_pokemon]['battles']
            elo_dict[right_pokemon]['win_rate'] = elo_dict[right_pokemon]['wins'] / elo_dict[right_pokemon]['battles']
    
    elo_df = pd.DataFrame.from_dict(elo_dict, orient='index')
    elo_df = elo_df.reset_index()
    elo_df = elo_df.rename(columns={'index': 'pokemon'})
    elo_df['elo'] = elo_df['elo'].astype(int)
    elo_df['battles'] = elo_df['battles'].astype(int)
    elo_df['wins'] = elo_df['wins'].astype(int)
    elo_df['losses'] = elo_df['losses'].astype(int)
    elo_df['draws'] = elo_df['draws'].astype(int)
    elo_df['win_rate'] = elo_df['win_rate'].astype(float)
    
    rows = [tuple(x) for x in elo_df.to_numpy()]
    combined_row_string = ''
    for i in rows:
        combined_row_string = combined_row_string + str(i) + ', '
    combined_row_string = combined_row_string[:-2]
     
    database_query('insert into elo_table values {}'.format(combined_row_string))

    rows = [tuple(x) for x in battle_df.to_numpy()]
    combined_row_string = ''
    for i in rows:
        combined_row_string = combined_row_string + str(i) + ', '
    combined_row_string = combined_row_string[:-2]

    battle_ids_processed = battle_df['battle_id'].to_list()
    
    database_query('insert into historical_battles values {}'.format(combined_row_string))
    database_query('delete from pokemon_rating where id in ({})'.format(', '.join(map(str, battle_ids_processed))))

if __name__ == '__main__':
    create_elo_table()
    create_historical_battles()
    battles_to_elo()