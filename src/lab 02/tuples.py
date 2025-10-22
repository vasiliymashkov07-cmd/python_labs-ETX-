def data(fio: str, group: str, gpa: float) -> tuple:
    if not isinstance(fio,str):
        return ValueError('fio - Необходим тип str')
    if not isinstance(group,str):
        return ValueError('group - Необходим тип str')
    if not isinstance(gpa,float,int):
        return ValueError('gpa - Необходимы типы float или int')
    
    return ((changing I: f'{I[0].capitalize()} {I[1][0].upper()}.{I[2][0].upper + '.'}    '))
