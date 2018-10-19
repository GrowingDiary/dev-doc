安装系统时，设置的硬盘较小，另外一般工作环境，也不会与系统环境放在一起，所以我们通过挂载磁盘方式，增加磁盘空间，并设置工作环境。

# 1 创建虚拟硬盘

1. 关机已经打开的虚拟机；

2. 点击设置，并进入存储页面，并选择添加虚拟硬盘；

   ![](004_VirtualDisk_1.png)

3. 选择创建新的虚拟盘；

   ![](004_VirtualDisk_2.png)

4. 选择类型，并继续；

   ![](004_VirtualDisk_3.png)

5. 选择分配模式，并继续；

   ![](004_VirtualDisk_4.png)

6. 选择存储位置，并调整大小，点击创建；

   ![](004_VirtualDisk_5.png)

7. 创建成功；

   ![](004_VirtualDisk_6.png)

# 2 磁盘分区

1. 开机并登录系统；

   ![](004_VirtualDisk_7.png)

2. 查看当前磁盘信息；

   ![](004_VirtualDisk_8.png)

3. 操作对应的磁盘，输入 m 查看帮助；

   ![](004_VirtualDisk_9.png)

4. 支持的磁盘操作；

   ![](004_VirtualDisk_10.png)

5. 输入 p，查看当前分区；

   ![](004_VirtualDisk_11.png)

6. 输入 n，创建分区，选择主分区还是扩展分区，默认主分区；

   ![](004_VirtualDisk_12.png)

7. 选择磁盘分区在该硬盘中的序号；

   ![](004_VirtualDisk_13.png)

8. 磁盘起始位置；![](004_VirtualDisk_14.png)

9. 磁盘结束位置；![](004_VirtualDisk_15.png)

10. 创建分区结束，按 p 显示分区信息；![](004_VirtualDisk_16.png)

11. 输入 w，保存并退出；

    ![](004_VirtualDisk_17.png)

# 3 格式化分区

1. 格式化创建的分区，并等待格式化完成；

   ![](004_VirtualDisk_18.png)

# 4 挂载硬盘

1. 创建 `/data` 目录；

   ![](004_VirtualDisk_19.png)

2. 挂载硬盘到 `/data` 路径下；

   ![](004_VirtualDisk_20.png)

# 5 开机自动挂载硬盘

1. 编辑 `/etc/fstab` 文件；

   ![](004_VirtualDisk_21.png)

2. 在文件中，追加以下内容；

   ![](004_VirtualDisk_22.png)

3. 保存并退出；