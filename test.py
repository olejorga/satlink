from pipeline import Pipeline
from pipeline.helpers import openers
from pipeline.helpers import wrappers

# THIS IS JUST A TEST!

user = {
    "name": "Joe",
    "password": "Goldberg"
}

app = Pipeline()

def read_all_users(ctx) -> str:
    return wrappers.json(user)

app.get("/api/users", read_all_users)

app.run(3000)