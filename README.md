# Vault Operation
Hashicorp Vault Operation toolkit.  Support kv2 list, get, dump and restore.

## Build
```
docker build -t vault-operation -f container/vault-operation/Dockerfile .
```

## Run
```
docker run -d --name vault-operation --rm vault-operation
```

## Usage
```
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
```  
