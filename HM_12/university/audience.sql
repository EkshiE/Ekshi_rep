create table university.audience
(
    id           int auto_increment
        primary key,
    name         varchar(40)  not null,
    id_audience  int          not null,
    disciplines  varchar(100) not null,
    name_teacher varchar(40)  null,
    constraint id
        unique (id),
    constraint fk_1
        foreign key (id) references university.students (id)
            on update cascade
);

