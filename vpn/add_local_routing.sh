#!/bin/bash

local_gw=$1

# for github
route add -net 192.30.252.0 netmask 255.255.255.0 gw $local_gw
