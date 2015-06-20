drop table if exists entries;

create table stations (
  id integer primary key autoincrement,
  name text not null,
  longitude float not null,
  latitude float not null
);

create table trips (
  id integer primary key autoincrement,
  startStation integer,
  startMonth integer,
  startDay integer,
  startYear integer,
  startTime integer,
  startWeekDay integer,
  endStation integer,
  endMonth integer,
  endDay integer,
  endYear integer,
  endTime integer,
  endWeekDay integer,
  foreign key (startStation) references stations(name)
  foreign key (endStation) references stations(name)
);