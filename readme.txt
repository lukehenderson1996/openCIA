openCIA written by Luke Henderson

Open-source intelligence gathering/analysis platform utilizing OpenAI's LLMs 



installation instructions:
pip install openai


openai API resources
https://platform.openai.com/playground?lang=python&mode=complete&model=text-davinci-003
https://openai.com/pricing
https://platform.openai.com/docs/api-reference/chat/create
https://github.com/openai/openai-cookbook



didn't work:
curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer $OPENAI_API_KEY" -d '{"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": "Say this is a test!"}],"temperature": 0.7}'


-------------------------------------------------------Chat example:-------------------------------------------------------
System:
You are a helpful assistant that rates tweets for importance. The assistant responds simply with a float or int:
4
9.8
1
3.5

User:
How important is this tweet on a scale of 1-10?

<example tweet 1>This is a bombshell finding!</example tweet 1>
<example response 1>8</example response 1>
<example tweet 2>I am bored</example tweet 2>
<example response 2>1</example response 2>

<tweet>It turns out we have 100% proven that vaccines cause autism</tweet>




-----------------------------------------------------------completions example:-----------------------------------------------------------

How important is this tweet on a scale of 1-10?

This is a bombshell finding!
8

I am bored
1

[insert tweet here]




---------------------------------------completions summarization: (temp=0.25, max length=18, top P=1)---------------------------------------

Summarize this tweet in half the words or less

<tweet>
"How is it possible that all consumer protection laws we have for pharmaceuticals were simultaneously suspended?" - Former Big Pharma executive @sasha_latypova
 

Watch the full interview.
</tweet>



------------------------------------------------------completions bulk rate importance------------------------------------------------------
(temp=0, top p=1, stop_sequence='}')
How important are these tweets on a scale of 1-10?

<tweet 1>
He actually said...
"Woman is a social construct"

I'm getting out of the way.
#justsayin
</tweet 1>
<tweet 2>
Jikkyleaks 🐭 Retweeted
Broken Truth
@BrokenTruthTV
·
2h
"Vaccine enhancement" you say? This is why they kept Francis Collins away from the cameras.
</tweet 2>
<tweet 3>
Jikkyleaks 🐭 Retweeted
Jurassic Carl 🦖🐭
@carl_jurassic
·
3h
Replying to 
@masterlongevity
 and 
@Jikkyleaks
“Master longevity”

Add to the list of anti aging gurus who jibber jab for the Jibby jab!
</tweet 3>
<tweet 4>
Cringe tweet of the week
</tweet 4>
<tweet 5>
🚨 26.4% excess deaths in the 0-24 age bracket!! 

Wake up, everyone! 

These are kids!
</tweet 5>
Format:
{'tweet 1': x, 'tweet 2': x, 'tweet 3': x,  'tweet 4': x, 'tweet 5': x}

{
