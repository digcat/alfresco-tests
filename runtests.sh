trap 'exit 1' ERR
set -x
sudo xvfb-run python test_share.py
sudo xvfb-run python test_rm.py
sudo xvfb-run python test_jsconsole.py
#xvfb-run python test_services.py
#xvfb-run python test_share_site_creators.py
