#!/bin/sh

sudo tcpdump -n -i en0  | ./tcpdump_reader.py
