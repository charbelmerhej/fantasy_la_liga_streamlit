# Stuff to still check:
    # If player gets a red card but his team concedes goals, he should get -
    # Zabbit eno eza fari2 akal golen bas ken wahad OG, ydal yenhasab two gc
    # If player first conceded min 90 and went out min 90+2, will get considered as CS
    # If a player got a yellow in game, then went out and got on bench, now btenhasab yellow+red, it should not
    # Anytime player goes in and out same game, might have probs with CS and 2GC
    # Events happening at equal minutes could cause issues, i.e: Player conceding then getting substituted directly, need to check

import pprint
import sys
import pandas as pd
import requests

teams = [2816, 2817, 2818, 2819, 2820, 2821, 2824, 2825, 2826, 2828, 2829, 2833, 2836, 2858, 2859, 2885, 4488, 6577,
         24264, 33779]

round_number = 21

# players_df = pd.DataFrame(columns={"Name", "Slug", "Position", "Team", "Team Slug", "Pts", "GWs", "Mins Pts", "G",
#                                       "A", "CS", "YC", "RC", "OG", "2GC", "PenMiss", "Saves Pts", "PenSave", "Bonus"})

players_df = pd.read_csv("fantasy_all_players.csv", index_col=0)
# v = players_df["Slug"].value_counts()
# v = v.sort_values()
# print(v)
# sys.exit()

for team in teams:
    players_url = "https://api.sofascore.com/api/v1/team/{}/players".format(team)
    players_headers = {
        "authority": "api.sofascore.com",
        "accept-language": "en-US,en;q=0.9,ar;q=0.8",
        "cache-control": "max-age=0",
        "origin": "https://www.sofascore.com",
        "referer": "https://www.sofascore.com",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36 "
    }

    players_info = requests.request("GET", players_url, headers=players_headers)
    players_info_json = players_info.json()
    all_players = players_info_json["players"]
    for player in all_players:
        player_name = player["player"]["name"]
        player_slug = player["player"]["slug"]
        player_team = player["player"]["team"]["name"]
        player_team_slug = player["player"]["team"]["slug"]
        try:
            player_position = player["player"]["position"]
        except KeyError:
            continue

        # Remove betis juan cruz
        if player_slug == "juan-cruz" and player_team_slug == "real-betis":
            continue

        if player_slug == "raul-garcia" and player_team_slug == "osasuna":
            continue

        if player_slug == "sergio-arribas" and player_team_slug == "rayo-vallecano":
            continue

        if player_slug == "lamine-yamal" and player_team_slug == "barcelona-u19":
            player_team_slug = "barcelona"

        if player_slug == "joselu" and player_team_slug == "valencia":
            continue

        if player_slug in players_df['Slug'].values:
            # Get the row index of the player in the dataframe
            index = players_df[players_df['Slug'] == player_slug].index[0]

            # Check if Position from the file matches the Position in the dataframe
            if players_df.loc[index, 'Position'] != player_position:
                old_pos = players_df.loc[index, 'Position']
                # Update the Position in the dataframe
                players_df.at[index, 'Position'] = player_position
                print("Updated Position for player {} from {}: Changed from {} to {}".format(player_name, player_team,
                                                                                             old_pos, player_position))

            # Check if the Team is different from the dataframe
            if players_df.loc[index, 'Team Slug'] != player_team_slug:
                old_team = players_df.loc[index, 'Team Slug']
                # Update the Team in the dataframe
                players_df.at[index, 'Team Slug'] = player_team_slug
                players_df.at[index, 'Team'] = player_team
                print("Updated Team for player {}: Changed from {} to {}".format(player_name, old_team, player_team_slug))
        else:
            players_df = players_df.append({
                "Name": player_name,
                "Slug": player_slug,
                "Position": player_position,
                "Team": player_team,
                "Team Slug": player_team_slug,
                "Pts": 0,
                "GWs": 0,
                "Mins Pts": 0,
                "G": 0,
                "A": 0,
                "CS": 0,
                "YC": 0,
                "RC": 0,
                "OG": 0,
                "2GC": 0,
                "PenMiss": 0,
                "Saves Pts": 0,
                "PenSave": 0,
                "Bonus": 0
            }, ignore_index=True)
            print("Added player: {} from {}".format(player_name, player_team))

        # Beginning of season to create file
        # players_df = players_df.append({
        #     "Name": player_name,
        #     "Slug": player_slug,
        #     "Position": player_position,
        #     "Team": player_team,
        #     "Team Slug": player_team_slug,
        #     "Pts": 0,
        #     "GWs": 0,
        #     "Mins Pts": 0,
        #     "G": 0,
        #     "A": 0,
        #     "CS": 0,
        #     "YC": 0,
        #     "RC": 0,
        #     "OG": 0,
        #     "2GC": 0,
        #     "PenMiss": 0,
        #     "Saves Pts": 0,
        #     "PenSave": 0,
        #     "Bonus": 0
        # }, ignore_index=True)

# players_df.to_csv("fantasy_all_players.csv", columns=["Name", "Slug", "Position", "Team", "Team Slug", "Pts", "GWs",
#                                                       "Mins Pts", "G", "A", "CS", "YC", "RC", "OG", "2GC", "PenMiss",
#                                                       "Saves Pts", "PenSave", "Bonus"])

# sys.exit(27)
round_url = "https://api.sofascore.com/api/v1/unique-tournament/8/season/52376/events/round/{}".format(round_number)
round_headers = {
    "authority": "api.sofascore.com",
    "accept-language": "en-US,en;q=0.9,ar;q=0.8",
    "cache-control": "max-age=0",
    "origin": "https://www.sofascore.com",
    "referer": "https://www.sofascore.com",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36 "
}
round_info = requests.request("GET", round_url, headers=round_headers, data={})
round_info_json = round_info.json()
game_ids_from_round = round_info_json["events"]


mins_pts_2 = []
mins_pts_1 = []
goals = []
assists = []
clean_sheets = []
two_GC = []
yellow = []
red = []
own_goals = []
missed_pen = []
pen_save = []
saves_pts_1 = []
saves_pts_2 = []
saves_pts_3 = []
saves_pts_4 = []
bonus_1 = []
bonus_2 = []
bonus_3 = []

for game in game_ids_from_round:
    game_id = game["id"]

    # Posponed games
    if game_id == 11369460 or game_id == 11369459 or game_id == 11369463:
        continue

    incidents_url = "https://api.sofascore.com/api/v1/event/{}/incidents".format(game_id)
    game_incidents = requests.request("GET", incidents_url, headers=round_headers, data={})
    game_incidents_json = game_incidents.json()
    incidents = game_incidents_json["incidents"]
    player_slug_from_yellow_red = []
    home_goals_minutes = []
    away_goals_minutes = []

    for incident in incidents:
        incident_type = incident["incidentType"]

        if incident_type == "card":
            incident_class = incident["incidentClass"]
            try:
                player_slug = incident["player"]["slug"]
            except KeyError:
                continue
            if incident_class == "yellow":
                if player_slug not in player_slug_from_yellow_red:
                    yellow.append(player_slug)
            if incident_class == "red":
                red.append(player_slug)
            if incident_class == "yellowRed":
                player_slug_from_yellow_red.append(player_slug)
                red.append(player_slug)

        if incident_type == "goal":
            incident_class = incident["incidentClass"]
            incident_time = int(incident["time"])
            incident_is_home = incident["isHome"]

            if incident_is_home:
                home_goals_minutes.append(incident_time)
            else:
                away_goals_minutes.append(incident_time)

            if incident_class == "regular":
                goals.append(incident["player"]["slug"])
                try:
                    player_assist = incident["assist1"]["slug"]
                except KeyError:
                    player_assist = None
                if player_assist is not None:
                    assists.append(player_assist)
            if incident_class == "ownGoal":
                own_goals.append(incident["player"]["slug"])
            if incident_class == "penalty":
                goals.append(incident["player"]["slug"])

        if incident_type == "inGamePenalty":
            incident_class = incident["incidentClass"]

            if incident_class == "missed":
                missed_pen.append(incident["player"]["slug"])

    game_lineup_url = "https://api.sofascore.com/api/v1/event/{}/lineups".format(game_id)
    game_lineup_info = requests.request("GET", game_lineup_url, headers=round_headers, data={})
    game_lineup_info_json = game_lineup_info.json()

    players_from_away_team = game_lineup_info_json["away"]["players"]
    players_from_home_team = game_lineup_info_json["home"]["players"]
    players_with_ratings_list = []

    for playing_player in players_from_away_team:
        try:
            minutes_played = int(playing_player["statistics"]["minutesPlayed"])
        except KeyError:
            continue
        player_slug = playing_player["player"]["slug"]
        if int(minutes_played) >= 60:
            mins_pts_2.append(player_slug)
        else:
            mins_pts_1.append(player_slug)

        if playing_player["player"]["position"] == "G":
            try:
                saves_committed = playing_player["statistics"]["saves"]
                saves_committed = int(saves_committed)
            except KeyError:
                saves_committed = 0

            if saves_committed == 3 or saves_committed == 4 or saves_committed == 5:
                saves_pts_1.append(player_slug)
            elif saves_committed == 6 or saves_committed == 7 or saves_committed == 8:
                saves_pts_2.append(player_slug)
            elif saves_committed == 9 or saves_committed == 10 or saves_committed == 11:
                saves_pts_3.append(player_slug)
            elif saves_committed >= 12:
                saves_pts_4.append(player_slug)
            else:
                pass

            try:
                penalties_saved = playing_player["statistics"]["penaltySave"]
                penalties_saved = int(penalties_saved)
            except KeyError:
                penalties_saved = 0

            if penalties_saved == 1:
                pen_save.append(player_slug)
            elif penalties_saved == 2:
                pen_save.append(player_slug)
                pen_save.append(player_slug)
            elif penalties_saved == 3:
                pen_save.append(player_slug)
                pen_save.append(player_slug)
                pen_save.append(player_slug)
            else:
                pass

        try:
            player_rating = playing_player["statistics"]["rating"]
        except KeyError:
            player_rating = 0

        players_with_ratings_list.append({
            "Slug": player_slug,
            "Rating": float(player_rating)
        })

        substitute_player = playing_player["substitute"]
        home_goals_minutes.sort()
        filtered = []

        if minutes_played < 60:
            pass
        else:
            if not substitute_player:
                if not home_goals_minutes:
                    clean_sheets.append(player_slug)
                else:
                    if minutes_played < home_goals_minutes[0]:
                        clean_sheets.append(player_slug)
            else:
                try:
                    if home_goals_minutes[-1] < (90 - minutes_played):
                        clean_sheets.append(player_slug)
                except IndexError:
                    clean_sheets.append(player_slug)

        # Fill Two GC
        if not substitute_player:
            for goal_min in home_goals_minutes:
                if goal_min < minutes_played:
                    filtered.append(goal_min)
        else:
            for goal_min in home_goals_minutes:
                if goal_min > 90 - minutes_played:
                    filtered.append(goal_min)

        if len(filtered) == 2 or len(filtered) == 3:
            two_GC.append(player_slug)
        if len(filtered) == 4 or len(filtered) == 5:
            two_GC.append(player_slug)
            two_GC.append(player_slug)
        if len(filtered) == 6 or len(filtered) == 7:
            two_GC.append(player_slug)
            two_GC.append(player_slug)
            two_GC.append(player_slug)
        if len(filtered) == 8 or len(filtered) == 9:
            two_GC.append(player_slug)
            two_GC.append(player_slug)
            two_GC.append(player_slug)
            two_GC.append(player_slug)

    for playing_player in players_from_home_team:
        try:
            minutes_played = int(playing_player["statistics"]["minutesPlayed"])
        except KeyError:
            continue
        player_slug = playing_player["player"]["slug"]
        if int(minutes_played) >= 60:
            mins_pts_2.append(player_slug)
        else:
            mins_pts_1.append(player_slug)

        if playing_player["player"]["position"] == "G":
            try:
                saves_committed = playing_player["statistics"]["saves"]
                saves_committed = int(saves_committed)
            except KeyError:
                saves_committed = 0

            if saves_committed == 3 or saves_committed == 4 or saves_committed == 5:
                saves_pts_1.append(player_slug)
            elif saves_committed == 6 or saves_committed == 7 or saves_committed == 8:
                saves_pts_2.append(player_slug)
            elif saves_committed == 9 or saves_committed == 10 or saves_committed == 11:
                saves_pts_3.append(player_slug)
            elif saves_committed >= 12:
                saves_pts_4.append(player_slug)
            else:
                pass

            try:
                penalties_saved = playing_player["statistics"]["penaltySave"]
                penalties_saved = int(penalties_saved)
            except KeyError:
                penalties_saved = 0

            if penalties_saved == 1:
                pen_save.append(player_slug)
            elif penalties_saved == 2:
                pen_save.append(player_slug)
                pen_save.append(player_slug)
            elif penalties_saved == 3:
                pen_save.append(player_slug)
                pen_save.append(player_slug)
                pen_save.append(player_slug)
            else:
                pass

        try:
            player_rating = playing_player["statistics"]["rating"]
        except KeyError:
            player_rating = 0

        players_with_ratings_list.append({
            "Slug": player_slug,
            "Rating": float(player_rating)
        })

        substitute_player = playing_player["substitute"]
        away_goals_minutes.sort()
        filtered = []

        if minutes_played < 60:
            pass
        else:
            if not substitute_player:
                if not away_goals_minutes:
                    clean_sheets.append(player_slug)
                else:
                    if minutes_played < away_goals_minutes[0]:
                        clean_sheets.append(player_slug)
            else:
                try:
                    if away_goals_minutes[-1] < (90 - minutes_played):
                        clean_sheets.append(player_slug)
                except IndexError:
                    clean_sheets.append(player_slug)

        # Fill Two GC
        if not substitute_player:
            for goal_min in away_goals_minutes:
                if goal_min < minutes_played:
                    filtered.append(goal_min)
        else:
            for goal_min in away_goals_minutes:
                if goal_min > 90 - minutes_played:
                    filtered.append(goal_min)

        if len(filtered) == 2 or len(filtered) == 3:
            two_GC.append(player_slug)
        if len(filtered) == 4 or len(filtered) == 5:
            two_GC.append(player_slug)
            two_GC.append(player_slug)
        if len(filtered) == 6 or len(filtered) == 7:
            two_GC.append(player_slug)
            two_GC.append(player_slug)
            two_GC.append(player_slug)
        if len(filtered) == 8 or len(filtered) == 9:
            two_GC.append(player_slug)
            two_GC.append(player_slug)
            two_GC.append(player_slug)
            two_GC.append(player_slug)

    df_for_bonuses = pd.DataFrame.from_records(players_with_ratings_list)
    df_for_bonuses = df_for_bonuses.sort_values(by="Rating", ascending=False)
    df_for_bonuses = df_for_bonuses.reset_index()
    adding_to_bonus_3 = True
    adding_to_bonus_2 = False
    adding_to_bonus_1 = False
    temp_bonus_3 = []
    temp_bonus_2 = []
    temp_bonus_1 = []

    # Calculate bonus pts
    for idx, row in df_for_bonuses.iterrows():
        row_rating = row["Rating"]

        if idx == 0:
            highest_row_rating = row["Rating"]
            bonus_3.append(row["Slug"])
            temp_bonus_3.append(row["Slug"])
            continue

        if highest_row_rating == row_rating:
            if adding_to_bonus_3:
                highest_row_rating = row["Rating"]
                bonus_3.append(row["Slug"])
                temp_bonus_3.append(row["Slug"])
                continue
            if adding_to_bonus_2:
                highest_row_rating = row["Rating"]
                bonus_2.append(row["Slug"])
                temp_bonus_2.append(row["Slug"])
                continue
            if adding_to_bonus_1:
                highest_row_rating = row["Rating"]
                bonus_1.append(row["Slug"])
                temp_bonus_1.append(row["Slug"])
                continue
        else:
            if len(temp_bonus_3) == 1 and len(temp_bonus_2) == 0:
                adding_to_bonus_3 = False
                adding_to_bonus_2 = True
                adding_to_bonus_1 = False
            if len(temp_bonus_3) == 1 and len(temp_bonus_2) == 1 and len(temp_bonus_1) == 0:
                adding_to_bonus_3 = False
                adding_to_bonus_2 = False
                adding_to_bonus_1 = True
            if len(temp_bonus_3) == 1 and len(temp_bonus_2) == 1 and len(temp_bonus_1) >= 1:
                adding_to_bonus_3 = False
                adding_to_bonus_2 = False
                adding_to_bonus_1 = False
            if len(temp_bonus_3) == 1 and len(temp_bonus_2) > 1:
                adding_to_bonus_3 = False
                adding_to_bonus_2 = False
                adding_to_bonus_1 = False
            if len(temp_bonus_3) == 2 and len(temp_bonus_1) == 0:
                adding_to_bonus_3 = False
                adding_to_bonus_2 = False
                adding_to_bonus_1 = True
            if len(temp_bonus_3) == 2 and len(temp_bonus_1) >= 1:
                adding_to_bonus_3 = False
                adding_to_bonus_2 = False
                adding_to_bonus_1 = False
            if len(temp_bonus_3) > 2:
                adding_to_bonus_3 = False
                adding_to_bonus_2 = False
                adding_to_bonus_1 = False
            if adding_to_bonus_2:
                highest_row_rating = row["Rating"]
                bonus_2.append(row["Slug"])
                temp_bonus_2.append(row["Slug"])
                continue
            if adding_to_bonus_1:
                highest_row_rating = row["Rating"]
                bonus_1.append(row["Slug"])
                temp_bonus_1.append(row["Slug"])
                continue
            if adding_to_bonus_3 == False and adding_to_bonus_2 == False and adding_to_bonus_1 == False:
                break

weekly_df = players_df.copy()
# Initialize all values for weekly df
for col in weekly_df.columns:
    if col == "Name" or col == "Slug" or col == "Position" or col == "Team" or col == "Team Slug":
        continue
    else:
        weekly_df[col].values[:] = 0


for player in mins_pts_2:
    players_df.loc[players_df["Slug"] == player, 'Mins Pts'] += 2
    weekly_df.loc[weekly_df["Slug"] == player, 'Mins Pts'] += 2
for player in mins_pts_1:
    players_df.loc[players_df["Slug"] == player, 'Mins Pts'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'Mins Pts'] += 1
for player in goals:
    players_df.loc[players_df["Slug"] == player, 'G'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'G'] += 1
for player in assists:
    players_df.loc[players_df["Slug"] == player, 'A'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'A'] += 1
for player in clean_sheets:
    players_df.loc[players_df["Slug"] == player, 'CS'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'CS'] += 1
for player in yellow:
    players_df.loc[players_df["Slug"] == player, 'YC'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'YC'] += 1
for player in red:
    players_df.loc[players_df["Slug"] == player, 'RC'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'RC'] += 1
for player in own_goals:
    players_df.loc[players_df["Slug"] == player, 'OG'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'OG'] += 1
for player in missed_pen:
    players_df.loc[players_df["Slug"] == player, 'PenMiss'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'PenMiss'] += 1
for player in saves_pts_1:
    players_df.loc[players_df["Slug"] == player, 'Saves Pts'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'Saves Pts'] += 1
for player in saves_pts_2:
    players_df.loc[players_df["Slug"] == player, 'Saves Pts'] += 2
    weekly_df.loc[weekly_df["Slug"] == player, 'Saves Pts'] += 2
for player in saves_pts_3:
    players_df.loc[players_df["Slug"] == player, 'Saves Pts'] += 3
    weekly_df.loc[weekly_df["Slug"] == player, 'Saves Pts'] += 3
for player in saves_pts_4:
    players_df.loc[players_df["Slug"] == player, 'Saves Pts'] += 4
    weekly_df.loc[weekly_df["Slug"] == player, 'Saves Pts'] += 4
for player in pen_save:
    players_df.loc[players_df["Slug"] == player, 'PenSave'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'PenSave'] += 1
for player in bonus_1:
    players_df.loc[players_df["Slug"] == player, 'Bonus'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, 'Bonus'] += 1
for player in bonus_2:
    players_df.loc[players_df["Slug"] == player, 'Bonus'] += 2
    weekly_df.loc[weekly_df["Slug"] == player, 'Bonus'] += 2
for player in bonus_3:
    players_df.loc[players_df["Slug"] == player, 'Bonus'] += 3
    weekly_df.loc[weekly_df["Slug"] == player, 'Bonus'] += 3
for player in two_GC:
    players_df.loc[players_df["Slug"] == player, '2GC'] += 1
    weekly_df.loc[weekly_df["Slug"] == player, '2GC'] += 1
players_df["GWs"] += 1
weekly_df["GWs"] += 1
for index, row in players_df.iterrows():
    if (row["Slug"] in mins_pts_2) or (row['Slug'] in mins_pts_1):
        if row["Position"] == "G":
            players_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*6 + row["A"]*3 + row["CS"]*4 + row["YC"]*-1 +\
                                    row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Saves Pts"] +\
                                    row["PenSave"]*5 + row["Bonus"] + row["2GC"]*-1
        if row["Position"] == "D":
            players_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*6 + row["A"]*3 + row["CS"]*4 + row["YC"]*-1 +\
                                    row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"] + row["2GC"]*-1
        if row["Position"] == "M":
            players_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*5 + row["A"]*3 + row["CS"]*1 + row["YC"]*-1 +\
                                    row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"]
        if row["Position"] == "F":
            players_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*4 + row["A"]*3 + row["YC"]*-1 + row["RC"]*-3 +\
                                    row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"]

for index, row in weekly_df.iterrows():
    if (row["Slug"] in mins_pts_2) or (row['Slug'] in mins_pts_1):
        if row["Position"] == "G":
            weekly_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*6 + row["A"]*3 + row["CS"]*4 + row["YC"]*-1 +\
                                    row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Saves Pts"] +\
                                    row["PenSave"]*5 + row["Bonus"] + row["2GC"]*-1
        if row["Position"] == "D":
            weekly_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*6 + row["A"]*3 + row["CS"]*4 + row["YC"]*-1 +\
                                    row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"] + row["2GC"]*-1
        if row["Position"] == "M":
            weekly_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*5 + row["A"]*3 + row["CS"]*1 + row["YC"]*-1 +\
                                    row["RC"]*-3 + row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"]
        if row["Position"] == "F":
            weekly_df.at[index, "Pts"] = row["Mins Pts"] + row["G"]*4 + row["A"]*3 + row["YC"]*-1 + row["RC"]*-3 +\
                                    row["OG"]*-2 + row["PenMiss"]*-2 + row["Bonus"]

players_df["Pts"] = players_df["Pts"].astype(int)
players_df["2GC"] = players_df["2GC"].astype(int)
weekly_df["Pts"] = weekly_df["Pts"].astype(int)
weekly_df["2GC"] = weekly_df["2GC"].astype(int)
players_df.to_csv("fantasy_all_players.csv")
weekly_df.to_csv("fantasy_weekly_v2.csv")