import os,requests,sys
file = f"{sys.argv[1]}"
path=os.getcwd() + file
sub_list = open(file).read() 
subdoms = sub_list.splitlines()
for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[2]}"
try:
        requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domains)
