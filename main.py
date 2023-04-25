import sys
import requests
from bs4 import BeautifulSoup      # library to parse HTML
import pandas as pd                # library for data analysis
import urllib3.exceptions
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pretty_html_table import build_table

# Disable warning about "InsecureRequestWarning"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get list of UEA jobs
response = requests.get("https://myview.uea.ac.uk/webrecruitment/", verify=False)  # Not best practice!
table_class = "wikitable sortable jquery-tablesorter"

# Checks if request is OK
if response.status_code != 200:
    sys.exit("Error: Response is not 200.")

# parse data from the html into a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')
vacancies_table = soup.select("#latestVacancies\:vacancyList\:vacancies")

# Reads HTML of vacancies table and returns a list of dataframe objects
df = pd.read_html(str(vacancies_table))

# Converts list to Dataframe
df = pd.DataFrame(df[0])

# Remove unwanted columns: "Apply" and "Favourites"
df = df.drop(["Apply", "Favourites"], axis=1)

# Remove last string between brackets in Job Title column
df["Job Title"] = df["Job Title"].replace("[(A-Z0-9)]+$", "", regex=True)

# Convert "Category" and "Location" column's data to strings
df = df.astype({"Category": "string", "Location": "string"})

# Remove all rows except from those in "Category: Technical (TC)" or those in "Location: IT & Computer Science (ITCS)"
# Location is currently using "STS - Student Services" for testing. Will change to ITCS when a job appears.
vacancies = df[(df["Category"] == "Technical (TC)") | (df["Location"] == "STS - Student Services")]

# Converts "Vacancies" dataframe to HTML and makes it pretty
output = build_table(vacancies, color="blue_light", text_align="center", padding="10px")

# Email credentials and server variables for multipart email
sender_email =  # Enter sender email address as string
sender_password =  # Enter sender password as string
receiver_email =  # Enter receiver email address as string
smtp_server =  # Enter smtp server as string
smtp_port =  # Enter smtp server port as int

# Create multipart email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "UEA Job Alert - Technical and IT"

# Add the HTML table to email body
msg.attach(MIMEText(output, "html"))

# Connect to SMTP server and send email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully.')
except Exception as error:
    print('Error sending email: ', error)
finally:
    server.quit()
