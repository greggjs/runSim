from os import system

class MPIExecutor:
    def __init__(self, num_nodes, host_list='/home/ubuntu/mpi_hosts'):
        self.num_nodes = num_nodes
        self.host_list = host_list

    def exec_sim(self, filename, args):
        cmd = 'mpiexec -n {0} --hostfile {1} ./{2}'.format(self.num_nodes, self.host_list, filename)
        for arg in args:
            cmd = cmd + " " + arg
        #print cmd
        system(cmd)

