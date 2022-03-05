import toml

env = toml.load('env.toml')
misc: dict = env['Misc']


class Api:
    data: dict = env['Api']

    ID = data['id']
    HASH = data['hash']


SEND_AS_CHAT_ID = misc['send_as_chat_id']
MSG_TEXT = misc['msg_text']
