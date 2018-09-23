import pytest
{% if not without_postgres %}
from sqlalchemy import create_engine
import aiopg.sa
{% endif %}

from {{ name }}.utils import PATH, get_config
# todo: if for db
from {{ name }}.app import init_app
{% if not without_postgres %}
from {{ name }}.migrations import metadata
from {{ name }}.users.tables import users
{% endif %}


# constants
TEST_CONFIG_PATH = PATH / 'config' / 'api.test.yml'
CONFIG_PATH = PATH / 'config' / 'api.dev.yml'
#
config = get_config(['-c', CONFIG_PATH.as_posix()])
test_config = get_config(['-c', TEST_CONFIG_PATH.as_posix()])


{% if not without_postgres %}
# helpers
def get_db_url(config: dict) -> str:
    '''
    Generate a url for db connection from the config.
    '''

    return (
        f"postgresql://"
        f"{config['postgres']['user']}"
        f":{config['postgres']['password']}"
        f"@{config['postgres']['host']}"
        f":{config['postgres']['port']}"
        f"/{config['postgres']['database']}"
    )


engine = create_engine(
    get_db_url(config),
    isolation_level='AUTOCOMMIT',
)
test_engine = create_engine(
    get_db_url(test_config),
    isolation_level='AUTOCOMMIT',
)


def init_sample_data(engine) -> None:
    with engine.connect() as conn:
        query = users\
            .insert()\
            .values([{
                    'id': idx,
                    'username': f'test#{idx}',
                    'email': f'test#{idx}',
                    'password': f'{idx}'} for idx in range(10)
                ])

        conn.execute(query)

def setup_test_db(engine) -> None:
    '''
    Removing the old test database environment and creating new clean
    environment.
    '''
    # test params
    db_name = test_config['postgres']['database']
    db_user = test_config['postgres']['user']
    db_password = test_config['postgres']['password']

    teardown_test_db(engine)

    with engine.connect() as conn:
        conn.execute(
            f"create user {db_user} with password '{db_password}'"
        )
        conn.execute(
            f"create database {db_name} encoding 'UTF8'"
        )
        conn.execute(
            f"grant all privileges on database {db_name} to {db_user}"
        )


def teardown_test_db(engine) -> None:
    '''
    Removing the test database environment.
    '''
    # test params
    db_name = test_config['postgres']['database']
    db_user = test_config['postgres']['user']

    with engine.connect() as conn:
        conn.execute(
            f"""
            SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = '{db_name}'
            AND pid <> pg_backend_pid();
            """
        )
        conn.execute(f"drop database if exists {db_name}")
        conn.execute(f"drop role if exists {db_user}")


# fixtures

@pytest.yield_fixture(scope='session')
def db():
    '''
    The fixture for running and turn down database.
    '''
    setup_test_db(engine)
    yield
    teardown_test_db(engine)


@pytest.yield_fixture(scope='session')
def tables(db):
    '''
    The fixture for create all tables and init simple data.
    '''
    metadata.create_all(test_engine)
    init_sample_data(test_engine)
    yield
    metadata.drop_all(test_engine)

@pytest.fixture
async def sa_engine(loop):
    '''
    The fixture initialize async engine for PostgresSQl.
    '''

    return await aiopg.sa.create_engine(**test_config['postgres'])
{% endif %}

@pytest.fixture
async def client(aiohttp_client{% if not without_postgres %}, tables{% endif %}):
    '''
    The fixture for the initialize client.
    '''
    app = init_app(['-c', TEST_CONFIG_PATH.as_posix()])

    return await aiohttp_client(app)
