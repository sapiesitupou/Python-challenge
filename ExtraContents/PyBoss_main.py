import os, csv
import pandas as pd
from pathlib import Path 


file_path = Path(".." , "ExtraContents", "Resources", "PyBoss_employee_data.csv")


full_name = []
first_name = []
last_name = []
date_of_birth = []
d_o_b = []
ssn = []
ssn_private = []
abbrev = []
employee_id = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


with open(file_path) as employee_data:
    csv_reader = csv.reader(employee_data, delimiter = ",") 
    csv_header = next(csv_reader)   
    
    for row in csv_reader:

        employee_id.append(row[0])

        full_name = row[1].split(" ")   
        first_name.append(full_name[0])
        last_name.append(full_name[1])

        date_of_birth = row[2].split("-")
        d_o_b.append(date_of_birth[1] + "/" + date_of_birth[2] + "/" + date_of_birth[0])
        
        ssn = row[3].split("-")
        ssn_private.append("***-**-" + ssn[2])

        abbrev.append(us_state_abbrev[row[4]])


new_df = pd.DataFrame({"Employee Id": employee_id, "First Name": first_name, "Last Name": last_name, "DOB": d_o_b, "SSN":ssn_private, "State": abbrev})

new_df.to_csv(Path("..", "ExtraContents", "PyBoss_updated.csv"), index=False, header=True)

print(new_df.head())