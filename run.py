from python_class import lesson_01
from test_data import test_date
from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = test_date.url["url"]  # 取值 url
user = test_date.login_date["username"] # 取值登录用户名
pwd = test_date.login_date["password"] # 取值 登录的密码
s_key = test_date.s_key["s_key"] # 取值 搜索的 关键字
print(url,user,pwd,s_key)
result = lesson_01.search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)
if s_key in result:
    print("搜索结果是正确的！")
else:
    print("用例测试不通过！")