-- Active: 1719859538524@@127.0.0.1@5432@fpl_dwh@public
CREATE TABLE gameweeks (
    id VARCHAR(255) PRIMARY KEY,
    gw_name VARCHAR(255),
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
    code INTEGER,
    id INTEGER,
    team_name VARCHAR(255),
    short_name VARCHAR(255),
    strength INTEGER,
    strength_overall_away INTEGER,
    strength_overall_home INTEGER,
    strength_attack_away INTEGER,
    strength_attack_home INTEGER,
    strength_defence_away INTEGER,
    strength_defence_home INTEGER
);

CREATE TABLE players (
    code VARCHAR(255),
    id VARCHAR(255) PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    web_name VARCHAR(255),
    element_type VARCHAR(255),
    team VARCHAR(255),
    team_code VARCHAR(255),
    total_points INTEGER,
    selected_by_percent NUMERIC(5, 2),
    transfers_in INTEGER,
    transfers_out INTEGER,
    "minutes" INTEGER,
    goals_scored INTEGER,
    assists INTEGER,
    clean_sheets INTEGER,
    own_goals INTEGER,
    penalties_saved INTEGER,
    penalties_missed INTEGER,
    yellow_cards INTEGER,
    red_cards INTEGER,
    bonus INTEGER,
    ict_index FLOAT,
    goals_conceded_per_90 FLOAT,
    form_rank INTEGER,
    points_per_game_rank INTEGER,
    selected_rank INTEGER,
    dreamteam_count INTEGER,
    news TEXT,
    points_per_game FLOAT
);

