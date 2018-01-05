#!/bin/bash

# rock_isvalid.bash

# This script demonstrates a Java-function which validates that
# SHA-256(r|msg) matches a given secure-hash is True or False.


export JAVA_HOME=${HOME}/jdk
export PATH=${JAVA_HOME}/bin:${PATH}

javac    src/us/cryp4/Main.java
ls -la   src/us/cryp4/Main.class
java -cp src us.cryp4.Main

exit

