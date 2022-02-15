from pipeline import Pipeline
from pipeline.helpers import wrappers

users = []

app = Pipeline()

def read_user_by_id(ctx):
    for user in users:
        if user["id"] == ctx.path["id"]:
            return wrappers.json(user)

    return wrappers.json(user)
    return wrappers.error(404, "dddd")

app.get("/users/[id]", read_user_by_id)

@app.get("/users")
def read_all_users(ctx):
    ctx.res.code = 400
    ctx.res.body = {}

    return ctx