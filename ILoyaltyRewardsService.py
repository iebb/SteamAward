import messages_pb2
import base64
import requests


class ILoyaltyRewardsService:
    BASE_URL = 'https://api.steampowered.com/ILoyaltyRewardsService/'

    def __init__(self, access_token, steamid64):
        self.access_token = access_token
        self.steamid64 = steamid64

    def add_reaction(self, target_type, target_id, reaction_id):
        input_protobuf_encoded = base64.b64encode(messages_pb2.CLoyaltyRewards_AddReaction_Request(
            target_type=target_type,
            targetid=target_id,
            reactionid=reaction_id,
        ).SerializeToString()).decode("u8")
        data = requests.post(
            self.BASE_URL + 'AddReaction/v1',
            data={
                'access_token': self.access_token,
                'input_protobuf_encoded': input_protobuf_encoded
            }
        )
        return data.content == b''

    def get_reactions(self, target_type, target_id):
        input_protobuf_encoded = base64.b64encode(messages_pb2.CLoyaltyRewards_GetReactions_Request(
            target_type=target_type,
            targetid=target_id,
        ).SerializeToString()).decode("u8")
        data = requests.get(
            self.BASE_URL + 'GetReactions/v1',
            params={
                'access_token': self.access_token,
                'input_protobuf_encoded': input_protobuf_encoded
            }
        )
        decoder = messages_pb2.CLoyaltyRewards_GetReactions_Response()
        decoder.ParseFromString(data.content)
        return decoder

    def get_reaction_config(self):
        data = requests.get(
            self.BASE_URL + 'GetReactionConfig/v1',
            params={
                'input_protobuf_encoded': ''
            }
        )
        decoder = messages_pb2.CLoyaltyRewards_GetReactionConfig_Response()
        decoder.ParseFromString(data.content)
        return decoder

    def get_summary(self, steamid64=None):
        if not steamid64:
            steamid64 = self.steamid64

        input_protobuf_encoded = base64.b64encode(messages_pb2.CLoyaltyRewards_GetSummary_Request(
            steamid=steamid64
        ).SerializeToString()).decode("u8")
        data = requests.get(
            self.BASE_URL + 'GetSummary/v1',
            params={
                'access_token': self.access_token,
                'input_protobuf_encoded': input_protobuf_encoded
            }
        )
        decoder = messages_pb2.CLoyaltyRewards_GetSummary_Response()
        decoder.ParseFromString(data.content)
        return decoder
