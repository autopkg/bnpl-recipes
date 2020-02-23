#!/bin/zsh
#
# Extracts version information from an IzPack-installed application
#
# Params:
#     $1 - path to application
#
strings $1/.installationinformation | grep -A 1 "APP_VER" | grep -v "APP_VER" | cut -d t -f 1
