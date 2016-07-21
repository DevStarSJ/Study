# Auto run Mono background On Linux (Raspberry Pi)


### 1. Create script in /etc/init.d

```
~# sudo nano /etc/init.d/runSC
```

#### runSC
```
cd /root/SmartController.Web && mono bin/Debug/net451/win7-x64/SmartController.Web.exe > /root/mono.out &
```

### 2. Make Script executable

```
~# sudo chmod 755 /etc/init.d/runSC 
```

### 3. Test starting the script

```
~# sudo /etc/init.d/runSC start
```

### 4. Test stopping

```
~# sudo /etc/init.d/runSC stop
```

### 5. Regist your script in /etc/rc.local

```
sudo /etc/init.d/runSC start
```


#### Reference
<http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html>
<http://raspberrypi.stackexchange.com/questions/5148/how-do-i-run-a-background-service-written-in-mono>
