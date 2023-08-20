from telethon.sync import TelegramClient
import pandas as pd
import datetime
from configparser import ConfigParser

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)

api_id, api_hash = config['account']['api_id'], config['account']['api_hash']
telegram_channel = config['account']['tele_channel'] #place telegram channel here


df = pd.DataFrame()

with TelegramClient('scrape',api_id,api_hash) as client:
    for message in client.iter_messages(telegram_channel,offset_date=datetime.date(2021,1,1), reverse=True): #choose start date 
        data = {"text": message.text,
                "date":message.date}
        temp_df = pd.DataFrame(data, index=[1])
        df = df.append(temp_df)

df.to_csv("export.csv",index=False)



