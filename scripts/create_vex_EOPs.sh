#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
OUTDIR=../templates/common_sections/

pushd $SCRIPT_DIR  2>&1 > /dev/null

./geteop.pl 2025-092  5 $OUTDIR/eop_e25c05.vex

popd  2>&1 > /dev/null

