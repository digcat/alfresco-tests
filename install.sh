#!/bin/bash

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
	sudo apt-get install libyaml-dev -y
	sudo apt-get install python-yaml -y
	sudo apt-get install git -y
fi
if uname -a | grep "Centos" ; then
	echo "Centos"
	sudo yum install libyaml-dev -y
	sudo yum install python-yaml -y
	sudo yum install git -y
fi

echo "Build Virtual Environment"
pip install virtualenv --upgrade
mkdir testing_virt ; cd testing_virt
virtualenv venv
source venv/bin/activate
venv/bin/pip install selenium --upgrade
venv/bin/pip install configure --upgrade
venv/bin/easy_install PyYAML
venv/bin/easy_install cmislib
venv/bin/easy_install nose multiprocessing
cd $ROOT
./runtests.sh ./testing_virt/venv/bin

