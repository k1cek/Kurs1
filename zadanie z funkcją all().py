# zadanie z funkcją all()
# sprawdzam czy uzytkownik spełnia wymagania swoich umiejetnosci. 

#all wszystkie wymagania musza byc spełnione
#any jakikolwiek

john = {
    'name' : 'John Doe',
    'age' : 25,
    'skills' : ['Python', 'Java', 'C++']
}

marie = {
    'name' : 'Marie Willis',
    'age' : 35,
    'skills' : ['Python', 'C++']
}



def has_required_skills(person, skills):
    return any(skill in person['skills'] for skill in skills)


required_skills = ['Python', 'Java']


# print(has_required_skills(marie, required_skills))




# Ponumeruj zadania i pokaż je użytkownikowi | enumerate()

colors = ['blue', 'red', 'yelllow', 'green']

for i, kolor in enumerate(colors, start=1):
    kolor = kolor.capitalize()
    print(i, kolor)