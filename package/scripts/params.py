#!/usr/bin/env python
from resource_management import *
from resource_management.libraries.script.script import Script
import sys, os, glob
from resource_management.libraries.functions.version import format_hdp_stack_version
from resource_management.libraries.functions.default import default

# config object that holds the configurations declared in the config xml file
config = Script.get_config()

tomcat_dirname = 'apache-tomcat-8.0.30'

#params from tomcat-ambari-config
tomcat_install_dir = config['configurations']['tomcat-ambari-config']['tomcat.install_dir']
tomcat_port = config['configurations']['tomcat-ambari-config']['tomcat.port']
tomcat_log = config['configurations']['tomcat-ambari-config']['tomcat.log']

tomcat_dir = os.path.join(*[tomcat_install_dir,tomcat_dirname])
conf_dir=''
bin_dir=''

# params from tomcat-bootstrap

tomcat_user = config['configurations']['tomcat-bootstrap-env']['tomcat_user']
tomcat_group = config['configurations']['tomcat-bootstrap-env']['tomcat_group']
tomcat_log_dir = config['configurations']['tomcat-bootstrap-env']['tomcat_log_dir']
tomcat_log_file = os.path.join(tomcat_log_dir,'tomcat_setup.log')

tomcat_lock_file = '/var/lock/subsys/tomcat'


temp_file='/tmp/'+tomcat_dirname+'.zip'
