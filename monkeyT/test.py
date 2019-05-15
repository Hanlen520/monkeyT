import os
import re

os.system("adb devices")
content = os.popen('adb shell dumpsys activity  |findstr "mResumedActivity" ').read() #读取当前页面
pattern = re.compile(r'/[a-zA-Z0-9\.]+')
alist = pattern.findall(content)
print(alist[0])