# Yep, o3-mini is WORTH the money - Build your own reasoning agent

- **Channel:** AI Jason
- **Date:** 2025-02-03
- **Duration:** 8:39
- **Views:** 19K views
- **URL:** https://www.youtube.com/watch?v=iGfCrCxPbdQ

## Transcript

open AI 03 Mini model is one of the most under hype released recently despite all sorts of different oneshot coding example that people has been sharing on Twitter what's really interesting about O3 Mini model it is reason model that support function calling structur output it is also 93% cheaper than 01 model but

four times faster meaning 03 Mini model is probably the first reasoning model that is good enough for building real production agents and open AI today released deep research mode in CH gbt it is a fine tune O3 model specifically designed for research agents and the result seems really good much better

than normal gbd for old based research agent we saw before as a deep research agent is taking not only one round of research actions but multiple rounds of actions alongside reflection result synthesis adjusted research planning that enable it do much deeper research than we can before and this is great

early example showcasing how reasoning model going to really shape the landscape of a at 2025 those new IQs we got from the inference stage V reasoning model going overking a lot of hurdles that we have been fighting for with normal Chan model like gbt 4 and considering the price of os Mini model

is so much lower that it's even lower than GB 40 we should really start trying and adopting raising model for your autonomous agent systems one question you might have is how much additional performance you can gain from SWAP your gbt 4 old model to old Mini model for your agent existance that's why today I

want to show you how can we replicate this deep research agent using reasoning model like UL mini or deep seek R1 and we're do side by side comparison of the same research task between those reasoning agents versus normal agents so let's get it I'm going to quickly put together two research agent between the

reasoning model versus non- reasoning model and let them test through a few Gia Benchmark tasks Gia is a benchmark introduced by meta where it has a huge data set for General AI assistant task including a lot of research tasks that involve huge amount research synthesize and summarization ability and each of

tasks normally require a list of different actions and steps to take to be able to answer the question and each question will have a very clear unambiguous answer so that we can verify whether the task has been completed properly or not and to making sure this Benchmark data is not public and quable

I'm going to hide away all the answers in this video and only tell whether the agent pass or fail but if you want to see the specific data set you can go to hugging phase and search for Gia and this research agent itself is going to be a basic tool calling agent it will have access to list of different

scrippers if you're not familiar with tool C it is key components that enable the agent assistance it is basically special mode of large L model that can output what type of actions agent should take and what's the input per if you want to dive deeper you can join AI build Club Community where I have four

Deep dive of how can you build production agent from scratch not relying on any Frameworks and for this deep research agent with ultra Mei we're going to do something similar we're Define a basic agent with system prompt that you are an internet researcher you always use tools to find latest internet

data based on research topic and give detailed and comprehensive results never make up information but the model will be allr Mei and the reasoning efforts I put at high you can swap to low or median as well generally more effort L model spend on reasoning better result it will be but it is balanced between

speed and reasoning accuracy and we pass on the message as well as a list of tools that were defined after L Lang model generates out we append the tool calling message into conversation history if there's no to call anymore which means lar model thinks the task has been finished then we'll just return

the final response to give but if it this output any to call then we extract the function name and try to call an inputs then call the action function get a result and inserts the two cor response this process will be repeated multiple times until agent thinks they finished task in outp put final response

so this is basic replicate of deep research agent with also Mini model as you can see it's actually very basic and St forward the rest will just need to define a list of tools that it can has access to one is a sriping website where there are platform like file cor and spidercloud as well as Google search

where I'm using serer for the Google search API and you can also bring more and more different type scrier like LinkedIn Instagram from script Marketplace like API file and Rapid API here are two examples I got from each platform and in the end I also add a tool called reflection where I want the

model to do a reflection before it GES the final answer and of course you can add more and more different tools than data scripper to make your deep research better in specific vertical research then you will need to define a list of tool schema so tool schema will communicate to the large Range model

when to use this tool and what is the input that it need to generate for running this tool so you don't actually need to write everything yourself you can go to opening a playground click on ADD functions and this is generate button you can just copy the actual function and paste in this will generate

a schema that you can just paste in directly and we need to repeat this process for every single function that you want agent to run and in the end do a mapping about if the agent try to call this function what is exact function name so I just replicate that in this notebook load the package defin

environment key the basic two calling agent that we just talked about for o Mini model as well as 40 model we Define a list of different tools and now we're going to compare the results the first research task is that I'm researching species that became invasive after people who CT them as P released them

there are certain species of fish that was popularized as Pat by being the main character of the movie fine Nemo according to USGS where was the fish found as a non native species before the year 2020 I need answer for me as a five digigit zip code of the places the species was found separate by comma if

there are more than one places so this a pretty complex research query because it required not only you go online find some information but require quite strong synthesis and transformation of the information F like it requires them to know what's the main character in the movie Finding Nemo and also need to

convert that into five digit ZIP codes of the place they found and let's test out first it run the full all agent so as you can find it did take a few actions but in the end it couldn't find the information about zip code of the location but now let's try the O3 deep research agent that would build

here you can see the ulr agent does take a bit longer but also successfully gor up so this first task the ultr mini based agent passed and GPD for all agent fa and next one I want to test is in natural journalist scientific reports conference proceeding from 20 in the article that didn't mention plasmon or

plasmonic what Nano compound is studied don't use prefix Nano in your answer if there's one so this is also a pretty complex research you need to scroll a amount data and then do some synthesiz in the end so in this example when I run the 40 agent it is giving the wrong answer but when I'm using o stre mini

agent the answer is correct and this was quite interesting because I was testing the same task in the Deep research function in chpt even deep research got around here after 4 minutes research this also align with a few other tests I did so in general I found phas that require a huge amount of planning as

well as synthesis like a research also meaning General deliver better results than gbt 40 agent but there are also cases where both agent failed and that task was successful result with deep research and when I look at the source I think the key things here is that chat gbt seems has better sriping tool it can

access a few website that the normal scrier that I was using just couldn't access so I do think you can build very good research agent in specific vertical research topics if you can bring more and more specific data sraer in so with this quick example I do really think if your age task require very complex

planning and synthesize you should definitely swap out the model to Al Mini model to try whether it gain better performance for those complex tasks and I believe this is just a very first step towards this new era of Agents where it is utilizing those reasoning capabilities if you want to learn more

about building agents and large Range model applications I'll put this notebook in the AI Builder Club community so you can use that template to build a more and more sophisticated vertical research agent and there're also tutorial of how to deploy this agent as API service that you can use in

other workflows I have put the link in the description below so you can click and join I hope you enjoy this video thank you and I see you next time
