import sqlite3
import uuid
from faker import Faker
import random

fake = Faker()

db = sqlite3.connect("twitter.db")

db.executescript(
    """
    BEGIN;
    DROP TABLE IF EXISTS users;
    CREATE TABLE users(
        id              TEXT,
        name            TEXT,
        email           TEXT UNIQUE,
        PRIMARY KEY(id)   
    ) WITHOUT ROWID;
    COMMIT;
    """
)

for x in range(1000):
    id = str(uuid.uuid4()) # uuid is type uuid, convert into text
    name = fake.first_name()
    email = name.lower() + id.replace("-", "s") + "@" + fake.free_email_domain()
    db.execute(f"INSERT INTO users(id,name,email) VALUES('{id}','{name}','{email}')")
    db.commit()