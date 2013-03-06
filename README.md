chmgr
=====

Chroot manager for Fedora hosts. It uses YUM to create a chroot environment and provides a set of sub-commands for managing the chroot environments.

Use case could be a test or a build environment where a new and clean environment can be provided whenever a build or a test needs to be run.

Another use case are public facing services where chroots provide additional level of security.

Usage
=====

```shell
# chmgr 
    backup		Creates a configuration backup of a target
    create		Creates a target
    delete		Delete a target
    install		Install a package into a target
    list		List available targets
    login		Login to a target
    protect		Protects a target
    run   		Run a command in target
    service		Manages automatic stop/start of the services in the target
    start		Start a target
    stop		Stop a target
```

```shell
# chmgr create -t new-chroot 
===========================================================
Creating target new-chroot
===========================================================

* Initializing
* Target started

===========================================================
Chroot created: new-chroot
===========================================================
```

# chmgr list
Target                         Protected Services Created                     
============================== ========= ======== ============================
test                           no        0        Sat Nov 10 22:17:38 CET 2012
new-chroot                     no        0        Wed Mar 6 21:18:00 CET 2013

# chmgr install -t new-chroot -i tcpdump mtr
* Installing packages ... done

# chmgr login -t new-chroot
new-chroot# exit

# chmgr protect -t new-chroot

# chmgr run -t new-chroot -c "ls /tmp/test-file; touch /tmp/test-file; ls /tmp/test-file; rm /tmp/test-file"

drwxr-xr-x 16 root root 4096 Nov 10 22:18 /var

exit code: 0

# chmgr service -t new-chroot 
Services for: new-chroot
====================
No services defined

# chmgr service -t new-chroot -a httpd
new-chroot: Added service /etc/init.d/httpd

# chmgr service -t new-chroot 
Services for: new-chroot
====================
/etc/init.d/httpd

# chmgr start -t new-chroot
* Target started

# chmgr stop -t new-chroot

# chmgr delete -t new-chroot
error: Protected environment new-chroot

# chmgr protect -t new-chroot -r

# chmgr delete -t new-chroot
Deleting target new-chroot ... done

TODO
=====
[ ] Add inter-chroot dependancy during startup. E.g. chrootB depends on chrootA already running.
[ ] Update chroot
