# DisplayMakerDisk
Filesystem exploration for Kodak DisplayMaker diskettes

This is some code to try and figure out the filesystem of the disks used with the Kodak DisplayMaker. It's currently an early prototype but can do some basic listing of files & sizes on disk images.

The system seems to use HD 5.25" disks but it uses both 15 and 16 sector per track versions, and some of them are interleaved and some are not. 
It's weird, and potentially a side-effect of how the disks were imaged, and the system itself doesn't need them formatted that way.

# Disk images:
No disk images are included in this repo, but you can get them on the internet archive:
https://archive.org/details/KodakDisplayMakerDisks

These are unfortunately TeleDisk images, and this tool needs raw IMG disks. You can convert them using the [HxCFloppyEmulator software](http://hxc2001.free.fr/floppy_drive_emulator/index.html#download).

# Links
* [Twitter thread where I'm recording my findings](https://twitter.com/Foone/status/1299108629660889088)
* [Lazy Game Reviews video on this same hardware](https://www.youtube.com/watch?v=ABOJLR7bRIA)
