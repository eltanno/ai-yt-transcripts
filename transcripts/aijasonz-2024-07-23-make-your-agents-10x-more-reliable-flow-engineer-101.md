# Make your agents 10x more reliable? Flow engineer 101

- **Channel:** AI Jason
- **Date:** 2024-07-23
- **Duration:** 17:11
- **Views:** 18K views
- **URL:** https://www.youtube.com/watch?v=01g_EfO-Dms

## Transcript

for people who build AI application before you'll know that building AI application is somewhat weird experience everything works during the test but after the release things looks not as good and just keep praying to God that please let large langage model follow my prompt the nature of large langage model

is that it is undetermined and this led to many weird and interesting prompts that people have tried for the past 12 months I remember seeing an awesome open source project where also report part of problem like this is very important to my career please follow for some important inst instructions and there

also some common prompt tactics that people tried like give gbd4 some tips to making sure it follows some specific part of instructions and believe it or not some of those weird promp actually back up by some academic paper to Pro and test actually works but in general One Challenge across all the AI engineer

is How Can you tame the large language model better to making sure it follows instructions consistently a lot of people are talking about how the next stage of promp engineer is a flow engineer like Andrew csy talk about how flow engineer moving from a naive prompt answer Paradigm to a flow Paradigm where

the answer is construct iteratively and there are also popular open source project like laning start building products specifically for this type of flow engineer design and I think to many people mostly you can't understand the concept of flow engineer which is instead of getting the large L model a

prompt we can break down a task into small steps and try to improve the result it trat a step by step but even though conceptually it makes sense there's not a lot of information about what flow engineer actually is and how do you actually adopt it in your day-to-day a large L mode application

design that's why today I want to dive into a bit more about what flow engineer actually is and how can you start adopting those methodology in your design so at high level flow engineer is something in between L model chain which is extremely reliable but not very flexible and a free form AI agent which

you basically just give High Lev goal it will try to use whatever tool it has access to to complete task in a fairly Dynamic way the flow engineer is something in between it still Define high level steps but still using agent or large L model to control some hard of flow and let's take a very concrete

example let's say I'm building a research agent if I'm using large Lang model chain I'll probably build a very specific function flow where it will do the Google search based on a top user GI and then generate outline first write each section and merge them together and C it down so this flow is extremely

reliable and specific but downside is that maybe the research is not as good because comany the research can take multiple different tries until you can find right information same as a Content generation but if you build an agent to do the research you don't really need to Def find a specific process you just

give agent list of different tools and functions that it can have access to like Google search extract website content and you just give it topic and it will be able to plan Sy what kind of action it can take and continuously taking all sort different action until it think there's no further action can

be taken so the benefits here is that it is extremely Dynamic and flexible the the problem is often you don't really have control about what kind of process the agent should take and if you ever try to build AI automation for a business most of the time they actually do have a specific procedure process the

AI needs to follow and this where flow engineer that become interesting so flow engineer is basically try to get human predefined what are the high level process or procedure that AI should follow but you can still get large L model to make a lot decisions in specific steps of points like you can do

the research and I have a check to see if all information has been found if no then do it again and repeat this process until all information is found then move to Next Step which is right content where you can also insert the critic and review process and now you might argue that to achieve this type of process

theoretically we can just give a agent a specific instruction and system problem about a specific process is should follow and that should already achieve some kind of flow control that we want to achieve with Flo engineer well that is true for many of the simple cases but when you dive into a lot of real user

cases the procedure in sop is a lot more complicated than a few simple step flowchart it can have wide range of different branch and it is extremely difficult for you to convert a complex flowchart like this into a prompt and even though you do as the process became bigger and bigger the agent start

struggling to follow the instructions because there are limited amount of effective context window so just using prompt to guide agent to follow specific procedure might work one or two times but it's very hard for agents to consistently follow instructions at this point in my wondering is this flow

control looks extremely similar to those multi-agent Frameworks that people have been using like crei or autogen and that is exactly right most of those multi-agent system provide a way for you to control what are the different steps that the AI should follow by breaking them down into different agents and all

those multi-agent framework like K or autogen they just provide different ways for you to control flow and different ways for you to manage the memory and state for example if you're using autogen the way the person flow is controlled is that they will have something called group chat manager who

is continuously monitoring the chat conversation and decide which node or agent to go next and state share across all agents are just the full or partial chat history and that's the reason why when you run autogen you realize the cost is a lot higher than just any normal agents because for every single

point the large L model is processing the full chat history well L graph is just another framework that allow you to control the flow and State Management you can basically control the flow using either code or large L model and the share State can be been more optimized where you can define specific important

information like for a research agent example you might just want to share what kind of website has been scripped already and what information we can added for each data and if you're interested here's my take of different sorts of multi-agent Frameworks they all have its PRS and cons and it's hard to

say which specific one are the best but the one I want to dive into a bit more today is Lang graph from what I can see lra seems to be a framework that does provide a lot more flexibility in term of flow control and State Management though it is a lot more complex in term of setup I think it is definitely worth

diving into so what is Lang graph and how does it work fundamentally Lang graph has two key components one is graph which you can just consider as a flow another is a share state so share state is a memory or contact that is going to be shared across all different steps but before we get into it I know

many of you might be using GitHub co-pilot which was absolutely a game changer but recently I canceled my GI cop co-pilot subcription because I found something that is better and free that is codent so you can think of codent as a free alternative to GitHub co-pilot where it has a killer use case of auto

complete but with a bunch of unique and useful feature like you can ask codium to refact your existing function to add a new feature fix bug or add comments and documents or translate your python code into other languag like JavaScript or typescript and one of the most powerful and useful feature to me is

that codium is context we which means it'll be able to explain and answer your question about the whole code base and this is extremely useful because when we start a new framework like Lang graph often there's no enough documentation to tell us how to use this framework every time when I open new report like L graph

if I open codent you can see that it start loading and vectorizing the whole code base and once it is finished I can go to chat and start asking any question about this codebase to understand better for example when I'm viewing some example I don't really understand what tool node is so I can just switch to

codent and just ask what is to node and do command enter it will start looking through the whole code base and explain to me what a tool node is and also the code example so this really speed up the learning process for me whenever I use a new framework and they support you to chat with AI in any sort of context like

a specific function or class or even popular Ripple on the GitHub and while I'm in the code aner I can just do commend I to activate codium and ask help me build a reactor agent with L graph then we start processing and Genera a whole code example for me about how to use lra and I can either accept

reject or give feedback by followup and for existing function I can click on this refactor button and ask it to automatically add documentation and comments for me and the most important thing is that it is free forever if you are just indiv user they really just try to make money for teams I'll put a link

in the description below where you can go and click on get codium and select any type of code editor you are using now if you're using visual studio code like me there's a quick button you can just click and install now let's get back to what Lang graph is and how can you use it so first thing let's talk

about the key components of graph there are two key components one is called node and each node you can think of as a specific step in your workflow it can be either a large Range model call or a specific function you can call or it can be even a agent and second concept is AG age is basic connection between

different nodes so that you can use to control the flow if you are building a research agent your graph might look something like this you'll have two note one is a website research agent that can do the Google search and find the latest news or information and the second note is a large Range model call to generate

report and here will be a connection age between those two notes and this is one of the most simplest possible graph but the age can also be conditional for example if you want to make this research agent a bit more powerful we can change the graph a little bit it will try to research within the

company's website first to get firsthand information and after that we can run conditional age where it can run a function or get a large Dage model to make a decision is all information that we supposed to found already found if yes go generate report directly if no we can pass on to another agent who have

access to whole internet so that it can research and pass on all the research data to the lar L model to generate report but to achieve such workflow po play we actually need some sort of share knowledge between the first agent second agent as well as large L motor step in the end and that's where the second part

State come in so the state is almost like a shared memory between all those different steps So In This research agent example we might have a few different states one is a web that we have script already as well as the latest data points that we found from different states and those States can be

updated and read from any single steps a framework like autogen is pretty much similar except in autogen the process of flow is controlled by the group chat manager which is a large Range model that going to look at conversation history and decide what's the next step and actions while the state is basically

the full chat history that keep broadcasting to every single agents whereas a framework like Lang give you a spefic specific information inside State instead of passing on the full conversation history so you have more control of the memory and optimization of the cost and the flow most of the

time will be controlled by the code instead of just a lar model so this is pretty much how can you build a reliable agentic system it does require a bit more pre planning because you are basically offloading a lot of planning and decision making from the agent to the assistant designer which is human

and the common person to start design such system is that you firstly want to map out the whole flow and graph so that you can understand the key components then you can start listenting out all the different states and data will be useful and necessary to be shared across every single steps and I want to show

you a quick example of how can you create a reliable SQL agent where user can just ask natural language question and agent can turn that question into a proper SQL query to get data form database and generate answer and I think this is a great example because you can totally just build a free form agent

where it just have basic tools like getting a table getting a schema and let it decide what other order to execute but the problem if you ever try to build a SQL is is that often they are not Genera the right SQL query so we actually want a good retry mechanism there if you can break down the process

into a more linear and controlled flow we might get a much better result so we can actually use a graph to build a agentic system where if follow is very specific process it will try to get the most relevant data table based on the user question first and then it will also try to get a schema of those data

table and then it will try to generate query reflect a bit and extract the proper query and in the end to execute it if the execution result is wrong then it will send back to query generation step to generate again and if success then it can generate answer so I'm going to quickly take you through how can we

build this and team form langar already compare these two type of Agents one is free form agent another is those kind of multi-step breakdown agentic process you can see the simple evaluation score the breakdown version answer score is around 0.67 while the free form agent is only 0.53 so it is significant improvement

compar with free form agent and I'm going to quickly show you how can we view this so I'm going to open the notebook and then we'll try to download a simple database to the local machine install L chain and then use Ling SQL database tool and then quickly test if the SQL database is already running you

can see it returned this database and you can also download free software like DB browser to quickly take a look at any database to understand structure and here if you take a look it loaded all the data table as well as rating schema public and next we will use l graph to build a tool node so tool node basically

is a special node or step in the graph that you can just give this graph a tool like execute SQL query get a specific table schema things like that and for this one we will set up some error handling it can send back error message and retry and next we will also test the two default tools from the Ling SQL

database toolkit once is list all table tool another is get schema tool you can see below it is working well and we will also create helper function called DB query tool this is basically tool that agent can use to run the SQL query generated and then we will also quickly create a query check tool that can

basically review the initial query generated fix any issues if the initial one is wrong like this table here you can see that it will automatically self correct to making sure the query is more likely to be accurate and those are all the tools that we need next we can start setting up the graph so we're import a

few different libraries the state here will be pretty basic it's just the chat history then we're Define a new graph with this state and first you want to add a node to get rant table based on user query so I Define function called list table note where we will compose a message about the user message and we

will just quickly force a tool WR so in here I put a AI message try to run a specific tool and then I will do the tool message by invoke the list table tool directly so this should return the message about the user request AI get it AI try to do the function code to get all the tables available and then I will

pass on this message to get agent continuously generate a request to G schema tool to G schema of rather tables and in the end I will return the full message so this function will basically gather rant table as well as generate message to try to call the guas schema and then we'll add this node to be list

table tools and then we'll also add a second node which is guas schema tool then after that I want to create the query Genera Noe but before we do that we will create a tool called submit final answer so this is tool that query generation node can call if they think they already get a final result and then

we'll give a promp of cury generation system quickly create a chain for the cury generation and then Define a function called query generation node and here you can see we put some Logics there the log model here only should have one tool which is submitted final answer if the tool is not submitt final

answer then we'll put a arrow message here and then we're adding those no to the graph this will basically look at the initial query generated by this query generation node and do some fix with the function that we created earlier which the query check and in the end we add this note of SQ query uh and

the last part is a part that going to be quite interesting so if you remember there will be special type of AG that is conditional that can allow you to control where the things should go next and this should only have three potential output and the workflow correct query or query generation so if

the last message from the query generation is to cost which means it actually call this function submit final answer that means the workflow has been finished so it will return end but if the last message is Arrow then it should ret try the query generation again otherwise you can return correct query

to continue the workflow and this pretty much now we can just connect everything together firstly go to the list table tools and then go to get schema tools and then query generation after query generation we should wrun this should continue function to decide where to go next and if it's correct query then go

to execution and after execution we go back to qu generation to validate whether the answer is correct and we can compile and you can run this to quickly visualize the graph you just created and if we try to quickly run this graph by asking which sales agent made the most in sales in 2009 you can say turn the

sales agent who made the most in sales 2009 is Steven Johnson with 164 and if we go back to the DB browser you can see among all those table for that question we probably will need to look at employees and if I go to browse data for the employee table among all the sales support agent Steven Johnson does look

like made them and this will require to run the query across invoice as well to calculate all the invoice relevant to this person and we can also stream the result to see the step by step so first it run on this tool successfully identify that it need to get schema of this two table in EMP and invoice then

try to get schema then you generate the query for three times only third time it seem to work then dat a correction then try to reflect review the query execute it so this example of how can you create a more reliable agentic workflow with graph it definitely feels a lot more complicated than creating free form

agent but the trade off here is that you will have a much more controlled behavior for those agents so I'm really ke to see kind of interesting projects you're going to start building with those kind of graph flow engineer type of projects if you enjoy this video please consider give me a like And

subscribe I will continue posting interesting a just thank you and I see you next time
