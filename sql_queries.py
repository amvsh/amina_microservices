import psycopg2
from sqlalchemy.engine import Connection
from sqlalchemy import text



from object import Object



def create_table(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS objects_amina (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        capacity INTEGER NOT NULL,
        amount_of_people INTEGER,
        is_full INTEGER NOT NULL,
        top_level INTEGER NOT NULL,
        likes INTEGER NOT NULL
        )
    """


    conn.execute(text(query))
    conn.commit()


def insert_object(conn: Connection, object: Object):
    query = """
    INSERT INTO objects_amina (name, capacity, amount_of_people, is_full, top_level, likes)
    VALUES (:name, :capacity, :amount_of_people, :is_full, :top_level, :likes)
    """

    conn.execute(
        text(query),
        parameters={
            "capacity": object.capacity, 
            "amount_of_people" : object.amount_of_people,
            "is_full" : object.is_full, 
            "top_level" : object.top_level, 
            "likes" : object.likes,
            "name": object.name,
            },
    )
    conn.commit()



def set_object_top_level(conn: Connection, level_value: int, object_id: int):
    query = "UPDATE objects_amina SET top_level={} WHERE id={};".format(
        level_value, object_id)
    conn.execute(text(query))
    conn.commit()


def check_object_is_full(conn: Connection):
    query = "UPDATE objects_amina SET is_full=1 WHERE amount_of_people>=capacity;"
    conn.execute(text(query))
    conn.commit()


def get_objects(conn: Connection) -> list[Object]:
    query = "SELECT * FROM objects_amina;"
    print("ddd")
    transactions = conn.execute(text(query)).fetchall()
    print("ddd1")
    return [Object(
        id=object[0],
        name=object[1],
        capacity=object[2],
        amount_of_people=object[3],
        is_full=object[4],
        top_level=object[5],
        likes=object[6],
    ) for object in transactions]
