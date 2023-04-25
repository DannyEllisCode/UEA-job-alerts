# UEA Job Alerts
> A program that scrapes the UEA vacancies webpage and emails a cleaned up dataset to the user.

This program scrapes the UEA vacancies webpage using BeuatifulSoup4 and returns a table using a CSS selector. Pandas is then used to convert it into a dataframe and clean up the data. Once cleaned up it will then remove all rows except those that contain categories or locations specified in the script, puts it into a "pretty" HTML table using "pretty_html_table" module. Lastly it takes credentials for sending an email, creates the email and attempts to send it.

---

## Installing / Getting started

Set up required:
 
  1. Download main.py and install the necessary modules.
    
  2. Input email credentials into rows 49 - 53.
  
  3. Edit vacancies variable to return only wanted information.
  
---

## Additional Features

Additional features that could be added:

  • Create a copy to be able to run from a RaspberryPi (or even a RaspberryPi Pico using MicroPython)
  
  • In built automation (currently using Windows Task Scheduler)
  
  • Have configuration variables in a seperate file
  
  • requests.get is set to verify=False which does not seem like good practice but allows the code to run - would be good to fix if possible

---

## Motivation

The motivation for this program was because at the time of creation the built-in job alerts only sent an email once a week saying "New Jobs Posted" or something similar so was not helpful to me as you then needed to check the website anyway to see if it was anything was relevant.

I felt this would be a good first project to use some of the things I have learned in pandas and BeautifulSoup and to learn how Github works (although Git was not used locally).

I hold no affiliation with the UEA and am happy to remove this repository upon request as this is only for personal use and to display as part of a working portfolio.

---

## Licensing

Daniel Ellis
