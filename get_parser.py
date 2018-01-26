#!/usr/local/bin/python2.7
# -*- coding: UTF-8 -*-
#
#  Parse args for thorughpy with argparse
#


from argparse import ArgumentParser


def set_parser(options="args"):

    parser = ArgumentParser()
    parser.add_argument(
      "-s", dest="server", action="store",
      help="IP of server to connect")
    parser.add_argument(
      "-t", dest="time", action="store",
      help="Choose time to execute the test in seconds")
    parser.add_argument(
      "-d", dest="data", action="store",
      help="Choose data to execute the test in MegaBytes")
    parser.add_argument(
      "-np", dest="n_ports", action="store",
      help="\
        Choose number of ports to use. For tests with more \
        than one port, specified it separated by a colon(,). \
        To test a range of ports use 1..10. \
        To test a range of ports with a interval use 1..100..10, \
        where the last sequence is the interval of ports.\
        Range can't start with 0. \
        NUMBER MAX OF PORTS IS 128",
      default="1")

    if options != "help":
        return parser.parse_args()
    else:
        parser.print_help()
