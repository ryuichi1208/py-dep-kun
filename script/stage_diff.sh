#!/bin/bash
tr '\n' '\001' | sed 's/\x01\x01/\x01 \x01/g' | sed 's/\x01\([^-+ @]\)/ \1/g' | tr '\001' '\n'
