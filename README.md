# NginX load balancer/reverse proxy server

This show cases use of NGINX container to load balance the incoming traffic to upstream servers. 

####Version 1.0: (tag v1.0)

To keep it simple, this version assumes that there are two different applications (app1, app2) and nginx server load balances the incoming traffic to either using round robin algorithm

##### To run it:

        docker-compose up --build
Then direct your web browser to "http://localhost:8080/". Refresh the page multiple times. The page should toggle between: 

        "This is App 1 :)" 
    and
        "This is App 2 :)"

* Relevant files/folders for this version are: app1, app2, nginx, and docker-compose.yml


####Version 2.0: (tag v2.0)

This version scales up a single app (app-scalable) and uses NginX server to load balance the incoming traffic to running upstreams.

##### To run it:

         docker-compose -f docker-compose-scalable.yml  up --scale webapp=5 --build
Then direct your web browser to "http://localhost:8080/". The page should show you a simple message like

        This web application is running on host:"9f15b2d0b0f0" with ip:"172.25.0.3"
Refresh the page, and host and ip should change depending on which upstream server is being used.

* Adjust "--scale webapp=5" to match the number of instances you  like to run.  

* Relevant files/folders for this version are: app-scalable, nginx-scalable, and docker-compose-scalable.yml
    


