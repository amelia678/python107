phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob' : '857-384-1234',
    'Elizabeth' : '484-584-2923'
}

#print Elizabeth's phone number
print(phonebook_dict['Elizabeth'])

#add entry to directory
phonebook_dict['Kareem'] = '938-489-1234'

#delete Alice's phone entry
del phonebook_dict['Alice']

#change bob's phone number
phonebook_dict['Bob']= '968-345-2345'
print(phonebook_dict)