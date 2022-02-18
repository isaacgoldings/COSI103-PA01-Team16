'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
    courses = json.load(jsonfile)
    
 #   print(courses)

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def sort(self,field):
        '''sorts the list of courses by a specific field'''
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        print("can't sort by "+str(field)+" yet")
        return self
        
    def name(self,phrase):
        '''returns a list of course names that contains the user-inputted phrase'''
        phrase_string = str(phrase[0])
        return Schedule([course for course in self.courses if phrase_string in course['name']])
    
    def description(self,descriptions):
        '''returns a list of courses which contain the user-inputted phrase in the description'''
        description_string = str(descriptions[0])
        return Schedule([course for course in self.courses if description_string in course['description']])
    
    #Mat's filter
    def enroll_limit(self,lim):
        '''returns a list of courses that either have the specific enrollment limit
           or no limit at all'''
        limit = int(lim)
        if limit > 0:
            return Schedule([course for course in self.courses if course['limit'] == limit])
            
        return Schedule([course for course in self.courses if course['limit'] == None])
        
    #David's Filter
    def waiting(self,waitings):
        '''returns a list of courses with a specific number of students waitlisted'''
        waiting_string = int(waitings[0])
        return Schedule([course for course in self.courses if waiting_string == course['waiting']])
        
    
    #Isaac's filter
    def courses_per_term(self):
        '''returns a list of courses that are independent study courses'''
        return Schedule([course for course in self.courses if course['independent_study'] == True])
    
        
    #Lucians filter
    def classcode(self,class_name):
        '''returns a list of classes that contain the inputted name'''
        equal= []
        for course in self.courses:
            if class_name in course['code'][1]:
                equal.append(course)
        return("Titles matching = ",equal)



 
