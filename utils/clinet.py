def client():
    """this function for socket programming to recieving data from sarso.py"""
    import socket
    import json



    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.1.1", 8080))
        full_msg = ''
        while True:
            msg = s.recv(128)
            if len(msg) <= 0:
                break
            full_msg += msg.decode("utf-8")
            a = json.loads(full_msg)
            print(a)

if __name__ == '__main__':
    client()