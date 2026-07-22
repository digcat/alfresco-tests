#!/bin/bash

cd "`dirname $0`"

ROOT=`pwd`

if [ -e config.yml ] ; then
	echo "Found local config.yml copy into test environment"
fi

if [ -e testing_virt ] ; then
	echo "Deleting Testing Virtual"
	sudo rm -rf testing_virt
fi


if [ -f /etc/debian_version ] ; then
	echo "Ubuntu"
	sudo apt-get install -y gcc python2.7 python2.7-dev libyaml-dev python-yaml git python-pip xvfb firefox python-simplejson
fi
if [ -f /etc/redhat-release ] ; then
	echo "Centos"
	sudo yum install -y gcc python-devel libyaml-dev python-yaml git python-pip xvfb firefox yum info xorg-x11-server-Xvfb python-simplejson
fi

echo "Build Virtual Environment"
sudo pip install --upgrade pip
sudo pip install virtualenv --upgrade
mkdir testing_virt ; cd testing_virt
virtualenv venv
source venv/bin/activate
venv/bin/pip install selenium --upgrade
venv/bin/pip install configure --upgrade
venv/bin/pip install PyYAML
venv/bin/pip install cmislib
venv/bin/pip install simplejson
cd $ROOT
./runtests.sh ./testing_virt/venv/bin

