#!/bin/bash

set -x
args=("$@")
PYTH=${args[0]}
HOST=${args[1]}

CMD="xvfb-run -a $PYTH/python"

#TESTS="share rm jsconsole services share_site_creators"
TESTS="share jsconsole cmis preview"

rm -rf /tmp/testres
mkdir -p /tmp/testres
for t in $TESTS
do
  $CMD test_$t.py
  if [ $? != 0 ] 
	then 
		echo " >>> $t FAIL"
		touch /tmp/testres/${t}_FAIL
	else
		echo " >>> $t PASS"
		touch /tmp/testres/${t}_PASS
	fi
done
