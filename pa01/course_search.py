'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''
#git demonstration
from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

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

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
            #filter courses exactly matching the instructor input
        elif command in ['i','instructor']:
            instructor = input("enter an instructor:")
            schedule = schedule.lastname([instructor])
            #filter courses exactly matching the instructor email
        elif command in ['e','email']:
            email = input("enter an email:")
            schedule = schedule.email([email])
            #filter by a String in class description
        elif command in ['d','description']:
            description = input("enter a description:")
            schedule = schedule.description([description])
            #filter by a String in class title
        elif command in ['n','name']:
            name = input("enter a name:")
            schedule = schedule.name([name])
            #filter by a int in waiting list
        elif command in ['c','code']:
            code=input('enter a class code')
            schedule = schedule.classcode([code])
        elif command in ['w','waiting']:
            waiting = input("enter a waiting list number:")
            schedule = schedule.waiting([waiting])
        elif command in ['l', 'independent_study']:
            schedule = schedule.independentStudy()
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the courses')
        for course in schedule.courses[:]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()

print(schedule.enrolled(5,100))
