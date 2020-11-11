# simple-rpm
Just an example of an rpm build

# Build
We have a very simple project structure: 3 src files, a specfile and a Makefile:
```
[developer@sandbox7 simple-rpm]$ tree
.
├── Makefile
├── README.md
├── SPECS
│   └── hello-rpm.spec
└── src
    ├── hello
    ├── hello.conf
    └── hello.py
```

The specfile defines how the rpm should be built and where we want the source files to be installed.
To build the rpm, run the following make target:
```
make rpm
```

Check result (you get some new directories which contain the rpms, srpms and the tar-ed sources):
```
[developer@sandbox7 simple-rpm]$ ll
total 8
-rw-r--r-- 1 808606712 287753940 347 Nov 11 22:35 Makefile
-rw-rw-r-- 1 808606712 287753940  45 Nov 11 22:34 README.md
drwxrwxr-x 6 808606712 287753940 192 Nov 11 22:37 RPMS
drwxrwxr-x 3 808606712 287753940  96 Nov 11 22:37 SOURCES
drwxrwxr-x 4 808606712 287753940 128 Nov 11 22:35 SPECS
drwxrwxr-x 5 808606712 287753940 160 Nov 11 22:35 src
drwxrwxr-x 4 808606712 287753940 128 Nov 11 22:37 SRPMS
```

See the content of the newly built rpm:
```
[developer@sandbox7 simple-rpm]$ rpm -qlvp RPMS/hello-rpm-0.1.0-1.bbc.el7.x86_64.rpm
drwxr-xr-x    2 root    root                        0 Nov 11 22:37 /etc/hello-rpm
-rw-r--r--    1 root    root                        0 Nov 11 22:37 /etc/hello-rpm/hello.conf
-rwxr-xr-x    1 root    root                        0 Nov 11 22:37 /usr/bin/hello
drwxr-xr-x    2 root    root                        0 Nov 11 22:37 /usr/lib/hello-rpm
-rw-r--r--    1 root    root                        0 Nov 11 22:37 /usr/lib/hello-rpm/hello.py
```
