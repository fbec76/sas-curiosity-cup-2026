library(airball)
season_22_26 <- nba_travel(start_season = 2022,
                           end_season = 2026)
colnames(season_22_26)
sapply(season_22_26, class)
