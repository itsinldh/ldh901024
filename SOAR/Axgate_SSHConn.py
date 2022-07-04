import os
import sys
import re
import subprocess
import paramiko
import time

from datetime import datetime


class getstart():

    def run_getstart(self, args):

        datetime.today()
        lyear=datetime.today().year
        lmonth=datetime.today().month

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("183.111.67.58", username="axroot", password="2022Dlcmdls!@", port=2222)
            
            channel = ssh.invoke_shell()
            
            #cmds = [self.mPassword, "conf t","security zone untrust ip group G_%s/%s_BlockIP" % (lyear, lmonth),"address %s/32" % srcIpAddr,"end","wr"]
            
            out = channel.recv(9999)
            channel.send("2022Dlcmdls!@\n")  
            
            while not channel.recv_ready():
                time.sleep(3)
                
            out = channel.recv(9999)
            print(out.decode("utf-8"))
            
        
            channel.send("ping 8.8.8.8 count 5\n")  
            
            while not channel.recv_ready():
                time.sleep(3)
              
            time.sleep(2)
            out = channel.recv(9999)
            print(out.decode('utf-8'))
            
            ssh.close() 
        
        except Exception as e:
            print("Except: " + str(e))
            
            #if find == os.system(findfile):
            #    print("find")
            #else:
            #    file_check.writelines(lfilename) 

        except:
            print("Unknown Exception")
            
        
        
    


if __name__ == "__main__":
    getssluser = getstart()
    getssluser.run_getstart(sys.argv)

