# send email from scripts, command line
ever wanted to automate emails to yourself?

its pretty simple to set up

## steps
1. setup app password for gmail account (here)[https://security.google.com/settings/security/apppasswords]
    + note that this is different from main account password
2. add a credentials.py script in mailme directory, where you add your personal email and password generated from previous step
3. go to main directory (where setup.py is found) and run
   `pip install -e .`
4. now you can invoke this module with whatever script you want

```
from mailme import mailto


mailto('jackappleseed@xyz.com', 'i love you man')
```
