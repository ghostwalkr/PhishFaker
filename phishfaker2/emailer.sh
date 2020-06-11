#!/bin/bash

for name in $(cat names.txt); do
	number=$(shuf -i 1-9999 -n 1)
	a=$(shuf -i 0-2 -n 1)
	if test $a == 0; then
		seperator="."
	elif test $a == 1; then
		seperator="_"
	elif test $a == 2; then
		seperator="-"
	fi

	a=$(shuf -i 0-3 -n 1)
	if test $a == 0; then
		domain="@gmail.com"
	elif test $a == 1; then
		domain="@yahoo.com"
	elif test $a == 2; then
		domain="@outlook.com"
	elif test $a == 3; then
		domain="@aol.com"
	fi

	echo "$name$seperator$number$domain"
done
