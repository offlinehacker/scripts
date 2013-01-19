#!/bin/bash
sudo badvpn-tun2socks --tundev tun0 --netif-ipaddr 10.0.0.2 --netif-netmask 255.255.255.0 --socks-server-addr 192.168.2.1:9050 &
sudo ifconfig tun0 10.0.0.1
sudo route add default gw 10.0.0.1
