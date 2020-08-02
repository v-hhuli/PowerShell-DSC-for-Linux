
print('Enter the SSH Server IP:')
hostinput = input()
host = hostinput
port = 22
username = "azureuser"
#password = "password"

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
OUTPUT