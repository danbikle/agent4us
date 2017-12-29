#!/bin/bash

# ~/cryp4/public/class01A1/hash03j.bash

# This script should compile and run a Java app.

export JAVA_HOME=${HOME}/jdk
export PATH=${JAVA_HOME}/bin:${PATH}

set -x
javac    src/com/mkyong/test/Main.java
ls -la   src/com/mkyong/test/Main.class
java -cp src com.mkyong.test.Main

exit

