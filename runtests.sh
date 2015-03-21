#!/bin/bash
trap 'exit 9' ERR
set -x
CMD="sudo xvfb-run -a -e /dev/stdout python"

#TESTS="share rm jsconsole services share_site_creators"
TESTS="share rm jsconsole"

for t in $TESTS
do
  $CMD test_$t.py
  # actually the trap line at top should handle this
  # if errorlevel==9 then the trap got it, if 99 then this
  if [ $? != 0 ]; then exit 99; fi
done
