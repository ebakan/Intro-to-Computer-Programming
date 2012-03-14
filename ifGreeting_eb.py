#ifGreet
#ebakan
def greet(name,school):
    print('Greetings, '+name+' from '+school+'.')
    if school=='bellarmine' or school=='bell':
        print('Congratulations. You go to the best school on the planet.')
    elif school=='st. francis' or school=='st francis' or school=='saint franics' or school=='sf':
        print('Ewww. You\'re a lancer. You go to the worst school on the planet. You suck.')
    elif school=='presentation' or school=='pres' or school=='notre dame' or school=='nd':
        print('You go to the best non-all-boys school on the planet! Thanks for supporting Bellarmine!')
    else:
        print('Sorry, your school is not that important.')
while __name__=='__main__':
    greet(raw_input('Name:').lower(), raw_input('School:').lower())
