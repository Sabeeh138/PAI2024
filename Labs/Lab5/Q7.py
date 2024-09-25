import re

# Sample block of text containing email addresses using chatgpt
text = """
Here are some email addresses:
john.doe@example.com
jane_doe123@sample.org
invalid-email@.com
another.invalid@domain
alice@example.co.uk
bob@company.info
"""


email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


valid_emails = re.findall(email_pattern, text)

# Print the list of valid email addresses
print("Valid email addresses found:")
for email in valid_emails:
    print(email)
