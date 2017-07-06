#pip3 install speedtest-cli

import os, platform
from time import gmtime, strftime
from subprocess import call
import os.path

host = "8.8.8.8"

def check_ping():
    times=strftime("%Y-%m-%d %H:%M:%S", gmtime())
    response = os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + host)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    pingstatus=times+", "+pingstatus+"\n"
    return pingstatus

####### CONNECTED TO INTERNET? #######
pings = check_ping()
#print pings
with open("ping.log", "a") as pinglogs:
    pinglogs.write(str(pings))
    pinglogs.close()

####### SECURE SPEEDTEST #######
if os.path.isfile("speedtest.log"):
    os.system('speedtest-cli --secure --csv >> speedtest.log')
else:
    os.system('speedtest-cli --csv-header >> speedtest.log')
    os.system('speedtest-cli --secure --csv >> speedtest.log')