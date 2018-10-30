初始化环境，安装一些常用的工具，设置远程登录等。

# 1 配置 SSH

为了服务器的安全，一般需要关闭密码登录，使用证书登录。

## 1.1 生成证书

在本地机器（非虚拟机上），生成公钥和私钥。

按照以下步骤生成。

``` sh
# 1. 生成秘钥；
ssh-keygen -t rsa -b 4096 -C "your-email@email.com"

# 2. 出现以下提示后，输入对应文件名，以保存秘钥；
# Generating public/private rsa key pair.
# Enter file in which to save the key (/Users/name/.ssh/id_rsa): devops.pem
# Enter passphrase (empty for no passphrase):
# Enter same passphrase again:
# Your identification has been saved in devops.pem.
# Your public key has been saved in devops.pem.pub.
```

## 1.2 虚拟机增加公钥

将刚才生成的公钥，拷贝到虚拟机环境上。由于 VirtualBox 上不能进行复制粘贴，所以先使用密码登录服务器，配置好公钥访问后，再关闭密码登录。

按照以下步骤操作。

``` sh
# 1. ssh 登录虚拟机环境；
ssh u@192.168.100.110

# 2. 创建 authorized_keys 文件；
mkdir ~/.ssh
cd ~/.ssh
vi authorized_keys

# 3. 复制生成的公钥 devops.pem.pub 内容，并粘贴到 authorized_keys 文件后，保存并关闭；

# 4. 验证私钥登录；
ssh -i devops.pem u@192.168.100.110
```

## 1.3 关闭密码登录

按照以下步骤操作。

``` sh
# 1. 编辑 ssh 配置文件；
sudo vi /etc/ssh/sshd_config

# 2. 找到文件中 PasswordAuthentication 对应描述位置；

# 3. 修改 PasswordAuthentication 如下，并保存关闭文件；
PasswordAuthentication no

# 4. 重新加载配置；
sudo service ssh reload

# 5. 尝试密码登录失败；
ssh u@192.168.100.110
```

# 2 切换 apt 源

为了下载安装软件更方便，速度更快，我们往往在使用 Linux 系统时修改 apt 源为国内的源。这里更新为阿里云的源。

按照以下步骤更新源。

``` sh
# 1. 备份原有 source.list；
cd /etc/apt/
sudo mv sources.list sources.list.backup

# 2. 编辑 source.list；
sudo vi source.list

# 3. 输入以下内容；
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse

# 4. 更新源；
sudo apt update
```

# 3 Oh My Zsh

Shell 的类型有很多种，Linux 下默认的是 Bash，虽然 Bash 的功能已经很强大，但对于以懒惰为美德的程序员来说，Bash 的提示功能不够强大，界面也不够炫，并非理想工具。

而 ZSH 的功能极其强大，只是配置过于复杂，起初只有极客才在用。后来，有个穷极无聊的程序员可能是实在看不下去广大猿友一直只能使用单调的 Bash, 于是他创建了一个名为 [oh-my-zsh](https://ohmyz.sh/) 的开源项目。

按照以下步骤安装 oh-my-zsh。

``` sh
# 1. 安装 zsh；
sudo apt install zsh

# 2. 安装 oh-my-zsh;
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# 3. 配置加载环境；
sudo vi /etc/zsh/zprofile

# 4. 输入以下内容，加载 /etc/profile.d/*.sh 内容，保存退出；
if [ -d /etc/profile.d ]; then
  for i in /etc/profile.d/*.sh; do
    if [ -r $i ]; then
      . $i
    fi
  done
  unset i
fi

# 5. 加载配置；
source /etc/zsh/zprofile
```

安装好 oh-my-zsh 后，可以选择性安装一些插件，增强功能。

## 3.1 autojump

autojump 可以记录历史路径操作，快速进入某一个路径。

安装步骤如下：

``` sh
# 1. 安装 autojump；
sudo apt install autojump

# 2. 初始化 autojump；
source /usr/share/autojump/autojump.zsh

# 3. 在 oh-my-zsh 中增加配置；
vi ~/.zshrc

# 4. 找到 plugins 描述位置，修改为以下内容后，保存退出；
plugins=(git, autojump)

# 5. 重新加载配置；
source ~/.zshrc
```

使用时，只需要 `j data` 就可以跳转到历史中路径中包含 `data` 的路径中。
