import os
import sys
import argparse

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('username', type=str, help='@username')
args = parser.parse_args()
if args.username[0] != "@":  # if first character isn't "@"
    args.username = "@" + args.username

bot = Bot()
bot.login()

# (The following functions apply if you have a private account)

# Approve users that requested to follow you
bot.approve_pending_follow_requests()

# Reject users that requested to follow you
bot.reject_pending_follow_requests()
