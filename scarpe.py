import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://realpython.github.io/fake-jobs/'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

results = s.find(id='ResultsContainer')
job_title = results.find_all('h2', class_='title is-5')

job_titles = [job.text for job in job_title]

# Print the job titles
for title in job_titles:
    print(title)

# Create a DataFrame to store the job titles
data = {'Job Titles': job_titles}
df = pd.DataFrame(data)

# Save the job titles to an Excel file
df.to_excel('job_titles.xlsx', index=False)
