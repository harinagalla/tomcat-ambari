#!/usr/bin/env/ python
from resource_management import *
import sys, os

config = Script.get_config()

tomcat_pid_dir=config['configurations']['tomcat-bootstrap-env']['tomcat_pid_dir']
tomcat_pid_file=tomcat_pid_dir + '/tomcat.pid'
