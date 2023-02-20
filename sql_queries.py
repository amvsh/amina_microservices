import psycopg2

from object import Object

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)


def create_table():
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

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_object(object: Object):
    query = """
    INSERT INTO objects_amina (name, capacity, amount_of_people, is_full, top_level, likes)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (object.name, object.capacity, object.amount_of_people,
                   object.is_full, object.top_level, object.likes))
    conn.commit()


def set_object_top_level(level_value: int, object_id: int):
    query = "UPDATE objects_amina SET top_level={} WHERE id={};".format(
        level_value, object_id)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def check_object_is_full():
    query = "UPDATE objects_amina SET is_full=1 WHERE amount_of_people>=capacity;"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def get_objects() -> list[Object]:
    query = "SELECT * FROM objects_amina;"
    cursor = conn.cursor()
    cursor.execute(query)
    return [Object(
        id=object[0],
        name=object[1],
        capacity=object[2],
        amount_of_people=object[3],
        is_full=object[4],
        top_level=object[5],
        likes=object[6],
    ) for object in cursor.fetchall()]
