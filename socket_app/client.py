import socketio

# standard Python
sio = socketio.Client()


@sio.on('message')
def on_message(data):
    print(data)
    # print('I received a message!')

sio.connect('http://localhost:8080')

# main()