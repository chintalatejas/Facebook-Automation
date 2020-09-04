
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from time import sleep


# In[29]:


path="C:\Program Files\chromedriver.exe"
browser=webdriver.Chrome(path) # creating the object 

browser.get("https://www.facebook.com/") #Opening the site
wait=WebDriverWait(browser,600) # site waits for 600 sec


# ### Login Page

# In[30]:


#Typing the email address or phone number
sleep(5)
email_phone = browser.find_element_by_id('email')
email_address = input("Enter the email address or phone number: ")
email_phone.send_keys(email_address)

#Typing the password for the account
pwd = browser.find_element_by_id('pass')
password = input("Enter the password: ")
pwd.send_keys(password)

#Clicking the login button
sleep(2)
log = browser.find_element_by_id('u_0_b')
log.click()


# ### Enabling/Disabling Dark Mode

# In[6]:


#Clicking on the drop-down button
sleep(3)
theme = browser.find_element_by_xpath("//div[@aria-label='Account']")
theme.click()

#Selecting the dark mode
sleep(3)
dark = browser.find_element_by_xpath("//input[@aria-label='Enabled']")
dark.click()

#Unclicking the drop-down button
sleep(2)
unclick = browser.find_element_by_xpath("//div[@aria-label='Account']")
unclick.click()


# ### Posting Story

# In[7]:


sleep(3)
browser.maximize_window() #Maximize the browser window

#Create the story
sleep(3)
story_login = browser.find_element_by_link_text('Create a story').click()
sleep(3)

#Selecting the Text Story
text_story = browser.find_element_by_xpath("//div[@class='i1fnvgqd j83agx80']//div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l']")
text_story.click()

#Adding the text
sleep(3)
text = browser.find_element_by_tag_name("textarea")
sleep(1)
text.send_keys("This story was created using Selenium")

#Confirming the story
sleep(2)
send = browser.find_element_by_class_name("s1i5eluu")
send.click()


# ### Add a new post

# In[7]:


#Selecting the create post 
sleep(3)
create = browser.find_element_by_xpath("//div[@class='oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn orhb3f3m czkt41v7 fmqxjp7s emzo65vh btwxx1t3 buofh1pr idiwt2bm jifvfom9 ni8dbmo4 stjgntxs kbf60n1y']")
create.click()
sleep(2)

#Typing the message
text = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div")
text.send_keys("This post was created using Selenium")

#Sending the post
sleep(3)
browser.find_element_by_class_name('s1i5eluu').click()


# ### Adding Bio for first time

# In[11]:


#Going to the profile page
sleep(3)
browser.maximize_window()
sleep(3)
profile = browser.find_element_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn e72ty7fz qlfml3jp inkptoze qmr60zad btwxx1t3 tv7at329 taijpn5t']")
profile.click()
sleep(3)

#Clicking the bio button
button = browser.find_element_by_css_selector("#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.ihqw7lf3.cddn0xzi > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.d1544ag0.tw6a2znq.discj3wi.b5q2rw42.lq239pai.mysgfdmx.hddg9phg > div > div > div.j83agx80.cbu4d94t.obtkqiv7.sv5sfqaa > div > span > span > div")
button.click()

#Typing the text in the textbox
sleep(3)
textbox = browser.find_element_by_xpath("//textarea[@placeholder='Describe who you are']")
text = input("Enter the bio: ")
textbox.clear
if len(text)<=101:
    textbox.send_keys(text)
else:
    textbox.quit()

#Saving the bio    
sleep(2)
send = browser.find_element_by_xpath("//div[@aria-label='Save']")
send.click()


# ### Sending a message via Messenger

# In[14]:


#Clicking on the Messenger icon
sleep(3)
msg_icon = browser.find_element_by_xpath("//div[@aria-label='Messenger']")
msg_icon.click()

#Searching for the person
sleep(3)
search = browser.find_element_by_xpath("//input[@placeholder='Search Messenger']")
search.click()

#Enter the person name
name = input("Enter the name: ")
search_bar = browser.find_element_by_xpath("//input[@placeholder='Search Messenger']")
search_bar.send_keys(name)

#Opening the chatbox
sleep(3)
tab = browser.find_element_by_xpath("//div[@class='j83agx80 oo9gr5id buofh1pr ni8dbmo4 stjgntxs cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr']")
tab.click()
sleep(2)

#Sending the message
message = browser.find_element_by_xpath("//div[@class='notranslate _5rpu']")
message.send_keys("This message was sent using Selenium")
sleep(3)
browser.find_element_by_xpath("//div[@aria-label='Press Enter to send']").click()

#Closing the Chatbox
sleep(3)
browser.find_element_by_xpath("//div[@aria-label='Close tab']").click()


# ### Logout of the account

# In[28]:


sleep(3)
browser.find_element_by_xpath("//div[@aria-label='Account']").click()
sleep(2)
log_out = browser.find_element_by_xpath("//div[@class='knvmm38d']//div[5]//div[1]//div[1]//div[2]")
log_out.click()

#Closing the browser
sleep(3)
browser.quit()

