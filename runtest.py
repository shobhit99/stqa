from selenium import webdriver
from selenium.webdriver.support.ui import Select
import sys

if len(sys.argv) == 1:
    print("Please provide module parameter for testing register/view")
    print("e.g python runtest.py register")
    sys.exit()

def register():
    values = open("register.txt","r").readlines()
    outfile = open("output_register.txt","w")
    output = []
    for index, record in enumerate(values):
        driver.get("http://medicalrecords.rf.gd/index.php")
        data = record.rstrip("\n").split(";")
        firstname, lastname, email, mobileno, address, password, repeatpassword, gender, blood_g, dob = data
        driver.find_element_by_name("firstname").send_keys(firstname)
        driver.find_element_by_name("lastname").send_keys(lastname)
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("mobileno").send_keys(mobileno)
        driver.find_element_by_name("address").send_keys(address)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("repeat_password").send_keys(repeatpassword)
        driver.find_element_by_name("dob").send_keys(dob)
        gender_select = Select(driver.find_element_by_name('gender'))
        gender_select.select_by_value(gender)
        blood_select = Select(driver.find_element_by_name('blood_group'))
        blood_select.select_by_value(blood_g)
        driver.find_element_by_name("register").click()
        message = driver.find_element_by_name("message").text
        print("Test Case {} Output : {}".format(index+1, message))
        outfile.write("Test Case {} Output : {}\n".format(index+1, message))
    outfile.close()

def view():
    values = open("view.txt","r").readlines()
    outfile = open("output_view.txt","w")
    output = []
    for index, record in enumerate(values):
        driver.get("http://medicalrecords.rf.gd/view.php")
        data = record.rstrip("\n").split(";")
        email, password = data
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("view").click()
        message = driver.find_element_by_name("msg").text
        print("Test Case {} Output : {}".format(index+1, message))
        outfile.write("Test Case {} Output : {}\n".format(index+1, message))
    outfile.close()

module = sys.argv[1]
driver = webdriver.Firefox()

if module == "register":
    register() 
elif module == "view":
    view()
else:
    print("Invalid module")