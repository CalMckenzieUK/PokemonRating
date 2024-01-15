import os
import MySQLdb
from dotenv import load_dotenv


load_dotenv()

def database_query(sql_query):
    try:
        connection = MySQLdb.connect(
        host=os.getenv("DATABASE_HOST"),
        user=os.getenv("DATABASE_USERNAME"),
        passwd=os.getenv("DATABASE_PASSWORD"),
        db=os.getenv("DATABASE"),
        autocommit=True,
        # ssl_mode="VERIFY_iDENTITY",
        ssl={"ca": "/etc/ssl/certs/ca-certificates.crt"})
    except:
        connection = MySQLdb.connect(
        host=os.environ["DATABASE_HOST"],
        user=os.environ["DATABASE_USERNAME"],
        passwd=os.environ["DATABASE_PASSWORD"],
        db=os.environ["DATABASE"],
        autocommit=True,
        # ssl_mode="VERIFY_iDENTITY",
        ssl={"ca": "/etc/ssl/certs/ca-certificates.crt"})
    try:
        c = connection.cursor()
        c.execute(sql_query)
        results = c.fetchall()
        return results
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        c.close()
        connection.close()

if __name__ == '__main__':
    sql = '''
    create table historical_battles_2 
    (battle_id int, 
    left_pokemon varchar(50), 
    right_pokemon varchar(50),
    result varchar(1),
    datetime_of_battle datetime) 
    '''
    print(database_query('show columns from pokemon_rating'))
    # print(sql)
    # print( database_query(f'{sql}')) 
    
    # database_query('drop table historical_battles')
    # database_query('create table historical_battles (battle_id int, left_pokemon varchar(50), right_pokemon varchar(50), result varchar(1), datetime_of_battle datetime)')
    # print(database_query('''insert into historical_battles 
    #                      select max(battle_id), max(left_pokemon), max(right_pokemon), max(result), 
    #                      datetime_of_battle from historical_battles_2
    #                      group by datetime_of_battle'''))
    
    # print(database_query('select count(*) from historical_battles'))
    
    # print( database_query(''' insert into historical_battles_2 select * from historical_battles'''))
    # print(database_query('show columns from historical_battles'))
    # print(database_query('show columns from historical_battles_2'))
    # print(database_query('drop table historical_battles_2'))