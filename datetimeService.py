from datetime import datetime
import pytz

def getDate():
    singaporeTimeZone = pytz.timezone('Asia/Singapore')
    dateInSG = datetime.now(singaporeTimeZone)
    singporeDate = dateInSG.strftime("%d-%m-%Y")
    return singporeDate

def getTime():
    singaporeTimeZone = pytz.timezone('Asia/Singapore')
    timeInSG = datetime.now(singaporeTimeZone)
    singporeTime = timeInSG.strftime("%H:%M:%S")
    return singporeTime




    
    
