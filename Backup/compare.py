import os
import sys
import paramiko
import time
import pdb
import pickle
from scp import SCPClient, SCPException


class Compare_result():
    def waitStrems(self,chan):
        time.sleep(1)
        outdata=errdata = ""
        while chan.recv_ready():
            outdata += str(chan.recv(1000))
        while chan.recv_stderr_ready():
            errdata += str(chan.recv_stderr(1000))
        return outdata, errdata
        
 

    def service_check(self,Cvendor,Cservice):
        if Cservice == "MSS":
            if Cvendor == "Backup_FG":
                Cresult="MSS_FG" 
                return Cresult
            elif Cvendor == "Backup_Axgate":
                Cresult="MSS_Axgate"
                return Cresult
            else:
                return "not search device"
        elif Cservice == "Maintain":
            if Cvendor =="Backup_FG":
                Cresult="Maintain_FG"
                return Cresult
            elif Cvendor == "Backup_Axgate":
                Cresult="Maintain_Axgate"
                return Cresult
            else:
                return "not search device"
        else:
            return "not search vendor"

    def SSH_Connection(self,host,id,pw,port_num,local_path):
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(host,username=id,password=pw,port=port_num, timeout=10)

            with SCPClient(ssh_client.get_transport()) as scp:
                scp.get("/sys_config", local_path)
                ssh_client.close()
                return True
        except SCPException:
            return False
        except:
            return False
             

    def SSH_Connection_Axgate(self,host,id,pw,port_num,local_path,cmd):
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(host,username=id,password=pw,port=port_num, timeout=10)

            channel = ssh_client.invoke_shell()
            channel.settimeout(30)        
            
            channel.send(pw+'\n')
            outdata, errdata = self.waitStrems(channel)
            print("\n")
            print(outdata)
            
            channel.send(cmd+'\n')
            outdata, errdata = self.waitStrems(channel)
            print("\n")
            print(outdata)

            channel.close()

        except Exception as e:
            print(e)
            return False   
       
        except:
            print("SSH_Connection Error")

    def SSH_SCPCheck(self,host,id,pw,port_num,cmd):
        print(host,id,pw,port_num)
        print("scpcheck")
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(host,username=id,password=pw,port=port_num,timeout=10)
        
            stdin, stdout, stderr = ssh_client.exec_command(cmd)
            lines = stdout.readlines()
            msg=""
            for s in lines:
                msg += s + " "
        
            result=msg.find("enable")
         
            if result<0:
                command="conf sys gl\nset admin-scp en\nend\n"
                stdin, stdout, stderr = ssh_client.exec_command(command)
                lines = stdout.readlines()
            else:
                print("SCP Enable") 

            ssh_client.close()

        except (paramiko.AuthenticationException, paramiko.ssh_exception.NoValidConnectionsError):
            print("Auth Fail")

        except:
            print("Compare Exception")


    def FileCheck(self,cmd,service,vendor,hostip):
        find=0
        file_check = open('/NAS/false_check.txt','a')
        if find != os.system(cmd):
            filecmd = service + " " + vendor + " " + hostip + "\n"
            file_check.writelines(filecmd)
        else:
            print("find!!!!")

        file_check.close



