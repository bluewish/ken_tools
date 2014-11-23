#!/bin/bash

local_gw=$1

# for github
route add -net 192.30.252.0 netmask 255.255.255.0 gw $local_gw

# for wx.qq.com
route add -net 140.206.160.0 netmask 255.255.255.0 gw $local_gw

# for music.163.com
route add -net 123.58.180.0 netmask 255.255.255.0 gw $local_gw
