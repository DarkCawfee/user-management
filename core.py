# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:07:06 2020

@author: andrewNY

This app is personal project by me (Alizain), you are allowed to change, copy, view, edit or publish it. But please do not remove this credit comment.
App is built for temporary attendance and user management using nested loops, inputs and lists

"""

print('This app is just meant for temporary attendance etc purposes. None of the data is stored permanently.')

person_list = []

try:
    def user_management():
        person_opp = str(input('Which operation you want to perform? \n View (v), Add (a), Search(s), Remove(r), Sort(o) '))
        if person_opp == 'v':
            if len(person_list) < 1:
                print('Oops, looks like you haven\'t added any elements yet.')
                user_management()
            else:
                print(person_list)
                user_management()
    
        elif person_opp == 'a':
            try:
                person_limit = int(input('How many persons you want to add? '))
                a = 0
                
                while a < person_limit:
                    person = str(input('Enter the name of the person: '))
                    person_list.append(person)
                    a += 1
                    
                user_management()
            
            except ValueError:
                print('Invalid value.')
                user_management()
                
        elif person_opp == 's':
            if len(person_list) < 1:
                print('You have no items yet.')
                user_management()
                
            else:
                person_search = str(input('Enter which person you want to search? '))
    
                try:
                    person_index = person_list.index(person_search)
                    print(person_list[person_index], 'on the index', person_index)
                    user_management()
                    
                except ValueError:
                    print('Looks like the person doesn\'t exists :(')
                    user_management()
                    
                except IndexError:
                    print('Looks like the person doesn\'t exists :(')
                    user_management()
                    
        elif person_opp == 'r':
            if len(person_list) < 1:
                print('Oops, looks like there are no elements to remove :(')

            else:
                person_remove = input('Enter which person you want to remove: ')
                
                try:
                    person_index = person_list.index(person_remove)
                    del(person_list[person_index])
                    user_management()
                    
                except ValueError:
                    print('Looks like the value is incorrect.')
                    user_management()

        elif person_opp == 'o':
            person_sort_opp = input('Do you want to sort in reverse order? (Y/n) ')
            if person_sort_opp.lower() == 'y':
                person_list.sort(reverse=True)
                print(person_list)
                user_management()

            elif person_sort_opp.lower() == 'n':
                person_list.sort(reverse=False)
                print(person_list)
                user_management()

            else:
                print('Incorrect option chosen.')

        else:
            print('Invalid command input.')
            user_management()
            
except ValueError:
    print('Invalid value inputed.')
    user_management()

user_management()