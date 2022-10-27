#!/usr/bin/env python

import hvac
import json
import tqdm
import time

class VaultClient:
    def __init__(self, vaultAddr, vaultToken):
        self.vaultAddr = vaultAddr
        self.vaultToken = vaultToken
        self.client = hvac.Client(url=self.vaultAddr, token=self.vaultToken)
 
        if not self.client.is_authenticated():
            raise Exception("Vault authentication error!")

    def kvList(self, mountPoint, path=None):
        result = []
        if not path:
            path = "/"
        secrets = self.client.secrets.kv.v2.list_secrets(mount_point=mountPoint, path=path)
        for secret in secrets['data']['keys']:
            if secret[-1:] == "/":
                result.extend(self.kvList(mountPoint, path+secret))
            else:
                result.append((path+secret)[1:])
        return result

    def getValue(self, mountPoint, path):
        value = self.client.secrets.kv.v2.read_secret(mount_point=mountPoint, path=path)
        return value['data']['data']

    def dumpKv(self, mountPoint, dumpFileName=None):
        result = {}
        if not dumpFileName:
            dumpFileName = '{}.json'.format(mountPoint)
        kvList = self.kvList(mountPoint)
        for kv in tqdm.tqdm(kvList):
            result[kv] = self.getValue(mountPoint, kv)
            time.sleep(0.01)
        with open(dumpFileName, 'w') as data:
            data.write(json.dumps(result))
        print('Dump kv to file {} completed.'.format(dumpFileName))

    def restoreKv(self, mountPoint, restoreFileName):
        with open(restoreFileName, 'r') as data:
            kvList = json.load(data)
        for k, v in tqdm.tqdm(kvList.items()):
            self.client.secrets.kv.v2.create_or_update_secret(mount_point=mountPoint, path=k, secret=v)
            time.sleep(0.01)
        print('Restore kv from file {} to {} completed.'.format(restoreFileName, mountPoint))

def processArgs(args):
    return args
