#!/usr/bin/env python

import os
import sys
import glob

done    = []
roots   = {}
chroots = '/chroot'

if not os.path.isdir(chroots):
    print "error: Chroot dir does not exist"
    sys.exit(1)

os.chdir(chroots)
list    = glob.glob('*')
reverse = False

try:
    if sys.argv[1] == '-r':
        reverse=True
except:
    pass

for dir in list:
    if dir != 'lost+found' and os.path.isdir(os.path.join(chroots, dir)):
        roots[dir] = {}
        if os.path.isfile(os.path.join(chroots, dir, '.requires')):
            f = open(os.path.join(chroots, dir, '.requires'))
            roots[dir]['requires'] = f.read().strip()
            f.close()

z=0
while roots:
    if z > 20:
        break

    for i in roots:
        attr  = roots[i]
        ready = True
        if attr.get('requires', False):
            for a in attr['requires'].split():
                if a not in done:
                    ready = False
        if ready:
            done.append(i)
      
    for d in done:
        if d in roots:
            roots.pop(d)
    z += 1

if reverse:
    done.reverse()

print ' '.join(done)
