from dputils import scrape
import pandas as pd

#step1. get the data at soup object
#step2. create the setup dictionary
#step3. pass the dictionary into the extract_many( ) function
#step4. repeat the step 1 to 3 util data keep coming
# step5. check and save data into file
def getdata(q):
    t={'tag':'div','attrs':{'class':'_1YokD2 _3Mn1Gg'}}
    rep_items={'tag':'div','attrs':{'class':'_1AtVbE col-12-12'}}
    titles={'tag':'div','attrs':{'class':'_4rR01T'}}
    price={'tag':'div','attrs':{'class':'_30jeq3 _1_WHN1'}}
    link={'tag':'a','attrs':{'class':'_1fQZEK'},'output':'href'}

    pos=1    
    all_data=[]
    while True:
    # understanding the URL
        url='https://www.flipkart.com/search?q={q}&page={pos}'
        print(url)
        soup=scrape.get_webpage_data(url)
        data=scrape.extract_many(soup,target=t,items=rep_items,title=t)
        if isinstance(data,list):
            if len(data)>0:
                pos+=1
                all_data.extend(data)
            else:
                break
        else:
            break
    return all_data    
#use
laptops=getdata('laptops')
pd.DataFrame(laptops).to_csv('laptop_data.csv')       


