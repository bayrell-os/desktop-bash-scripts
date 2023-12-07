#!/bin/bash

DRIVER="intel_backlight"
CURRENT=`cat /sys/class/backlight/${DRIVER}/brightness`
MIN=50
MAX=`cat /sys/class/backlight/${DRIVER}/max_brightness`
STEP=10

function set_value(){
  VALUE=$1
  if (( "$VALUE" < "$MIN" ))
  then
    VALUE=$MIN
  fi
  
  if (( "$VALUE" > "$MAX" ))
  then
    VALUE=$MAX
  fi
  
  echo $VALUE
  echo $VALUE > /sys/class/backlight/${DRIVER}/brightness
}

case $1 in

  -dec)
    CURRENT=$((CURRENT-STEP))
    set_value $CURRENT
    ;;
  
  -inc)
    CURRENT=$((CURRENT+STEP))
    set_value $CURRENT
    ;;

  -get)
    echo $CURRENT
    ;;

  -set)
    set_value $2
    ;;

  *)
    echo "Usage: $0 [-inc|-dec|-get|-set]"
    exit 1
    ;;

esac
