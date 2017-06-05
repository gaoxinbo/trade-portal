#!/bin/bash


VIRTUAL_ENV_BASE="portal_env"


if [ ! -d $VIRTUAL_ENV_BASE ]; then 
  virtualenv -p /usr/local/bin/python3 $VIRTUAL_ENV_BASE 
  . $VIRTUAL_ENV_BASE/bin/activate
fi


