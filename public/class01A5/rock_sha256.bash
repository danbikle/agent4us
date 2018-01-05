#!/bin/bash

# rock_sha256.bash

# This script compiles and runs a Java-app which creates and
# demonstrates a function which converts a msg into a
# random number, r, and SHA-256(r|msg).

export JAVA_HOME=${HOME}/jdk
export PATH=${JAVA_HOME}/bin:${PATH}

javac    src/us/cryp4/Main.java
ls -la   src/us/cryp4/Main.class
java -cp src us.cryp4.Main

exit

