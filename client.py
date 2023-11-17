import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('192.168.188.94', 12345))

# Receive the intro message from the server
print(client_socket.recv(1024).decode())

# Get username and password from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Send username and password to the server
client_socket.send(username.encode())
client_socket.send(password.encode())

# Receive the authentication response from the server
auth_response = client_socket.recv(1024).decode()
print(auth_response)

# Check if authentication was successful
if auth_response.startswith("Authentication successful"):
    print(client_socket.recv(1024).decode())

    while True:
        
        # Get user's guess
        guess = input("Enter your guess: ")
        
        # Send guess to the server
        client_socket.send(guess.encode())
        
        # Receive response from the server
        res = client_socket.recv(1024).decode()
        print(res)
        
        # Check if guess was correct
        if res.startswith("You"):
            break

    print("Game over!")
else:
    print("Closing connection")
    
