树莓派是一款基于 ARM 的微型电脑主板，具备所有 PC 的基本功能。默认情况下其系统基于 Linux，可以在树莓派上安装一些简单的服务，提供访问。

# 1 安装系统

1. 从官网[下载页面](https://www.raspberrypi.org/downloads/)下载系统镜像文件；
2. 下载镜像烧录软件，Mac 上可以使用 [balenaEtcher](https://www.balena.io/etcher/)；
3. 将镜像烧录到 SD 卡上；
4. 将 SD 卡查到树莓派上，上电启动；

注意:

1. 树莓派默认情况下只支持从 SD 卡上启动系统；
2. 树莓派 3 及以上版本支持从 U盘启动系统，但是需要先用 SD 卡启动后修改 boot 参数；
3. 树莓派 3b+ 及以上版本支持 1000 Mbps 网卡；

# 2 U盘启动系统

可以通过外部 U盘或者 SSD 进入系统，三种情况下有对应的[系统速度测试](https://www.raspberrypi.org/forums/viewtopic.php?t=199414)，默认的 SD 卡速度最慢。

所以这里[使用 U盘启动系统](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md)（实际因为手头 U盘太多，SD 卡反而没几个）。

1. 使用 SD 卡进入系统；
2. 执行 `echo program_usb_boot_mode=1 | sudo tee -a /boot/config.txt` 写入配置；
3. 执行 `sudo reboot` 重启系统；
4. 执行 `vcgencmd otp_dump | grep 17:` 查看是否成功，成功结果应该为 `17:3020000a`；
5. 执行 `sudo poweroff` 关机，并断电；
6. 拔出 SD 卡，插入烧录好系统的 U盘，上电启动；
7. 进入 U盘系统；

# 3 设置键盘布局

默认情况下，键盘布局为英式键盘布局，而我们常用的是美式键盘布局，很多键位是不一样的，所以需要更改键盘布局。

1. 执行 `sudo raspi-config`；
2. 找到键盘布局更改选项，并执行；
3. 选择 Generic 101-key pc；
4. 选择 Other；
5. 选择国家为 English(US)；
6. 选择布局为 English(US)；
7. 选择 The default for the keyboard layout；
8. 选择 No compose key；
9. 执行 `sudo reboot` 重启系统；

# 4 打开 SSH

默认情况下，SSH 是关闭的，即不能远程登录，所以需要打开 SSH 以提供远程登录。

1. 执行 `sudo raspi-config`；
2. 找到 SSH 选项，选择打开；

# 5 配置 WiFi

1. 执行 `sudo raspi-config`；
2. 找到 WiFi 选项；
3. 输入 WiFi 名称和密码；

