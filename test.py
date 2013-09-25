#coding:utf-8
import package
import file_util
import os

if __name__ == '__main__':

    os.system("rm -rf release/*")
    
    channels = file_util.getChannels()
    package.compress(u"test_data/crazysight.apk", channels)
