#!/bin/bash

# hash_afile.bash

# This script should compile and run a Java app.

export JAVA_HOME=${HOME}/jdk
export PATH=${JAVA_HOME}/bin:${PATH}

echo This Java-app should calculate a SHA-256 "secure-hash" AKA hash-digest of a large file.

echo I should get the large file now:

set -x

/usr/bin/curl https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh > /tmp/Anaconda3-5.0.1-Linux-x86_64.sh

javac    src/us/cryp4/Main.java
ls -la   src/us/cryp4/Main.java
java -cp src us.cryp4.Main

exit

