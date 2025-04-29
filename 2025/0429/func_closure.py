# -*- encoding: utf-8 -*0

def func_closure():
    def get_message(message):
        print('Got a message: {}'.format(message))
    return get_message

send_message = func_closure()
send_message("Hello world")
send_message("Hello chengdu")