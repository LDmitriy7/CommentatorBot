import toml

env = toml.load('env.toml')


class Api:
    data: dict = env['Api']

    ID = data['id']
    HASH = data['hash']
