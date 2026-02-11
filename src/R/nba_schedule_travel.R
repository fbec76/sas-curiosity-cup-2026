library(airball)
season_22_26 <- nba_travel(start_season = 2002,
                           end_season = 2026)
write.csv(season_22_26, "schedule_metrics_2002_2026.csv", row.names = FALSE)
# count nan values in the flight_time column
sum(is.na(season_22_26$`Flight Time`))
