
# coding: utf-8

# In[196]:


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from time import sleep


# In[199]:


path="C:\Program Files\chromedriver.exe"
browser=webdriver.Chrome(path) # creating the object 

browser.get("https://www.facebook.com/") #Opening the site
wait=WebDriverWait(browser,600) # site waits for 600 sec


# ### Login Page

# In[200]:


#Typing the email address or phone number
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

# In[202]:


#Clicking on the drop-down button
sleep(3)
theme = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[1]/span/div/div[1]")
theme.click()

#Selecting the dark mode
sleep(3)
dark = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/div/div/div/input")
dark.click()

#Unclicking the drop-down button
sleep(2)
unclick = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[1]/span/div/div[1]")
unclick.click()



# ### Posting Story

# In[219]:


sleep(3)
browser.maximize_window()
sleep(3)
story_login = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]/div/a/div/div/div/div[2]")
story_login.click()
sleep(3)

#Selecting the Text Story
text_story = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]")
text_story.click()
#Adding the text
sleep(3)
decription = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[3]/div/div[1]/div/label/div/div/textarea")
decription.click()
text = browser.find_element_by_tag_name("textarea")
sleep(1)
text.send_keys("This story was created using Selenium")
#Confirming the story
sleep(2)
send = browser.find_element_by_class_name("s1i5eluu")
send.click()


# ### Add a new post

# In[207]:


#Selecting the create post 
sleep(3)
create = browser.find_element_by_css_selector("#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.dp1hu0rb.j6ylrsjq > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pmt1y7k9.buofh1pr.g5gj957u.hpfvmrgz.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.f7vcsfb0.fjf4s8hc > div > div > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div.k4urcfbm.g5gj957u.buofh1pr.j83agx80.ll8tlv6m > div")
create.click()
sleep(2)

#Typing the message
text = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div")
text.send_keys("This post was created using Selenium")

#Sending the post
sleep(3)
send = browser.find_element_by_class_name('s1i5eluu')
send.click()


# ### Adding Bio for first time

# In[215]:


#Going to the profile page
sleep(3)
browser.maximize_window()
sleep(3)
browser.maximize_window()
profile = browser.find_element_by_link_text("Tejas")
profile.click()
sleep(3)

#Clicking the bio button
button = browser.find_element_by_css_selector("#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.ihqw7lf3.cddn0xzi > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.d1544ag0.tw6a2znq.discj3wi.b5q2rw42.lq239pai.mysgfdmx.hddg9phg > div > div > div.j83agx80.cbu4d94t.obtkqiv7.sv5sfqaa > div > span > span > div")
button.click()

#Typing the text in the textbox
sleep(3)
textbox = browser.find_element_by_css_selector("#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.ihqw7lf3.cddn0xzi > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.d1544ag0.tw6a2znq.discj3wi.b5q2rw42.lq239pai.mysgfdmx.hddg9phg > div > div > div.j83agx80.cbu4d94t.obtkqiv7.sv5sfqaa > div > span > div > div > label > textarea")
text = input("Enter the bio: ")
textbox.clear
if len(text)<=101:
    textbox.send_keys(text)
else:
    textbox.quit()

#Saving the bio    
sleep(2)
send = browser.find_element_by_css_selector("#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.ihqw7lf3.cddn0xzi > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.d1544ag0.tw6a2znq.discj3wi.b5q2rw42.lq239pai.mysgfdmx.hddg9phg > div > div > div.j83agx80.cbu4d94t.obtkqiv7.sv5sfqaa > div > span > div > div > div.aahdfvyu.i1fnvgqd.j83agx80.bp9cbjyn > div:nth-child(2) > div.oajrlxb2.s1i5eluu.gcieejh5.bn081pho.humdl8nn.izx4hr6d.rq0escxv.nhd2j8a9.j83agx80.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.d1544ag0.qt6c0cv9.tw6a2znq.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.l9j0dhe7.abiwlrkh.p8dawk7l.beltcj47.p86d2i9g.aot14ch1.kzx2olss.cbu4d94t.taijpn5t.ni8dbmo4.stjgntxs.k4urcfbm.tv7at329")
send.click()


# ### Sending a message to Messenger 

# In[203]:


#Clicking on the Messenger icon
sleep(3)
msg_icon = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[1]/div[2]/span/div/div[1]")
msg_icon.click()

#Searching for the person
sleep(3)
search = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/label/input")
search.click()

#Enter the person name
name = input("Enter the name: ")
search_bar = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/label/input")
search_bar.send_keys(name)

#Opening the chatbox
sleep(3)
tab = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/ul/div[1]/li/div/div[1]/div/div[2]/span")
tab.click()
sleep(2)

#Sending the message
message = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div")
message.send_keys("This message was sent using Selenium")
sleep(3)
send = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/span[2]/div")
send.click()


# ### Logout of the account

# In[209]:


sleep(3)
drop = browser.find_element_by_css_selector("#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div:nth-child(2) > div.n7fi1qx3.hv4rvrfc.b3onmgus.poy2od1o.kr520xx4.ehxjyohh > div.bp9cbjyn.j83agx80.rl25f0pe.byvelhso.l9j0dhe7.du4w35lb > span > div > div.oajrlxb2.tdjehn4e.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.j83agx80.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.l9j0dhe7.abiwlrkh.p8dawk7l.bp9cbjyn.s45kfl79.emlxlaya.bkmhp75w.spb7xbtv.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.taijpn5t.qypqp5cg.q676j6op")
drop.click()
sleep(2)
log_out = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[5]/div")
log_out.click()

