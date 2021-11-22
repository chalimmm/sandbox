from bs4 import BeautifulSoup
import json
import re

regexDay = '([A-Za-z]+, [0-9]+.[0-9]+-[0-9]+.[0-9]+)'

with open("CoursePlan.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

courses = soup.find_all("tr")

elements = ""

with open("CoursePlan.json", "w") as file:    
    for course in courses:    
        selected = course.find_all("td", nowrap="")
        for element in selected:
            # link = element.find('a', target="_blank")
            # if link is not None:
            #     elements += str(link['title']) + "\n"
            elements += element.text + "\n"
    
    listElements = elements.split("\n\n\n")
    
    listElements = listElements[9:]
    
    courses = {}
    
    temp = ""
    
    for element in listElements:
        #print(element)
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

        else:
            tempClass = element.split('\n')
            
            if len(tempClass) > 1 and ';' in tempClass[1]:
                break
            
            if len(tempClass) > 6 :
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
    file.write(json.dumps(courses, indent=4))