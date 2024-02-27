import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parentOfParent = os.path.dirname(parent)
sys.path.append(parentOfParent)
import utils

def sendTask(tasks, workers):
    """Send tasks to worker nodes and receive/display the results"""
    try:
        # connect to the available worker nodes
        for worker, task in zip(workers, tasks):
            # create a client socket object
            client_socket = utils.clientSetup(worker)
            
            # pickle the function (task) and send it
            client_socket.sendall(utils.pickler(task))

            # receive and display the result coming from the worker
            result = client_socket.recv(1024)
            print(f"Result from {worker}: {result.decode()}")
            client_socket.close()
    except Exception as error:
        print("Error from client:", error)


if __name__ == "__main__":
    taskList = [(utils.doMath, (3, 2)), (utils.doMath, (4, 3)), (utils.doMath, (5, 4))]
    workerList = [("localhost", 5000), ("localhost", 5001), ("localhost", 5002)]

    sendTask(taskList, workerList)