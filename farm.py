from ILoyaltyRewardsService import ILoyaltyRewardsService
from SteamUGC import fetch_target_ugc
from reactions import Reactions

# replace with your steamid64 and webapi token
# can be found in https://store.steampowered.com/points/shop
# check source code

token = '0123456789abcdef0123456789abcdef'
steamid_64 = 76560000000000000
target_url = 'id/iebbbb'


s = ILoyaltyRewardsService(token, steamid_64)

reaction_config = s.get_reaction_config()

target_ugc = fetch_target_ugc(target_url)
for ugc_type, target_id in target_ugc:
    print(ugc_type, target_id)
    summary = s.get_summary()
    reactions = s.get_reactions(2, target_id)
    points = summary.summary.points

    for reaction in reaction_config.reactions:
        if ugc_type in reaction.valid_ugc_types:
            if reaction.reactionid not in reactions.reactionids:
                print(Reactions[reaction.reactionid], "Available")
                if points >= reaction.points_cost:
                    s.add_reaction(2, target_id, reaction.reactionid)
                    points -= reaction.points_cost
                    print("Added Reaction!")

    if points < 300:
        break





