import time
from sql_queries import create_table, check_object_is_full

create_table()

if __name__ == '__main__':
    while True:
        check_object_is_full()
        print("updated")
        time.sleep(5)