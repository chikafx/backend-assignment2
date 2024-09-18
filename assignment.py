data = {
        'company': {
            'departments': [
                {
                    'name': 'Engineering',
                    'employees': [
                        {
                            'id': 101,
                            'name': 'Alice',
                            'role': 'Software Engineer',
                            'projects': [
                                {'name': 'Alpha', 'status': 'completed'},
                                {'name': 'Beta', 'status': 'in progress'}
                            ]
                        },
                        {
                            'id': 102,
                            'name': 'Bob',
                            'role': 'DevOps Engineer',
                            'projects': [
                                {'name': 'Gamma', 'status': 'completed'},
                                {'name': 'Delta', 'status': 'not started'}
                            ]
                        }
                    ]
                },
                {
                    'name': 'Marketing',
                    'employees': [
                        {

                        'id': 201,
                        'name': 'Charlie',
                        'role': 'Content Strategist',
                        'campaigns': [
                            {'title': 'Product Launch', 'budget':5000},
                            {'title': 'Rebranding', 'budget': 8000}
                        ]
                    }
                ]
            }
        ]
    }
}

# question(2a) what this code i wrote simply means is that am printing company's data which has a department,
# now to locate the 'name' of department i used the position[0],[1] then what am targeting at that position e.g[name] 


print(data['company']['departments'][0]['name'])
print(data['company']['departments'][1]['name'])


#question(2b)... Print the names of all employees in the 'Engineering' department.

# here what i did, i printed company's data which has 2 departments, so to locate the first department(engineering)
# i used its position at index(0), then located the 'employee' string based on the question which is at index [0]
# because we have 2 employees, then i indicated what exactly we are looking for which is the 'name' string of the employee 
print(data['company']['departments'][0]['employees'][0]['name'])
print(data['company']['departments'][0]['employees'][1]['name'])

# question2c..Print the list of projects assigned to 'Alice'.
print(data['company']['departments'][0]['name'])
print(data['company']['departments'][0]['employees'][0]['name'])
print(data['company']['departments'][0]['employees'][0]['projects'])
print(data['company']['departments'][0]['name'])
print(data['company']['departments'][0]['employees'][1]['name'])
print(data['company']['departments'][0]['employees'][1]['projects'])

# question2c..Print the budget for the 'Rebranding' campaign.
print(data['company']['departments'][1]['employees'][0]['campaigns'][0]['budget'])
print(data['company']['departments'][1]['employees'][0]['campaigns'][1]['budget'])


# b. Modify Nested Data:
#  Update the status of the 'Beta' project to 'completed'.
old_status= 'in progress'
new_status='completed'
data['company']['departments'][0]['employees'][0]['projects'][1]['status']='completed'
print(data['company']['departments'][0]['employees'][0]['projects'][1]['status'])

# Add a new project {'name': 'Epsilon', 'status': 'planned'} to Bob's list of
# projects.

new_project= {'name': 'Epsilon', 'status': 'planned'}
data['company']['departments'][0]['employees'][1]['projects'].append(new_project)
print(data['company']['departments'][0]['employees'][1]['projects'])