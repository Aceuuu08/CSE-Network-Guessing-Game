import socket
import random

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections (maximum 5 queued connections)
server_socket.listen(5)
print('Server listening on port 12345...')

while True:
    clientsocket, address = server_socket.accept()
    print(f"Connection from {address} has been established.")
    
    
    secret_num = random.randint(1, 100)
    
    # Send a welcome message and request username input
    clientsocket.send("Welcome to the guessing game!\n".encode())
    username = clientsocket.recv(1024).decode().strip()
    
    # Send a request for password input
    password = clientsocket.recv(1024).decode().strip()
    
    # Check username and password
    if (username == "arvin" and password == "password") or (username == "serge" and password == "password"):
        clientsocket.send("Authentication successful!\n".encode())
        print(username + " is playing.....")
        # Game logic
        clientsocket.send("Guess a number between 1 and 100:".encode())
        times = 0
        while True:
            data = clientsocket.recv(1024).decode()
            guess = int(data)
            
            
            if guess < secret_num:
                response = "Too low, try again!"
                clientsocket.send(response.encode())
                times += 1
            elif guess > secret_num:
                response = "Too high, try again!"
                clientsocket.send(response.encode())
                times += 1

            else:
                response = "You guessed it! The number was " + str(secret_num)
                clientsocket.send(response.encode())
                times += 1

                break
        
        print(f"{username} won the game with {times} guess/es..... client logged out ")
        clientsocket.close()
    else:
        print(username + " is trying to login... closing client connection")
        clientsocket.send("Authentication failed!".encode())
        clientsocket.close()
