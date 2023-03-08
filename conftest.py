from typing import Generator
import pytest
from sqlalchemy import Connection, create_engine
from testcontainers.postgres import PostgresContainer

from sql_queries import create_table, insert_object
from object import Object


@pytest.fixture()
def postgres_container1() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer(image="postgres:latest") as container:
        container.get_container_host_ip = lambda: 'localhost'       
        container.start()
        yield container

@pytest.fixture()
def postgres_container() -> PostgresContainer:
    container = PostgresContainer(image="postgres:latest")
    container.get_container_host_ip = lambda: 'localhost'
    container.start()
    return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    return postgres_container.get_connection_url()


@pytest.fixture(scope="function")
def conn_with_data(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    object = [
        Object(
            name = "test_name 1",
            capacity = 90,
            amount_of_people = 69,
            is_full = 0,
            top_level = 2,
            likes = 20,
            ),
        Object(
            name = "test_name 2",
            capacity = 91,
            amount_of_people = 51,
            is_full = 0,
            top_level = 1,
            likes = 87,
        ),
        Object(
            name = "test_name 3",
            capacity = 99,
            amount_of_people = 23,
            is_full = 0,
            top_level = 1,
            likes = 72,
        ),
    ]
    for object in object:
        insert_object(conn, object)
    return postgres_container.get_connection_url()

