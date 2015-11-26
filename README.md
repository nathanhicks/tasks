# Instructions

## Scheduling

### Windows 7 cmd.exe
    schtasks /Create /SC DAILY /TN CallGrandma /TR "C:\Users\<username>\Documents\reminder.py"

### Linux
Use crontab.

Crontab fields and Allowed Ranges (Linux syntax)

| Field | Description | Allowed Value
--------|-------------|--------------
| MIN   | Minute field| 0 to 59
| HOUR  | Hour field  | 0 to 23
| DOM   | Day of Month | 1-31
| MON   | Month field  | 1-12
| DOW   | Day of Week | 0-6
| CMD   | Command     | Any command to be executed

    $ crontab -e 
    30 08 10 06 * /home/username/Documents/reminder.py

<ul>
<li> 30 - 30th Minute</li>
<li>08 - 08 AM</li>
<li>* - Every day of the month</li>
<li>* - Every month of the year</li>
<li>* - Every day of the week</li>
</ul>
