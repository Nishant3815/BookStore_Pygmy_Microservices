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

### :man_technologist: Maintainers
- [Noel Varghese](https://github.com/envy7)
- [Nishant Raj](https://github.com/Nishant3815)
- [Rishika Bharti](https://github.com/rishikabharti)
