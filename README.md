# tomcat-ambari
#### An Ambari Stack for Tomcat
Ambari stack for easily installing and managing TOMCAT on HDP cluster


###Assumptions

- Ambari is installed and running. If not, you can use sandbox VM Image provided by [Hortonworks website](http://hortonworks.com/products/hortonworks-sandbox/)
- No previous installations of tomcat exist. If there any, you can either remove it or rename it.

Follow given step to install and manage tomcat using Ambari.

####Connect to the VM via SSH (password hadoop for sandbox image) and start Ambari server
```
ssh root@ambari.machine
```

####To deploy the tomcat, run below
```
cd /var/lib/ambari-server/resources/stacks/HDP/2.2/services
git clone https://github.com/harinagalla/tomcat-ambari.git   
```

####Restart Ambari
#####on sandbox
```sudo service ambari restart```

#####on non-sandbox
```sudo service ambari-server restart```

#### Remove tomcat

- To remove the Tomcat: 
  - Stop the service via Ambari
  - Delete the service
  
    ```
    curl -u admin:admin -i -H 'X-Requested-By: ambari' -X DELETE http://replace_with_your_ambari_hostname.com:8080/api/v1/clusters/ambari_cluster_name/services/TOMCAT
    ```
  - Remove artifacts 
  
    ```
    rm -rf /var/lib/ambari-server/resources/stacks/HDP/2.2/services/TOMCAT
    ```
  - Restart Ambari
    ```
    service ambari restart
    ```
    
