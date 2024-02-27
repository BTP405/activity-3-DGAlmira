import threading
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parentOfParent = os.path.dirname(parent)
sys.path.append(parentOfParent)
import utils

def handle_client(client_socket, client_address, clients):
    """Handle each client connection and its main functionalities"""
    print(f"{client_address} connected.")

    # always listening for client messages
    while True:
        try:
            data = client_socket.recv(1024)
            # checks if data is received
            if data:
                # unpickle the received data for the message
                message = utils.unpickler(data)
                print(f"[{client_address}]: {message}")
                # broadcast/send the message to all connected clients
                broadcast(message, clients)
            else:
                # remove client and break the loop if no data is received
                remove_client(client_socket, clients)
                break
        except Exception as error:
            print(f"Error: {error}")
            break

def broadcast(message, clients):
    """Broadcast a message to all connected clients"""
    for client in clients:
        try:
            # pickle the inputted message and send it
            client.send(utils.pickler(message))
        except:
            # remove client from the list if cannot send the message
            remove_client(client, clients)

def remove_client(client_socket, clients):
    """Remove a client from the list of active clients"""
    if client_socket in clients:
        clients.remove(client_socket)
        print("Client disconnected.")
        client_socket.close()

def run_server():
    """
    Run the server to handle client connections for a real-time chat system
    
    Setup the server socket, listen for incoming connections, and starts
    a new thread for handling each client connection
    """
    server_socket = utils.serverSetup()

    print("Server is listening")

    clients = []

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address, clients))
        thread.start()

if __name__ == "__main__":
    run_server()
