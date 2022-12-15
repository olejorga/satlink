from src.satlink import Satellite


api = Satellite()


@api.get("/[id]")
def index(uplink, downlink):
    return downlink.json(uplink.query)


@api.get("/")
def index(uplink, downlink):
    return downlink.text("Hello, World!")

@api.get("/users")
def index(uplink, downlink):
    return downlink.text("Hello, Tom!")


api.transmit(3000)
