# Lab2 COMPSCI 677

## Book Store
This project will implement a book store. The store will employ a two-tier web design - a front-end and a back-end - and use microservices at each tier. The front-end tier will accept user requests and perform initial processing.

## :hammer_and_wrench: Requirements
* Operating System: Linux / MacOS X
* Docker (Above 17.04.0+)
* Docker-compose (Above 3.2)

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
curl http://localhost:8080/health
```

6. Checking the logs
```
docker logs -f frontend
```

### :man_technologist: Maintainers
- [Noel Varghese](https://github.com/envy7)
- [Nishant Raj](https://github.com/Nishant3815)
- [Rishika Bharti](https://github.com/rishikabharti)

