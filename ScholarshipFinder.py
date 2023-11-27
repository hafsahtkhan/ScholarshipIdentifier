import xml.etree.ElementTree as ET

#Load file
tree = ET.parse('studentdata.xml')
root = tree.getroot()
scholartree = ET.parse('scholardata.xml')
scholarRoot = scholartree.getroot()

#list of dictionaries for students
students = []
scholarships = []
#Iterate though each record element
for record in root.findall('.//record'):
    #extract information
    first_name = record.find("FirstName").text
    last_name = record.find("LastName").text
    major = record.find("Major").text
    gpa = record.find("GPA").text
    level = record.find("Academic").text
    
    student_dict = {
        'name': first_name+last_name,
        'major': major,
        'gpa': gpa,
        'level': level
    }

    students.append(student_dict)

for record in scholarRoot.findall('.//record'):
    name = record.find("Scholarship").text
    major = record.find("Major").text
    gpa = record.find("GPA").text
    classi = record.find("Classification").text

    scholar_dict = {
        'name': name,
        'major': major,
        'gpa': gpa,
        'classification': classi
    }

    scholarships.append(scholar_dict)


scholarStudent = dict()
studentScholar = dict()

for scho in scholarships:
    studList = []
    for stu in students:
    #Makes sure the major matches
        if (scho['major'].startswith('Engineering') and 'Engineering' in stu['major']) or (stu['major'] in scho['major']):
            #Makes sure the students GPA is valid
            if (stu['gpa'] >= scho['gpa']):
                #Making sure student's classification is correct
                if(stu['level'] in scho['classification']):
                    #print(f"Student:{stu['name']}  GPA:{stu['gpa']}  Grade:{stu['level']}")
                    studList.append(stu['name'])
    scholarStudent[scho['name']] = studList

for stu in students:
    schoList = []
    for scho in scholarStudent:
        if stu['name'] in scholarStudent[scho]:
            schoList.append(scho)
    studentScholar[stu['name']] = schoList

line = "-----------------------------------------"
print("SCHOLARSHIPS CANDIDATES")
print(line)
for scholarship in scholarStudent:
    print(f"Candidates for {scholarship} are: {scholarStudent[scholarship]}")
    print()
    
print(line)
print(line)

for student in studentScholar:
    if len(studentScholar[student]) > 1:
        print(f"{student} meets {studentScholar[student]}")
        print()


