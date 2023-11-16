from struct import *
import socket
import binascii
import select


def socket_handling(conn):
    # Receive the 4st four bytes
    msg = conn.recv(8)

    type, length, message_id, operation = unpack_from("HHHH", msg, 0)

    padSize = 0
    if operation == 2:
        padsize = 2
    rest_of_msg = conn.recv(length + padSize - 4)

    if operation == 0:
        num1, num2, num3, num4 = unpack_from("HHHH", rest_of_msg, 0)
    elif operation == 1 or operation == 2 or operation == 4:
        num1, num2 = unpack_from("HH", rest_of_msg, 0)
    elif operation == 3:
        num1, num2, num3 = unpack_from("HHHxx", rest_of_msg, 0)

    # Response Code values
    # 0 : Wrong input for Mathematical opperation
    # 1 : everithing is correct
    # 2 : Integer values out of bounds
    res_code = 1
    # the calculations
    result = 0

    if operation == 0:
        if num1 <= 60000 and num2 <= 60000 and num3 <= 60000 and num4 <= 60000:
            result = num1 + num2 + num3 + num4
        else:
            res_code = 2
    elif operation == 1:
        if num1 <= 30000 and num2 <= 30000:
            result = num1 - num2
        else:
            res_code = 2
    elif operation == 2:
        if num1 <= 60000 and num2 <= 60000:
            result = num1 / num2
        else:
            res_code = 2
    elif operation == 3:
        if num1 <= 60000 and num2 <= 60000 and num3 <= 60000:
            result = num1 * num2 * num3
        else:
            res_code = 2
    elif operation == 4:
        if num1 <= 60000 and num2 <= 60000:
            result == num1 % num2
        else:
            res_code = 2
    else:
        res_code = 0

    print("Result: ", result)

    # done receiving now time to do calculations and send
    send_type = 1
    message = pack("HHIf", send_type, res_code, message_id, result)
    err = conn.sendall(message)

    # close = True
    # conn.close()
    # serverSocket.close()


serverIP = ""
serverPort = 12345
close = False


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((serverIP, serverPort))
    print("The server is ready to receive at port", str(serverPort))
    serverSocket.listen()

    incoming = [serverSocket]
    outgoing = []

    while not close:
        readable, writable, exceptional = select.select(incoming, outgoing, incoming)

        for s in readable:
            if s == serverSocket:
                conn, addr = serverSocket.accept()
                incoming.append(conn)
            else:
                try:
                    socket_handling(s)
                except:
                    incoming.remove(s)
