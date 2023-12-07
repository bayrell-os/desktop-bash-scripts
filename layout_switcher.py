#!/usr/bin/env python3

from pynput import keyboard
import sys
import os

# Current pressed keys
key_pressed = set()

# Keys for toggle layout keyboard switch
toggle_switch = { keyboard.Key.ctrl, keyboard.Key.shift }

# Toggle layout keyboard switch commands
toggle_ru = "/usr/bin/setxkbmap -layout ru,us -option ''"
toggle_us = "/usr/bin/setxkbmap -layout us -option ''"
toggle_next = toggle_ru

# Clear keyboard layout
os.system("/usr/bin/setxkbmap -layout us -option ''")


def any_equal(s1, s2):
	
	for k in s1:
		if k in s2:
			return True
	
	return False
	
	
def in_equal(s1, s2):
	
	for k in s1:
		if not (k in s2):
			return False
	
	return True
	
	
def is_set_equal(s1, s2):
	
	if not in_equal(s1, s2):
		return False
	if not in_equal(s2, s1):
		return False
	
	return True
	
	
def toggle():
    
	global toggle_next
	
	
	if is_set_equal(key_pressed, toggle_switch):
		
		print (toggle_next)
		os.system(toggle_next)
		
		if (toggle_next == toggle_ru): toggle_next = toggle_us
		else: toggle_next = toggle_ru
		
		
pass


def on_press(key):
	
	valid_key = None
	
	if isinstance(key, keyboard.Key):
		
		if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r or key == keyboard.Key.shift:
			valid_key = keyboard.Key.shift
		
		elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r or key == keyboard.Key.ctrl:
			valid_key = keyboard.Key.ctrl
		
	
	if valid_key == None:
		valid_key = key
	
		
	if valid_key != None:
		if not(valid_key in key_pressed):
			key_pressed.add(valid_key)
			
			#print(key_pressed)
		
		if not any_equal(key_pressed, toggle_switch):
			key_pressed.clear()
		
pass	


def on_release(key):
	
	toggle()
	
	valid_key = None
	
	if isinstance(key, keyboard.Key):
		
		if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r or key == keyboard.Key.shift:
			valid_key = keyboard.Key.shift
			
		elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r or key == keyboard.Key.ctrl:
			valid_key = keyboard.Key.ctrl
		
	elif isinstance(key, keyboard._xorg.KeyCode):
		if key.vk == 65032:
			valid_key = keyboard.Key.shift
	
	if valid_key == None:
		valid_key = key
	
	if valid_key in key_pressed:
		key_pressed.remove(valid_key)
		
		#print(key_pressed)
	
pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
