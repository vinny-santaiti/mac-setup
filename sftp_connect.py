# connect to sftp server on linux with paramiko
# paramiko==2.8.1

import paramiko
ssh = paramiko.SSHClient()
key = paramiko.RSAKey.from_private_key_file("open_pp2.pem", "test_sftp_pw")
host_address='test_sftp_server_name.com'
username='test_sftp_username'
ssh.load_system_host_keys()
# https://docs.paramiko.org/en/stable/api/client.html#paramiko.client.SSHClient.load_system_host_keys

ssh.connect(hostname=host_address, username=username, pkey=key)

# paramiko.ssh_exception.SSHException: Server 'test_sftp_server_name.com' not found in #known_hosts
# $ ssh-keyscan test_sftp_server_name.com
# cat ~/.ssh/config

sftp = ssh.open_sftp()

# https://www.puttygen.com/#Download_PuTTYgen_for_Mac
# $ puttygen  key.ppk -O private-openssh -o open_pp.pem
# Enter passphrase to load key:
