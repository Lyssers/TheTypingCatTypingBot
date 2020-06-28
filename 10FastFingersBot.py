from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import time

#Enabling Extension Support:
#Change /q634iaqw.default-esr/ to your Firefox profile location
extensions = [
    "~/.mozilla/firefox/q634iaqw.default-esr/extensions/https-everywhere@eff.org.xpi", #HTTPS Everywhere
    "~/.mozilla/firefox/q634iaqw.default-esr/extensions/uBlock0@raymondhill.net.xpi", #Ublock Origin
    ]

#Going on 10FastFingers
firefox = webdriver.Firefox()
firefox.get('https://10fastfingers.com/typing-test/english')

#Installing Extensions
#Sometimes extensions disappear when navigating to a different URL, so we do it after we go to the website
#This can cause some ads to still display
for extension in extensions:
    firefox.install_addon(extension, temporary=True)

#Sleep so the website can load and not slow us down loading
time.sleep(5) #Seconds

# Using javascript to get the typing content from the website and storing value in "string" variable
string = firefox.execute_script('return document.querySelectorAll(".highlight")[0].innerHTML')

#Type the word, then type space for every word.
while string != "":
	string = firefox.execute_script('return document.querySelectorAll(".highlight")[0].innerHTML')
	print(string)
	
#Type the text!
	action = ActionChains(firefox)
	action.send_keys(string)
	action.perform()
	action = ActionChains(firefox)
	action.send_keys(Keys.SPACE)
	action.perform()
