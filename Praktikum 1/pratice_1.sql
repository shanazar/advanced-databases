CREATE DATABASE soccer;
CREATE SCHEMA IF NOT EXISTS newEuropeanSoccer;


-- Base entities --
CREATE TABLE neweuropeansoccer.League (
                        leagueid SERIAL UNIQUE,
                        name_league VARCHAR(100),
                        country VARCHAR(100),
                        CONSTRAINT PK_league PRIMARY KEY (leagueid)
);

CREATE TABLE neweuropeansoccer.Team (
                      teamid SERIAL UNIQUE,
                      nameteam VARCHAR(100),
                      shortname VARCHAR(3),
                      leagueid INT,
                      CONSTRAINT PK_team PRIMARY KEY (teamid),
                      CONSTRAINT FK_team_league FOREIGN KEY (leagueid) REFERENCES neweuropeansoccer.League(leagueid)
);

CREATE TABLE neweuropeansoccer.Season (
                        seasonid SERIAL UNIQUE,
                        nameseason VARCHAR(100),
                        datestart DATE,
                        dateend DATE,
                        CONSTRAINT PK_season PRIMARY KEY (seasonid)
);

CREATE TABLE neweuropeansoccer.Player (
                        playerid SERIAL UNIQUE,
                        lastnameplayer VARCHAR(100),
                        firstnameplayer VARCHAR(100),
                        birth DATE,
                        height INT, -- assuming height is stored in cm
                        weight INT -- assuming weight is stored in kilograms
);
CREATE TABLE neweuropeansoccer.Match (
                       matchid SERIAL UNIQUE,
                       datematch DATE,
                       localscore INT,
                       visitorscore INT,
                       leagueid INT,
                       teamid_local INT,
                       teamid_visitor INT,
                       seasonid INT,
                       CONSTRAINT PK_match PRIMARY KEY (matchid),
                       CONSTRAINT FK_match_league FOREIGN KEY (leagueid) REFERENCES neweuropeansoccer.League(leagueid),
                       CONSTRAINT FK_match_team_1 FOREIGN KEY (teamid_local) REFERENCES neweuropeansoccer.Team(teamid),
                       CONSTRAINT FK_match_team_2 FOREIGN KEY (teamid_visitor) REFERENCES neweuropeansoccer.Team(teamid)
);

-- Relationships --

CREATE TABLE neweuropeansoccer.MARK (
                      playerid INT,
                      matchid INT,
                      minutes_played INT,
                      CONSTRAINT FK_mark_player FOREIGN KEY (playerid) REFERENCES Player(playerid),
                      CONSTRAINT FK_mark_match FOREIGN KEY (matchid) REFERENCES Match(matchid)
);

CREATE TABLE neweuropeansoccer.ENGAGE (
                        teamid INT,
                        seasonid INT,
                        playerid INT,
                        CONSTRAINT FK_engage_team FOREIGN KEY (teamid) REFERENCES neweuropeansoccer.Team(teamid),
                        CONSTRAINT FK_engage_season FOREIGN KEY (seasonid) REFERENCES neweuropeansoccer.Season(seasonid),
                        CONSTRAINT FK_engage_player FOREIGN KEY (playerid) REFERENCES neweuropeansoccer.Player(playerid)
);
