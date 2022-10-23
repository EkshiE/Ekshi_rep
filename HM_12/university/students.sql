create table university.students
(
    id                      int auto_increment
        primary key,
    name                    varchar(40) not null,
    `date of birth`         date        not null,
    `identification number` varchar(14) not null,
    `group`                 int         not null,
    constraint id
        unique (id)
);

