"""openCIA"""

# Author: Luke Henderson 
__version__ = '0.0'

import time
import os
import sys
import openai
import ast

import apiKeys
import colors as cl
import debugTools as dt
import api


#constants:
#https://openai.com/pricing
MODEL_PRICES = {'text-davinci-003': 0.02, 'text-curie-001': 0.002, 'text-babbage-001': 0.0005, 'text-ada-001': 0.0004,
                'gpt-3.5-turbo': 0.002} #$/1k tokens
SIMULATE_COMPLETIONS = True #simulate openAI paid API calls

def checkFinish(resp):
    reason = resp["choices"][0]["finish_reason"]
    if reason != 'stop':
        cl.red('Error (main.py): Model stopped with incorrect finish reason: ' + reason)

def printPrice(resp, model):
    if model in MODEL_PRICES:
        cl.yellow(f'Cost: ${MODEL_PRICES[model]}*{resp["usage"]["total_tokens"]}/1000 = ' +
                  f'{MODEL_PRICES[model]*resp["usage"]["total_tokens"]/10}¢')
    else:
        cl.red('Error (main.py): Other model costs not defined')

def costStr(resp, model):
    ret = cl.WARNING
    if model in MODEL_PRICES:
        ret += f'{round(MODEL_PRICES[model]*resp["usage"]["total_tokens"]/10, 4)}¢'
    else:
        cl.red('Error (main.py): Other model costs not defined')
    return ret

cl.green('Program Start')

#--------------------------------------------------------------init--------------------------------------------------------------
#assert correct module versions 
modV = {cl:   '0.8',
        api:  '0.5'}
for module in modV:
    errMsg = f'Expecting version {modV[module]} of "{os.path.basename(module.__file__)}". Imported {module.__version__}'
    assert module.__version__ == modV[module], errMsg
#init openai
openai.api_key = apiKeys.openaiPriv
#warn if using paid API calls
if SIMULATE_COMPLETIONS:
    cl.yellow('Using simulated completions')
else:
    input(f'{cl.WARNING}Warning: main.py using paid API calls. Press enter to continue...{cl.ENDC}')






#------------------------------------------------------------main loop------------------------------------------------------------
# #list models available
# openListResp = openai.Model.list()
# # dt.info(openListResp)
# modelList = openListResp['data']
# for model in modelList:
#     print(model['id'])


#pull latest tweets from account
twAccount = 'Jikkyleaks'
tweetResp = {'tweet 1': None, 'tweet 2': None, 'tweet 3': None, 'tweet 4': None, 'tweet 5': None}
tweetResp['tweet 1'] = "\nHe actually said...\n\"Woman is a social construct\"\n\nI'm getting out of the way.\n#justsayin\n"
tweetResp['tweet 2'] = "\nJikkyleaks 🐭 Retweeted\nBroken Truth\n@BrokenTruthTV\n·\n2h\n\"Vaccine enhancement\" you say? This is why they kept Francis Collins away from the cameras.\n"
tweetResp['tweet 3'] = "\nJikkyleaks 🐭 Retweeted\nJurassic Carl 🦖🐭\n@carl_jurassic\n·\n3h\nReplying to \n@masterlongevity\n and \n@Jikkyleaks\n“Master longevity”\n\nAdd to the list of anti aging gurus who jibber jab for the Jibby jab!\n"
tweetResp['tweet 4'] = "\nCringe tweet of the week\n"
tweetResp['tweet 5'] = "\n🚨 26.4% excess deaths in the 0-24 age bracket!! \n\nWake up, everyone! \n\nThese are kids!\n"


model = "text-davinci-003"
# prompt = "How important are these tweets on a scale of 1-10?\n\n<tweet 1>\nHe actually said...\n\"Woman is a social construct\"\n\nI'm getting out of the way.\n#justsayin\n</tweet 1>\n<tweet 2>\nJikkyleaks 🐭 Retweeted\nBroken Truth\n@BrokenTruthTV\n·\n2h\n\"Vaccine enhancement\" you say? This is why they kept Francis Collins away from the cameras.\n</tweet 2>\n<tweet 3>\nJikkyleaks 🐭 Retweeted\nJurassic Carl 🦖🐭\n@carl_jurassic\n·\n3h\nReplying to \n@masterlongevity\n and \n@Jikkyleaks\n“Master longevity”\n\nAdd to the list of anti aging gurus who jibber jab for the Jibby jab!\n</tweet 3>\n<tweet 4>\nCringe tweet of the week\n</tweet 4>\n<tweet 5>\n🚨 26.4% excess deaths in the 0-24 age bracket!! \n\nWake up, everyone! \n\nThese are kids!\n</tweet 5>\nFormat:\n{'tweet 1': x, 'tweet 2': x, 'tweet 3': x,  'tweet 4': x, 'tweet 5': x}\n\n{'tweet 1': 3, 'tweet 2': 6, 'tweet 3': 4,  'tweet 4': 1, 'tweet 5': 10}/n/n{"
prompt = "How important are these tweets on a scale of 1-10?\n\n" + \
                     "<tweet 1>" + tweetResp['tweet 1'] + \
         "</tweet 1>\n<tweet 2>" + tweetResp['tweet 2'] + \
         "</tweet 2>\n<tweet 3>" + tweetResp['tweet 3'] + \
         "</tweet 3>\n<tweet 4>" + tweetResp['tweet 4'] + \
         "</tweet 4>\n<tweet 5>" + tweetResp['tweet 5'] + \
         "</tweet 5>\nFormat:\n{'tweet 1': x, 'tweet 2': x, 'tweet 3': x,  'tweet 4': x, 'tweet 5': x}\n\n{"
if SIMULATE_COMPLETIONS:
    compResp = {'id': 'cmpl-7GIqPtDF3cFJVvTaFkBTPP8o7izcV', 'object': 'text_completion', 'created': 1684120041, 'model': 'text-davinci-003', 'choices': [{'text': "'tweet 1': 3, 'tweet 2': 6, 'tweet 3': 4,  'tweet 4': 1, 'tweet 5': 10", 'index': 0, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 360, 'completion_tokens': 35, 'total_tokens': 395}}
else:
    compResp = openai.Completion.create(model=model, prompt=prompt, temperature=0, max_tokens=100,
        top_p=1, frequency_penalty=0, presence_penalty=0, stop=["}"])

# dt.info(compResp, 'compResp')

cost = costStr(compResp, model)
cl.blue(f'\nResponse from {compResp["model"]}:\t\t' + cost)
checkFinish(compResp)
#convert response (with error detection)
try:
    impDict = ast.literal_eval('{' + compResp['choices'][0]['text'] + '}')
    assert isinstance(impDict, dict)
    assert len(impDict)==5
    keyList = [str(key) for key in impDict.keys()]
    for i in range(len(impDict)):
        assert keyList[i] == f'tweet {i+1}'
        value = impDict[keyList[i]]
        assert isinstance(value, int)
        assert value >= 1
        assert value <= 10
except AssertionError:
    cl.red('Error (main.py): Response from model in wrong format')
    dt.info(impDict, 'impDict')
    exit()
print('Importance ratings: ')
for key, value in impDict.items():
    print(f'\t{key}: {value}')



#summarize important tweets:
sortedImpDict = sorted(impDict.items(), key=lambda x: x[1], reverse=True)
tweetList = []
tweetList.append(sortedImpDict[0][0]) #most important tweet
tweetList.append(sortedImpDict[1][0]) #second most important tweet

model = "text-davinci-003"

sumList = []
for i in range(2):
    prompt = "Summarize this tweet in half the words or less\n\n<tweet>" + tweetResp[tweetList[i]] + "</tweet>"
    if SIMULATE_COMPLETIONS:
        sumList.append({'id': 'cmpl-7GKXMxBe5cxWeXjOzHliMp1W0KVIZ', 'object': 'text_completion', 'created': 1684126548, 'model': 'text-davinci-003', 'choices': [{'text': "Excess deaths in 0-24 age group; urgent call.", 'index': 0, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 56, 'completion_tokens': 14, 'total_tokens': 70}})
    else:
        sumList.append(openai.Completion.create(model=model, prompt=prompt, temperature=1, max_tokens=25,
            top_p=1, frequency_penalty=0, presence_penalty=0))

cl.purple('\nTweet Analysis Report: \n')
for i in range(2):
    cost = costStr(sumList[i], model)
    cl.blue(f'1: {twAccount} tweet summary from {sumList[i]["model"]}:\t\t' + cost)
    checkFinish(sumList[i])
    text = sumList[i]['choices'][0]['text'].strip('\n')
    print(text + '\n')

