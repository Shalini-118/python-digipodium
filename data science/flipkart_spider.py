from dputils import scrape

#step1. get the data at soup object
#step2. create the setup dictionary
#step3. pass the dictionary into the extract_many( ) function
#step4. repeat the step 1 to 3 util data keep coming
# step5. check and save data into file

# understanding the URL
url='https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=of'
print(url.split('?')[-1].split('&'))

#step1
query='laptop'
pos=1
url=f'https://www.flipkart.com/search?q={query}&page={pos}'
