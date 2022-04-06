#seding mail using SMTP protocol
import smtplib 
mail="varthpraneeth@gmail.com"
password="machilipatnam"
connection=smtplib.SMTP("smpt.gmail.com")
connection.starttls()
connection.login(user=mail,password=password)
connection.sendmail(from_addr=mail,to_addr="saipraneethvartha172@gmail.com",msg="python visual studio code testing")
connection.close()
