Use build-all to build and start project for the first time on single machine. Docker and docker-compose are required.

down-all for stopping, start-all for starting.

All auth-pages are allocated to different subnets.

Load between 1 - 2 (node 1) and 3 - 4 (node 2) is balanced with haproxy.

Load between those nodes is balanced with keepalived (work in progress...)

Simple python backend for registration and auth is provided.

Node 1 is avaliable on localhost:8081, node 2 - localhost:8082

Enjoy!
