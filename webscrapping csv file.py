import re
import requests
from bs4 import BeautifulSoup
import csv
url = "https://infopark.in/companies/company"
r = requests.get(url, verify=False)
soup = BeautifulSoup(r.content, 'html.parser')
data_dict = {'Email Addresses': [], 'H3 Tags': [], 'P Tags': []}
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
for tag in soup.find_all(['h3', 'p']):
    tag_text = tag.get_text(strip=True)
    
    if tag.name == 'h3':
        data_dict['H3 Tags'].append(tag_text)
    elif tag.name == 'p':
        data_dict['P Tags'].append(tag_text)
        
    # Extract and store email addresses
    email_addresses = re.findall(email_pattern, tag_text)
    data_dict['Email Addresses'].extend(email_addresses)

# Write data to CSV file
csv_file_path = 'output_data.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header
    csv_writer.writerow(['Email Addresses', 'company names', 'address'])
    
    # Write data rows
    max_rows = max(len(data_dict['Email Addresses']), len(data_dict['H3 Tags']), len(data_dict['P Tags']))
    for i in range(max_rows):
        email = data_dict['Email Addresses'][i] if i < len(data_dict['Email Addresses']) else ''
        h3_tag = data_dict['H3 Tags'][i] if i < len(data_dict['H3 Tags']) else ''
        p_tag = data_dict['P Tags'][i] if i < len(data_dict['P Tags']) else ''
        
        csv_writer.writerow([email, h3_tag, p_tag])

print(f'Data has been written to {csv_file_path}')
