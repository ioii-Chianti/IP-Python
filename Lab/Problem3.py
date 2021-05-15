python = {'Alex': 83, 'Harry': 77, 'Davy': 93, 'Lisa': 65, 'Sunday': 89}
algorithm = {'Lisa': 91, 'Andrew': 88, 'Kevin': 76}
os = {'Harry': 60, 'Louis': 100, 'Mike': 90, 'Lisa': 58}

Name = input()
found = False

if (Name in python):
    print('%s gets %d on Python.' % (Name, python[Name]))
    found = True
if (Name in algorithm):
    print('%s gets %d on Algorithm.' % (Name, algorithm[Name]))
    found = True
if (Name in os):
    print('%s gets %d on OS.' % (Name, os[Name]))
    found = True

if not found:
    print('%s is not taking any courses.' % Name)
