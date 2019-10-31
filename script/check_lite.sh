#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

find_files() {
  find . -not \( \
    \( \
      -wholename './vendor' \
      -o -wholename './pkg/proto' \
      -o -wholename '*testdata*' \
    \) -prune \
  \) \
  \( -name '*.go' -o -name '*.sh' -o -name 'Dockerfile' \)
}

if (( ${#failed_license_header[@]} > 0 )); then
  echo "Some source files are missing license headers."
  for f in "${failed_license_header[@]}"; do
    echo "  $f"
  done
  exit 1
fi

if (( ${#failed_copyright_header[@]} > 0 )); then
  echo "Some source files are missing the copyright header."
  for f in "${failed_copyright_header[@]}"; do
    echo "  $f"
  done
  exit 1
fi
