https://www.influxdata.com/blog/getting-started-python-influxdb/
python3 -m pip install influxdb
python3 -m pip install beautifulsoup4
python3 -m pip install selenium


get lscpu output:

pi@raspberrypi:~/seleniumInstall $ lscpu
Architecture:          armv7l
Byte Order:            Little Endian
CPU(s):                4
On-line CPU(s) list:   0-3
Thread(s) per core:    1
Core(s) per socket:    4
Socket(s):             1
Model:                 5
Model name:            ARMv7 Processor rev 5 (v7l)
CPU max MHz:           900,0000
CPU min MHz:           600,0000
BogoMIPS:              38.40
Flags:                 half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm


/// WITH FIREFOX -----> No
install firefox Firefox 52.5.0:
sudo apt-get install firefox-esr

Download geckodriver v0.17.0 for ARM7:

wget -O geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-arm7hf.tar.gz

wget -O latest-hugo.zip Using Wget Command to Save the Downloaded File Under Different Name
wget -P /mnt/iso  Using Wget Command to Download a File to a Specific Directory

tar -xzf geckodriver.tar.gz


Install bs4:
pip3 install beautifulsoup4

Install selenium:
#pip3 install selenium==2.53.5
sudo python3 -m pip install selenium==2.53.5


/// WITH CHROMIUM -----> YEAH!
pi@raspberrypi:~/seleniumInstall $ lsb_release -a
No LSB modules are available.
Distributor ID: Raspbian
Description:    Raspbian GNU/Linux 9.13 (stretch)
Release:        9.13
Codename:       stretch


pip install selenium

Install the chromium webdriver from apt:
sudo apt install chromium-chromedriver
driver = webdriver.Chrome()

Or download the chromium driver from:
http://launchpadlibrarian.net/361669488/chromium-chromedriver_65.0.3325.181-0ubuntu0.14.04.1_armhf.deb
wget http://launchpadlibrarian.net/361669488/chromium-chromedriver_65.0.3325.181-0ubuntu0.14.04.1_armhf.deb

Install the deb:
sudo dpkg -i chromium-chromedriver_65.0.3325.181-0ubuntu0.14.04.1_armhf.deb
sudo apt-get install -f

It will install the driver to the path:
/usr/lib/chromium-browser/chromedriver
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')  # Optional argument, if not specified will search path.


- apk update
- wget "https://mirror.fsmg.org.nz/alpine/v3.9/community/armv7/libcouchbase-libevent-2.9.5-r1.apk"
- wget "https://mirror.fsmg.org.nz/alpine/v3.9/community/armv7/chromium-72.0.3626.121-r0.apk"
- wget "https://mirror.fsmg.org.nz/alpine/v3.9/community/armv7/chromium-chromedriver-72.0.3626.121-r0.apk"
- apk add --allow-untrusted libcouchbase-libevent-2.9.5-r1.apk
- apk add --allow-untrusted chromium-72.0.3626.121-r0.apk chromium-chromedriver-72.0.3626.121-r0.apk
