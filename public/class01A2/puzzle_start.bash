#!/bin/bash

# ~/cryp4/public/class01A2/puzzle_start.bash

# This script should compile and run a Java app.

export JAVA_HOME=${HOME}/jdk
export PATH=${JAVA_HOME}/bin:${PATH}

set -x
javac    src/us/cryp4/Main.java
ls -la   src/us/cryp4/Main.java
java -cp src us.cryp4.Main

exit

