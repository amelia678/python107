ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print ramit's email address
print(ramit['email'])

get first of Ramit's interests
(ramit['interests'][0])

get email address of Jasmine
print(ramit['friends'][0]['email'])

get second of Jan's interests
print(ramit['friends'][1]['interests'][1])