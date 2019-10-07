#!/bin/bash

function rewrite_dockerfile()
{
  DOCKER_FILE=$1
  DOCKER_FILE_PATH=$(pwd)/${DOCKER_FILE}

  echo ${DOCKER_FILE_PATH}

  if [ ! -f ${DOCKER_FILE_PATH} ]; then
    echo "[ERROR] No such file or directory"
    exit 1
  fi

  if [ "$(cat ${DOCKER_FILE_PATH}) | grep microscanner" ]; then
    echo "" >> ${DOCKER_FILE_PATH}
    echo "RUN apk add --no-cache ca-certificates && update-ca-certificates" >> ${DOCKER_FILE_PATH}
    echo "ADD https://get.aquasec.com/microscanner ." >> ${DOCKER_FILE_PATH}
    echo "RUN chmod +x microscanner" >> ${DOCKER_FILE_PATH}
  fi

  cat ${DOCKER_FILE_PATH}
}

function main()
{
  rewrite_dockerfile $@
}

main $@
