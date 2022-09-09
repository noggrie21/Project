from socket import *
import threading

port = 10000
name = "hi"
# disconnection_message = "연결이 비 정상적으로 종료된 소켓 발견"
my_name = 1


server_socket = socket(AF_INET, SOCK_STREAM)  # 소켓 정의
server_socket.bind(('', port))  # 서버가 정해진 포트번호로 지정된 소켓을 생성
server_socket.listen(5)  # 최대로 들어올 수 있는 소켓 갯수 지정

user_list = dict()  # 채팅 유저 관리를 위한 딕셔너리


def receive(client_socket, addr, user):
    while True:
        data = client_socket.recv(1024)  # 클라이언트 소켓에서 데이터 받아오기
        string = data.decode()  # 받아온 데이터는 비트로 인코딩되어 있기 때문에 디코딩하기

        if string == "/종료":
            message = f'{user.decode()}가 퇴장하셨습니다.'

            for con in user_list.values():
                try:
                    con.sendall(message.encode())
                except:
                    print("연결이 비 정상적으로 종료된 소켓 발견")

            print(message)
            break
        
        string = f'{user.decode()} : {string}'
        print(string)

        for con in user_list.values():
            try:
                con.sendall(string.encode())
            except:
                print("연결이 비 정상적으로 종료된 소켓 발견")

    del user_list[user]  # 채팅 서버를 나간 클라이언트는 딕셔너리에서 제거
    client_socket.close()  # 클라이언트 소켓 제거


while True:
    client_socket, addr = server_socket.accept()  # 클라이언트 소켓 정의
    user = client_socket.recv(1024)  # 처음 클라이언트 소켓이 정의되고 난 후 처음 받는 데이터
    user_list[user] = client_socket  # 유저 리스트에 유저 추가
    print(f'{user.decode()}가 입장하였습니다.')

    # 각각의 클라이언트 서버가 채팅을 따로 치기 위해 각 클라이언트로부터 데이터를 받고 보내는 부분은 스레드로 정의
    receive_thread = threading.Thread(
        target=receive, args=(client_socket, addr, user))
    receive_thread.start()
