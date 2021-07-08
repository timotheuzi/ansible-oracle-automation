alter profile DEFAULT limit PASSWORD_LIFE_TIME UNLIMITED;

grant scheduler_admin to inspy_ap;
grant create job to inspy_ap;
grant create synonym to inspy_ap;
grant execute on utl_http to inspy_ap;
GRANT CREATE ANY DIRECTORY TO inspy_ap;

grant create session to inspy_ap;
grant create table to inspy_ap;
grant create sequence to inspy_ap;
grant create view to inspy_ap;
grant create type to inspy_ap;
grant create procedure to inspy_ap;
grant create trigger to inspy_ap;

grant create session to inspy_config;
grant create table to inspy_config;
grant create sequence to inspy_config;
grant create view to inspy_config;
grant create type to inspy_config;
grant create procedure to inspy_config;
grant create trigger to inspy_config;

grant create session to inspy_sc;
grant create table to inspy_sc;
grant create sequence to inspy_sc;
grant create view to inspy_sc;
grant create type to inspy_sc;
grant create procedure to inspy_sc;
grant create trigger to inspy_sc;

-- this statement needs to be run when dynamic discounting is implemented
create or replace directory INSPY_CASH_LIMIT_DIR as '{{ oracle_base }}/product/12.1.0/cashlimits';
grant read on directory INSPY_CASH_LIMIT_DIR TO inspy_ap;
