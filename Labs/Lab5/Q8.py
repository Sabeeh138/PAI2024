import re

# Sample block of text containing various date formats using chatgpt
text = """
Here are some dates:
12/09/2023
2023-09-12
Sep 12, 2023
Not a date: 2023-13-01
Another date: 01-12-2023
"""


date_pattern = r'\b(\d{1,2}/\d{1,2}/\d{4}|'
               r'\d{4}-\d{1,2}-\d{1,2}|'
               r'[A-Za-z]{3} \d{1,2}, \d{4})\b'

# Find all valid dates in the text
valid_dates = re.findall(date_pattern, text)

# Print the list of valid dates
print("Valid dates found:")
for date in valid_dates:
    print(date)
