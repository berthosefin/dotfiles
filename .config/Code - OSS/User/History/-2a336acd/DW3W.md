# [Grub](grub) custom entry

- OS: [Linux](linux)
- Tags: #conf

---

Edit: **_/etc/grub.d/40_custom_**

```sh
#!/bin/sh
exec tail -n +3 $0
# This file provides an easy way to add custom menu entries.  Simply type the
# menu entries you want to add after this comment.  Be careful not to change
# the 'exec tail' line above.
menuentry "Windows 10"{
	set root='(hd0,4)'
	search --no-floppy --fs-uuid --set 43BD21B81740DDBF
	drivemap -s (hd0) ${root}
	chainloader +1
}
```
