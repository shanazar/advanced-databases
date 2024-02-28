CREATE SCHEMA IF NOT EXISTS oldEuropeanSoccer;

-- Imported the tables form the sqllite file into the oldEuropeanSoccer schema.

INSERT INTO neweuropeansoccer.league
    SELECT
        L.id,
        L.name,
        C.name
    FROM oldeuropeansoccer."League" as L
        LEFT JOIN oldeuropeansoccer."Country" as C on L.country_id = C.id
;

INSERT INTO neweuropeansoccer.player
    SELECT player_api_id as id,
           substring(player_name , '^\S+') as firstnameplayer,
           substring(player_name, '^\S+\s+(.*)') as lastnameplayer,
           date(birthday) as birth,
           height,
           weight
    FROM oldeuropeansoccer."Player"
;

INSERT INTO neweuropeansoccer.team
    SELECT DISTINCT
        T.team_api_id,
        T.team_long_name as nameteam,
        T.team_short_name as shortname,
        M.league_id as leagueid
    FROM oldeuropeansoccer."Team" as T
        LEFT JOIN oldeuropeansoccer."Match" as M ON M.home_team_api_id = T.team_api_id
;

INSERT INTO neweuropeansoccer.season (nameseason, datestart, dateend)
    SELECT season as nameseason,
           DATE(min(date)) as season_start,
           date(max(date)) as season_end
    FROM oldeuropeansoccer."Match"
    GROUP BY season
;

INSERT INTO neweuropeansoccer.match
    SELECT
        M.match_api_id as matchid,
        MAX(date(M.date)) as datematch,
        MAX(M.home_team_goal) as localscore,
        MAX(M.away_team_goal) as visitorscore,
        M.league_id as league_id,
        M.home_team_api_id as matchid_local,
        M.away_team_api_id as team_id_visitor,
        S.seasonid as seasonid
    FROM oldeuropeansoccer."Match" as M
             LEFT JOIN neweuropeansoccer.season as S ON M.season = S.nameseason
    GROUP BY M.match_api_id, M.league_id, M.home_team_api_id, M.away_team_api_id, S.seasonid
;


INSERT INTO neweuropeansoccer.mark (matchid, playerid)
        SELECT DISTINCT match_api_id AS matchid, home_player_1 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, home_player_2 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, home_player_3 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, home_player_4 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, home_player_5 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, home_player_6 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, home_player_7 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, home_player_8 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, home_player_9 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, home_player_10 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, home_player_11 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_1 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_2 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_3 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_4 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_5 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_6 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_7 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_8 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_9 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_10 AS playerid
        FROM oldeuropeansoccer."Match"
    UNION
        SELECT DISTINCT match_api_id AS matchid, away_player_11 AS playerid
        FROM oldeuropeansoccer."Match"
;

INSERT INTO neweuropeansoccer.engage
        SELECT DISTINCT
            match.teamid_local as teamid,
            match.seasonid as seasonid,
            mark.playerid as playerid
        FROM neweuropeansoccer.mark as mark
                 LEFT JOIN neweuropeansoccer.match as match ON mark.matchid = match.matchid
    UNION
        SELECT DISTINCT
            match.teamid_visitor as teamid,
            match.seasonid as seasonid,
            mark.playerid as playerid
        FROM neweuropeansoccer.mark as mark
                 LEFT JOIN neweuropeansoccer.match as match ON mark.matchid = match.matchid
;