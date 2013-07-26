#coding:utf-8
import package
import file_util

if __name__ == '__main__':

    channels = file_util.getChannels();
    package.compress(u"test_data/51zhangdan-debug.apk", channels);
