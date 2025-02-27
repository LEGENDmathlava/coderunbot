import json
import os
import re

import discord

from .languages import load_languages

here = os.path.dirname(__file__)


async def main(message: discord.Message, arg: str):

    await load_languages()
    with open(f'{here}/languages.json', 'r') as f:
        language_dict = json.load(f)
    arg = re.sub(r'```[A-z\-\+]*\n', '', arg).replace('```', '')
    language = arg.split()[0]
    code = arg.replace(language, '', 1).lstrip(' \n')
    language = language.lower() \
        .replace('pp', '++').replace('sharp', '#') \
        .replace('clisp', 'lisp').replace('bash', 'bashscript')
    if language not in language_dict.keys():
        embed = discord.Embed(
            title='The following languages are supported',
            description=', '.join(language_dict.keys()),
            color=0xff0000
        )
        embed.set_author(
            name=message.author.name,
            icon_url=message.author.display_avatar.url
        )
        return await message.reply(embed=embed)
    with open(f'{here}/saved_codes/{message.author.id}.json', 'w') as f:
        json.dump({'language': language, 'code': code}, f)
    embed = discord.Embed(
        title='保存しました Saved'
    )
    embed.set_author(
        name=message.author.name,
        icon_url=message.author.display_avatar.url
    )
    return await message.reply(embed=embed)
