import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parentOfParent = os.path.dirname(parent)
sys.path.append(parentOfParent)
import utils

def run_server():
    server_socket = utils.serverSetup()

    print("Server is listening for incoming connections...")

    while True:
        try:
            # Accept a connection
            client_socket, client_address = server_socket.accept()

            print("Connected to:", client_address)
            
            # receive the file infos using client socket with buffer size 4096
            received = client_socket.recv(4096).decode()
            # stores filename details from the received file info
            filename = received

            # receive the pickled file data using client socket
            pickledData = client_socket.recv(4096)
            # unpickle the file data
            fileData = utils.unpickler(pickledData)
            
            # ensures saving file within the folder this Server is in
            filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
            # open to write to the file in binary
            with open(filepath, "wb") as file:
                file.write(fileData)
        except Exception as e:
            print("Error:", e)
        finally:
            # Clean up the connection
            client_socket.close()

            print(f"File '{filename}' has been received!")

if __name__ == "__main__":
    run_server()