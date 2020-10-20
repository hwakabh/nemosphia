from slackbot.bot import Bot
# When imported Bot class, `slackbot_settings.py` will run first.


if __name__ == '__main__':
    bt = Bot()
    bt.run()