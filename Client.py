from struct import *
import socket
import binascii
import ctypes
import random
import time


serverIP = "127.0.0.1"

serverPort = 12345


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((serverIP, serverPort))


for i in range(2):
    #  0               16                31
    #  +----------------+-----------------+
    #  |      Type      |      Length     |
    #  +----------------+-----------------+
    #  |       ID       |    operation    |
    #  +----------------+--------+--------+
    #  |       num1     |       num2      |
    #  +----------------+--------+--------+
    #  |       num3     | num4.. or | Pad |
    #  +----------------+--------+--------+

    #  0               16                31
    #  +----------------+-----------------+
    #  |      Type      |      Length     |
    #  +----------------+-----------------+
    #  |       ID       |    operation    |
    #  +----------------+--------+--------+
    #  |       num1     |       num2      |
    #  +----------------+--------+--------+

    # Create the data for the header
    message_type = 0
    message_id = random.randrange(1, 60000)

    operation = random.randrange(0, 5)

    packString = "HHHHHH"

    if operation == 0:  # Addition
        num1 = random.randrange(0, 60000)
        num2 = random.randrange(0, 60000)
        num3 = random.randrange(0, 60000)
        num4 = random.randrange(0, 60000)

        # Total length in bytes with no pading
        length = 4 * 4

        packString = packString + "HH"

        message = pack(
            packString,
            message_type,
            length,
            message_id,
            operation,
            num1,
            num2,
            num3,
            num4,
        )
    elif operation == 1:  # Deduction
        num1 = random.randrange(0, 30000)
        num2 = random.randrange(0, 30000)

        # Total length in bytes with no pading
        length = 3 * 4

        message = pack(
            packString, message_type, length, message_id, operation, num1, num2
        )
    elif operation == 2 or operation == 4:  # Division or modulo
        num1 = random.randrange(0, 60000)
        num2 = random.randrange(0, 60000)

        # Total length in bytes with no pading
        length = 3 * 4

        message = pack(
            packString, message_type, length, message_id, operation, num1, num2
        )
    elif operation == 3:
        num1 = random.randrange(0, 60000)
        num2 = random.randrange(0, 60000)
        num3 = random.randrange(0, 60000)
        # Total length in bytes with no pading
        length = 3 * 4 + 2
        packString = packString + "Hxx"
        message = pack(
            packString, message_type, length, message_id, operation, num1, num2, num3
        )

    # Send the message through the socket
    clientSocket.sendall(message)

    #  0               16                31
    #  +----------------+-----------------+
    #  |      Type      |  Response Code  |
    #  +----------------+-----------------+
    #  |               ID                 |
    #  +----------------+--------+--------+
    #  |              Result              |
    #  +----------------+--------+--------+

    ServerMessage = clientSocket.recv(12)

    # Unpack the message
    msg_type, msg_response_code, Response_id, result = unpack("HHIf", ServerMessage)

    #  Operation numbers
    #  Addition       : 0
    #  Deduction      : 1
    #  Division       : 2
    #  Multiplication : 3
    #  Modulo         : 4

    if Response_id == message_id:
        print("Operation: ", operation)
        if msg_response_code == 0:
            print("Response code is 0: Wrong spelling of the mathematical opperation")
        elif msg_response_code == 1:
            print("The result is: ", result)
        elif msg_response_code == 2:
            print("Response code is 2: Integer values are out of bounds")
    else:
        print("This is not the right response")

    time.sleep(5)

clientSocket.close()
