#!/bin/bash
folder_in=00_Master
folder_out=1

# name folder like: SC_Voltage_Case
# e.g. 1_80_2

sc=0
#~ cp -r ${folder_in} ${sc}_${vol}_${vol_case}
cp -r ${folder_in} ${sc}_70_0
cp -r ${folder_in} ${sc}_85_0

sc=1
vol=70
cp -r ${folder_in} ${sc}_${vol}_0
cp -r ${folder_in} ${sc}_${vol}_1
cp -r ${folder_in} ${sc}_${vol}_2

vol=85
cp -r ${folder_in} ${sc}_${vol}_0
cp -r ${folder_in} ${sc}_${vol}_1
cp -r ${folder_in} ${sc}_${vol}_2