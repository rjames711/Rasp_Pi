#!/bin/bash
shopt -s expand_aliases
#echo "setting up terminal aliases"
function set_aliases(){
	echo "setting aliases"
	alias run="python test_step.py"
	alias p="pwd"
	echo "aliases set"
}
set_aliases

function run(){
python step_motor.py
}