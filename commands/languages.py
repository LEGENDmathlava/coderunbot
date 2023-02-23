import aiohttp
import json
import os

here = os.path.dirname(__file__)

async def load_languages():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://wandbox.org/api/list.json') as r:
            if r.status == 200:
                result =  await r.json()
                language_names = set(map(lambda data:data['language'], result))
                languages_dict = {}
                for language_name in language_names:
                    language_information = next(filter(lambda language_information: language_information['language'] == language_name, result))
                    languages_dict[language_name.lower().replace(' ', '')] = language_information['name']
                with open(f'{here}/languages.json', 'w') as f:
                    json.dump(languages_dict, f, indent=4, sort_keys=True)