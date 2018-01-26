#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
#
#  Use iperf3 to get throughput of interfaces and print a formatted output
#  Silvio Ap Silva a.k.a Kanazuchi <contato@kanazuchi.com>
#


import re
import sys
from get_parser import set_parser
from subprocess import check_output


def get_data(ports):

    if opts.time:
        command = "iperf3 -c {} -t {} -P {}; exit 0".format(
              opts.server, opts.time, ports)
    elif opts.data:
        command = "iperf3 -c {} -n {}M -P {}; exit 0".format(
              opts.server, opts.data, ports)
    else:
        set_parser("help")

    data_pkt = check_output([command], shell=True)

    if int(ports) == 1:
        p = re.compile(r'\[\ +[0-9]+\].*bits\/sec')
    else:
        p = re.compile(r'\[SUM\].*bits\/sec')

    return p.findall(data_pkt)


def main():

    get_n_ports = opts.n_ports.split(',')

    if len(get_n_ports) == 1 and ".." in get_n_ports[0]:
        ranges = get_n_ports[0].split('..')
        if (len(ranges) == 2):
            n_ports = range(int(ranges[0]), int(ranges[1]))
        elif len(ranges) == 3:
            n_ports = range(int(ranges[0]), int(ranges[1]), int(ranges[2]))
    else:
        n_ports = get_n_ports

    try:
        print('')
        for port in n_ports:

            if int(port) > 128 or int(port) < 1:
                set_parser("help")

            sum_data = get_data(port)
            if int(port) == 1:
                f_data = 6
            else:
                f_data = 5
            print("#####  Test using {} ports  #####".format(port))
            print("Bandwidth min: {}".format(min([int(x.split()[f_data].split('.')[0]) for x in sum_data])))
            print("Bandwidth max: {}".format(max([int(x.split()[f_data].split('.')[0]) for x in sum_data])))
            print("Bandwidth media: {}".format(
              " ".join([sum_data[-1].split()[f_data], sum_data[-1].split()[f_data+1]])))
            if opts.data:
                print("Time to transfer {} Mb: {} seconds".format(opts.data, sum_data[-1].split()[-6].split('-')[1]))

            print('')
    except UnboundLocalError:
        pass
    except Exception, error:
        print error


if __name__ == "__main__":
    opts = set_parser()
    main()
