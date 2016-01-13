import sys, os, pwd, grp, signal, time, glob
from resource_management import *
from subprocess import call

class Master(Script):
  def install(self, env):
  	import params
  	import status_params
  	stable_package = 'http://download.nextag.com/apache/tomcat/tomcat-8/v8.0.30/bin/apache-tomcat-8.0.30.tar.gz'
  	service_packagedir = os.path.realpath(__file__).split('/scripts')[0]
  	
  	self.install_packages(env)
  	self.create_linux_user(params.tomcat_user, params.tomcat_group)
  	if params.tomcat_user != 'root':
  		Execute('cp /etc/sudoers /etc/sudoers.bak')
  		Execute('echo "'+params.tomcat_user+' ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers')
  		Execute('echo Creating ' + params.tomcat_log_dir + ' ' + status_params.tomcat_pid_dir)
  	
  	Directory([status_params.tomcat_pid_dir, params.tomcat_log_dir],
  	  owner=params.tomcat_user,
  	  group=params.tomcat_group,
  	  recursive=True
  	  )
  	Execute('touch ' + params.tomcat_log_file, user=params.tomcat_user)
  	Execute('rm -rf ' + params.tomcat_dir, ignore_failures=True)
  	Execute('rm '+ params.temp_file, ignore_failures=True)
  	Execute('mkdir -p ' + params.tomcat_dir)
  	Execute('chown -R ' + params.tomcat_user + ':' + params.tomcat_group + ' ' + params.tomcat_dir)
  	Execute('echo Installing pachages')
  	
  	if not os.path.exists(params.temp_file):
  	  Execute('wget ' + stable_package + ' -O ' + params.temp_file + ' -a ' + params.tomcat_log_file, user=params.tomcat_user)
  	Execute('tar xvf ' + params.temp_file+' -C ' + params.tomcat_install_dir +'/'+ params.tomcat_dirname + ' --strip-components=1 >> ' + params.tomcat_log_file, user=params.tomcat_user)
	Execute('rm '+params.temp_file) 	
  	self.configure(env,True)
  	
  def create_linux_user(self, user, group):
	  try: pwd.getpwnam(user)
	  except KeyError: Execute('adduser ' + user)
	  try: grp.getgrnam(group)
	  except KeyError: Execute('groupadd ' + group)
	  
  def configure(self, env, isInstall=False):
	  import params
	  import status_params
	  env.set_params(params)
	  env.set_params(status_params)
	  
  def stop(self, env):
	  import params
	  import status_params
	  self.set_conf_bin(env)
	  Execute(params.bin_dir+'/shutdown.sh >>' + params.tomcat_log_file, user= params.tomcat_user)
	  Execute('rm '+status_params.tomcat_pid_file)

  def start(self, env):
	  import params
	  import status_params
	  self.configure(env)
	  self.set_conf_bin(env)
	  #Execute('echo pid file ' + status_params.tomcat_pid_file)
	  
	 #Execute(params.bin_dir+'/startup.sh >> ' + params.tomcat_log_file, user=params.tomcat_user)
	  
	  #Execute('cat '+params.bin_dir+'/tomcat.pid'+" | grep pid | sed 's/pid=\(\.*\)/\\1/' > " + status_params.tomcat_pid_file)
    	  #Execute('chown '+params.tomcat_user+':'+params.tomcat_group+' ' + status_params.tomcat_pid_file)
    	  Execute('touch ' + params.tomcat_lock_file)
	  Execute('chown ' + params.tomcat_user + ':' + params.tomcat_group + ' ' + params.tomcat_lock_file)
	  Execute(params.bin_dir+'/startup.sh >> ' + params.tomcat_log_file, user= params.tomcat_user)
	  Execute('mkdir -p '+status_params.tomcat_pid_dir)
	  Execute('chown -R ' + params.tomcat_user + ':' + params.tomcat_group + ' ' +status_params.tomcat_pid_dir)
	  Execute('ps -ef | grep -i tomcat | awk {\'print $2\'} | head -n 1 > ' + status_params.tomcat_pid_file, user= params.tomcat_user)
	  
    
  def status(self, env):
    	import status_params       
    	check_process_status(status_params.tomcat_pid_file)
	  
  def set_conf_bin(self, env):
    	import params
	params.conf_dir = os.path.join(*[params.tomcat_install_dir,params.tomcat_dirname,'conf'])
    	params.bin_dir = os.path.join(*[params.tomcat_install_dir,params.tomcat_dirname,'bin'])
	  
if __name__ == "__main__":
  Master().execute()
