#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-


import re
from subprocess import check_output


def get_data(ports, g_opts):

    if g_opts.time:
        command = "iperf3 -c {} -t {} -P {}; exit 0".format(
          g_opts.server, g_opts.time, ports)
    elif g_opts.data:
        command = "iperf3 -c {} -n {}M -P {}; exit 0".format(
          g_opts.server, g_opts.data, ports)

    data_pkt = check_output([command], shell=True)

    if int(ports) == 1:
        p = re.compile(r'\[\ +[0-9]+\].*bits\/sec')
    else:
        p = re.compile(r'\[SUM\].*bits\/sec')

    return p.findall(data_pkt)
