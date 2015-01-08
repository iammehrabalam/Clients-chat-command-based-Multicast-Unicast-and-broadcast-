import socket
import threading
import datetime

lock=threading.Lock()

down=False

def receving(name,sock):
    while not down:
        try:
            lock.acquire()
            while True:
                data,addr=sock.recvfrom(1024)
                print('\n'+str(data.decode('utf-8'))+'\n')
        except:
            pass
        finally:
            lock.release()

host='127.0.0.1'
port=0

server=('127.0.0.1',5000)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

rt=threading.Thread(target=receving,args=("RecvThread",s))
rt.start()

name=input('Enter Name:: ')
mess=''
while str(mess).lower()!='exit':
            if str(mess).strip()!='':
                if int(choice)!=3:
                    m=name+':;'+str(choice)+'__'+str(clint)+':'+str(mess)
                else:
                    m=name+':;'+str(choice)+'__'+str(mess)
                s.sendto(str.encode(m),server)
            lock.acquire()
            choice=(input(name+'>>'+' Press 1 for Unicast\n\tPress 2 for Multicast\n\tPress 3 for Broadcast\n\tPress Enter for Refresh\n\tPress 0 for exit\n\tEnter your choice:: '))
            try:
                    if int(choice)==1:
                        clint=input('\tEnter Client name:: ')
                        mess=input('Me>> ')
                    elif int(choice)==2:
                        clint=input('\tEnter Clients name (colon): seperated:: ')
                        mess=input('Me>> ')
                    elif int(choice)==3:
                        mess=input('Me>> ')
                    elif int(choice)==0:
                        mess='exit'
                    else:
                        mess=''
            except:
                    mess=''
        
            lock.release()
down=True
rt.join()
s.close()
