import pandas as pd                #  WRITE IN TERMINAL "pip install pandas" TO INSTALL PANDAS
import datetime                      
import smtplib                     #  WRITE IN TERMINAL "pip install secure-smtplib" TO INSTALL SMTPLIB
import os

#                                         ENTER THE DATA.XLSX FILE PATH WHERE IT IS LOCATED LIKE C:\Users\HP\Desktop\codes\birthday IN THE " " BELOW

os.chdir(r"")

#                                                                  ENTER YOUR GMAIL_ID AND PASSWORD BELOW IN ' '

GMAIL_ID=''
GMAIL_PSWD=''

#                                                                                MAIN PROGRAM
def sendEmail(to,sub,msg):
    print(f"Email is sent to {to} with subject: {sub} and message {msg} is sent")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)

    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()
    

if __name__ == "__main__":
    df=pd.read_excel("data.xlsx")
    
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow=datetime.datetime.now().strftime("%Y")
    
    writeInd=[]
    for index,item in df.iterrows():
        
        bday=item['Birthday'].strftime("%d-%m")
        
        if(today==bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday" , item['Dialogue'])
            writeInd.append(index)

    
    for i in writeInd:
        yr=df.loc[i,'Year']
        df.loc[i,'Year']= str(yr) + ','+ str(yearNow)
        

    
    df.to_excel('data.xlsx',index=False)