# Stop Learning n8n in 2026...Learn THIS Instead

- **Channel:** Nate Herk | AI Automation
- **Date:** 2026-03-21
- **Duration:** 18:37
- **Views:** 21K views
- **URL:** https://www.youtube.com/watch?v=ZeJXI2MAhj0

## Transcript

A new phase for a automations has begun. For the past few years, we've all been using the same approach. Drag and drop platforms. Nitn make.com and Zapier allowed anyone to create automations in a matter of days that used to take weeks. But now with software like cloud code and anti-gravity, anyone can build

those same automations in just hours just by describing what they want in natural language. Drag and drop platforms are becoming the old way of building. And it's happening faster than anyone expected. It's even estimated that 50% of enterprises will have deployed these systems by 2027. So if

you're not learning how to build aic workflows right now, in a few years you'll be left behind. That's why today I'll tell you why this is happening, why you should be learning how to build aic workflows and how to actually build one in minutes using cloud code. So let's get into it. So what exactly is

changing? Well, for the past couple of years, if you wanted to build an AI automation, you'd open up something like NN or make and you drag a node onto a canvas, configure it, you'd connect it to the next one, you'd pass the right variables, you'd set up your API calls, if you had an error, you'd read the

error, you'd figure out what went wrong, you'd fix it, you test it, and you would repeat that cycle until everything worked. And don't get me wrong, that was a massive leap forward. Before these tools existed, you needed to be a developer to automate pretty much anything. Tools like Eniden made it

possible for anyone to build real automations without writing code. And that was massive. But now, Aensic Workflows kind of flipped that process because instead of telling the system how to do something step by step, you're just telling it what you want. You explain where the data is coming from,

what needs to happen to it, and where it should end up. And this is all natural language because all of us are really good at explaining what we want to be taken off our plate. We just don't know exactly how to do that. Just think about it like this. If you hired a talented developer to build something for you,

you wouldn't sit there dictating every line of his or her code, you'd explain the problem, you describe the outcome, and then you'd just say, "What do you need from me?" And that's exactly how Agentic workflows work. You describe the destination, and the system figures out the route. And I'm not just speculating

about something that might happen. The shift is actually here. The Aentic AI market was valued at just over $5 billion in 2024, and by 2034, it's projected to hit nearly 200 billion. 96% of enterprises plan to expand their Aentic AI usage this year. And by 2028, a third of all enterprise software is

expected to have Aentic AI built into it. So these aren't predictions from some random blog. This is where the money is going. And when you see numbers like that, it tells you one thing. This is the direction the entire industry is moving in. Now, if this feels sudden, it's really not. We've actually seen

this pattern play out before. Think about how AI automation has evolved in waves. The first major wave was back in November of 2022 or 2023. ChatBT AI chatbots hit the scene and blew everybody's mind. Suddenly anyone could have conversation with AI. They could generate content, write poems,

brainstorm ideas, and people started bolting chat bots onto everything. Websites, customer support, you name it. It was super exciting, but it was mostly conversational. It wasn't really doing work for you. The second wave was when people started combining that AI brain with automation platforms like Nen. And

this wasn't just simple stuff. This was plugging in real tools, real APIs into real workflows to classify tickets, to personalize emails, to summarize documents, take action for you. because you could also build full AI agents inside these platforms that made decisions, referenced memory, used

tools, and handled complex multi-step logic. And this was huge for the whole space. It's where most of the real value has been delivered so far. And it's when I really got obsessed with AI automation. And that is still incredibly powerful today. But here's the thing. No matter how advanced the automation was,

you were still the one building all of those advanced features. You were still dragging nodes, you were configuring API calls, you were mapping variables, you were debugging errors, and you were wiring everything together by hand. The ceiling wasn't what these systems could do, but the ceiling was how long it took

you to build them. And that's exactly what this third change really is. Agentic tools like cloud code don't change exactly what you build, but they significantly change how you build it. Natural language becomes the interface. The agent handles the implementation. It connects to your tools. It writes the

code. It fixes its own errors and you focus on just clearly describing the outcome that you want. The same automation that used to take a full day to build an NADN, you can now describe in pretty much just plain English and have running in minutes. So, it's one of those things where each wave didn't kill

the previous wave. It was just a stepping stone. Chatbots are still alive. They still work. They still provide value. I still build traditional AI workflows and traditional AI agents. But each wave made you way more productive. So, we're seeing this massive shift right now. But here's the

question. Why are people actually making the switch? Well, to explain that, I thought that it would just be easiest for me to show you the process of if I was building something in NN or building something using this kind of new method. So, let's say we wanted to build an automation that's going to check in on a

specific AI news YouTube channel every 8 hours. Now, this particular channel usually posts daily, but you don't always know the exact time. So, that's why we're deciding to check every 8 hours. If there is a new video, then we'll get sent the key highlights. If no, then nothing will happen. Now, the

key here is how do we actually know if it's a new video or not? Well, if we were building this init, what we'd do is I'd probably grab a schedule trigger and I would say, okay, cool. I want this to run every 8 hours. So, I would just change this to hours and then I would say 8 hours between every single

trigger. And then what would be next? Well, I would probably need to figure out how do I actually go check the data from that YouTube channel to see if there's a new video. At this point, I would be on my own to try to find out, do I use ampify? Do I use super data? Do I use Google API? How do I actually get

this information? And then from there, once I actually found out the text stack I wanted to use, I would have to set up my own HTTP request with the URL credentials, parameters, stuff like that. So, let's say we've gotten to the point where we're getting data back from this HTTP request. What would be next is

we'd have to check, is this video new or not? And now, this is where it gets a little more complicated. If we were building out this logic ourselves, we'd have to first think about, okay, we need some sort of database to see if a video has been processed or not. So maybe I'd use the video ID and I would just mark

it off on our sheet, which means that first we'd have to do some sort of filter. So I'd have to do like a Google sheet row or maybe a data table. And I'd have to get rows from that sheet, but I'd only want to return rows if they don't already exist in the database, which means I'd also have to go

configure some sort of third party storage. After we figured that out, we'd realize, okay, cool. If a video comes through and we've already processed it, it's going to go down here and do nothing. But if it hasn't been processed yet, once again, we have to go figure out how do we actually scrape the

transcript from this? How do we prompt the AI agent to read the transcript and give us the key highlights? And then most importantly, we have to mark it off in that database to make sure that it doesn't get processed again. So, this is not to say that it's not doable. I've built tons of systems like this in Naden

and it's really not too difficult once you understand logic and workflow patterns and dduplication and stuff like that. So, off the top of my head, just to show you guys, it probably would look something similar to this. And it's not that bad. I'm sure all of you guys have built editin automations that are just

this complicated or even more. But when you consider the fact that you can literally come into cloud code and just tell it in natural language that you want that and then everything's handled for you. It's pretty extraordinary. So you can see here this conversation had to be compressed because it ran out of

context. But basically I started off by just saying hey I want to build workflows. I want to use trigger dev and I want to use cloud. I want to scrape daily news from the YouTube channel Nate B Jones. I want a structured summary and I want it delivered to ClickUp. It built the initial version in like 2 minutes. I

ran it. It worked. And then I thought to myself, cool, the things I'm curious now about are how do we make sure that it doesn't give me the same video twice? I don't want it to analyze the same one again. So, prove to me that that's the case. And then I asked it another question which was more about this

workspace. But as far as the automation, it basically said, "Okay, cool. Dduplication. Here's exactly how it works. Every time your YouTube check type script runs, we get this sort of item potency key, which is the video ID." So, if we get a run that happens and that same video comes back, it's not

going to process it again. So, really what it's doing is the exact same flow that we set up here except for we didn't have to think about the logic. We didn't have to build the database. We didn't have to build the extra rightback step. It just handled all of that for us. So really the main point that I wanted to

drive home here is that these agentic workflows or these kind of like new, you know, v2 of automations, they're not actually like extraordinarily different. It's the way you build them that's extraordinarily different. They're so so so much easier to build now using tools like cloud code and trigger.dev. And

we're not just limited to having automations that are pretty deterministic and on a schedule. Here's an example of one that we would trigger by creating a new task in ClickUp by putting in a company name. The agent would wake up. It would grab that company name. It would decide its own

research strategy and it would be in this loop of research until it realizes that it's good enough to give the output to the human. It would put together a structured competitive brief and then it would post it back to wherever we want. And I wanted to show you guys what that actually looks like in trigger.dev

because a lot of us love n for the visual element. I love it for the visual element. I think that's why it blew up. But trigger.dev also has a visual component so we can actually see what's going on. So the example I'm about to show you right now are going to use two automations. We have the ClickUp

research polar and we have the actual company researcher agent. Okay, here we are in ClickUp and what I'm going to do is create a new task and I'm going to enter a company name. So, I'm going to do lovable. Hopefully, it's able to find the right one. I'm going to hit save and then what's going to happen is the agent

is going to pick up this task. It's going to move this to in progress, which lets us know that it's now working on it. There we go. It just got moved to in progress. I'm going to go back to trigger. I'm going to click on runs. And you can see that the first one was the polar which picked it up and it said,

"Okay, cool. I'm going to trigger the company researcher agent." If I click on the agent, you can see that what it's doing now is it is doing its research. It called the search web tool twice. It's looking for lovable. It called the search web tool one more time. And we can see this in real time actually kind

of spinning and thinking through what it's going to do next. There we go. So, it basically just decided that it was good enough. It finished up. It sent us a brief. And now, if I go back into my ClickUp, we should see that Lovable got moved to a complete task. If I open it up, we can see that our Upai agent right

here gave us a brief on Lovable. We got some recent news. We got some growth signals, all this kind of stuff. And keep in mind, I built this by literally saying to Claude Code, I want an AI agent that can see tasks in ClickUp, do research, and then send me a brief. I didn't give it like anything else

besides obviously like API keys and stuff like that and obviously building something like this is very very doable in end but once again it would just take you longer. Okay, so aentic workflows are this good then why isn't everyone already using them? Well, there are a few reasons and it's important you

understand this before we dive in. So the first one I would say is context drift. The longer you work within an agent within a single session, the more it'll start to forget what you told it earlier and maybe hallucinate a little bit. It might reference old code. It might revert to patterns that you

already used. It might forget things that you just told it. So, think of it like giving someone instructions for an hour straight without letting them take any notes. [music] Stuff is going to slip through the cracks. But that fix is pretty simple. There's lots of ways you can handle this. You can break your work

into shorter focused sessions. You can keep a project summary updated so the agent always knows where things stand. There are tons of ways to fix this problem. And the second thing is hallucinations. The agent will sometimes invent things that don't exist. Maybe functions or maybe specific rules that

it somehow made up or API endpoints that aren't real. It'll make code that looks clean but it breaks the moment real data hits it. And these aren't super obvious errors, especially if you've never actually written code yourself. They're subtle and they only get caught if you're actually testing. So that's the

rule. Whenever you have code, you always have to run whatever builds. They'll just take its word for it. You can even build custom sub aents whose only job is to review and QA everything before it actually ships. And I've actually seen studies and interviews from big firms like Anthropic saying that their QA

agents or their code reviewing agents are actually catching things that humans are missing. So they are definitely capable. It's just a matter of context and direction. Now the third thing is scoping. Sometimes it overengineers. You ask for something simple and it hands you a multi-layered architecture with

all these special frameworks that you don't actually need. Now other times it might underengineer. It might just try to slap on a band-aid fix to something instead of actually fixing the root issue and fundamentally making the code base scalable. Either way, the solution is pretty much the same. Be very

specific upfront. Use plan mode. Have it ask you questions. Set boundaries and the agent will be able to stay inside of them. And then the last thing I want to talk about is what happens after you actually build the automation. Because in NN you've got like a dashboard. You can see everything. You've got all your

execution data right there and it just feels more visible. With Agentic workflows, you're writing code and the code that you're running in production needs to be managed somehow. You need to make sure you have error notifications so you find out when something breaks at 2 a.m. You need observability so you can

actually see what your automations are doing. And you need version control so you can track every change and maybe collaborate on projects with other people on your team. Now, the agent can help you set all of this stuff up. This isn't new. This is still how code used to work before all of this stuff. Every

single one of these problems is manageable. I'm not telling you this to scare you off. I'm just telling you this because if you jump in with zero awareness, you may hit these walls and then just think the tool is broken when in reality you just needed to know how to work with it. And if you've been

learning, which I know a lot of us have been, you might be wondering, was all of that time spent learning that tool a waste? No, it's actually a huge advantage for you. And it taught you how to think in terms of automation, triggers, actions, data flow, error handling, AI prompting, observability.

That's exactly what matters when you're directing an agentic system. The knowledge doesn't just disappear because the building method changed. It was the fundamentals. So it was the foundation that you needed to step into the AI automation world. So think about it when like NN came out, people who already

understood programming logic had a head start on someone starting from ground zero. The same thing is happening now. Your understanding of workflow architecture is what makes you better at directing cloud code than someone starting from ground zero. Because now our jobs shift to no longer configuring

nodes individually, but more so to provide the plan, the direction, and the guardrails and to spot when the agent gets things wrong. And that's a skill that only comes from experience. You already have it, hopefully. Okay, now that we've seen a demo and we've talked about some of the technical things that

go into actually building these automations, let's just do one live. So, I'm going to be building on top of this project here, but if you want to see a full breakdown of how exactly like trigger.dev works and how you can get started from scratch, then check out this video. I'll link it right up there.

And I basically walked through all of this. And what I'm going to do here is I'm going to build on top of this project which has the agent that we saw earlier which was the AI news digest as well as the company researcher just to show you that as you build more and more automations and as your project grows

it's even easier to extend the functionality. So once again I always like to recommend that you start on plan mode and you talk to your agent a little bit to figure out what you're exactly going to build first. But for the sake of video I'm just going to go on bypass permissions and we're going to see if we

can essentially oneshot prompt this thing. Hey Claude. So, I want to build another agent and I want this one to be triggered by a ClickUp task. Once again, similar to our company researcher. However, this one I want it to be a different list. So, I need you to create that and I will drop in a topic and the

agent needs to basically pick that up, do some research, write me a LinkedIn post about it, also give me a infographic that can go with it and it would be ideal if it could create that infographic using Nano Banana Pro and you can use key.ai in order to access that via API. So figure all that out and

ask me any questions that you may have, but let's go ahead and build that automation. And now I'm going to shoot that thing off and I'm going to let it do its job. My whisperflow didn't spell key. Right, so hopefully it finds the right one. It's searching for the wrong one right now, but maybe it'll be able

to figure it out. Nice. It found the right endpoint. Okay, so this is awesome. Just like I wanted it to. It's going to ask us some questions before it keeps building. It said you mentioned key, but based on my research, I believe you meant this type of key. And do you already have an account? Yes, I have an

account, and I can add it to the&env file right away. Where should the LinkedIn post and infographic be delivered when the agent finishes? I wanted to comment on the ClickUp task just like the researcher. ClickUp list style. Same space as research Q. Just name it LinkedIn content Q. That's

perfect. And for the post style, let the AI decide. Always write in first person thought leadership. Yeah, sure. Let's just do thought leadership style and shoot off those answers. All right. So, it's written this new plan for us. It made a new ClickUp list. So, I'll open up ClickUp. We can see right here we've

got LinkedIn content Q. And now it has two files to create. It's going to make another ClickUp polar which is going to watch for the LinkedIn content Q tasks and if it sees any, it will send them over to this Claude agent called the content creator. It has three tools, search web, read URL, and finish. It's

going to do a research phase. It'll do a writing phase, an infographic phase. It'll also pull to see when the image is done. So, that's awesome. We don't have to set that up ourselves. And it will then output a comment with the full LinkedIn post and the image. All I need to do now is add in my key, API key, and

then it should be good to go. I've added that API key. go ahead and build the automation. All right, so I sent that off. It made a to-do list and it's going through and building that right now. But while it's doing that, I wanted to show you guys in Nitn what it actually looks like to generate an image and then pull

to make sure that you're actually getting that image back. So here's a YouTube video I did about nitn for nano banana pro. There's text image, image image, all this kind of stuff, but they're all the same, right? Basically, when you use a service like key.AI, you make multiple requests. Your first one

is to actually create the image and then you have to wait and then you have to check in on the image. If it's done, great. But if it's not done, you have to make sure that you go back and you continuously loop or pull to make sure that it is done. And so this isn't extremely difficult, but it is a concept

that trips up a lot of people. So the fact that Claude Code just handles this automatically for us is pretty cool. And of course, we don't have to set up the different API calls to make the different requests, all that kind of stuff. Okay, so what it's doing right now is it's firing a test run in our

trigger. So if I go in here, you can see that we have some new things added. We have a LinkedIn content puller and then we have a LinkedIn content creator. So I'm going to go ahead and go to runs and see if any of these are running. Right now the content creator is running and we can see that it's it's going through

some stuff. So we've got an issue right here but it's searching the web. It's reading the URLs and then it should be creating an image. The topic that was sent over by the way was the rise of AI agents in enterprise automation. And once again this is just a test run. We'll see how it works and if

everything's perfect then we would push it to production because you guys can see up here I'm currently in development. So what you can see is that we actually got two errors. We got a clickup error and then we also got an infographic error. And I went back into cloud code to have it fix it for us but

it already came back and said nice the agent works. It did three searches. It did three URLs. But we ran into two issues. So the prompt field is being sent incorrectly. So it's going to fix that. And ClickUp 401 expected some sort of weird ID, but because no task was actually created, didn't work. So it's

already on these fixes, and I didn't even have to tell it anything. So now it's firing off another test run. So back in here, we can see that the content creator agent is running once again, and this time it should be able to hopefully make that infographic for us. You can see right here that it's

doing the polling. So, it attempted to wait here and then it waited again and then it waited again and it's going to keep waiting until the infographic is actually done. So, it's pretty cool. Now, once we actually realize that it doesn't actually happen this quick, it looks like it's checking like every 2

seconds. We can tell it to increase the interval between each step. We can tell it to increase the interval after each attempt to maybe like 10 seconds or 20 seconds because this is a little bit much. But that's why it's so nice on Trigger Dev that we can see every single step and we can see how much time is in

between each step. All right. And now it's going to actually do it for real. So, it just created a task. The agent moved it to in progress and it's going through that exact same flow again. It called search web four times. It did three read URLs and now you can see after 30 attempts of polling the

infographic is ready. And apparently the results have been posted to ClickUp. The task is marked as complete. If I open this up, we can see that we have our LinkedIn post right here. 79% of organizations have adopted AI agents, but only 34% have successfully implemented them. There's a gap. There's

actual numbers right here, which is great. And then if I go to the bottom, we can see the infographic. I'll click on this, and this is the infographic we got. So the AI agent revolution, we've got stats, we've got the implementation gap, proven business impact, scaling to standard, what winners do differently,

and that run took 2 minutes and 23 seconds. So considering that I didn't give that any prompt as far as like how to write the post or what the infographic should look like, that's a really solid first iteration. And now all we'd have to do is tell Claude to push that into production. We would come

into trigger dev and then instead of being in development, we would see these in our production environment, meaning they'd actually be able to run all the time. And then in ClickUp, all I'd have to do is make a new task with a short description of a topic that I want a LinkedIn post about. And then in about

two minutes, I would get a LinkedIn post and an infographic. So, Aentic Workflows just became the cutting edge for automation builders. But here's what I need you to understand. NN is certainly not dead. It just became the foundation. Aentic Workflows made everything way faster, but you still need to understand

how workflows actually work to spot mistakes, optimize systems, and make [music] smart decisions. That's not going away anytime soon. So if you want to stay ahead of the shift and learn both the foundations and the cutting edge stuff, then check out my free community with over a quarter million

members who are building AI automations. Here you can find full courses on both end and cloud code, plus weekly live calls where you can ask me anything. And in case you want to go even further in your automation journey and specifically learning more about how to spin up a business around this kind of stuff, then

check out my paid community. Both links are in the description. But that's going to do it for today. Thanks for sticking with me to the end and I will see you guys in the next one. Thanks everyone.
