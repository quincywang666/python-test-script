#!/bin/bash

for ii in 123 456
	do
	arr=(${ii})
	for((i=0;i<${#arr[@]};i++))
	do
	echo  "\033[36m${arr[i]}\n\033[0m"
	done
	echo "\033[33m please Select[0/1/2/3...]:\033[0m"
	read sl
	sel_tag=$(echo "${arr[$sl]}")
	echo ${sel_tag}
	
done
