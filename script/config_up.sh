#!/bin/bash

set -eu
trap "" ERR

echo "Please enter IP address or FQDN:"
read ip
if [ "${ip}" = "" ]; then
    echo "IP address or FQDN is not entered"
    exit 1
fi

regex_ip='^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
passphrase=""

get_ipaddr() {
     printf '%s' "$1" | python -c 'import socket,sys; print(socket.gethostbyname(sys.stdin.read()))'
}

if [[ ${ip} =~ ${regex_ip} ]]; then
    passphrase=${ip}
else
    # FQDN -> IP
    passphrase=`get_ipaddr ${ip}`
fi

echo "Please enter port number:"
read portNo
if [ "${portNo}" = "" ]; then
    echo "Port number is not entered"
   exit 1
fi

echo "Please enter user name:"
read userName
if [ "${userName}" = "" ]; then
    echo "User name is not entered"
    exit 1
fi

echo "Please enter password:"
read password
if [ "${password}" = "" ]; then
    echo "Password is not entered"
    exit 1
else
    password=`echo -n "${password}" | openssl enc -aes-256-cbc -e -base64 -pass pass:"${passphrase}"`
fi

echo "Please enter full path of certificate file:"
read certificate
if [ "${certificate}" = "" ]; then
    echo "full path of certificate file is not entered"
    exit 1
fi

json_escape () {
     printf '%s' "$1" | python -c 'import json,sys; print(json.dumps(sys.stdin.read()))';
}

if [[ "$BL_FILE" == "" ]]; then
  echo "[-] Missing blacklist file"
  usage
fi

# Hashes gather mode
if [ $nArgs -gt 2 ]; then
  if [[ "$INPUT_DIR" == "" || ! -e "$INPUT_DIR" ]]; then
    echo "[-] Missing or invalid input directory"
    usage
  fi

  if [[ "$FILE_EXT" == "" ]]; then
    echo "[-] Missing file extension"
    usage
  fi

  if [[ "$ARCH" != "MAC" && "$ARCH" != "LINUX" ]]; then
    echo "[-] Invalid architecture, expecting 'MAC' or 'LINUX'"
    usage
  fi

  if [[ "$ARCH" == "LINUX" ]]; then
    STACKHASH_FIELD=5
  elif [[ "$ARCH" == "MAC" ]]; then
    STACKHASH_FIELD=6
  else
    echo "[-] Unsupported architecture"
    exit 1
  fi
  gatherMode=true
fi

# Value escape
ip=`json_escape ${ip}`
portNo=`json_escape ${portNo}`
userName=`json_escape ${userName}`
password=`json_escape ${password}`
certificate=`json_escape ${certificate}`

echo \{\"ip\":${ip},\"portNo\":${portNo},\"credentials\":\{\"userName\":${userName},\"password\":${password}\},\"certificate\":${certificate}\} > ism_config.json

echo completed
exit 0
