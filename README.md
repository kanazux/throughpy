# throughpy
### Test throughput of interface using iperf3
#### Version: 0.1

Execute tests for throughput with iperf3 and get some formatted responses

## USAGE:
usage: throughpy [-h] [-s SERVER] [-t TIME] [-d DATA] [-np N_PORTS]

```
optional arguments:  -h, --help show this help message and exit

	-s SERVER  IP of server to connect
	-t TIME  Choose time to execute the test in seconds
	-d DATA  Choose data to execute the test in MegaBytes
	-np N_PORTS  Choose number of ports to use.

	For tests with more than one  port, specified it separated by a colon(,).
	To test a range of ports use 1..10.
	To test a range of ports with a interval use  1..100..10, where the last sequence is the interval of ports.
	Range can't start with 0. NUMBER MAX OF PORTS IS 128
```

## Install
```
%> python setup.py install
%> pip throughpy install
```
### [\[PyPi\]](https://pypi.python.org/pypi/throughpy "throughpy on PyPi")

## Output formatted:
```
%> throughpy -s 159.2100.100.1 -d 1024 -np 1,2

#####  Test using 1 ports  #####
Bandwidth min: 50
Bandwidth max: 539
Bandwidth media: 529 Mbits/sec
Time to transfer 1024 Mb: 15.00 seconds

#####  Test using 2 ports  #####
Bandwidth min: 95
Bandwidth max: 986
Bandwidth media: 753 Mbits/sec
Time to transfer 1024 Mb: 11.37 seconds
```
