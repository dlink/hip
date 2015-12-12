-- Create folks table

create table folks (
   id            integer unsigned auto_increment primary key ,
   phonenumber   varchar(15)      not null ,
   active        integer unsigned not null ,
   created       datetime         not null ,
   last_updated  timestamp        not null 
        default current_timestamp on update current_timestamp
) 
engine InnoDB default charset=utf8;
;

show warnings;

create trigger folks_created before insert on folks
   for each row set new.created = now()
;

desc folks;


-- Create quotes table

create table inspiration (
   id            integer unsigned auto_increment primary key ,
   quote         varchar(512) not null,
   created       datetime         not null ,
   last_updated  timestamp        not null 
        default current_timestamp on update current_timestamp
) 
engine InnoDB default charset=utf8;
;

show warnings;

create trigger inspiration_created before insert on inspiration
   for each row set new.created = now()
;

desc inspiration;
