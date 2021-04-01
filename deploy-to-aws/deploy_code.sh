#!/bin/bash

echo "Starting Script"
echo "Please make sure passwordless ssh is working for ubuntu@publicdnsname using the key provided as argument to the script"
echo "i.e ssh -i <key> ubuntu@<ec2-public-dns-name> should be working"
echo -e "Pausing script for 5s, exit out of the script if the above is not setup\n"
sleep 5

argumentList=("$@")
argumentLength=${#argumentList[@]}
awsPrivateKey=${argumentList[0]}

if [[ $argumentLength -eq 0 ]];
then
    echo "Usage ./deploy_code.sh <path-to-private-key> <public-dns-1> <public-dns-2>"
    exit 1
fi

echo -e "Making sure permission of private key $awsPrivateKey is 400\n"
chmod 400 "$awsPrivateKey"

echo -e "Shipping and running the installer script to all provided ec2 instances\n"
for (( i=1; i<${argumentLength}; i++ ));
do
    echo "Started with ${argumentList[$i]}"
    echo "Scping setup.tar.gz to the server"
    scp -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR -i $awsPrivateKey setup.tar.gz ubuntu@${argumentList[$i]}:~/
    
    echo "Untarring setup.tar.gz on the server"
    ssh -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR -i $awsPrivateKey ubuntu@${argumentList[$i]} 'tar -xzf setup.tar.gz'

    echo "Setting up the dependencies"
    ssh -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR -i $awsPrivateKey ubuntu@${argumentList[$i]} './setup.sh 2> setup.log'

    if [[ $i -ne 4 ]]; 
    then
        echo "Shipping docker-compose.yml to the server"
        scp -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR -i $awsPrivateKey docker-compose$i.yml ubuntu@${argumentList[$i]}:~/BookStore_Pygmy_Microservices/docker-compose.yml

        echo "Building and Starting the docker containers"
        ssh -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR -i $awsPrivateKey ubuntu@${argumentList[$i]} './start_containers.sh'
    fi

    echo ""
done

echo "All instances setup, containers are running. You can now login to the 4th server and run tests from there"
