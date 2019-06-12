想要创建一个 HTTPS 的网站，需要以下几个步骤：

1. 一个域名；
2. 一个外网可以访问的服务器；
3. 一个认证的证书；

现在前两个条件，几乎很便宜，但是对于证书来说，还是不小的一笔花费。

好处是 Let's Encrypt 这个认证机构，可以提供期限是 90 天的免费证书，且可以无限次更新，所以能省则省，使用免费的资源来支持 HTTPS。

# 1 下载并初始化 Certbot

Certbot 是 Let's Encrypt 官方提供的工具，直接通过工具可以自动化生成证书。

``` sh
# 下载 Certbot
wget https://dl.eff.org/certbot-auto

# 设置为可执行程序
chmod a+x certbot-auto

# 移动到官方推荐目录下
sudo mv certbot-auto /usr/local/bin

# 修改用户及用户组
sudo chown root:root /usr/local/bin/certbot-auto

# 执行初始化
sudo certbot-auto
```

由于初始化需要安装很多 Python 的库，这个过程可能会比较漫长，如果需要，可以通过优化 Python 的源来进行加速。

``` sh
# 创建 pip 配置目录
sudo mkdir ~/.pip

# 创建 pip 配置
touch ~/.pip/pip.conf

# 输入以下内容到 pip.conf 中
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```

# 2 创建 Nginx 服务

在漫长的初始化过程中，可以先执行下一步操作。在生成证书时，一般有两种模式可以选择：

* webroot：在已有的 HTTP 服务中增加 HTTPS；
* standalone：帮助创建带有 HTTPS 的服务；

这里我们选择使用 webroot 模式，所以我们需要事先准备好一个 HTTP 服务。

``` sh
# 安装 Nginx
sudo apt install nginx

# 创建 HTTP Root 路径
sudo mkdir /var/www/winking

# 修改 Nginx 配置
sudo vi /etc/nginx/sites-enabled/default

# 将 root 修改为
root /var/www/winking;

# 保存配置，并重新加载
sudo systemctl reload nginx
```

# 3 创建 Certbot 配置

这个时候，Certbot 应该已经初始化完成了，可以生产证书文件了。

首先，我们创建 Certbot 的配置，来指导生产证书文件。

``` sh
# 创建配置文件路径
sudo mkdir -p /etc/letsencrypt/configs

# 创建配置文件，并编辑
sudo vi /etc/letsencrypt/configs/winking.io.conf

# 输入配置内容
domains = winking.io
rsa-key-size = 2048
email = your-email@example.com
text = True
authenticator = webroot
webroot-path = /var/www/winking
```

其中，webroot-path 是我们在上一步中创建的 HTTP Root 路径。在生成证书的过程中，Certbot 会在这个路径中自动生成一个文件，来进行验证域名配置的正确性。

# 4 生成证书

调用 Certbot，并根据配置来生成证书。

``` sh
sudo certbot-auto -c /etc/letsencrypt/configs/winking.io.conf certonly
```

运行顺利，则会在 `/etc/letsencrypt/live/winking.io/` 这个路径下，生成以下几个文件：

* cert.pem
* privkey.pem
* chain.pem
* fullchain.pem

# 5 配置 HTTPS

顺利生成证书后，我们需要将 Nginx 的 HTTP 服务，修改为 HTTPS 服务。

``` sh
# 修改 Nginx 配置文件
sudo vi /etc/nginx/sites-enabled/default

# 增加以下内容
listen 443 ssl default_server;
listen [::]:443 ssl default_server;
ssl_certificate /etc/letsencrypt/live/miai.winking.io/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/miai.winking.io/privkey.pem;

# 保存配置，并重新加载
sudo systemctl reload nginx
```

这样，就可以用 HTTPS 的方式打开你的网站了。

# 6 参考

* [LET'S ENCRYPT 给网站加 HTTPS 完全指南](https://ksmx.me/letsencrypt-ssl-https/)
* [部署Let’s Encrypt免费SSL证书&&自动续期](https://www.linuxidc.com/Linux/2017-03/142248.htm)
* [使用let's encrypt工具配置Nginx HTTPS](https://www.jianshu.com/p/3c67562b88a5)

