import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active

email_list = [
    ['John Smith', 'john@example.com', 'Hello'],
    ['Jane Doe', 'jane@example.com', 'Greetings'],
    ['Bob Johnson', 'bob@example.com', 'Important notice']
]

for row in email_list:
    print(row)  #debug
    sheet.append(row)

filename = 'email_information.xlsx'
workbook.save(filename)
