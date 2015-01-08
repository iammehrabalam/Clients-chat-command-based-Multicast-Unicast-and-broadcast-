import socket
import time
from datetime import *

host="127.0.0.1"
port=5000

clients={}
clients_add=[]
l=0 # for broadcast

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((host,port))

s.setblocking(0)

print('Server started')

flag=False

while not flag:
    try:
        data,addr=s.recvfrom(1024)
        data=data.decode('utf-8')
        name,data=data.split(':;')
        name=str(name).strip().lower()
        choice,data=data.split('__')
        choice=int(choice)
        #print(choice,type(choice))
        if int(choice)==1:
                #print('here')
                client,data=data.split(':')
        elif int(choice)==2:
                m=data.split(':')
                l=len(m)
        if 'exit' in str(data).lower():
            flag=True
        if name not in clients:
            clients[str(name)]=addr
        if addr not in clients_add:
                clients_add.append(addr)
        if str(data).strip()!='' and str(data).strip().lower()!='exit':
                print(datetime.now().ctime()+str(addr)+' send by '+str(name))
                #print('here1')
                if int(choice)==1:
                        s.sendto(str.encode(str(name+' >>> ')+str(data)),clients.get(str(client)))
                elif int(choice)==2:
                        for i in range(l):
                                if m[i]!=m[l-1]:
                                        s.sendto(str.encode(str(name+' >>> ')+str(m[l-1])),clients.get(m[i]))
                else:
                        for client in clients_add:
                            if client!=addr:
                                    s.sendto(str.encode(str(name+' >>> ')+str(data)),client)
                                    #print(client,'send')
    except:
            pass

s.close()
        
