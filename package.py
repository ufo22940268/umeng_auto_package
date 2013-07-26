import os
from bs4 import BeautifulSoup
import subprocess

TEST_DIR = "test_data/";
RELEASE_DIR = "release/";

def compress(inFn, channels):
    if not channels:
        print "channels is empty";
        return;

    for channelIndex in range(len(channels)):
        channel = channels[channelIndex];
        apktoolCmd = "java -jar tools/apktool/apktool.jar ";
        if channelIndex == 0:
            cmd = apktoolCmd + " d --no-src -f %s test_data/temp" % (inFn,);
            os.system(cmd);

        outStr = None;
        with open("test_data/temp/AndroidManifest.xml", "r") as xmlFile:
            soup = BeautifulSoup(xmlFile, "xml");
            for meta in soup.find_all(u"meta-data"):
                if unicode(meta).find(u"UMENG_CHANNEL") != -1:
                    meta["android:value"] = channel;

            outStr = soup.prettify();

        with open("test_data/temp/AndroidManifest.xml", "w") as xmlFile:
            xmlFile.write(outStr);

        #Package to new apk.
        subprocess.check_call((apktoolCmd + " b %s/temp %s/unsign-a.apk" % (TEST_DIR, TEST_DIR)).split());

        jarSignCmd = "java -jar tools/SignApk.jar ";
        os.system(jarSignCmd + " 51zhangdan.keystore 69fcwireless 51zhangdan.keystore 69fcwireless %s/unsign-a.apk %s/%s.apk" % (TEST_DIR, RELEASE_DIR, channel.encode("utf-8")));

