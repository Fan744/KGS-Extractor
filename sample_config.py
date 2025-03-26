import os

api_id = 24400704
api_hash = os.environ.get("API_HASH", "985be086326f373e026ea06e5fdef026")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "7150812859")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "7150812859")
owner_users = [int(num) for num in osowner_users.split(",")]
