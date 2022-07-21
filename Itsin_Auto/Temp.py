import csv
import os
import sys
import re
import subprocess
import paramiko
import time


class getstart():

    def run_getstart(self, args):
        """
        with open(r'C:\\Users\ldh\Documents\sslusers.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            array2d = list(csv_reader)

        f = open("inputcli.txt", "w")
        """
        array = []
        array.append([])
        arraynum = 0

        for line in array2d:
            list_len = len(line)
            num = 0

            if line is not None:
                Tempstr = line[num]
                array.append([])
                array[arraynum].append(line[num])
                array[arraynum].append(line[num + 1])
                array[arraynum].append(line[num + 2])
                array[arraynum].append(line[num + 3])
                arraynum = arraynum + 1
            else:
                break

            num = num + 1

            if Tempstr is None:
                break

            if num >= list_len:
                break

            arraylen = len(array)
            # print(array)
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect("172.16.21.1", username="itsadmin", password="2022Dlcmdls!@", port="22", timeout=10)

            cli="config system firewall\n sh"
            stdin, stdout, stderr = ssh_client.exec_command(cli)
            lines = stdout.readlines()
            print(lines)
            time.sleep(1)

            """
            for user, pw, email, group in array:
                f.write("edit {t_user}\n".format(t_user=user))
                f.write("set passwd {t_pw}\n".format(t_pw=pw))
                f.write("set email_to {t_email}\n".format(t_email=email))
                f.write("next\n")

                cli0 = "config user local\nedit {t_user}\nset passwd '{t_pw}'\nset email-to '{t_email}'\nend\n".format(
                    t_user=user, t_pw=pw, t_email=email)
                cli1 = "edit {t_user}".format(t_user=user)
                cli2 = "set passwd {t_pw}".format(t_pw=pw)
                cli3 = "set email_to {t_email}".format(t_email=email)
                cli4 = "end"

                stdin, stdout, stderr = ssh_client.exec_command(cli0)
                lines = stdout.readlines()
                time.sleep(1)

                # stdin, stdout, stderr = ssh_client.exec_command(cli1)
                # lines = stdout.readlines()
                # stdin, stdout, stderr = ssh_client.exec_command(cli2)
                # lines = stdout.readlines()
                # stdin, stdout, stderr = ssh_client.exec_command(cli3)
                # lines = stdout.readlines()
                # stdin, stdout, stderr = ssh_client.exec_command(cli4)
                # lines = stdout.readlines()

                print(lines)
            """
            ssh_client.close()


        except Exception as e:
            print("Except: " + str(e))

            # if find == os.system(findfile):
            #    print("find")
            # else:
            #    file_check.writelines(lfilename)

        except:
            print("Unknown Exception")

        #f.close()


if __name__ == "__main__":
    getssluser = getstart()
    getssluser.run_getstart(sys.argv)
