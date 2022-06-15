import socket
import json
from collections import OrderedDict

com_socket = socket.socket()
com_socket.bind(('',2500))
com_socket.listen(10)


print('Waiting connection from client... ')

connection, address =com_socket.accept()
print(address," Connected........")		

data = OrderedDict()
while True:
    direction, height, type, warm = input('direction,height,type,warm :').split()

    data['moter'] = {'direction':direction,'height':height,'type':type} 
    data['warm'] = warm

    send_data = json.dumps(data) #dict형 송신 데이터를 JSON으로 직렬화
    print(connection.recv(1024).decode()) #bytes형 데이터를 문자열로 변환 출력
    connection.send(send_data.encode()) #문자열로된 직렬화 데이터를 bytes로 변환 후 전
