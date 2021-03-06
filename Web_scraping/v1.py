# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:22:20 2018

@author: jmajor
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

person_data = []

df = pd.read_csv('Pit_3_partial.csv')


lis = ('ContentPlaceHolder1_FormView1_NAMELabel','ContentPlaceHolder1_FormView1_ADDL1Label'
    ,'ContentPlaceHolder1_FormView1_ADDL2Label','ContentPlaceHolder1_FormView1_CITYLabel',
    'ContentPlaceHolder1_FormView1_STATELabel','ContentPlaceHolder1_FormView1_ZIPLabel')


options = Options()
#options.set_headless('True')
driver = webdriver.Chrome(r'chromedriver.exe',chrome_options=options)

start = time.time()

for num in df['number'][:10]:
    driver.get('http://pittsburg.okcountytreasurers.com/legal/parcel.aspx')
    box = driver.find_element_by_id('ContentPlaceHolder1_TextBox1')
    box.send_keys(num)

    button = driver.find_element_by_id('ContentPlaceHolder1_Button1')
    button.click()


    button2 = link = driver.find_element_by_link_text('Details')
    button2.click()

    time.sleep(.3)

    l = []
    for i in lis:

        data = link = driver.find_element_by_id(i)

        print(data.text)
        l.append(data.text)

    person_data.append(l)
    print('\n')

print(time.time() - start)




#duplicates
#caught = []
#for i in range(len(df['number'])):
#    for j in range(len(df['number'])):
#        if i != j and df['number'][i] == df['number'][j] and j not in caught:
#            print(df['number'][i], '\n'+ df['number'][j])
#            print(i,j)
#            print('\n')
#            caught.append(i)

#google search bar element. used class name. fixes error InvalidSelectorException: invalid selector: Compound class names not permitted
#put periods after each word in the class name
#driver.find_element_by_css_selector('.gLFyf.gsfi')



#webdriver.Chrome(r'chromedriver.exe',chrome_options=options)
#driver.get('https://wd5.myworkday.com/nrel/d/home.htmld')
#button = driver.find_element_by_css_selector('.wd-applet.wd-applet-time')
#button.click()
#button2 = driver.find_element_by_css_selector('.WIXM.WMXM.WBDO.WHXM.WGKN.WJYM')
#button2.click()