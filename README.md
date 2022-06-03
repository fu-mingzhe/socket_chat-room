-Mywebsite
<br>

### 介绍

flask-简易的多功能网站


### 软件架构

<ul>
  <li>apps
    <ul>
      <li>filter        滤镜程序</li>
      <li>translate     翻译程序</li>
      <li>login         登录程序</li>
      <li>...           ......</li>
      <li>templates     模板文件</li>
      <li>static        资源文件</li>
    </ul>
  </li>
  <li>static
    <ul>
      <li>...           资源文件</li>
    </ul>
  </li>
  <li>main_app.py       主文件</li>
  <li>main_settings.py  配置文件</li>
  <li>requirements.txt  安装文件</li>
</ul>

### 安装教程

## 1.配置python环境
![在Linux系统中搭建Python编程环境](https://images.gitee.com/uploads/images/2022/0602/133209_f56fff00_11085717.png)
![在OS X系统中搭建Python编程环境](https://images.gitee.com/uploads/images/2022/0602/133507_c7ae974b_11085717.png)
![在Windows系统中搭建Python编程环境](https://images.gitee.com/uploads/images/2022/0602/133911_6229233a_11085717.png)
![在Windows系统中搭建Python编程环境](https://images.gitee.com/uploads/images/2022/0602/134117_8d93a067_11085717.png)
### [Python下载地址: http://https://www.python.org/downloads/](http://https://www.python.org/downloads/)
### 如果没有安装Python3请阅读以下内容
![安装Python3](https://images.gitee.com/uploads/images/2022/0602/151729_ebb87355_11085717.png)
![安装Python3](https://images.gitee.com/uploads/images/2022/0602/152102_c32b3147_11085717.png)
![安装Python3](https://images.gitee.com/uploads/images/2022/0602/152304_1d2ae3bf_11085717.png)
![安装Python3](https://images.gitee.com/uploads/images/2022/0602/152347_521974ac_11085717.png)
## 2.下载本项目
### 下载本项目
![下载本项目](https://images.gitee.com/uploads/images/2022/0602/135307_bb6f0c36_11085717.png)
### 解压文件
![解压文件](https://images.gitee.com/uploads/images/2022/0602/144839_76819853_11085717.png)
## 3.安装相关库
### 在项目文件目录下在终端运行如下命令
### `pip install -r requirements.txt`
### 最后输入后回车
![运行命令](https://images.gitee.com/uploads/images/2022/0602/145951_6c9f0f56_11085717.png)
## 4.配置下载Chrome浏览器并配置webdriver
### [Chrom浏览器下载地址: https://www.google.cn/chrome/index.html](https://www.google.cn/chrome/index.html)<br>
### 然后请查看Chrome浏览器的版本号
![查看Chrome浏览器的版本号](https://images.gitee.com/uploads/images/2022/0602/153900_d1063b57_11085717.png)
![查看Chrome浏览器的版本号](https://images.gitee.com/uploads/images/2022/0602/154038_78b43329_11085717.png)
### [chrom浏览器的web driver(chromedriver.exe)下载地址: https://registry.npmmirror.com/binary.html?path=chromedriver/](https://registry.npmmirror.com/binary.html?path=chromedriver/)<br>
### 选择对应自己Chrome浏览器版本的版本下载chromedriver.exe
![选择对应自己Chrome浏览器版本的版本下载chromedriver.exe](https://images.gitee.com/uploads/images/2022/0602/155001_5712e26b_11085717.png)
![选择对应自己Chrome浏览器版本的版本下载chromedriver.exe](https://images.gitee.com/uploads/images/2022/0602/155052_dc97977b_11085717.png)
### 解压文件
![解压文件](https://images.gitee.com/uploads/images/2022/0602/155240_675d7ff3_11085717.png)
### 配置chromedriver.exe
### 把chromedriver.exe放入Python安装文件夹的Scripts文件夹下
![把chromedriver.exe放入Python安装文件夹的Scripts文件夹下](https://images.gitee.com/uploads/images/2022/0602/160006_9741c03f_11085717.png)
![把chromedriver.exe放入Python安装文件夹的Scripts文件夹下](https://images.gitee.com/uploads/images/2022/0602/160030_01544c0b_11085717.png "3.PNG")
## 5.下载MongoDB数据库
### [MongDB下载地址: https://www.mongodb.com/try/download](https://www.mongodb.com/try/download)
### 选择配置后点击Download下载
![MongDB下载](https://images.gitee.com/uploads/images/2022/0602/164335_dfc9fbb5_11085717.png)
### 点击下载好的安装包
![点击下载好的安装包](https://images.gitee.com/uploads/images/2022/0602/164615_ba4c2ff6_11085717.png)
### 勾选同意
![勾选同意](https://images.gitee.com/uploads/images/2022/0602/164852_9a2faec1_11085717.png)
### 点击Custom
![点击Custom](https://images.gitee.com/uploads/images/2022/0602/165044_ccf83e63_11085717.png)
### 点击Browse可以修改软件的安装地址，然后点击Next
![点击Browse可以修改软件的安装地址，然后点击Next](https://images.gitee.com/uploads/images/2022/0602/165340_7183f550_11085717.png)
### 保持不变,点击Next
![保持不变,点击Next](https://images.gitee.com/uploads/images/2022/0602/165657_88b5db5a_11085717.png)
### 取消左下角的Install MongoDB Compass，点击Next
![取消左下角的Install MongoDB Compass](https://images.gitee.com/uploads/images/2022/0602/171046_a897f532_11085717.png)
### 再点击Install就可以下载了
![再点击Install就可以下载了](https://images.gitee.com/uploads/images/2022/0602/171238_b04e792c_11085717.png)
### 安装成功后如果运行代码报错你可以阅读以下内容（代码运行成功可跳过）
### 打开任务管理器（快捷键为Ctrl+Shift+Esc）
### 点击服务
![点击服务](https://images.gitee.com/uploads/images/2022/0602/173136_8e03c535_11085717.png)
### 按下键盘上的M键然后回车
![按下键盘上的M键然后回车](https://images.gitee.com/uploads/images/2022/0602/173425_f0151338_11085717.png)
### 如果状态为正在运行就右击它然后点重新启动，如果为已停止就开始
![点击](https://images.gitee.com/uploads/images/2022/0602/174025_d682ec3d_11085717.png)

# 注意 你需要完成安装教程的所有步骤才可以运行

## 使用说明
### 如要运行此项需要运行main_app.py
![运行](https://images.gitee.com/uploads/images/2022/0602/180135_6c9b45f1_11085717.png)
### 运行后在浏览器输入http://127.0.0.1:5656或http://{你的IP地址}:5656
### [运行后也可以点击此链接进入](http://127.0.0.1/)
![运行后在浏览器输入http://127.0.0.1:5656](https://images.gitee.com/uploads/images/2022/0602/180341_42c7a1ee_11085717.png)
### 第一次登录会显示: 您的账号未开通使用权限!请联系管理员~
![第一次登录会显示: 您的账号未开通使用权限!请联系管理员~](https://images.gitee.com/uploads/images/2022/0602/180704_5f81029c_11085717.png)
### 然后在浏览器输入http://127.0.0.1:5656/admin
### [也可以点击此链接进入](http://127.0.0.1/admin)
### 默认的管理员用户名为amdin，密码为123456
![管理员](https://images.gitee.com/uploads/images/2022/0602/180838_f1ab79bf_11085717.png)
### 请把你要开通使用权限的用户选中，然后点击提交
![请把你要开通使用权限的用户选中，然后点击提交](https://images.gitee.com/uploads/images/2022/0602/181100_4ca59e82_11085717.png)
## 其他说明
### 如果你不想使用默认的管理员用户名和密码，请打开项目的main_settings.py配置文件
![配置文件](https://images.gitee.com/uploads/images/2022/0602/171726_8121bf68_11085717.png)
### 然后你会看到如下代码
```
ADMIN_USER = {
    "admin","123456",
}
```
### 你可以更改为你想要的用户名和密码

```
ADMIN_USER = {
    "用户名":"密码",
}
```
### 它还支持多个用户

```
ADMIN_USER = {
    "用户名":"密码",
    "用户名":"密码",
    "用户名":"密码",
    ...............
}
```




### 参与贡献

# 如果有什么问题或建议可以发邮件给2372769798@qq.com

