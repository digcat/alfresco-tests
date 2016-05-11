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


if uname -a | grep "Ubuntu" ; then
	echo "Ubuntu"
	sudo apt-get install -y gcc python-dev libyaml-dev python-yaml git python-pip xvfb firefox
fi
if uname -a | grep "Centos" ; then
	echo "Centos"
	sudo yum install -y gcc python-dev libyaml-dev python-yaml git python-pip xvfb firefox
fi

echo "Build Virtual Environment"
sudo pip install --upgrade pip
sudo pip install virtualenv --upgrade
mkdir testing_virt ; cd testing_virt
virtualenv venv
source venv/bin/activate
venv/bin/pip install selenium --upgrade
venv/bin/pip install configure --upgrade
venv/bin/easy_install PyYAML
venv/bin/easy_install cmislib
cd $ROOT
#./runtests.sh ./testing_virt/venv/bin

