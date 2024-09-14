# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25713846"))
API_HASH = getenv("API_HASH", "ca57c019f37ab7bf0bd9caead4846c88")
BOT_TOKEN = getenv("BOT_TOKEN", "7520519550:AAE1kW4NqyFcU7_203b-bxh49RAnL64pvvI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5768102179").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ab123456789ab321:oph3WwTQWbG1FY0h@cluster0.w4ql1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002154322189")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002154322189"))
