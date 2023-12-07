#!/bin/bash

case $1 in

  current_window)
    FILE_NAME="Screenshot_`date '+%Y%m%d_%H%M%S'`.png"
    DIR_NAME="${HOME}/Pictures/Screenshots"
    scrot -u -b ${DIR_NAME}/${FILE_NAME} 
    notify-send "Saved to ${FILE_NAME}"
    ;;
  
  screenshot)
    spectacle -r
    ;;
  
  *)
    echo "Usage: $0 [current_window]"
    exit 1
    ;;

esac

