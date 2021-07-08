# weblogic-ansible
<!-- Piwik Image Tracker -->
<noscript>
<img src="http://www.link.net.gr/piwik/piwik.php?idsite=1&rec=1" style="border:0" alt="" />
</noscript>
<!-- End Piwik -->

An Ansible Playbook (weblogic-fmw-domain.yml) for install and configure a WebLogic server 10.3.6 with 
Oracle Fusion Middleware software for hosting Oracle Fusion Middleware applications in Redhat Linux 7 (RHEL/CentOS/Oracle Linux) system.
This playbook is for version 10.3.6 of WebLogic and Fusion Middleware Infrastructure software.

Requirements for running the playbook:
- Configure your environment variables in infra-vars.yml. 
- Set your passwords in secrets.yml.
- A running Oracle Database for hosting the repositories is required and sys user password for generates the repositories.
- A running RHEL 7 system with minimal installation with network configured. (IP address, hostname etc).
- Download the latest Java jdk and put the file in roles/linux-jdk/files and configure infra-vars.yml with that file name.
- Download the 10.3.6 Oracle Fusion Middleware installer from Oracle support and put it in roles/fmw-software/files

The playbook includes the following Ansible Roles:
- linux-wls: Configures the linux system with required packages, kernel settings etc.
- linux-jdk: Installs Oracle JDK 7.
- fmw-software: Installs Oracle Fusion Middleware Infrastructure software.


<!--For test the playbook you can download Vagrant and Virtual Box and then run: 
- $ vagrant plugin install vagrant-hostmanager
- $ vagrant up

vagrant will provision vm with ansible playbook automatically

When the playbook finishes execution you can connect to weblogic server using wls12c1.private:7001/console.-->

For execute it alone use the following command
- $ ansible-playbook weblogic-fmw-domain.yml
