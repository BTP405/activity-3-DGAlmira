import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parentOfParent = os.path.dirname(parent)
sys.path.append(parentOfParent)
import utils

def run_client():
    # the name of file we want to send, make sure it exists
    filename = "random.txt"
    # get the file size using the full filepath for the file inside the folder the Client is in
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

    try:
        client_socket = utils.clientSetup()

        # send the filename 
        client_socket.send(f"{filename}".encode())

        # read the file contents
        with open(filepath, "rb") as file:
            content = file.read()

        # pickle the file contents and send to Server
        client_socket.sendall(utils.pickler(content))
        print(f"Successfully sent pickled file {filename}!")
    except Exception as error:
        print("Error: ", error)
    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == "__main__":
    run_client()