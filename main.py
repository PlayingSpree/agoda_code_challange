from api_requests import apiRequest
from formatter import formatRequest
from app_config import app_config

# Read repository
repository = input('Enter the repository name (format: owner/repository): ')

# Read information type
info_type = input('Enter the information type (pull-requests, issues): ')
while not (info_type == 'pull-requests' or info_type == 'issues'):
    info_type = input('Invalid input.\nEnter the information type (pull-requests, issues): ')

# Request info by information type
res = apiRequest(repository,info_type)
if res is not None:
    formatRequest(res,info_type,repository)

# PlayingSpree/AnimeDiscordRichPresence
# chromium/chromium