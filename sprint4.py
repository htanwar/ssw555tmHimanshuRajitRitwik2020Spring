import datetime
import main_parser

# US19 First Cousins shoud not marry
# first cousins should not marry one another
# Author: Himanshu Tanwar

def US19():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = main_parser.parse(file_)
	
    individualError = []

    #check if parents of husband and spouse. If parents are siblings in each others families then first cousins. Return
    for fam in listFam:
        if fam.husbandId != 'NA' and fam.wifeId != 'NA':
            hParents = main_parser.findParents(fam.husbandId, listFam)
            wParents = main_parser.findParents(fam.wifeId, listFam)
            if hParents and wParents:
                #check if either hParents are siblings with wParents
                siblings = main_parser.checkIfSiblings(hParents,wParents,listFam)
                if siblings == True:
                    individualError.append(fam)
    return individualError


# US20 Aunts and Uncles
# Aunts and Uncles should not marry their neices or nephews
# Author: Himanshu Tanwar

def US20():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = main_parser.parse(file_)

    individualError = []
    for fam in listFam:
        if fam.husbandId != 'NA' and fam.wifeId != 'NA':
            hParents = main_parser.findParents(fam.husbandId, listFam)
            wParents = main_parser.findParents(fam.wifeId, listFam)
            if hParents and wParents:
                hSiblings = main_parser.checkIfSiblings(hParents,fam,listFam)
                wSiblings = main_parser.checkIfSiblings(wParents,fam,listFam)
                if hSiblings == True:
                    individualError.append(fam)
                elif wSiblings == True:
                    individualError.append(fam)
    return individualError


#Author Ritvik Tiwari
def US23():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = main_parser.parse(file_)
    
    birthdayError=[]
    dictionary={}
    for person in listPeople:
        if person.name in dictionary and person.birthday == dictionary[person.name][0] and person.id != dictionary[person.name][1]:
            birthdayError.append((person.birthdayError,person.name))
        else:
            dictionary[person.name] = (person.birthday,person.id)

    return birthdayError

#Author Ritvik Tiwari
def US24():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = main_parser.parse(file_)

    familyError=[]
    dictionary={}
    for fam in listFam:
        if fam.husbandId != 'NA' and fam.wifeId !='NA':
            husb= main_parser.findPerson(fam.husbandId, listPeople)
            wife= main_parser.findPerson(fam.wifeId, listPeople)
            if husb.name in dictionary and dictionary[husb.name][0] == wife.name and dictionary[husb.name][1] == fam.married:
                familyError.append((husb.name,wife.name,fam.married))
            else:
                dictionary[husb.name]=(wife.name,fam.married)
    return familyError
