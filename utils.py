import socket
import pickle

def pickler(obj):
    """Serialize an arbitrary object using pickle"""
    return pickle.dumps(obj)

def unpickler(obj):
    """Deserialize an arbitrary object using pickle"""
    return pickle.loads(obj)

def clientSetup(serverAddress = ('localhost', 12345)):
    """
    Setup a client socket and connect to the server
    Default value of parameter "serverAddress" is ('localhost', 12345)
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(serverAddress)
    return client_socket

def serverSetup(serverAddress = ('localhost', 12345)):
    """
    Setup a server socket and start listening for connection requests
    Default value of parameter "serverAddress" is ('localhost', 12345)
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(serverAddress)
    server_socket.listen(1)
    return server_socket

def doMath(x, y):
    """Perform operation x^2 - y with two parameters x and y"""
    return (x ** 2) - y