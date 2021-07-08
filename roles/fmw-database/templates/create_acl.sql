begin
   DBMS_NETWORK_ACL_ADMIN.drop_acl ( 
   acl => 'INSPY_AP.xml'); 
   COMMIT;
end;

begin
    dbms_network_acl_admin.create_acl (
    acl => 'INSPY_AP.xml',
    description => 'Inspyrus AP Utilities',
    principal => 'INSPY_AP',
    is_grant => true,
    privilege => 'connect',
    start_date => null,
    end_date => null
    );
end;

begin
    DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE(
    acl => 'INSPY_AP.xml',
    principal => 'INSPY_AP',
    is_grant => true,
    privilege => 'resolve');
end;

--- Update host to the hostname for OSB ---
begin
    DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL(acl => 'INSPY_AP.xml',
    host => '{{ server_hostname }}');
end;
