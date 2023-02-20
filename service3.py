import time
from sql_queries import create_table, set_object_top_level, get_objects

create_table()

if __name__ == '__main__':
    while True:
        objects = get_objects()
        for object in objects:
            if object.likes > 20:
                set_object_top_level(1, object.id)
            else:
                set_object_top_level(2, object.id)
        print("updated")
        time.sleep(10)