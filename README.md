#使用方法

###前提环境

需要保证安装有python2.7, java并且在命令行下能够直接执行aapt命令。

###配置渠道

编辑`all_channels`加入你想发布的渠道即可。

###发布

首先把需要发布的文件copy覆盖`test_data`下面的`crazysight.apk`， 然后执行`make`.  
完成之后，生成的apk会放在`release`文件夹下
