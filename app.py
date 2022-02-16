from pipeline import Pipeline

app = Pipeline()

@app.get("/users")
def read_all_users():
    pass

@app.get("/users/<id>")
def read_user_by_id(ctx):
    pass

app.run()