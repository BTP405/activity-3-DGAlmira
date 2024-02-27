import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parentOfParent = os.path.dirname(parent)
sys.path.append(parentOfParent)
import utils

def runWorker():
    """
    Run a worker node to execute the received tasks.

    
    Setup a server socket, listen for incoming connections, receive and
    execute the task, and sends the result back.
    """
    try:
        # create socket object
        server_socket = utils.serverSetup(('localhost', 5001))

        print("Worker node is listening for incoming connections...")

        try:
            # Accept a connection
            client_socket, client_address = server_socket.accept()

            print("Connected to:", client_address)

            pickledTask = client_socket.recv(1024)
            # Unpickle and execute the task
            task = utils.unpickler(pickledTask)
            function, args = task
            result = function(*args)

            # Send result to the client
            client_socket.sendall(str(result).encode())
        except Exception as error:
            print("Error from server:", error)
        finally:
            client_socket.close()
    except Exception as error:
        print("Error from server:", error)
    finally:
        print(f"Task completed!")
        server_socket.close()

if __name__ == "__main__":
    runWorker()