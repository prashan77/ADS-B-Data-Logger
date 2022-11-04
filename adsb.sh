
#!/bin/bash


#run ads-b data logger script every second
while true
do
    python3 ADS-B_logger.py &
    sleep 1
done