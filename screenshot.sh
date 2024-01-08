#!/bin/bash

case $1 in

  current_window|current-window)
    FILE_NAME="Screenshot_`date '+%Y%m%d_%H%M%S'`.png"
    DIR_NAME=`xdg-user-dir PICTURES`
    DIR_NAME="${DIR_NAME}/Screenshots"
    scrot -u -b ${DIR_NAME}/${FILE_NAME} 
    notify-send "Saved to ${FILE_NAME}"
    ;;
  
  screenshot)
    spectacle -m -b
    ;;

  region)
    spectacle -r -b
    ;;
  
  *)
    echo "Usage: $0 [screenshot|current_window|region]"
    exit 1
    ;;

esac

