#!/usr/bin/env python

"""
List HashiCorps's Vault kv2 keys
Get HashiCorps's Vault kv2 value
Dumps from HashiCorps's Vault kv2 to json
Restore from dump file to HashiCorps's Vault kv2

Usage:
  pyvaultoperation kv2 list [-a=<vaultAddr>] (-t=<vaultToken>) (-p=<vaultPath>) [-s=<vaultSubPath]
  pyvaultoperation kv2 get [-a=<vaultAddr>] (-t=<vaultToken>) (-p=<vaultPath>) (-s=<vaultSubPath>)
  pyvaultoperation kv2 dump [-a=<vaultAddr>] (-t=<vaultToken>) (-p=<vaultPath>) [-f=<fileName>]
  pyvaultoperation kv2 restore [-a=<vaultAddr>] (-t=<vaultToken>) (-p=<vaultPath>) (-f=<fileName>)

Options:
  -h, --help                                           Show this screen.
  -a=<vaultAddr>, --vaultAddr=<vaultAddr>              Vault Server Address [default: https://127.0.0.1:8200]
  -t=<vaultToken>, --vaultToken=<vaultToken>           Vault Token
  -p=<vaultPath>, --vaultPath=<vaultPath>              Vault KV Path
  -s=<vaultSubPath>, --vaultSubPath=<vaultSubPath>     Vault KV SubPath
  -f=<fileName>, --fileName=<fileName>                 Dump or restore filename
"""

from docopt import docopt
import pyvaultoperation.kv2.common as common
import pprint

def list(args):
    args = common.processArgs(args)
    vaultClient = common.VaultClient(args["--vaultAddr"], args["--vaultToken"])
    secretList = vaultClient.kvList(args["--vaultPath"], args["--vaultSubPath"])
    pprint.pprint(secretList)

def get(args):
    args = common.processArgs(args)
    vaultClient = common.VaultClient(args["--vaultAddr"], args["--vaultToken"])
    value = vaultClient.getValue(args["--vaultPath"], args["--vaultSubPath"])
    pprint.pprint(value)

def dump(args):
    args = common.processArgs(args)
    vaultClient = common.VaultClient(args["--vaultAddr"], args["--vaultToken"])
    vaultClient.dumpKv(args["--vaultPath"], args["--fileName"])

def restore(args):
    args = common.processArgs(args)
    vaultClient = common.VaultClient(args["--vaultAddr"], args["--vaultToken"])
    vaultClient.restoreKv(args["--vaultPath"], args["--fileName"])
