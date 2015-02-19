# removes all but the most current nightly build

import os, sys

path = "/var/www/nightly/"

for f in os.listdir(path):
    ffilepath = os.path.join(path, f)
    if os.path.isfile(ffilepath):
        fnamearray = f.split('-') #split string to parts ..-472.4-windows.zip -> [.. 472.4 windows.zip]
        flen = len(fnamearray)

        fbranch = "" #a_teammate-json-384.4-windows.zip -> a_teammate json 384.4 windows.zip
        for x in range(0, flen - 2):
            fbranch += fnamearray[x] #master-dirty -> ["master", "dirty"] -> masterdirty
        
        fversion = fnamearray[flen-2].split(".")[0] # 472.4 -> 472
        fsys = fnamearray[flen-1]
            
        for g in os.listdir(path):
            gfilepath = os.path.join(path, g)
            if os.path.isfile(gfilepath):
                gnamearray = g.split('-') #split string to parts ..-472.4-windows.zip -> [.. 472.4 windows.zip]
                glen = len(gnamearray)
                
                gbranch = ""
                for x in range(0, glen - 2): 
                    gbranch += gnamearray[x] # append the branch even if branchname contains - 
                
                gversion = gnamearray[glen-2].split(".")[0] # 472
                gsys = gnamearray[glen-1]
                if f.find("--") == -1: #old corrupted filenames 
                    if gsys == fsys and gbranch == fbranch:   # same system: windows or linux
                        if fversion != "" and gversion != "": # corrupt (outdated) filename
                            if int(fversion) > int(gversion): # newer version of file
                                os.remove(gfilepath)
