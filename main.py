from numpy import record
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas
#import xlrd


driver = webdriver.Firefox()
driver.get("http://ofb.net/misofb/mis.html")
username_element = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/div[3]/table/tbody/tr[1]/td/input")
username_element.send_keys("sysadmin.cfa")

password_element = driver.find_element_by_name("passwd")
password_element.send_keys("aipr@2018")


#login button
driver.find_element_by_xpath("//input[@type='submit']").click()



#read excel file
data=pandas.read_excel("NIC.xlsx",sheet_name='Test', usecols=['perno','First_Name','Last_Name','Designation','Section','Category','Group','DOB','DOR','Phone'])

#change the data into a python dictionary
data_dict = data.to_dict(orient = 'records')

#loop through the excel data and assign field values
for d in data_dict:

    #new nic email application form link
    driver.get("http://ofb.net/misofb/nicapp/addaplication.php")

    #option: Group B (Non-Gazetted) (for SPARROW only)
    driver.find_element_by_xpath("/html/body/div/form/div/div/table/tbody/tr/td[1]/input[1]").click()

    #Next Button
    driver.find_element_by_xpath("/html/body/div/form/div/div/table/tbody/tr/td[2]/input").click()

    perno = d['perno']
    f_name = d['First_Name']
    l_name = d['Last_Name']
    desg = d['Designation']
    sec = d['Section']
    cat = d['Category']
    group = d['Group']
    # date of birth
    dob = d['DOB']
    # date of retirement
    dor = d['DOR']
    phone = d['Phone']
    # mail = d['mail']
    
    print(dob.date())    
    #convert date to string
    print(str(dob.date()))

    #select box for sparrow purpose
    driver.find_element_by_xpath("/html/body/div/form/div/div[1]/div[4]/div/select/option[5]").click()

    #enter the various field data
    driver.find_element_by_xpath("/html/body/div/form/div/div[1]/div[5]/div/input").send_keys(perno)
    driver.find_element_by_xpath("/html/body/div/form/div/div[1]/div[6]/div/input").send_keys(f_name)
    driver.find_element_by_xpath("/html/body/div/form/div/div[1]/div[8]/div/input").send_keys(l_name)
    driver.find_element_by_xpath("/html/body/div/form/div/div[1]/div[9]/div/input").send_keys(desg)
    


    driver.find_element_by_xpath("/html/body/div/form/div/div[1]/div[12]/div/input").send_keys(sec)
    driver.find_element_by_xpath("/html/body/div/form/div/div[1]/div[13]/div/input").send_keys(phone)
    driver.find_element_by_xpath("/html/body/div/form/div/div[1]/div[14]/div/input").send_keys(phone)
    driver.find_element_by_xpath("/html/body/div/form/div/div[1]/div[15]/div/input").send_keys("GM")


    # enter date of birth after making the read only field writable
    dob_el = driver.find_element_by_xpath('//*[@id="dob"]')
    # enable read only input, and enter new value
    driver.execute_script("arguments[0].readonly=false;",dob_el)    
    driver.execute_script("arguments[0].value='"+str(dob.date())+"';",dob_el) 

    # enter date of retirement after making the read only field writable
    dor_el =  driver.find_element_by_xpath('//*[@id="dor"]')
    driver.execute_script("arguments[0].readonly=false;",dor_el)    
    driver.execute_script("arguments[0].value='"+str(dor.date())+"';",dor_el) 

    
    # click on next button
    driver.find_element_by_xpath("/html/body/div/form/div/div[1]/nav/ul/li[1]/button").click()
    #click on save button
    driver.find_element_by_xpath("/html/body/div/form/div/div[2]/nav/ul/li[1]/button").click()
    # accept alert prompt
    alert = Alert(driver)
    alert.accept()
    # Alert alert = driver.switchTo().alert();
    # WebDriverWait(driver, 10).until(EC.alert_is_present())
    # driver.switch_to.alert.accept()