#!/usr/bin/env python

"""pyvaultoperation

vault operation toolkit

Usage:
  pyvaultoperation <module> <func> [<args>...]

Options:
  -h --help            Show this screen.
"""

from docopt import docopt
import sys
import pyvaultoperation.kv2
from pyvaultoperation.kv2 import *

def main():
    """
    run module
    example:
    pyvaultoperation tigerair <git_url> <version>
    """
    args = docopt(__doc__, options_first=True)
    module = args['<module>']
    func = args['<func>']
    argv = [module, func]+args['<args>']
    module_script = getattr(pyvaultoperation.kv2, module)
    module_args = docopt(module_script.__doc__, argv=argv)
    return getattr(module_script, func)(module_args)

if __name__ == '__main__':
    main()
