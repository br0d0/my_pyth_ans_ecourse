#!/usr/bin/env python
# Class-based telnet connector

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6


class TelnetConn(object):
    # Establish and manage telnet connections

    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

        try:
            self.remote_conn = telnetlib.Telnet(self.ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out.")


    def login(self):
        # Login to network device

        output = self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(self.username + '\n')

        output += self.remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        self.remote_conn.write(self.password + '\n')

        time.sleep(1)
        return output


    def send_command(self, cmd="\n", sleep_time=1):
        # Send command down telnet channel and return response

        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(sleep_time)

        return self.remote_conn.read_very_eager()


    def disable_paging(self, paging_cmd="terminal length 0"):
        # Disable the paging of output; "-- More --"

        return self.send_command(paging_cmd)


    def close_conn(self):
        # Close telnet connection
        self.remote_conn.close()



def main():

    command = "show ip int brief"

    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()

    username = "pyclass"
    password = getpass.getpass()

    my_conn = TelnetConn(ip_addr, username, password)
    my_conn.login()
    my_conn.send_command()
    my_conn.disable_paging()

    output = my_conn.send_command(command)

    print
    print output
    print

    my_conn.close_conn()



if __name__ == "__main__":
    main()
            
