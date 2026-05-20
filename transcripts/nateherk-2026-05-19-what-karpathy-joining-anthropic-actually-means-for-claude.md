# What Karpathy Joining Anthropic Actually Means For Claude

- **Channel:** Nate Herk | AI Automation
- **Date:** 2026-05-19
- **Duration:** 16:24
- **Views:** 26K views
- **URL:** https://www.youtube.com/watch?v=brB-hSiV2iU

## Transcript

All right, so today is May 19th and a few hours ago, this tweet just went up. It was Andre Carpathy announcing that he has joined Enthropic. And if you don't know who that is, this is one of the most important people in modern AI. He was founding team at OpenAI. He ran AI at Tesla for like 5 years. He went back

to OpenAI, left again, and then started an AI education company. And now he's anthropic. So normally the easy version of this video is, you know, big AI person joins big AI lab and that's the headline. But I think the more interesting question here is why Enthropic and why now? Because I'm

assuming all of these big AI labs have wanted a guy like Cararpathy to hop on board. Because if you look at what Carpath has been building and talking about over the last multiple months and when you look at what Cloud Code has actually been shipping already, it almost starts to feel like these two

things were kind of moving towards the same direction. So in this video, I want to show you the pattern that I think most people might miss when they sort of see this news, which is like the wrapper around the model, why your data and context are becoming the real product and where do I think Claude Code is

probably heading next. So let's get into it. So real quick, just so that we're all on the same page, Andre Capathy is like one of the goats for sure. He's taken a really weird tour around the modern AI world because founding member at OpenAI back in like 2015. Then he ran AI at Tesla, came back to OpenAI in

2023, left again a year later, and then started Eureka Labs, which was basically his AI education company. And that's where he built stuff like LLM 101N, which is like a free course that teaches you how to build a language model from scratch. Not something that I know how to do. And he's also the person who like

coined the term vibe coding, which is kind of what a lot of us are doing right now. You describe what you want in English and you let the AI write the code and then you kind of are just there vibing and steering it and editing and iterating with it. So he hasn't just been working in AI. He's been shaping

how people think about and understand AI for a long time and now he's going to be at Enthropic and that matters for a lot of reasons but the two that I wanted to talk about today. So first anthropic already has a ton of momentum with builders, right? like cloud code has become one of the main tools people

reach for when they want an agent or they want to code or you know do work like that even just general knowledge work and then about a week ago ramp put out their AI index which tracks like business spending across companies and for the first time in this data set anthropic has passed openai in business

adoption it was like 34.4% to 32.3%. Now, to be fair, this isn't the entire market. It's RAMP's customer base. And OpenAI still has a massive consumer brand and huge enterprise contracts that may not end up like on that sort of data or breakdown. So, I don't want to overstate it, but it's definitely a

momentum signal. It's hard to ignore. Enthropic has obviously been moving really, really fast, shipping new things really, really fast and getting a lot more adoption. That's clear. And part of that story seems to be cloud code. And there's another signal here that I think really does matter, which is earlier

this month, Enthropic also announced a new enterprise AI services company, kind of like a joint venture with Blackstone, Helman and Freiedman, and Goldman Sachs. And the whole point of that is to help midsize businesses actually bring Claude into their core operations. So, if you think about what that means and why

they're doing it, because they have all these impressive revenue figures from like a cloud code subscription standpoint, but they're basically saying way more than just, hey, here's a model. Good luck, go use it. They're building the model. They're also building the product surface. They're building their

partner network. And of course, now like a services layer that helps companies adopt their product. And that's a completely different game. And it points to the same thesis, which is the model is not the moat forever. The moat is the application and the adoption and the IP that doesn't live in the model, but it's

getting clawed embedded into the real workflows where businesses actually can make money, save time, reduce errors, scale without increasing headcount, and all that kind of stuff. Now, Carpathy's entire public philosophy right now lines up almost perfectly with what Anthropic seems to be building. And that's the

part that I think is really important to be paying attention to because the real story is not like AI famous goat joins Anthropic. The real story is the rapper and what is actually the product at Enthropic because most people still talk about AI like the model is the end all beall you know is GBT 5.5 better opus

4.7 Gemini all of these which one has the best benchmark what about the leaderboards and obviously the model matters I'm not saying it doesn't like it it matters but the longer that I use these tools and the longer that I see how good they're getting so quick the more I realize that the model is only

one small layer of the product. The thing that actually changes your day-to-day experience is the wrapper around the model because you see people getting crazy outputs and you see other people using the same model that are getting horrible outputs, right? Like there's obviously something going on

there. And when I say wrapper, I mean like the stuff that goes into how the model gets used. So cloud code is a rapper, codex is a wrapper, skills, sub aents, hooks, mcp connectors, your cloudmd, your memory, your docs, your examples, all that kind of stuff. That is the environment that the model lives

inside of and operates inside of. And this is where Karpathy has been extremely consistent. You know, he also kind of coined the term context engineering instead of prompt engineering, which basically means the real skill is not writing the perfect prompt. The real skill is building the

right environment and folder structure and um documents so that the model can actually work and be useful over and over again and remember things. So, if you think about it like this, you open up a brand new chat window and you ask Claude to help you with your business and it knows nothing about you. Like

these things are essentially stateless every single time you use them, meaning there's no context for memory. And it can still be useful, but it's usually guessing and you find yourself reexplaining stuff and that's where you get frustrated. But if Claude has your files and your examples and your

workflows and your style guides and the actual success criteria for what good looks like, now you're playing a completely different game. So same model, totally different outcome. And that's why I think that this hire matters. Anthropic has been building the rapper and Cararpathia has been teaching

people how to think about and understand and get the most out of the model with different methods for like wrapping it in something. And those two philosophies basically just merge into one company. And once you see it like that, you also see that the last few months of Karpathy's public work, they start to

look a lot less random. You know, they look like a road map of how to be using AI. So back in April, Karpathy dropped what he called the LLM wiki. And I made a full video breaking this down. It's doing really well. Like people were obsessed with this idea. It was going viral on X Carbathy's LLM wiki. So I'll

tag that right up there if you want to check it out. But the short version is basically very simple. It's that you create a raw folder with a bunch of markdown files and you have a wiki folder and the agent like synthesizes it. It builds connections and it gives you this like mindm of all of your

research or documents or whatever it is. And then you give it a schema document. So like kind of a cloud.MD or agents.MMD style file that tells the agent how the system works and how to look through it and how to um you know ingest more stuff into it. So instead of the AI just searching through a bunch of raw files

or even just doing like a vector database query, it actually builds like a living evolving knowledge base where it can read the sources and understand relations between different things. And you know people were building their second brains with this thing. And it's really important because when people say

like data is the moat, I think most people picture some giant enterprise database. But for actual users, for normal builders, your data moat might be much smaller and much more practical because it could just be like your meeting notes, your internal SOPs, your customer calls, your transcripts, things

like that. You know, your random internal naming conventions, the stuff that makes your frameworks and your work actually yours or your businesses. And if Claude can turn that into usable context that the model then gets to see and use, the model gets smarter and more useful to you specifically every single

week. And that's kind of like the lock in. Not because you can't switch models because you can, but because the longer that you get addicted to this operating system, the more context, workflows, and memory you build inside of it, the more you're going to want to use it, right? So the LM wiki is more than just a cool

side project. It is a clue about what Cloud Code might be doing. I wouldn't be surprised if eventually there's a much more native version of this sort of like LLM wiki structure within Claude code or Claude's like project memory. So you've got the agent that builds and maintains and inspects. You know, you're already

seeing stuff they're doing with like the autodream feature. So that obviously is very important and you don't have to wait for that. You know, you could build your own tiny version of this stuff this weekend by having Cloud Code look through all of your documents and your important files and building a wiki and

even using the LLM wiki style. So something worth checking out because if you really want to be like AI first and have your own agentic operating system, your data is only useful if the agent knows how to find it and use it in the right way. Now also back in March, Karpathy released a project he was

working on called auto research. And what that thing does basically is it sets up like an autonomous research loop. And we might have seen something similar with like the Ralph loop earlier, the Ralph Wigan plugin where it takes a training script, it proposes a change, it runs a short training job. So

it basically auto research, it experiments and then it checks it against typically an objective criteria, some sort of objective metric where we can say yes, it passed or no, it didn't. And the idea is that it continuously optimizes for however long it takes to hit that. So honestly, it's not a

feature that I use a ton because I'm not like building apps or I'm not training models. So I don't have a ton of need for like this auto research, auto experimenting for some sort of metric type of deal. But it is very cool to think about the ability for agents to be long running like that and work towards

a goal. And it's basically that loop of define the goal, let the agent work, and then you come back when hope it's done. And then very recently, we'd already seen Codeex have like a SLG goal. Now Hermes got a SL goal. Cloud Code has their own native SLG goal, which is essentially this idea of like the auto

research. And I'm assuming it's going to be something that all AI models natively adopt very soon. Now, I do want to be careful here because I'm not saying that Carpathy personally like invented this feature. I have no idea. And under the hood, auto research and/go goal are kind of different things, but the pattern is

clearly related. You know, both are trying to move us away from one prompt, one answer. They move us towards setting the outcome. We define sort of like the what. We don't exactly define the how, which is kind of like just vibe coding on steroids, and coming back to an output that's done. And that's just a

massive shift because once you have the context from the LLM wiki idea and you have the autonomous loops from stuff like auto research and goal, the whole thing stops feeling like just a chatbot. It starts feeling way more like an actual employee that knows the stuff about your business and can just work

for you until you have said goal. So now let's go back to the announcement tweet because there's one sentence in his actual tweet that I think we need to sort of double click on, which is the education sentence. He says, "I remain deeply passionate about education and that matters because Eureka Labs, his

last company was basically an education play. The whole point was helping people understand AI from inside out. So beyond just like, hey, click this button, connect the nodes here, do this, it was more so like how do these systems actually work." And Karpathy is one of the rare people who can take something

insanely technical like that and make it feel weirdly approachable and understandable. And that's the skill, you know, knowing the thing is one skill, but teaching it in a way where other people can understand it and use it is the real skill. And I think that that's a huge clue for enthropic because

if the next phase is about context and workflows and skills and, you know, memory and loops, then the bottleneck is not only technical, but it's also educational. you know, we're seeing that study that we just talked about on, you know, a previous video, the IBM study about adoption and change management and

how much of a gap there is between skills and actual usage of those skills. So, having one of the best educators in your org to help get all of these businesses to adopt and get stuck and get addicted on stuff, it's interesting to think about, right? Okay, so I want to make three predictions. And just to

be clear, like to be very clear, these are just predictions and just things that popped in my head when I read that tweet and thought about it a little bit. So I could very well be wrong. I don't know anthropics roadmap. You know, I don't have any insider info. But if you look at what Carpathy has been building

in public and you look at what Cloud Code has already been shipping and has shipped, I think the direction is getting clear. So this first prediction is that they are going to build their own app store for context and they're kind of already doing that, right? They have their official plugins and skills,

but I'm not meaning like just a prompt marketplace. I think the value of this is something deeper like skills and workflows and project memories and domain specific contexts and evaluation loops and connectors to real data. So examples that teach the model what good looks like in a specific job so that

people can take these little components and plug them into their own domains and own workflows and just instantly get more value out of that model even though the model itself is already really smart because like I said that model is becoming less of the differentiator for normal users. The real question is who

can surround the model with the right data and the right harness to I guess earlier I wasn't saying harness I was saying um wrapper to get that right like you know feedback loop to actually get results that drive real ROI for a business. So the LM wiki was a pattern for turning messy info into

usable memory/goal is a pattern for turning a goal into an autonomous loop and Karpathy's education work is a pattern for making hard AI concepts feel usable for the average person. that content is useful, but the deeper thing is that he's packaging behavior. And if Enthropic can turn that behavior and

that teaching style into a real ecosystem, then cloud code starts looking less like a coding tool and more like a marketplace. So prediction number two is that we're going to see way more of this /goal style um prompts and functionality. You know, I think that slash goal is probably one of just the

first versions of this, but it's not the final version. You know, I can imagine so many more commands that work in a similar way with maybe research loops or debug loops or things that are specialized for not just, hey, give it a goal and it will do that, but hey, give it a goal about X, Y, and Z very

specifically and it will do it better. It's more specialized. And again, I don't know the exact feature names. That's not the point. The point is that the interface changes. So you stop saying do this one step. You start saying keep going until this condition is true in this specific vertical. So

prediction number three, Enthropic ships an education layer for packaging your own workflows. This is the one that is a little bit more out on a limb, but honestly it's the one that I think is really interesting because if Enthropic wants a context marketplace, then they need to have regular people be able to

not only use it but contribute to it. So developers, researchers, but also people with specific subject matter expertise, specific domain knowledge from normal jobs. So, the accountant who knows the monthly close process, or the real estate person who knows every step about a property intake, maybe even the

YouTuber who knows good packaging versus bad packaging and how to brainstorm an idea and lay it out from beginning to end because all of that knowledge is really valuable. But right now, a lot of it's just trapped in people's heads or it's scattered across messy docs and um Slack threads or ClickUp channels or

whatever it is that they use on the day-to-day. So, I don't know what that's going to look like, but it's like how do you actually get subject matter expertise from someone in an area where you're not a subject matter expert, you know, like if I wanted to build, for example, an advertising agent, it would

be tough for me because I don't have that subject matter expertise. But if there was a marketplace that I could subscribe to and have like just all of this really good data and like, you know, you're seeing these people, these coaches create their own chat bots. They're creating their own AI avatars

and chat bots and charging people to talk to them because the people need to extract that data and apply it to their business. So anyways, this one might have been all over the place, but hopefully some of this made you guys think and maybe you agree with me on some points, maybe you disagree. Feel

free to let me know in the comments. I think it's just really interesting to be thinking about this kind of stuff and especially when you have this new news, it's like why? Like how did we get here? Because this isn't something where like yesterday they called up Carpathy and they said, "Hey, do you want to come

work for us?" And he goes, "Yeah." like this was probably in discussion for a long long time and I just I like to try to think about when it started and why and what they talked about. You know what I mean? So anyways, that is going to do it for this one, but hopefully you guys enjoyed or you learned something

new and if you did, please give it a like. It helps me out a ton. And as always, I appreciate you guys making it to the end of the video. I will see you guys all in the next one. If you guys
