# Find Emails In Excel File

As a teacher, I end up acquiring many excel files with class lists and contact lists and frequently want to pull out a bunch of emails from these.  But how?

## How does it work?

- The utility will ask you to provide an excel file
- It will ask you which sheet (optional)
- It will then spit out a set of emails found in the excel file
    - comma seperated
    - space seperated
    - semi-colon seperated
    - new-line seperated
 
## For what?
- Use this output to copy and paste it into online web-forms, sign-up sheets, etc.

## Why? Just open the excel file and find the emails yourself!
- no, go away.

## Install
```bash
pip3 install -r requirements.txt
```

## Run it:
```bash
python3 find_email_in_excel.py
```