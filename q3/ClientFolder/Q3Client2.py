import threading
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parentOfParent = os.path.dirname(parent)
sys.path.append(parentOfParent)
import utils

def receive_messages(client_socket):
    """Receive and display messages from the server"""
    while True:
        try:
            data = client_socket.recv(1024)
            # check if data was received
            if data:
                # unpickle the received data to get the message and display it
                message = utils.unpickler(data)
                print(message)
        except Exception as error:
            print("Error:", error)
            break

def send_message(client_socket):
    """Send messages to the server"""
    while True:
        # Get input for a message, and pickle it before sending
        message = input()
        client_socket.send(utils.pickler(message))

def run_client():
    """
    Setup and run the client
    
    Setup a client socket, start a thread to receive messages from the server,
    and start another thread to send messages to the server
    """
    client_socket = utils.clientSetup()

    # start a thread to receive messages from the central server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # start a thread to send messages to the central server
    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    run_client()
