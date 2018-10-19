Ubuntu 18.04 已经默认安装了 Python 3.6 版本，但是 Ubuntu 14.04 等系统上，默认安装 Python 3.4 版本，如果需要更新 Python 版本的话，需要执行以下步骤。

``` sh
# 1. 删除系统自带的 Python 3 版本；
sudo apt-get autoremove python3

# 2. 增加 Python 源；
sudo add-apt-repository ppa:deadsnakes/ppa

# 3. 更新源；
sudo apt-get update

# 4. 安装 Python 3.6 版本；
sudo apt-get install python3.6

# 5. 建立 python3 链接；
sudo ln -s /usr/bin/python3.6 /usr/bin/python3

# 6. 下载 get-pip.py 脚本；
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# 7. 使用清华源（速度快）安装 pip；
sudo python3 get-pip.py -i https://pypi.tuna.tsinghua.edu.cn/simple
```

