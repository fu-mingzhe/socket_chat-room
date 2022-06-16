

email_content = open("1.html",'r',encoding='utf-8').read()#.format(name="付明哲",Verification=749376)
template = Template(email_content)
template = template.render(name="付明哲",Verification=239642)

smtp_address = 'smtp.qq.com'
sender = '2372769798@qq.com'
password = "dttkrtttevtvdicg"
# receiver = ['250173585@qq.com','2372769798@qq.com']
receiver = ['2372769798@qq.com']
# f = open("1.mp4","rb")
# image_data = f.read()
# f.close()
# image = MIMEApplication(image_data)
# image.add_header('Content-Disposition','attachment',filename=('UTF-8','','Flask Web开发：基于Python的Web应用开发实战.mp4'))
# 
# string = '''
# <h1>我是付明哲</h1>
# <h3>下面是我给你发送的文件</h3>
# <img src='cid:img1'>
# '''
message = MIMEText(template,'html','utf-8')
multiMsg = MIMEMultipart()
multiMsg.attach(message)
# multiMsg.attach(image)
multiMsg['Subject'] = '[FMZ] 验证码'
multiMsg['From'] = sender
multiMsg['To'] = ';'.join(receiver)
content = multiMsg.as_string()
print(content)
server = smtplib.SMTP_SSL(smtp_address, 465)
server.login(sender, password)
server.sendmail(sender, receiver, content)
server.quit()