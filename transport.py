from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

class Transporter:
    def __init__(self, host_list='/home/ubuntu/mpi_hosts'):
        self.hosts = []
        for host in open(host_list, 'r'):
            self.hosts.append(host.rstrip())

        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
    def transport_file(self, filename):
        for host in self.hosts:
            self.ssh.connect(host)
            scp = SCPClient(self.ssh.get_transport())
            scp.put(filename, filename)
            print 'Successfully transported {0} to {1}'.format(filename, host)
