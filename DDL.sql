-- Active: 1719859538524@@127.0.0.1@5432@fpl_dwh@public
CREATE TABLE gameweeks (
    id VARCHAR(255) PRIMARY KEY,
    GW_name VARCHAR(255),
    deadline_time TIMESTAMP,
    highest_score INTEGER,
    average_entry_score INTEGER,
    most_selected VARCHAR(255),
    most_transferred_in VARCHAR(255),
    top_element VARCHAR(255),
    most_captained VARCHAR(255),
    most_vice_captained VARCHAR(255)
);

CREATE TABLE positions (
    id VARCHAR(255) PRIMARY KEY,
    plural_name VARCHAR(255),
    plural_name_short VARCHAR(255),
    singular_name VARCHAR(255),
    singular_name_short VARCHAR(255)
);

CREATE TABLE teams (
    code VARCHAR(255) ,
    id VARCHAR(255),
    team_name VARCHAR(255),
    short_name VARCHAR(255),
    strength INTEGER,
    strength_overall_away INTEGER,
    strength_overall_home INTEGER,
    strength_attack_away INTEGER,
    strength_attack_home INTEGER,
    strength_defence_away INTEGER,
    strength_defence_home INTEGER,
    PRIMARY KEY(id),
    UNIQUE(code)
);

CREATE TABLE players (
    code VARCHAR(255),
    id VARCHAR(255),
    full_name VARCHAR(255),
    web_name VARCHAR(255),
    element_type VARCHAR(255),
    team VARCHAR(255),
    team_code VARCHAR(255),
    dreamteam_count INTEGER,
    news TEXT,
    value_season FLOAT,
    PRIMARY KEY(id),
    UNIQUE(code),
    FOREIGN KEY(element_type) REFERENCES positions(id) ON DELETE CASCADE,
    FOREIGN KEY(team) REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE player_history (
    season_name VARCHAR(255),
    element_code VARCHAR(255),
    start_cost FLOAT,
    end_cost FLOAT,
    total_points INT,
    "minutes" INT,
    goals_scored INT,
    assists INT,
    clean_sheets INT,
    goals_conceded INT,
    own_goals INT,
    penalties_saved INT,
    penalties_missed INT,
    yellow_cards INT,
    red_cards INT,
    saves INT,
    bonus INT,
    PRIMARY KEY (season_name, element_code),
    CONSTRAINT fk_players FOREIGN KEY(element_code)
    REFERENCES players(code) ON DELETE CASCADE
);

CREATE TABLE fact_table (
    element VARCHAR(255),
    fixture VARCHAR(255),
    opponent_team VARCHAR(255),
    total_points INTEGER,
    was_home BOOLEAN,
    kickoff_time TIMESTAMP,
    team_h_score INTEGER,
    team_a_score INTEGER,
    GW VARCHAR(255),
    minutes_played INTEGER,
    goals_scored INTEGER,
    assists INTEGER,
    clean_sheets INTEGER,
    goals_conceded INTEGER,
    own_goals INTEGER,
    penalties_saved INTEGER,
    penalties_missed INTEGER,
    yellow_cards INTEGER,
    red_cards INTEGER,
    saves INTEGER,
    bonus INTEGER,
    bps FLOAT,
    influence FLOAT,
    creativity FLOAT,
    threat FLOAT,
    ict_index FLOAT,
    starts INTEGER,
    expected_goals VARCHAR(255),
    expected_assists VARCHAR(255),
    expected_goal_involvements VARCHAR(255),
    expected_goals_conceded VARCHAR(255),
    price FLOAT,
    transfers_balance INTEGER,
    selected INTEGER,
    transfers_in INTEGER,
    transfers_out INTEGER,
    PRIMARY KEY (element, fixture, GW),
    FOREIGN KEY (element) REFERENCES players(id) ON DELETE CASCADE,
    FOREIGN KEY (opponent_team) REFERENCES teams(id) ON DELETE CASCADE,
    FOREIGN KEY (GW) REFERENCES gameweeks(id) ON DELETE CASCADE
);


-- CREATE TABLE fixtures (
--     code VARCHAR(255),
--     GW VARCHAR(255),
--     finished BOOLEAN,
--     finished_provisional BOOLEAN,
--     id VARCHAR(255),
--     kickoff_time TIMESTAMP,
--     team_a VARCHAR(255),
--     team_a_score INT,
--     team_h VARCHAR(255),
--     team_h_score INT,
--     team_h_difficulty VARCHAR(255),
--     team_a_difficulty VARCHAR(255)
-- );
