import requests
import re



url = 'http://127.0.0.1:56182'
control=0
throttle=2
data1 = {'driver':'august','steering_control': control, 'throttle': throttle}

pattern = r'弯道(.*?)，(.*?)</font>'

with requests.Session() as session:
    for i in range(7):
        response = session.post(url, data=data1)
        print(response.text)
        match = re.search(pattern, response.text)
        if match:
            if match.group(1) == "向左":
                control=1
            elif match.group(1)=="向右":
                control=-1
            else:
                control=0
            
            if match.group(2)=="抓地力太小了！":
                throttle=0
            elif match.group(2)=="抓地力太大了！":
                throttle=2
            else:
                throttle=1    
            data1 = {'driver':'august','steering_control': control, 'throttle': throttle}
            # print(f"output:{match.group(1)},{match.group(2)}\n{control},{throttle}")
        else:
            print("error")
            break    

# response = session.post(url, data=data1)
# print(response.text)
