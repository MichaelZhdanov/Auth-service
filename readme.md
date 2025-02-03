Use 2 servers and docker-compose on them for each node.

If fetching dependencies from Russian IP address, VPN/proxy might me required on certain steps :-(

All auth-pages are allocated to different subnets.

Load between 1 - 2 (node 1) and 3 - 4 (node 2) is balanced with haproxy.

Load between those nodes is balanced with keepalived. Nodes are avaliable on port 8080 of keepavlied VIP.

Keepalived does **not** run in docker, required to install in system on each server

Simple python backend for registration and auth is provided.


