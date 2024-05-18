import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# 指定GeckoDriver路径
gecko_driver_path = 'C:\\Users\\unzip\\scoop\\apps\\firefox\\current\\geckodriver.exe'  
# 请替换为你的GeckoDriver路径

# 设置Firefox选项（可选）
firefox_options = Options()
# 可以设置无头模式（Headless），即不显示浏览器窗口
# firefox_options.add_argument('--headless')

# 创建GeckoDriver服务
service = Service(gecko_driver_path)

# 创建Firefox浏览器实例
driver = webdriver.Firefox(service=service, options=firefox_options)

# 打开一个网页
driver.get('http://10.0.100.3/')


my_username = 'LTB20210304319'
my_password = '230635'
cnt = 0 # 允许最多连5次


while True:
    # 判断是否已经成功连接
    msg = driver.find_element(By.NAME, "PageTips")
    if msg.text == '您已经成功登录。' or msg.text == 'You have successfully logged into our system.' :
        print("Success")
        break

    # 重复登录5次，登录不上则抛给上层
    if cnt == 5:
        print("Failure")
        break
    
    f3_elements = driver.find_elements(By.CLASS_NAME, "edit_lobo_cell");

    username = f3_elements[1]
    password = f3_elements[2]
    login_button = f3_elements[0]
    # 找到密码输入框并输入密码
    username.send_keys(my_username)
    password.send_keys(my_password)
    time.sleep(1)
    # 找到登录按钮并点击
    login_button.click()
    

    f1_elements = driver.find_elements(By.CLASS_NAME, "edit_lobo_cell");
    msg = f1_elements[0]
    back_button = f1_elements[1]

    if msg.text == 'Access Server authentication failure':
        back_button.click()
    elif msg.text == '您已经成功登录。' or msg.text == 'You have successfully logged into our system.':
        print("Success")
        break
    else:
        cnt = cnt + 1
    time.sleep(2)
# 关闭浏览器
driver.quit()
