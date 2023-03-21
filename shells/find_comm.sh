#!/bin/bash

dir1=$1
dir2=$2

( cd $dir1; find . -maxdepth 1 -type f -print | sort ) > dir1_file.lst
( cd $dir2; find . -maxdepth 1 -type f -print | sort ) > dir2_file.lst

comm dir1_file.lst dir2_file.lst
