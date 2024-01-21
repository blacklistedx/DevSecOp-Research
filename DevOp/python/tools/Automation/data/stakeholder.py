import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


# Generate report using pandas

data = {'NAME': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 90, 75]}
df = pd.DataFrame(data)

# Save the report to a file (e.g CSV)
df.to_csv('report.csv', index=False)

# Send the report via email

msg - MIMEMultipart()
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'recipient@example.com'
msg['Subject'] = 'Monthly Report'

body = "Please find the monthly report attached below."
msg.attach(MIMEText(body, 'plain'))

with open('report.csv', 'rb') as attachment:
    part = MIMEApplication(attachment.read(), Name='report.csv')
    part['Content-Disposition'] = f'attachment; filename={"report.csv")'
    msg.attach(part)



server = smtplib.SMTP('smtp.gmail.com', 587)
server.startlist()
server.login('marchesejake@gmail.com', 'password')
server.sendmail('marchesejake@gmail.com', 'recipient@example.com', msg.as_string())
server.quit()
