Full Name = Ramiyah Davidson
Student email = rrdavidson@aggies.ncat.edu
Hometown = Atlanta ,GA
Graduation semester = Spring 2029
Major = Computer Engineering

#Academic Data Organization
current_course_list = ['COMP 163', "MATH 150", "ENG 101", "HIS 150"]
credit_hours = [3,3,3,3]
gpa_history = [3.2, 3.6, 3.4, 3.7]
completed_courses = ['Biology', "Chemistry",  "Calculus", "Spanish II", "World History"]

#Contact Information Storage
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", 28202)
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordan_codes", 127)
birthday = ("Birthday", 5, 22, 2006)

#Interest Trcacking
current_skills = {"Python basics", "HTML", "Problem solving", "Time management","Photography"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interest = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One peice", "Barry", "Life", "Incantation", "Memento"}

#Organizational Mapping
# shows students course credits
course_credits = {
    "COMP 163": 3,
    "MATH 150": 3,
    "ENG 101":  3,
    "HIS 105":  3,
}
# shows students professors
course_professors = {
"COMP 163": "Prof. Rhodes", 
"MATH 150": "Dr. Lee",
"ENG 101": "Dr. Martinez", 
"HIS 105": "Dr. Brown"
}
#shows students course rooms
course_rooms = {"COMP 163": "M-Eric 300", 
"MATH 150": "Marteena 201", 
"ENG 101": "Crosby 121", 
"HIS 105": "Crosby 210"
}
#shows students monthly budget
monthly_budget = {
    "Food": 450, 
    "Entertainment": 200, 
    "Books": 125, 
    "Transportation": 100
}
#shows students study hours
study_hours_per_subject = {
    "Programming": 10,
    "Math": 8,
    "English": 4, 
    "History":3
      }
#shows students contacts
contact_directory = {
    "Mom": "704-555-0199",
    "Roommate":"336-555-7821",
    "Acadmeic Advisor": "336-334-5000"
    }

#Required Calculations
total_current_credits = sum(credit_hours)
cumulative_gpa = sum(gpa_history) / len(gpa_history)
count_of_completed_courses = len(completed_courses)
total_study_hours = study_hours_per_subject["Programming"] + study_hours_per_subject["Math"] + study_hours_per_subject["English"] + study_hours_per_subject["History"]
academic_load = total_current_credits + total_study_hours
monthly_budget_total = monthly_budget["Food"] + monthly_budget["Entertainment"] + monthly_budget["Books"] + monthly_budget["Transportation"]
daily_food_budget = monthly_budget["Food"] / 30
annual_budget_projection = monthly_budget_total * 12
study_cost_per_hour = round((monthly_budget["Books"] / total_study_hours),2)

#Analytics Calculations
total_social_media_followers = twitter_info[2] + instagram_info[2]
skills_count = len(current_skills) / len(skills_to_learn)
contact_directory_size = len(contact_directory)
entertainment_backlog_count = len(entertainment_backlog)
 #printed values

print("=" * 64)
print(f"    PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("=" * 64)
print(f"Student: Jordan Smith | Email: jsmith@ncat.edu")
print(f"From: Charlotte, NC | Graduating: Spring 2028")
print(f"Major: Computer Science")
print("")
print(f"=== ACADEMIC PROFILE ===")
print(f"Current Semester: {sum(credit_hours)} credits across {len(current_course_list)} courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print(f"Weekly Study Time: {total_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour")
print("")
print(f"Current Courses:")
print(f"{current_course_list[0]} - {course_credits["COMP 163"]} credits - {course_professors["COMP 163"]} - {course_rooms["COMP 163"]}")
print(f"{current_course_list[1]} - {course_credits["MATH 150"]} credits - {course_professors["MATH 150"]} - {course_rooms["MATH 150"]}")
print(f"{current_course_list[2]} - {course_credits["ENG 101"]} credits - {course_professors["ENG 101"]} - {course_rooms["ENG 101"]}")
print(f"{current_course_list[3]} - {course_credits["HIS 105"]} credits - {course_professors["HIS 105"]} - {course_rooms["HIS 105"]}")
print("")
print(f"=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {career_interest}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_to_learn)}")
print("")
print(f"=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget["Food"]} ${daily_food_budget}/day")
print(f"Entertainment: ${monthly_budget["Entertainment"]}")
print(f"Books: ${monthly_budget["Books"]}")
print(f"Transportation: ${monthly_budget["Transportation"]}")
print(f"Annual Projection: ${annual_budget_projection}")
print("")
print(f"=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]}")
print(f"Social Media Presence: {total_social_media_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory")
print("")
print(f"=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(completed_courses)}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog)} items")
print(f"Current Hobbies: {len(hobbies)} activities")

print("=" * 64)

