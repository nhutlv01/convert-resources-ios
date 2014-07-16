convert-resources-ios
=====================

Auto create resources for ios devices

You need to install PIL

Copy convert.py to your folder.

Run    python convert.py   and choose your device (iPhone or iPad)

All of files will create inside Resized folder


#INSTALL PIL ON MAC OS X 10.9

curl -O -L http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz

tar -xzf Imaging-1.1.7.tar.gz

cd Imaging-1.1.7

python setup.py build

sudo python setup.py install


#If you get this error when installing:

/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/usr/include/tk.h:78:11: fatal error: 'X11/Xlib.h' file not found

include <X11/Xlib.h>

 ^

1 error generated.

error: command 'cc' failed with exit status 1


#RUN: xcode-select --install. After install software, try install PIL again
