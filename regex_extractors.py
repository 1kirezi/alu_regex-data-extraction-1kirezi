text = """
Congrats! $2,000.00 was sent to emily.dev@alu.edu at 09:30 AM. #RichQueen
"""
import re

# 1. Extract Email
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print("Email(s):", emails)

# 2. Extract Currency
currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
currencies = re.findall(currency_pattern, text)
print("Currency Amount(s):", currencies)

# 3. Extract Time (12-hour format)
time_pattern = r'\b\d{1,2}:\d{2}\s?[APMapm]{2}\b'
times = re.findall(time_pattern, text)
print("Time(s):", times)

# 4. Extract Hashtags
hashtag_pattern = r'#\w+'
hashtags = re.findall(hashtag_pattern, text)
print("Hashtag(s):", hashtags)
