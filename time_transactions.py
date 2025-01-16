from datetime import *
def bugun():
    bugun = datetime.today().date()
    bugun = bugun.strftime("%d.%m.%Y")
    return bugun
def dogum_tarihi_dogrulama(dogum_tarihi):
    try:
        datetime.strptime(dogum_tarihi, "%d.%m.%Y")
        return True  
    except ValueError:
        return False  

def due_date():
    current_time = datetime.now()
    due_date = current_time + timedelta(weeks=2)
    return due_date.strftime("%d.%m.%Y")

def parse_date(date_string):
    if date_string == "":
        return None 
    return datetime.strptime(date_string, "%d.%m.%Y")  

def ikitarihfarki(d1=False,d2=False):
    if not d1 or not d2:
        return 0
    else:
        date_1 = datetime.strptime(d1, "%d.%m.%Y")
        date_2 = datetime.strptime(d2, "%d.%m.%Y")
        difference = date_2 - date_1
        days_difference = difference.days
        return(days_difference)