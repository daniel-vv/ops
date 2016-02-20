#!/bin/bash
# Des: check VPN network
# Author: Daniel
# Date: 2015/11/25 13:02
# Version: 1.0

IP1=10.1.1.122
NET1=10.1.1.0/24
IP2=10.1.2.18
NET2=10.1.2.0/24
IP3=10.1.3.11
NET3=10.1.3.0/24
IP4=10.1.4.196
NET4=10.1.4.0/24


GW=`route -n|grep '^10.100.0.0' |awk '{print $2}'`

check() {
	ping -c 3 -w 5 $1 &> /dev/null
	return $?
}

Addroute() {
	ip route add $2 via $GW
}

Unrechable() {
	echo '=================================================='
	echo -e "\033[1;31m $1 network is not unreachable\033[0m" 
	echo -e "\033[1;31m Add routing entries $1......\033[0m"
 	echo '=================================================='	
}


echo_add_complate() {
	echo -e "\033[1;31m The successful route add $1 \033[0m"
}
echo_add_falure() {
	echo -e "\033[1;31m The falure route add $1 \033[0m"
}

check_route() {
NET=`echo "$2"|awk -F'/' '{print $1}'`
if ! check $1;then
	Unrechable $2
	if ! route -n|grep "$NET" &>/dev/null;then
		Addroute $1 $2
		if [ $? -eq 0 ];then
			echo -e "\033[1;31m $2 network add is complate\033[0m"
			if check $1;then
				echo_add_complate $2
			else
				echo_add_falure $2
			fi
		fi
	fi
else
	echo "$2 is available!"
		
fi
}

# Check AWS network
check_route $IP1 $NET1 
check_route $IP2 $NET2
check_route $IP3 $NET3 
check_route $IP4 $NET4 


#CHECK bj office network
IP40=192.168.40.253
NET40=192.168.40.0/24
check_route $IP40 $NET40

# check FZ IDC 1 
IP201=172.20.1.253
NET201=172.20.1.0/24
check_route $IP201 $NET201

# check FZ IDC 1 
IP206=172.20.6.205
NET206=172.20.6.0/24
check_route $IP206 $NET206

# check FZ offece 17 
IP17=192.168.17.253
NET17=192.168.17.0/24
check_route $IP17 $NET17

# check Ucloud Net 10
IP10=10.10.172.222
NET10=10.10.0.0/16
check_route $IP10 $NET10

# check FZ offece 10
#IP10=192.168.10.253
#NET10=192.168.10.253/24
#check_route $IP10 $NET10
