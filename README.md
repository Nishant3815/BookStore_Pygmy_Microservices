# Lab2 COMPSCI 677

## Book Store
This project will implement a book store. The store will employ a two-tier web design - a front-end and a back-end - and use microservices at each tier. The front-end tier will accept user requests and perform initial processing.

## :hammer_and_wrench: Requirements
* Operating System: Linux / MacOS X
* Docker (Above 17.04.0+)
* Docker-compose (Above 3.2)
* Python3
* Available Ports: 8000-8002 (This can be changed through the docker-compose file if needed) 

## :rocket: Quickstart
1. Clone the code 
```
git clone https://github.com/Nishant3815/BookStore_Pygmy_Microservices.git
```

2. cd to directory
```
cd BookStore_Pygmy_Microservices
```

3. Build the images
```
docker-compose build
```

4. Start the containers
```
docker-compose up -d
```

5. Check health of frontend
```
curl http://localhost:8000/health
```

6. Checking the logs
```
docker logs -f frontend
docker logs -f catalog
```

## :paintbrush: Running and Checking testcases
1. Follow the Quickstart section

2. Run the testcase client script
```
python3 run_api_tests.py
```

3. Check the logs of the various containers
```
docker logs -f <container-name>
docker logs -f frontend|order|catalog
```

4. Checking state of sqlite database
```
❯ docker exec -it sqlite sqlite3 bookstore.db
SQLite version 3.28.0 2019-04-16 19:49:53
Enter ".help" for usage hints.
sqlite> select * from books;
1|How to get a good grade in 677 in 20 minutes a day|Distributed Systems|200|200
2|RPCs for Dummies|Distributed Systems|200|200
3|Xen and the Art of Surviving Graduate School|Graduate School|200|200
4|Cooking for the Impatient Graduate Student|Graduate School|200|200
```

5. Checking the db queries done by catalog service
These queries can be used to reconstruct the sqlite db if needed
```
less logs/catalog.log
```

6. Running tests manually
Below curl calls can be used to test the application functionality manually
```
Search: curl "http://localhost:8000/search?topic=Graduate%20School"
Lookup: curl "http://localhost:8000/lookup?id=4"
Buy: curl -X POST -H 'Content-Type: application/json' "http://localhost:8000/buy" -d '{"id": 4}'
```

## :cloud: Deploying and running on AWS

### Pre-requisites
1. Make sure the instances running in AWS are running the latest version of Ubuntu OS. It might work even on previous versions but it hasn't been tested. The script has been tested for the following AMI ID(`ami-0b4eac045bf0ceb49`)
2. Ensure you have the private key through which you ssh to the ec2 instances present locally and have already ensured that ssh to the instances is working using this key. I.e `ssh -i <key> ubuntu@<ec2-public-dns-name>` is working
3. Have the private ips of your ec2 instances ready, as you will need to add these ips to the docker-compose files. You can find this ip by doing the command `ip a` and checking which ip is binded on eth0 interface. It should also be present in the aws console.

### Steps
1. cd to deploy-to-aws directory inside project directory
```
cd deploy-to-aws
```

2. To deploy the code to ec2 instances we need to change the docker-compose files and post that run the command shown

So we need 4 ec2 machines each hosting frontend, order, catalog and client in this order.
Before executing the above script edit docker-compose1.yml and docker-compose2.yml. Change the CATALOG_SERVICE_ENDPOINT and ORDER_SERVICE_ENDPOINT to the corresponding pvt ips of catalog-service-ec2-public-dns & order-service-ec2-public-dns respectively. This is how the services will know how to reach themselves internally within AWS. i.e
CATALOG_SERVICE_ENDPOINT=http://<catalog-ec2-instance-pvt-ip>:8080
ORDER_SERVICE_ENDPOINT=http://<order-ec2-instance-pvt-ip>:8080
```
./deploy_code.sh <path-to-private-key> <frontend-service-ec2-public-dns> <order-service-ec2-public-dns> <catalog-service-ec2-public-dns> <client-testing-ec2-public-dns>
```

Once the ips are changed, the deploy_code.sh script can be run as shown in the example. The first parameter to the script is the path to the private key which you use to ssh to the ec2 instances.

3. Check if services are running
SSH to the first 3 ec2 servers and check if the docker-containers are running properly, using the below command.
```
docker ps
```

4. Test the endpoints from the 4th ec2 instance post doing ssh to it
```
cd BookStore_Pygmy_Microservices
python3 run_api_tests.py -h <frontend-ec2-instance-pvt-ip> -p 8080
```

5. Further testing can be done by manually doing curl calls as highlighted in the running and checking testcases section
Ensure to replace localhost with ip and port 8000 with 8080

### :man_technologist: Maintainers
- [Noel Varghese](https://github.com/envy7)
- [Nishant Raj](https://github.com/Nishant3815)
- [Rishika Bharti](https://github.com/rishikabharti)
