#!/bin/bash

CWD=$(dirname $(readlink -f $0))
PYTHON=$CWD/env/bin/python

export DRIVE_BACKUPS_LIST=$CWD/backup.cfg

$PYTHON $CWD/backup.py
