#!/bin/bash
# ----------------------------------------
# JAVA HOME LOCATION FOR DEPLOYMENT SERVER
# ----------------------------------------
JAVA_HOME="/oracle/jdk"
export JAVA_HOME

# ----------------------------------------
# ANT HOME LOCATION FOR DEPLOYMENT SERVER
# ----------------------------------------
ANT_HOME="/oracle/Middleware/modules/org.apache.ant_1.7.1"
export ANT_HOME

# ----------------------------------------
# DO NOT CHANGE PATH VARIABLE
# ---------------------------------------- 
PATH="${PATH}:${ANT_HOME}/bin:${ANT_HOME}/lib"
export PATH