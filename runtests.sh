#!/bin/bash
trap 'exit 1' ERR
set -x
sudo xvfb-run python test_share.py
if [ $0 != 0 ]; then exit 99; fi
sudo xvfb-run python test_rm.py
if [ $0 != 0 ]; then exit 99; fi
sudo xvfb-run python test_jsconsole.py
if [ $0 != 0 ]; then exit 99; fi
#xvfb-run python test_services.py
#xvfb-run python test_share_site_creators.py
