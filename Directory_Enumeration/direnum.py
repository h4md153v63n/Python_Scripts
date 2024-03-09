import os,requests,sys
file = f"{sys.argv[1]}"
path=os.getcwd() + file
sub_list = open(file).read() 
directories = sub_list.splitlines()
for dir in directories:
    dir_enum = f"http://{sys.argv[2]}/{dir}.html" 
    r = requests.get(dir_enum)
    if r.status_code==404: 
        pass
    else:
        print("Valid directory:" ,dir_enum)
