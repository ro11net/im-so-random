#!/bin/env bash


S1_HOSTNAME=bm1
S2_HOSTNAME=bm2
S3_HOSTNAME=bm3
S1_IP=10.10.10.1
S2_IP=10.10.10.2
S3_IP=10.10.10.3
DOMAIN=domain.corp
VIP_IP=10.10.10.5
VIP_HOSTNAME=vip
declare -A S1=( ${S1_HOSTNAME} ${S1_IP} )
declare -A S2=( ${S2_HOSTNAME} ${S2_IP} )
declare -A S3=( ${S3_HOSTNAME} ${S3_IP} )
declare -a serverdict=("S1" "S2" "S3")

for server in "${serverdict[@]}"; do
    echo "$server :"
    declare -n p="$server"  # now p is a reference to a variable "$member"
    for attr in "${!p[@]}"; do
        echo -e "    Hostname: $attr \n    IP: ${p[$attr]}"
        mkdir -p /home/rollnet/shell/$attr
        echo -e "
127.0.0.1   localhost localhost.local{domain} localhost4 localhost4.local{domain}4
::1         localhost localhost.local{domain} localhost6 localhost6.local{domain}6
${p[$attr]} $attr $attr.${DOMAIN}
${VIP_IP} ${VIP_HOSTNAME} ${VIP_HOSTNAME}.${DOMAIN}"
