import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Custumer_Service@compagny.inc'
email['to'] = 'custumer email address'
email['subject'] = 'Thank you!'

email.set_content(html.substitute({'custumer': 'Custumer_name'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_personal email address', 'your_password')
    smtp.send_message(email)
print('Email sended! thank you.')

# PS: If you use gmail smtp server, be sure you have check this link
# https://myaccount.google.com/lesssecureapps
# before send email!
