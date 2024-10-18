import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv
from llama_index.core.tools import FunctionTool

load_dotenv()

def send_email(body):
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    body = f'''
        <html>
            <body>
                <p>Hello,</p>

                {body}
            
                <p>Thanks.<br>
            </body>
        </html>'''

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Email from the llamaindex agent!'

    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, os.environ.get('EMAIL_PASSWORD'))
            server.send_message(msg)
            print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {e}')
        return f'An error has occurred while trying to send email: {e}.'
    

email_engine = FunctionTool.from_defaults(
    fn=send_email,
    name="email_sender",
    description="This tool sends email to a person when requested by the user.",
)