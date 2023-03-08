from os import name
import time
import random

from sql_queries import create_table, insert_object
from object import Object
from credentials import conn

create_table(conn)

if name == 'main':
    while True:
        insert_object(
            conn,
            Object(
                name=random.choice(["Coffee Boom", "Travelers", "Papa Johns", "McDonalds", "KFC", "Burger King", "Pizza Hut", "Subway", "Starbucks"]),
                capacity=random.randint(20, 100),
                amount_of_people=random.randint(20, 100),
                is_full=0,
                top_level = 0,
                likes = random.randint(0, 100)
            )
        )
        print("Inserted")
        time.sleep(3)