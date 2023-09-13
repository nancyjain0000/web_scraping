##importing the important libraries

import requests
import time
from bs4 import BeautifulSoup

#filtering out the unfamiliar skills
print("Put some skills that you are not familiar with!")
unfamiliar_skills=input(">")
print(f"Filtering out {unfamiliar_skills}!")
print(" ")

def find_jobs():
    #requesting the link to the site
    html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=")

    #access data from html pages
    soup = BeautifulSoup(html_text.text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    #print(jobs)

    #printing jobs in loop for all the details we need
    for index,job in enumerate(jobs):
        
        #check if the job has 'few' word in it, only when it will get printed
        published_date=job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            
            #fetching company names
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            
            #fetching skills
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            
            #fetching links
            more_info=job.header.h2.a['href']
            
            #print only jobs with familiar skills
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    #printing the necessary details
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Skills Required: {skills.strip()}\n")
                    f.write(f"More Information: {more_info}\n")
                print(f'File saved:{index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f"Waiting for {time_wait} minutes.....")
        time.sleep(time_wait*60)