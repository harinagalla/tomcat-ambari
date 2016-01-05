# tomcat-ambari
#### An Ambari Stack for Tomcat
Ambari stack for easily installing and managing TOMCAT on HDP cluster

####To deploy the tomcat, 
```
cd /var/lib/ambari-server/resources/stacks/HDP/2.3/services
git clone https://github.com/harinagalla/tomcat-ambari.git   
```

####Restart Ambari

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
    rm -rf /var/lib/ambari-server/resources/stacks/HDP/2.3/services/TOMCAT
    ```
  - Restart Ambari
    ```
    service ambari restart
    ```
    
