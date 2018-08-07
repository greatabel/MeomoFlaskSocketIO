from flask import Flask, render_template
from flask_socketio import SocketIO



luminagic_socket_random = 'f174b966fxx29y'
hardcoded_roomid = '1#2R4_'
patient_count = 0

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


# @app.route('/')
# def sessions():
#     return render_template('session.html')


# def messageReceived(methods=['GET', 'POST']):
#     print('message was received!!!')


@socketio.on('my_event_' + luminagic_socket_random)
def handle_my_custom_event(json, methods=['GET', 'POST']):
    global patient_count
    if 'role' in json:
        if json['role'] == 'patient' and json['userid'] == '':
            patient_count += 1
            
    json['patient_count'] = patient_count


    if 'roomid' in json and json['roomid'] == hardcoded_roomid:
            print('received my event: ' + str(json))
            # socketio.emit('my_response_' + luminagic_socket_random, json, callback=messageReceived)
            socketio.emit('my_response_' + luminagic_socket_random, json)



if __name__ == '__main__':
    socketio.run(app, debug=True)
