import openpyxl


def return_excelValue(Sheet):
    # The source xlsx file is named as source.xlsx



    wb = openpyxl.load_workbook('userstolike.xlsx')
    worksheet = wb[Sheet]

    values = [c.value for c in worksheet['A'][0:]]
    return values

def appendLink(url):
    wb = openpyxl.load_workbook('userstolike.xlsx')
    worksheet = wb['Cruda']
    # worksheet['A'+str(pos+1)] = url
    rows = (
        (url,),
    )
    for row in rows:
        worksheet.append(row)
    wb.save('userstolike.xlsx')






