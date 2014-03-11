'''
-------------------------- runSim  ----------------------------

runSim is a CLI tool that allows the user to run a MUSE
Simulation on Miami OpenStack platform. It moves the
designated simulation file to the cloud and runs it with
the given parameters of the user.

@author:     Jake Gregg

@copyright:  2014 Miami University. All rights reserved.

@license:    license

@contact:    greggjs@miamioh.edu
@deffield    updated: Mar 5, 2014
'''
import sys
from sys import argv
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

# Simulation Packages
from transport import Transporter
from mpi import MPIExecutor

__all__ = []
__version__ = 1.0
__date__ = '2014-03-05'
__updated__ = '2014-03-05'


class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  runSim is a CLI tool that allows the user to run a MUSE
  Simulation on Miami OpenStack platform. It moves the
  designated simulation file to the cloud and runs it with
  the given parameters of the user.

  Created by Jake Gregg on %s.
  Copyright 2014 Miami University. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.



USAGE
''' % (program_shortdesc, str(__date__))

    # Setup argument parser
    parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('-V', '--version', action='version', version=program_version_message)
    parser.add_argument('--input', help="The executable to run.")
    parser.add_argument('--args', nargs='+', help='list of arguments to input for MUSE simulation. Remove all "-" and "--" in positional arguments.')
    parser.add_argument('--output', help='Designated output .asm file for the generated code to go. Defaults to output.asm')
    parser.add_argument('--shared-object', help='the shared-object file that the sim depends on')
    # Process arguments
    args = parser.parse_args()
    arguments = []
    for i, arg in enumerate(args.args):
        if i % 2 == 0:
            arguments.append('--'+arg)
        else:
            arguments.append(arg)

    t = Transporter()
    t.transport_file(args.input)

    if (args.shared_object):
        t.transport_file(args.shared_object)

    m = MPIExecutor(4)
    m.exec_sim(args.input, arguments)

if __name__ == "__main__":
    sys.exit(main())

