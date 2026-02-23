import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "36464925")
    API_HASH = environ.get("API_HASH", "942f6440a3ab83321135d7c1927aba0a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8454259213:AAHfg0CE0Em5ZrRB79ZcjUnY8Q1QpK0bFxM") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://for:for@cluster0.fgu4b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "AutoForward")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8422190094').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003597680452'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1003601738198") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
