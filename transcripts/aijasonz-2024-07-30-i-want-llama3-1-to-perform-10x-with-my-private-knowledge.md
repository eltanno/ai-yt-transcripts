# "I want Llama3.1 to perform 10x with my private knowledge" - Self learning Local Llama3.1 405B

- **Channel:** AI Jason
- **Date:** 2024-07-30
- **Duration:** 25:34
- **Views:** 125K views
- **URL:** https://www.youtube.com/watch?v=2PKCOVqhngY

## Transcript

we're basically already starting to work on on llama 4 and our goal is to completely close the gap with all the others on that Lama 3.1 is probably the biggest news last week meta is killing it with open source play and looks like it is already working on llama 4 which might drop end of year but llama 3.1

demonstrate really promising performance across multiple different capabilities like mask coding instruction following one part that I found people are not talking a lot about but I'm extremely exciting is that the meta seem to start really investing in the agent related use case they mention that they aim to

not just position llama as a model but a system to provide tools that enable developers to build their own customer agents as well as new type of agentic behavior they have a public report called llama agentic system where they showcase whole components of the Llama stack it includes things like llama

guard which is a specialized model trained to moderate content as well as promp guard to prevent the jailbreak and koser to prevent insecure code produced by lar L model but the most exciting part for me tool calling cuz tool calling is probably so far main reason I have to use open AI because their model

just way better at tool calling related agent use case if you don't know what tool calling is it is a concept introduced by open at end of last year this basically type of model train to given a user task predict what is a function that it need to be called as well as input for this function so that

we can take this Json output to actually run the function and send information back to the large L model it is different from the other type of popular agent framework like react agent where use a prompt Force large Range model to always go through this process of sought action observation they're both great

approach for building autonomous agents but tool calling has a lot of core benefits you can actually support calling multiple different functions at the same time instead of doing one by one and Tool calling is generally better because all those model providers will continuously improve their model to

calling ability instead of optimizing for the react model from the initial evaluation result llama 3.1 model's tool calling ability seem to be performed really really well against other model like gbd4 and Closs 3.5 but the majority of those evaluation Benchmark are kind of zero short tool use which not

necessarily represent the actual tool usage performance in real world because it's fairly easy and simple to do zero short single tool usage like user have question what's the weather in C and you just predict to call one function get a weather with Loc in but the real world agic use case is a lot more complicated

like multi-turn to usage where the user task cannot be complete just within calling one tool it require some sort of planning and reasoning ability to be able to break down a big task into small steps and then based on the result of each step to predict and plan the best next action like if the user query is I

like hot weather and cheap fly help me plan a trip that suits me the most at moment between to and Bok you need to call function for for both toky and Bangkok for get weather as well as function get flight price and based on the result of those four different function calling generally Source like

talku seem to be the best option and then call different function like bookfly book hotel and book cars and on top of that this model will also need to do both those function calling plus conversation so in the end it probably need to generate a good report based on all those research findings so all

things are a lot more complicated than just zero short to usage but the good thing is that in the Llama 3.1 model it seem like they do train the model specifically for those multi-turn dialoges so if the query require multiple tool calls the model can write a step-by-step plan call the tool in

sequence and do the reasoning after each tool call one thing to know is that for smaller model like llama AB it can't reliably maintain conversation alongside calling yet it can only reliably use for zero short to calling while the 70b and 405b is more suable for Combined conversation and calling together and L

one also showcase the actual prompt that has been used to drive those tool calling ability and this is really useful because that will help us to understand how do it work behind the scenes and you can take this to fine tune a specific agentic model so normal prompt looks something like this at the

beginning you'll give some context about what are the tool names that the model has access to as well as actual tool schema very similar to how the open AI function schema look like then they will give a Model A very specific instruction about what kind of result to generate for calling a function so at default it

is something like a tag function with a function name as well as the actual function input details in the middle and after that it will generate tag called eomom represent for end of message so these two things together are kind of like a system prompt to instruct how the model should behave and then you can

insert a user message into a prompt and based on all those information the model or generates a function calling output based on the instruction it was given and we can take this Json output to actually execute the function after we get the function result we can send result back by wrapped under a python R

and based on the information the model will generate answer so this tool calling ability from llas 3.1 is really exciting step for us to have an alternative other than open AI to have a really strong model for agents so I'm going to show you how can you create agents with llama 3.1 model to get a

sense of how well it perform but before I dive into this I know many of you are interested in using AI to automate your work but there's no clear Playbook or role map of how can you actually adopt AI in real world scenario and overcome the common challenges and pitfalls that's why I want to introduce you to

Hops spot free bundle called five essential resource for using chbt at work it has a useful flowchart for you to think through what type of things that you should use chbt versus the one that you shouldn't and also a really cool template you can use when you use chbt or other large Lang model

application to making sure any of those AI created content is following your Brand's voice and tone you have ai generate content refinement checklist to double check the work delivered by Ai and making sure the content you publish is actually what you want and there's a full page checklist that you can easily

use all about adopting AI at work and a super comprehensive PDF guide about how can you use AI to supercharge your work productivity and that including a section at Boton where it covers 100 ways of how top firms are using chat GPT today like Market segmentation and target audience analysis and provide

recommendation for improving the website SEO each of use case can either serve as a reference about how can you use AI to automate work or you can take inspiration to figure out what kind of things people are hacking with chbt and you can build a micro a product to serve this Market the link to this completed

free resource is in the description below click on that link to get a free report today and thanks hopspot for sponsoring this video now let's get back to how can we build a llama 3.1 AI agent but what type of use case should we start building with lamaas 3.1 and here's a use case that Mark zugerberg

has mentioned in his interview with broomberg you know there's almost 200 million creators on our platforms they all are trying to build their Community people want to interact with them there aren't enough hours in the day like I want to make it so that every single one of them can easily train like an AI

version of themselves they can make it what they want so it's almost like a like a kind of artistic artifact that they're putting out there that allows their Community interact with them but also gives them control over how that interaction happens and I think that that's going to be great and there's

going to be Millions there eventually hundreds of millions of those so this where you almost have some sort of digitized version of yourself is a very interesting one cuz I can definitely feel the pain there cuz one use case that's Adent to this digitized Creator is a company knowledgement distribution

for any domain experts who host specific type of knowledge inside a company how to distribute those information to all the other employees and team members is really big problem if you can build agent to digitize some sort of domain experts in the company is almost like having your top performing employees

always accessible to everyone 247 and this problem also mentioned by chass in O podcast if you have a Google workspace my entire company runs on on Google workspace and click a button where all of a sudden now all of that stuff in all of my G drives all of a sudden is trainable so that the npl first employee

comes in and has an agent that's tuned on every deck every model spread that's every document that's a huge huge Edge huge Edge so I really believe that this is a exciting and very big use case and the beautiful thing is that it's actually very easy and simple to build an agent that live inside your slack

that can consume all the documentations that written by your domain experts using llama 3.1 that is running fully on your local machine using old llama and we can build this llama agent that is not only doing knowledge retrieval but also continuously improving itself when observing new knowledge and eventually

Auto make some simple repetitive tasks just like another team member or employee so I'm going to show you step by step how can you build such agent in next 5 minutes firstly we want to download the Llama 3.1 model on your local machine and we're going to use o Lama which is a package that allow you

to run those open source large L model on your local machine so if you have Ama already installed you can open Terminal and type olama P Lama 3.1 this at default will download AB Model which should be small enough to be able to run on your MacBook Pro and after it is downloaded you can do o Lama Rong llama

3.1 okay so you can see this model is working on my MacBook Pro with pretty decent speed so the next step is that we want to build a llama 3.1 agent that exists in your slack workspace and can be tag to answer question and automate tasks and most importantly Distributors domain knowledge to different employees

and team members on demand and to do that we firstly need to decide how we want to train large L model with our private data commonly there are two ways you can either F tune the Lama 3.1 model or you can build a rack Pipeline and there PR and conses for each method here well the funing benefits is it's going

to be faster but also is more involved process you need to prepare a lot of data to make it work and also the model's knowledge will be Frozen at the time when it is trained so if you have new data that you want to bring into the model you kind of need to find tuning again versus rack is a method that's way

easier to start and also support scenario where you have a dynamic knowledge table like notion or conference very well and this is the PA I'm going to take for the Llama agent and then we need to decide how we want to build this rack Pipeline and traditionally most of the time people

kind of start building the rack pipeline bys using open source framework like llama index L chain and open source Vector storage like chroma because it is easy to start however the tricky part of rack is that there are thousands of different techniques you can try to make a rack better and this actually a bunch

of emerging fully managed rack pipel platform that is doing all those optimization for you and also have benefits where it can schedule to automatically revor in the database so whenever you add new stuff to your notion or confidence page the index can always be keep up to date and there are

platform like llama Cloud carbon Ai and for my purpose I actually don't want to manage this r p line I just want to Outsource to someone else that's why I'm going to use one of the platform Lama Cloud which is fully managed rack pipeline platform built by the Llama index team and because the whole

platform is built on top of llama index so it is a lot more transparent to understand what is going on behind the scenes and fairly easy to migrate over if you're already using llama index and they also provide playground for you to play with different combination between chunk size re ranking metadata filtering

and other techniques that has been optimized so the first step is I want to turn my notion knowledge base into a llama Cloud R pipeline so when I go to llama Cloud I can create a index and index is like a data source so I can give a name called notion database and then I can select the data source it can

be PDF file which will connect to their Lama Powers which is really good or they can support Amazon S3 bucket Aero one drive SharePoint slack notion and J and the one I want to use in notion so it will ask you for a few information with the integration token to get integration token you will go to notion. so/ myy

Integrations create an app in notion select the workspace that you want to connect data to and click save then you will go to integration settings copy over this internal integration secret and paste in here into Lama Cloud but one thing you need to know is that in notion after you set up the integration

you actually need to go to page and workspace where you want to give access to knowledge bar click on three dots button and choose connect to and select the app that you just created only after this the application can have access to specific content and page that connect to the app can be retrieved from Lama

cloud and you can also specify which specific database ID as well as page ID to scope down the amount of knowledge that it should retrieve and in the URL this is the database ID same thing for the page ID you can just go to a page that you want to share and you will see in the page URL the list of number

unique ID here is a page ID and after that you can select where do you want to save the data it can be fully managed or use Pyon or other data storage as well as embedding model it will start fashing data in indexing the whole notion database and then you can just retrieve information directly from this API in

point very easily and next is we want to connect this rack ply into slack and to do that we need to quickly create a custom slack barot you can go to slack click on settings and manage apps then click on the build button on top right corner and click on create a new app we will just do from scratch and give a

name Jason B choose the workspace where you want to develop this app and go to all and permissions and I add a few different Scopes from R chat history in Channel groups St message and group message as well as ADD and read reaction to message view people in the work and also send out message so this should be

enough scope for us build a lot of interesting uh interactions then we will try to install the app to your work space click allow then you will get a oros token that you can copy and use later but for now if you go to your slack and try to add Manion your Brad name you can see this bot already exists

but it didn't do anything yet so next step is we want to connect this bot to llama 3.1 model on your local machine Val or llama as well as build those Advanced functionality like knowledge retrieval and learning ability so our open Visual Studio code our first is set up A.V file this is where we store all

the credential that we need from slack notion llama Cloud as well as firework which is large L model inference service that can allow you to access like Lama 45 model so Select ball token is the oos token that you will get in oos and permission while the slack signing secret is the signing Secret Under the

basic information here and we're going to get the slackbot user ID by calling a API in point so I will import a few different libraries as well credential we just added and create a function called get bought user ID so this will test whether your slack authentication is Success so I will open Terminal and

then do python app.py then get this B user ID which you can paste over to the EMV file and that also means the connection is Success so we can basically command out this part then add a few new functions so I have one function called post message that allow the B to post message B slack as well as

add a reaction to the message remove reaction to the message so I can create some sort of interesting interactions we also need help function to get user name based on user ID as well as fetch the whole thre conversation history and in the end I will create two event listener one is when the bot is ADD menion as

well as when bot receive a message in the end I will set up a web hook and point for select to send message to us so this is a very basic simple function that every time when you receive a message it will just reply back yo so now you can see that it is uppr running we will also need to add another

terminal and we're going to use angro so enro is service that can put our local running end point to public internet so I will do Endor HTTP which is the port that we set up here so now you can see this end point has been set up popularly so next we want to select to send us all those information whenever it's a new

message so I go to event subscription turn on on this enable event and then you can paste in the URL one thing to note is that for this endpoint you will need to change a little bit to add this channel response back for the validation otherwise this won't be verified and then we add a few different events to

listen to from App Manion message Channel message group message I am and message MPI so that the agent will receive message whenever it is at menion or some new message from existing chattered is already involved okay great so now I can give a test I can go to my slack and then add this spot give a

message you can say it respond back with this message so it is working well the next thing is we want to start building a agent that can retrieve knowledge and respond poply and to do that I will create a new file called functions. py and this is where we will create agent so I'm going to import a few different

libraries in here I'm using the Llama index and AMA so AMA is a package that allow you to run this open source model on your local machine but I also import fireworks which the large L model inference system that allow you to run llama 3.1 401b in pretty good speed so our firstly create a large L model20

llama with a llama 3.1 model that I download on my MacBook now create a function called draft message taking the latest user input as well as a chat history and created one function called answer which rakes the user input and history called the local model I'm running and get response back as well as

wrong function called this answer function and this should be able to connect slack bar to this local model that's running on your machine so I can just go to the app.py import this function draft message and then go to the app mension replace the response from Yo to drop message passing on text

and same thing for the message event to call the drop message function passing on both the text as well chat history and now we can do contrl c and run the app again so if I open Slack now and do Bob SL hey you can say firstly it will add a Emoji to my message as a nice little interaction to indic it's working

and after message generated the Emoji will be removed it so this agent is running now so we have connect this to the Llama 3.1 AB Model and next thing you want to do is connect to the knowledge retrieval that we set up on the Llama cloud and firstly I want to add a knowledge agent so this agent will

be able to call function like knowledge retrieval get response back and generate answer so I will give you one tool called knowledge retrieval where I I basically call the Llama Cloud index and retrieve most relevant information back if the score is more than 80% and now here I also add one function called

reflect so this kind of one technique I found quite useful to force the agent to syn a bit before it answer the question to either say whether the knowledge retrieved is actually useful or reflect if there's any additional information can be provided to the user and they are convert them into tools but here because

I'm using the AB Model which is not that capable for my experiment so I basically just command out the reflect tool just like use the knowledge retrieval tool and now I'll give it a system prompt and create a react agent so here you will find that I'm actually using the react agent then the reason is because at this

point when I'm recording this video the two core support didn't seem to be that good it will still output some kind of weird message from my experimentation from the old Lama tool call that's why I still used react agent for now but later as inference provider like fireworks actually support function calling

properly then you can just Swap this with open AI agent or function calling agent so this pretty much it for knowledge agent but on the other hand I also want to add a ox Trader agent who will be looking at the user query and then decide whether the question can already be answered or it'll require

additional knowledge because if something can already be answered I don't want the agent to actually run the knowledge retrieval for simple query like hi or Hey but only do the knowledge retrieval when it's needed so we're basically have this kind of three steps in our agentic workflow Ox trator agent

to tr Arch and then delegate to either answer agent or knowledge retrieval agent now make a change to the wrong function our setup is retri cuz sometime I found AB Model is not that great as it can hallucinate the result and output something not those categories I around this otion agent first get a response

back if the result is non retrieval then call this non retrieval agent but if the category can be answered directly then just call Ama right away and return response so I can save this around the endpoint again and open Slack at Bob who is Jason's wife so I can see the agent is working so you can see the ox trator

agent categorized as knowledge retrieval then start running the knowledge retrieval agent and knowledge retrieval agent decid to call the function about Jason's wife and get a response back and give me the answer here but if I just give a simple message like hey then return can be answered and skip the

knowled retrieval and return answer back directly so this is kind of simple knowledge retrieval agent we created I do observe that AB Model often is not that great in term of categorization like sometimes it can categorize things wrong and often when the context became a bit longer it really struggle to

answer question based on the know retriev as well that's why I think you can use either hosting model on fireworks or replicate and then just comand out o Lama and still switch to bigger model like 405b and with bigger model I can also do some more sophisticated things like reflect as

well and the last thing I want to do is that I want the agent to be able to self- learning which means it might struggle to answer some question but if I come and provide some new information I want it to be able to learn and remember so next time it will be able to answer new questions and to do that I

can BAS created a new agent if it detect this new information received it can save the data to this notion Doc and also trigger a sync on my llama Cloud so everything will be up to date and to do that I will add two new functions so add knowledge is basically function that will call notion API to add new

information to this specific page and it will taking FAQs as well as page ID if FAQ is string then it return to Json and convert that into the specific format that notion API will accept then get page ID and block ID and insert data to that page so this is function one the second function is sync data after I add

the information to notion I want to trigger the sync data on llama Cloud so that it can vectorize again and get the latest information then I will add a learning agent who will be able to look at conversation abstract and reflect what a general knowledge can be saved for later and then save learnings which

will add data to notion and sync data on Lama Cloud I'll create tools from those function give a system PRP and create a new react agent and then go to O TR agent a new category called new learnings and move to the actual round function and one new condition if the categorization is new

learning then delegate to the learning agent and that's pretty much it so I can restart server to get a latest version and here if I give a new question hey who is Barry's wife and this is kind of new information that didn't really exist in the notion doc so it will answer back sorry I'm unable to find information and

then as a human I can come in saying bar wife is made then it will notice this new message in the chat so here is interesting that seem to fail to do this simple categorization okay I think I my found the reason this part of code is kind of duplicating the message because the

latest history already includes the latest user message so I can just remove that part for both the ox trator agent as well as the answer and I will make a quick update for otion agent I remove the user input but for the knowledge agent I will do this to GA all the chat history except

the latest information that be passed on by user input okay so this time is successfully categorized as new learnings and save data point if I open notion I can see this new information saved the barrier's wife is made so next time if someone ask same question again it will be able to answer so yeah this

pretty much a simple self-learning lar 3.1 knowledge agent that exist in your slack that you can interact with I'm really Keen to see what kind of interesting AI agents and new agentic Behavior you can start creating with llamas 3.1 on the other hand if you want to learn more in depth about building AI

products I'm actually starting a private Community called AI Builder Club where I'm going to share more detailed code breakdown of every single project I show in the video which should cover a lot more in detail of every single step and Basics so you can actually dive a lot deeper and copy the code if you need and

also and also leave comment for any question you have so I can prioritize answer them on the other hand every month I would do a deep dive with some top industry AI experts to share pragmatic experience of building production ready AI applications or even Workshop to learn in more interactive

way and I'm also working with some core AI platform to provide credits for you to use so I started this with aim to provide more enablement for you to become better AI buers you can click the link in the description below to join this community our continue sharing new learnings and Explorations I did with

those latest model so if you enjoy this video please like And subscribe subscribe and also comment below for any new topics that you want me to explore thank you and I'll see you next time
