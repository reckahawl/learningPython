from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = 'secret_key'
socketio = SocketIO(app)


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('command')
def handle_command(command):
    print('Received command:', command)
    # Execute the command here and send the output back to the browser
    output = 'Command executed: ' + command
    emit('output', output)


if __name__ == '__main__':
    socketio.run(app)




<!DOCTYPE html>
<html>
<head>
    <title>Web-based terminal</title>
</head>
<body>
    <div id="terminal"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.1.3/socket.io.js"></script>
    <script>
        var socket = io();
        var terminal = document.getElementById('terminal');
        socket.on('connect', function() {
            terminal.innerHTML += '<p>Connected to server</p>';
        });
        socket.on('disconnect', function() {
            terminal.innerHTML +=
