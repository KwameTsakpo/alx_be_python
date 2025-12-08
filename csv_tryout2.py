import csv

rows = []
fieldnames = ['name','age','city','superpower']

def getDetails(name):
    with open('items.csv','r') as file:
        details = csv.DictReader(file)
        fieldnames = details.fieldnames
        for row in details:
            if row['name'] == str(name):
                print(f'Hero name: {row['name']},\nAge: {row['age']},\nCity: {row['city']},\nSuper powers: {row['superpower']}\n\n\n ')
                row['age'] = '100'
            rows.append(row)
            
        print(f'\n\nValue of Rows variable: {rows}')
    
    with open('items.csv','w',newline='') as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def load_csv():
    with open('items.csv','r') as file:
        details = csv.DictReader(file)
        fieldnames = details.fieldnames
        
        for row in details:
            rows.append(row)
            
        print(f'\n\nValue of Rows variable: {rows}')

def addDetails(name,age,city,superpower):
    
    rows.append({'name':name,'age':age,'city':city,'superpower':superpower})
    
    with open('items.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# load_csv()
getDetails('Sylvia')
# addDetails('Kwame','26','Accra','Pocket thieve')
