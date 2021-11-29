from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import json
import re
import time
import sys
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# op = webdriver.ChromeOptions()
# op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# op.add_argument("--headless")
# op.add_argument("--disable-dev-sh-usage")
# op.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

# Now you can start using Selenium
# driver.get("https://www.google.com")
# print(driver.page_source)
# driver.close()

driver.get("https://academic.ui.ac.id/")

username = driver.find_element(By.NAME, "u")
username.send_keys(sys.argv[1])

password = driver.find_element(By.NAME, "p")
password.send_keys(sys.argv[2])

login = driver.find_element(By.CSS_SELECTOR, "input[value='Login']")
login.click()

time.sleep(3)

driver.get("https://academic.ui.ac.id/main/Schedule/Index")

page_source = driver.page_source

driver.close()

cuts = []
        
for m in re.finditer('<table class="box">', page_source):
    cuts.append([m.start(), m.end()])

iter = 0
for m in re.finditer('</table>', page_source):
    cuts[iter][1] = m.end()
    iter += 1
    if iter >= len(cuts):
        break

filtered_page = ""
for i in range(len(cuts)):
    filtered_page += page_source[cuts[i][0]:cuts[i][1]]

regexDay = '([A-Za-z]+, [0-9]+.[0-9]+-[0-9]+.[0-9]+)'

soup = BeautifulSoup(filtered_page, 'html.parser')

courses = soup.find_all("tr")

elements = ""
   
for course in courses:
    selected = course.find("th")
    if selected is not None:
        if ";" in selected.text:
            elements += selected.text
            elements += "--------------"
    selected = course.find_all("td", nowrap="")
    if len(selected) > 0:
        for element in selected:
            elements += element.text + "\n"
        elements += "--------------"

with open("output.txt", "w") as file:
    file.write(str(elements))

listElements = elements.split("--------------")

courses = {}

temp = ""

for element in listElements:
    element = element.strip()
    if ";" in element and "-" not in element[:11]:
        temp = element[:11].strip()
        temp = temp.strip('\n')
        # print(temp)
        name = element[13:-28].strip()
        name = name.strip('\n')
        courses.update({
            temp : {
                'Nama' : name,
                'Kelas' : []
            }
        })
    elif temp != "":
        tempClass = element.split('\n')
        if (len(tempClass) > 1 and ';' in tempClass[1]):
            break
        elif len(tempClass) > 6 :
            courses[temp]['Kelas'].append({
                'Nama' : tempClass[1],
                'Jadwal' : re.findall(regexDay, tempClass[4]),
                'Ruang' : tempClass[5].strip("-"), 
                'Dosen' : tempClass[6].strip("- ").split("- ")
            })
        elif len(tempClass) > 5 :
            courses[temp]['Kelas'].append({
                'Nama' : tempClass[1],
                'Jadwal' : re.findall(regexDay, tempClass[4]),
                'Ruang' : tempClass[5].strip("-"), 
                'Dosen' : ''
            })
        elif len(tempClass) > 4 :
            courses[temp]['Kelas'].append({
                'Nama' : tempClass[1],
                'Jadwal' : re.findall(regexDay, tempClass[4]),
                'Ruang' : '', 
                'Dosen' : ''
            })
        elif len(tempClass) > 3 :
            courses[temp]['Kelas'].append({
                'Nama' : tempClass[1],
                'Jadwal' : '',
                'Ruang' : '', 
                'Dosen' : ''
            })
print(json.dumps(courses, indent=4))
        
with open("CoursePlan.json", "w") as file: 
    file.write(json.dumps(courses, indent=4))
