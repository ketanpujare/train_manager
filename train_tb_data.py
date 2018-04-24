import requests
from csv import writer
from lxml import html


page = requests.get('http://konkanrailway.com:8080/TrainSchedule/trainschedule.action')
tree = html.fromstring(page.content)

train_list = tree.xpath('//*[@id="trainDetail"]/option/@value')[1:]

# Train Timetable(tb)
def train_tb(train_list):
    for train in train_list:
        filename = 'Data/train_timetable/'+train+'.csv'
        with open (filename,'wb') as tbfile:
            csv = writer(tbfile)

            payload = {
                'trainDetail': train,
                'objvo.selTrain': train
            }

            r = requests.post("http://konkanrailway.com:8080/TrainSchedule/onsubmit.action",data=payload)
            tree = html.fromstring(r.content)
            train_no = tree.xpath('//*[@id="trainCredNo"]/text()')
            print(train) 
            last_data = tree.xpath('//*[@id="mid_col"]//table[@border="1"]/tbody/tr[last()]/td[1]/text()')[0]

            #csv.writerow(['Sr.No','Station Code','Station Name','Arrival Time','Departure Time','Day'])
            for entry in range(1,int(last_data)+1):
                sr_no       = tree.xpath('//*[@id="mid_col"]//table[@border="1"]/tbody/tr['+str(entry)+']/td[1]/text()')[0]
                stn_code    = tree.xpath('//*[@id="mid_col"]//table[@border="1"]/tbody/tr['+str(entry)+']/td[2]/text()')[0]
                stn_name    = tree.xpath('//*[@id="mid_col"]//table[@border="1"]/tbody/tr['+str(entry)+']/td[3]/text()')[0]
                day         = tree.xpath('//*[@id="mid_col"]//table[@border="1"]/tbody/tr['+str(entry)+']/td[6]/text()')[0]
                
                try:
                    arrival_time = tree.xpath('//*[@id="mid_col"]//table[@border="1"]/tbody/tr['+str(entry)+']/td[4]/text()')[0]
                except IndexError:
                    arrival_time = "A"
                try:
                    dept_time   = tree.xpath('//*[@id="mid_col"]//table[@border="1"]/tbody/tr['+str(entry)+']/td[5]/text()')[0]
                except IndexError:
                    dept_time = "D"
                
                csv.writerow([sr_no,stn_code,stn_name,arrival_time,dept_time,day])


# All Train Data in one File(Train No. ,Train Name, Days Run)
def trains_data(train_list):
    with open('Data/train_run_data','wb') as trainfile:
        csv = writer(trainfile)

        for train in train_list:
            payload = {
                'trainDetail': train,
                'objvo.selTrain': train
            }

            r = requests.post("http://konkanrailway.com:8080/TrainSchedule/onsubmit.action",data=payload)
            tree = html.fromstring(r.content)
            
            train_no = tree.xpath('//*[@id="trainCredNo"]/text()')[0]
            train_name = tree.xpath('//*[@id="trainCredName"]/text()')[0]
            days_run = tree.xpath('//*[@id="trRemarks"]/text()')[0]        

            print(train_name)
            #csv.writerow(['Train No.','Train Name','Days Run'])
            csv.writerow([train_no,train_name,days_run])

trains_data(train_list)
#train_tb(train_list)