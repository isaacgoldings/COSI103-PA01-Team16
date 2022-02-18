'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

#import sys
from schedule import Schedule

SCHEDULE = Schedule()
SCHEDULE.load_courses()
SCHEDULE = SCHEDULE.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in SCHEDULE.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global SCHEDULE
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            SCHEDULE.load_courses()
            SCHEDULE = SCHEDULE.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            SCHEDULE = SCHEDULE.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject: ")
            SCHEDULE = SCHEDULE.subject([subject])
            #filter courses exactly matching the instructor input
        elif command in ['i','instructor']:
            instructor = input("enter an instructor: ")
            SCHEDULE = SCHEDULE.lastname([instructor])
            #filter courses exactly matching the instructor email
        elif command in ['e','email']:
            email = input("enter an email: ")
            SCHEDULE = SCHEDULE.email([email])
            #filter by a String in class description
        elif command in ['d','description']:
            description = input("enter a description: ")
            SCHEDULE = SCHEDULE.description([description])
            #filter by a String in class title
        elif command in ['n','name']:
            name = input("enter a name: ")
            SCHEDULE = SCHEDULE.name([name])
            #filter by code of class (Lucian)
        elif command in ['c','code']:
            code=input('enter a class code: ')
            SCHEDULE = SCHEDULE.code([code][1])
            #filter by waiting list number (David)
        elif command in ['w','waiting']:
            waiting = input("enter a waiting list number: ")
            SCHEDULE = SCHEDULE.waiting([waiting])
            #filter by independent study (Isaac)
        elif command in ['l', 'independent_study']:
            SCHEDULE = SCHEDULE.courses_per_term()
            #filter by enrollment limit (Mat)
        elif command in ['m', 'limit']:
            limit = input("enter an enrollment limit: ")
            SCHEDULE = SCHEDULE.enroll_limit(limit)
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(SCHEDULE.courses),'elements',end="\n\n")
        print('here are the courses')
        for course in SCHEDULE.courses[:]:
            print_course(course)
        print('\n'*3)
        SCHEDULE.load_courses()
        SCHEDULE = SCHEDULE.enrolled(range(5,1000))
        continue

def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()

print(SCHEDULE.enrolled(5,100))
