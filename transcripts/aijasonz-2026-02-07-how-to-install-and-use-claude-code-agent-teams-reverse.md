# How to install and use Claude Code Agent Teams (Reverse-engineered)

- **Channel:** AI Jason
- **Date:** 2026-02-07
- **Duration:** 9:39
- **Views:** 31K views
- **URL:** https://www.youtube.com/watch?v=S2WTTMXYcYY

## Transcript

Cloud code just had a massive upgrade of agent teams feature which is different from the task and sub aent feature we had before. This time it can spin up three to five different cloud co instance to collaboratively complete a task and project and each cloud co session here can communicate with each

other with different communication protocol method. I spent a bit time to look into the actual logs of the larger mode call from the new agent teams feature to understand how it actually works compared with the previous sub agent. And now I think I finally have a good grasp. I'm going to take you

through how exactly does team agent works and how each agent share contacts with each other and how they communicate step by step. But firstly, let's talk about how do you actually install and use agent teams. So to use cloud code agent teams, firstly making sure you update your cloud code to the latest

version which is 2.1.34. And then you want to set environment key cloud code experimental agent teams to be one in settings.json. You can just do code /.claw claw/s settings.json. This should open up your settings.json file at global level. You can insert this env key here to cloud code experimental

agent teams to be one and save it. And then making sure you're adding a new cloud code session. Now if you're prompted with something that mentioned that you should create agent teams to do certain tasks, it will start setting up different teammates and then create task list and trigger different cloud co

session for each task. Below you will see those different agent sessions start showing up. You can set enter on each one to see what it is doing. And looking at talk, you will see that for each agent team, it will be given a prompt about the task itself. You can talk to each individual team member if you want

to give specific instruction. Once finish, it will shut down the teammates. Basically closing off each cloud code sessions and go back to the main session. But to b use agent teams, you want a t-max type of terminal experience where you just bring up different sessions so you can see what each agent

is doing live. And to do that, the easiest way is you will download T-Max or if you're on Mac, you can download it term 2, which is more advanced terminal app. And you need to go to settings, general, and turn on the Python API option. Once you did that, just close it two and restart. And for the new

session, you can run cloud- teammate dash mode. So this open cloud code with agent teams function in split view. As team lead agents setting up new agent team members, you will see new session windows just popping up on the other side. So you can see clearly what each agent is doing just clicking inside the

session and send new message if you want. So this is the best way I found to use the agent teams but more important part is that we actually want to deeply understand how does this agent team works so that we can decide when to use this agent team methods versus the sub aent and here I did a whole back and

forth investigation to understand all the new tools that cloud code is having now and how the communication happen between different agents and let me break it down for you. So one of the key change is that before agent teams clock basically have this one tool called task tool that can spin up a sub agent to do

certain things and once sub agent finish the session just terminate and only the summary response will be sent back to the main agent. So this how it works but with agent teams it is going through a much more complicated process with a list of new tools that agent has. Firstly agent will call this new tool

called team create. Basically main agent can call this team create tool which will create new agent teams under your doc/ teams folder and this will create a config file including some basic information about the team and at this point the team member array is still empty. There's also one configuration

called agent type which allows main agent to define who the team lead is. Moment it's not entirely clear why they have this one. I assume it's for some future features that they might add. But this is the first step of team create and the second step is creating a list of tasks. So this is different from the

task tool which will spin up new agents. Task create tool is to log all the to-do for the teams which will be added to doc clause/task folder as well where each task will have its own JSON file to lock the status and you can see for each one it will including things like subject description status and block and block

by. So this is later will be used for identify the dependencies. So agent know when to pick up which tasks and once this task list is created that's where it will run the actual task two. So this task two is same task two as what we have before for spin up sub agent except it is getting some upgrades. So task two

now has two new entities. Team name will be used to identify which team it is and name is actual team member name. And once those are wrong, instead of spin up a new sub agent, it will actually create new cloud code session where each cloud code session will inherit the team information, the team ID as well as a

task list. So it can autonomously complete, update or even create new tasks. And typically for each new cloud instance, it is supposed to use task update tool to update status of task which looks something like this. It has task ID, the status which can be pending, in progress, complete or

deleted. The owner will be default this sub teammates and if they want they can add this dependency information to add blocks and add blocked by and they can continue this task until they feel like they need to send message to and this send message tool will allow the sub teammates to communicate back with team

leads which is main agent that coordinate the work but also it can talk to any other teammates. So this send message tool has a few methods. One is a message which is send a one-on-one message to any other agent or it can broadcast which means it can send same message to every single agents. But for

the sub agent most likely it will use this two methods. But for the main team lead agent which is agent that we are talking to and orchestrate whole agent teams will also have this shutdown request method to a specific agent and this is a way how the team leads closing or terminate sub teammates session. So

from what I understand is that the team leads will send a shutdown request to the sub teammate and after that request it can send back shutdown response to the main agent which will automatically terminate this sub teammate session and in the end the main agent will call this team delete tool to actually shut down

the whole team and the message communication protocol between different agents is basically injecting new user message to each other's conversation history. So in teams folder there's a inbox folder that is maintaining the inbox for every single agent teammates and it has a read status which probably

is used to identify whether the message has been sent to the sub teammates yet and for the agent who received the message the new user message will be sent to this agent with this teammate message tag that including the full message information based on the information can decide what to do next

here I'm using landfuse to actually track what exactly goes into each agenda model call for my cloud code. I was using cloud trace for this which normally gives me really indepth track of cloud code system prompt tools it has access to and everything but unfortunately that no longer works with

the latest cloud code but landfuse does this cloud co integration that you can use. Basically it is utilizing cloud code stop hook to automatically sync data with lampuse after each time cloud co finish the session. It is not as good as cloud trees but still give me good visibility about what is actually going

on for each request. So this how agent teams work. There's a lot of room for imagination with this new setup because they allow them to share context between each other on demand as well as a shared list of task. I'm pretty curious to see what kind of use case people come up with that actually utilize this

capability to send message to each other as well as let each sub teammates to update new task as they go. And here's one pretty interesting example for debugging because quite often when you just use one sub agent, it tend to find one plausible explanation and stop looking. But for some more trickier

situation, it is actually useful to have multiple agents explore different directions and critique share findings with each other to conclude what is most possible matter. And here I just tried with the super design production codebase that we have. And this one bug that has been hidden pretty deep. They

can tell the agent spin up five agent teammates to investigate different hypothesis have them talk to each other and try to disprove each other's theory like scientific debate update findings dock with whatever consensus emerge. So here you will see that the main agent first they create the task list as we

discussed before and then for each task it spin up a new cloud code sessions on the fly where each one is investigating a different directions and you can see this time sub agents were sometimes use forecast to send their findings to all the other agents debate with each other and in the end each one send their final

verdict back to the main agent. And meanwhile sometimes they will also use this right memory tool which is quite interesting and if I open it it seem to write a kind of documentation about the consens findings from each agent and in the end it come back with a complete picture which is a lot more in depth

than you will get from just one sub agents and this is just one quick example of what potential new use case can be unlocked with this new agent team structure compared with the previous simple sub aent setup as I mentioned I'm really keen to see what kind of use these people going to come up with this

new setup. Comment below, let me know any interesting findings you have. Meanwhile, if you want to dive deeper, you can join AI builder club, which is a community of top AI builders who are building and launching AI products. Their learning resource and weekly workshops where we dive deep into

building agents and AI coding workflow. I also put a link below so you can join if you're interested. I hope you enjoyed this. Thank you and I see you next time.
