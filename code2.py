import json

resume = {
    "data": [
        {
            "FullName":"John Louie B. Gonzales",            
  
            "Address":"Meycauayan, Bulacan",
            "Email":"louiegonzales3214@gmail.com",
            "ContactNumber":"+639326208011",

            "ElementarySchool":"Dominic Elementary School",
            "HighSchool":"Benedict School of Novalichez",
            "SeniorHighSchool":"Fatima:Accountancy,Business and Management",
            "College":"Harvard University:Computer Engineering",

            "Achievements1":"Honesty Award",
            "Achievements2":"Honor Student",

            "Experiences":"Researching software and computer hardware,Writing and testing software for mobile devices and computers,Know How to repair Computers and Laptops.",

            "Summary":"Hardworking individual looking to work in the position of a Computer Engineer.Always focus in goal when interms of working.",
            "Objective":"Im the person that is always doing overtime and i'm a hardworking person"
        }
    ]
}
json_string = json.dumps(resume, indent=1)
with open('data.json', 'w') as f:
    f.write(json_string)    