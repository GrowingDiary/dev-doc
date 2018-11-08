1. 上传代码到服务器；

   ``` sh
   scp -C -r AutoNavSystem u@192.168.100.110:/data/workspaces/
   ```

2. 安装依赖库；

   ``` sh
   sudo pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql
   sudo pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pillow
   ```

3. 创建数据库；

   ``` sh
   mysql -uu -h127.0.0.1 -P3306 -pu -e "CREATE DATABASE IF NOT EXISTS AutoNavSystem DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;"
   ```

4. 配置数据库；

   ``` sh
   cd AutoNavSystem
   vi AutoNavSystem/settings.py
   
   # 修改数据库配置为以下内容：
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'AutoNavSystem',
           'USER': 'u',
           'PASSWORD': 'u',
           'HOST': '127.0.0.1',
           'PORT': '3306',
       }
   }
   ```

5. 应用生成数据库；

   ``` sh
   python3 manage.py migrate
   ```

6. 启动服务；

   ``` sh
   nohup python3 manage.py runserver 0.0.0.0:9000 &
   ```
