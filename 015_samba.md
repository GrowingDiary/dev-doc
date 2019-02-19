Samba 是在 Linux 和 UNIX 系统上实现 SMB 协议的一个免费软件，由服务器及客户端程序构成。

SMB（Server Messages Block，信息服务块）是一种在局域网上共享文件和打印机的一种通信协议，它为局域网内的不同计算机之间提供文件及打印机等资源的共享服务。

1. 安装 Samba 服务；

   `sudo apt-get install samba`

2. 添加系统用户 `share`；

   `sudo adduser share`

3. 为该用户创建 Samba 密码；

   `sudo smbpasswd -a share`

4. 修改 Samba 配置，设置更新目录；

   `sudo vi /etc/samba/smb.conf`

   ```
   [share]
      comment = Share
      path = /data/share
      public = yes
      writable = yes
      guest ok = no
      valid user = share
   ```

5. 重启 Samba 服务；

   `sudo service samba restart`



