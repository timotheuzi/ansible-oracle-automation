# robotic-tim-weblogic-installer

Tim's Ansible Playbook (weblogic-fmw-domain.yml) for installing and configuring a WebLogic server 10.3.6 with 
Oracle Fusion Middleware software. 

Requirements for running the playbook:
- Configure your environment variables in infra-vars.yml. 
- Set your passwords in secrets.yml.
- A running Oracle Database for hosting the repositories is required as is the sys user password for generating the repositories. Can be cloud or local database.
- A running RHEL 7 system with minimal installation with network configured. (IP address, hostname etc).
- Download the latest Java jdk and put the file in roles/linux-jdk/files and configure infra-vars.yml with that file name.
- Download the 10.3.6 Oracle Fusion Middleware installer from Oracle support and put it in roles/fmw-software/files.

For execute it alone use the following command
- $ ansible-playbook weblogic-fmw-domain.yml

Author and Owner - timotheuzi
