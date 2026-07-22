import subprocess
import sys
import time
from threading import Thread

inputs = []

count = 10
sitecount = 10
app = "./makecontent.py"
url = "https://localhost/alfresco/cmisatom"
update = "Y"

for i in range(0, sitecount):
    inputs.append("site" + str(i))

print(inputs)


def call_script(site, name, count, update):
    """
    Call makecontent.py script with parameters.
    SECURITY FIX: Uses subprocess with list arguments instead of shell=True
    to prevent command injection vulnerabilities.
    """
    # Use list of arguments instead of string concatenation
    # This prevents command injection attacks
    subprocess.call([sys.executable, app, site, name, str(count), update], shell=False)


START = time.time()
threadcount = 0

for i in inputs:
    # 	print i
    tn = "t" + str(threadcount)
    tn = Thread(target=call_script, args=(url, i, count, update))
    tn.start()
    threadcount = threadcount + 1
    if threadcount == len(inputs):
        tn.join()
# 	print "end " + i


END = time.time()
DURATION = END - START
print(str(int(round(DURATION / 60, 0))) + " mins " + str(int(round(DURATION % 60, 0))) + "secs")
