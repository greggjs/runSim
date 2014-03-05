from mpi4py import MPI
from subprocess import call

class MPIExecutor:
    def __init__(self, num_nodes, host_list='/home/ubuntu/mpi_hosts'):
        self.num_nodes = num_nodes
        self.host_list = host_list

    def exec_sim(self, filename, args):
        cmd = ['mpiexec','-n', self.num_nodes, '--hostfile', self.host_list]

        call(cmd)

