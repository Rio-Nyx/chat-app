import socket, threading

nickname = input("Choose your nickname: ")

# host = '192.168.1.7'
# port = 8888
host = '127.0.0.1'
port = 4040
# host = '127.0.0.1'
# port = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))

# Listening to Server and Sending Nickname
def receive():
    while True:	
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()