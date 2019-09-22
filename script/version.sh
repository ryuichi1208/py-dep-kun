#!/bin/bash

if ! test "$revision"; then
    if (cd "$1" && grep git RELEASE 2> /dev/null >/dev/null) ; then
        revision=$(cd "$1" && git describe --tags --match N 2> /dev/null)
    else
        revision=$(cd "$1" && git describe --tags --always 2> /dev/null)
    fi
fi

version=$(cd "$1" && cat VERSION 2> /dev/null)
test "$version" || version=$revision

test -n "$3" && version=$version-$3

if [ -z "$2" ]; then
    echo "$version"
    exit
fi

NEW_REVISION="#define FFMPEG_VERSION \"$version\""
OLD_REVISION=$(cat "$2" 2> /dev/null | head -3 | tail -1)

GUARD=$(echo "$2" | sed 's/\//_/' | sed 's/\./_/' | tr '[:lower:]' '[:upper:]' | sed 's/LIB//')
