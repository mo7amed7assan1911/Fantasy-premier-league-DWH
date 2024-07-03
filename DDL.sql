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
    full_name VARCHAR(255),
    web_name VARCHAR(255),
    element_type VARCHAR(255),
    team VARCHAR(255),
    team_code VARCHAR(255),
    dreamteam_count INTEGER,
    news TEXT
);

