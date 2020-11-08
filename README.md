# NginX load balancer/reverse proxy server

This show cases use of NGINX container to load balance the traffic on two upstream servers. 

To keep it simple, it assumes that there are two different applications (app1, app2) and nginx server load balances the incoming traffic to either using round robin algorithm

## How?
To run it, simply do:

        docker-compose up --build
Then direct your web browser to "http://localhost:8080/"

Refresh the page multiple times. The page should toggle between "This is App 1 :)" and "This is App 2 :)"


    


