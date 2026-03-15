# n8n's New Chat Hub Release: What You Need to Know

- **Channel:** Nate Herk | AI Automation
- **Date:** 2025-12-15
- **Duration:** 10:05
- **Views:** 38K views
- **URL:** https://www.youtube.com/watch?v=jx-yvSRLKrA

## Transcript

Naden just dropped their new chat hub which lets you talk to all the different chat models that you already know and love in one spot and it also lets you talk to and trigger your Naden AI agents. So in today's video I'm going to be talking about what chat hub is and how you can start using it right away.

So here we are in my Nadn and we are in the new chat hub which as you can see kind of looks like a chatbt or a typical cloud interface where you've got past conversations on the left and you can start a new conversation right here in the middle. [music] If you're wondering how I got here in your typical end

environment, you can see there's a little chat bubble in the bottom left. And if you don't see this down here, then you probably just need to update your end instance. So, there's a few things that I wanted to break down once you are in this environment. So, right here, you can see that I'm talking to

Claude Haiku 4.5. So, I could just go ahead and say, "Tell me a joke." And what it's going to do is it's going to use that chat model in order to actually say something to us. And the way that I was able to connect to Claude was up here. I just basically put in my anthropic API key. And if you already

have that credential configured in your end, then it will already be there. But what's cool is now that we're already mid-con conversation, I could go ahead and switch the model if I wanted to. So, as you can see, I just switched over to GPT5 Mini and I can say, "Super funny, tell me another one." And now it has

switched over the model to an OpenAI model. And of course, you could also go ahead and connect to Open Router, which has basically all these other models already inside. So, I just switched to Google Gemini 2.5 Pro from Open Router. And now you can see that it's switched the model successfully down here. But

what I wanted to show you guys was the memory of basically this context window. So as you can see, even though we've switched models every time, whatever model you're currently talking to is going to be able to read the conversation that you've already been having in this thread. And that's why

it's stored over here as a tell me a joke thread. So there's a couple other things you can do here. You can see under each of these little elements, we have the ability to copy. We have the ability to read aloud. And then for some reason, we can also edit the AI's response. Not sure exactly what the use

case is there, but if I wanted to change what the AI said, I could. And then we also could just regenerate a new response if we didn't like it. So, when you speak the AI's response out loud, it actually just speaks it. I'll show that real quick. >> Of course, so far in our conversation,

I've told you these two jokes. >> Okay, so it doesn't really sound great. It's not like a 11 Labs or a really nice voice model, but it will read it aloud. So, I'm sure you guys are also wondering at the bottom, you can see that there is a tool section. And right now our only tool is Gina AAI, but that lets you

basically access the web, access URLs, and do web search. So here is what Gina.ai looks like. And then all I did was I went up to the top right and I made an account. And when I did that, it gave me this free API key that gives me a million tokens to play around with before I have to top up. So I took that

API key, I came into Nitn, and I basically just created a new GINA credential and pasted my API key right in there. Now, if I wanted to open up a new workflow and actually use the tool, I could connect to my Gina credential. And now I could do real web search. And now that I have the web search tool

enabled, I could go ahead and ask, "What is the Chicago Bears current record?" And it has to actually go search the web in order to pull that live information back. So, we have that first little line that basically indicates that it was able to call a tool and work. And now the model is responding to us. So, as

you can see, as of December 11th, 2025, which is today, the Bears are 9 and4. But what happened is I asked it to summarize this article and I gave it a URL and it was unable to do so. And that's because we didn't enable the tool that lets Gina read URL content. But now that I've enabled the tool that actually

allows us to read URLs, now it can look at that for me. All right. So that's basically the same thing that you guys are already used to with your typical large language models like Gemini, Claude, CHBT, whatever it is. But now you can also see that we have the ability to talk to our custom agents.

And you can see I have one right here called get agent logs tool. I could also come down here and click on custom agents and we can see all of the edit and workflows that we've actually configured. Now you could also basically create a custom GPT or project in here too. It doesn't have to be an edit and

workflow cuz I could click on new agent. I would name it and give it a system prompt. Choose a model and then I could allow the same GINA tools in here as well. So basically a custom GBT but of course like I said you can connect and workflows. And if I clicked into this one you can see that it is in fact an

NIN AI agent that I've got. So I'm going to show you guys how we can talk to it and what it can do. So in this particular example, we've got an AI agent that I'm calling a data analyst and it's basically able to search through our own end data table which has workflow executions. So this is

obviously mock data, but you can see we've got a date, we've got a workflow name, we have the input, the tools called, the tokens used, and then the final output. So basically, let's just say you have all of these workflow executions running. Now you have this easy chat interface in nitn where you

can talk to it and basically get some insights and analysis from those execution logs. So I just shot off how many times did the customer support workflow run in October. And so this agent over here basically just got that message. It's going to use its tools and maybe its calculator to look up the

information and then it's going to respond to us in the actual chat interface right over here. So anyways, you can see it did a few tool calls here. That's why we're getting these different lines. But then what happened is it gives us a concise answer which is that the customer support workflow ran

four times in October and then I told it to give us a detailed breakdown so we could actually validate that it is correct and it's not hallucinating. So if I switch over to the data set we should be able to see that in October which is all of these runs right here the customer support workflow got called

four times which as you can see it did execute four times in October. So now I'm asking how many total tokens did we spend with our code reviewer agent? And it should be smart enough to understand we're talking about the code review assistant workflow. And what it's going to do is it's going to find all of those

actual executions and then total up all the tokens and it's going to explain to us how it actually got there. So here we go. The code review assistant used a total of 10,260 tokens across all retrieved log entries. Then once again it gives us a detailed breakdown and it basically just had to sum up all of

those executions. 890 plus 3,400 plus 120 plus 1450 and that's how we got to 10 to 60. And as you can see in the data set, I summed up all of these rows myself and we did get 10,260. So it did its job right. But now what I want to do is real quick just show you that it actually did call this workflow. So this

is the agent that we were just talking to. If I go to executions, you can see that the two most recent runs, the first one that we asked was about the customer support flow. So how many times did the customer support flow run in October? And then it got us the answer that we saw in that chat interface. And the

second one was how many total tokens did we use on the code reviewer agent as you can see right here. So the question now is how do you actually go make an edit in workflow and then let yourself talk to it through this interface? Because when you click on custom agents, this is what you see. So I'm going to go back to

my workflows and open up a new one. And basically all you have to do is have a workflow that you talk to or that's triggered by the chat trigger. So, if I open up an AI agent right here, and I basically just by default get the connected chat trigger node, I'm going to add a chat model real quick. So,

we'll just go with the basic 4.1 mini from open router. And all I'm going to do in here is I'm just going to add a system message that says, "You are super mean and rude and sarcastic." And so, that's how we'll basically be able to validate that it is in fact talking to this workflow. Now, what it did is I

saved this, but what you'll notice is if I go back into the chat, we don't see anything here. Even if I refresh, we don't see that workflow. So, there's a couple things that you do have to do. So, the first one is that you have to go into the chat trigger and you have to make it available in edit and chat. As

you can see, it says whether to make the agent available in an end chat. And this is where you can give it a name and a description. And so, the other thing that you have to do before it can show up is you have to publish your workflow. So, I'm going to go up and hit publish. I'll just call this version one. And now

that it's actually a live published workflow, we should be able to go back to the chat. And if I just give this a quick refresh, we should see that mean workflow now. And I can go ahead and chat with it. So I'll click into this and I'll just say, hey, I am feeling sad. And now this should be running

through that main agent. Oh, Boohoo. Welcome to the club sunshine. Everyone feels sad sometimes. Want a medal or just some cheesy sympathy? Get over it. So that was pretty rude. But if I open up the workflow and I go to executions, we will of course see that that is the chat that just triggered this end

workflow. So hopefully you're starting to get some ideas of different workflows that you have in NADN. That would be really nice if you could just kind of use them right in here, especially if you're able to switch between all of these different chat models in the other threads. Now, one thing that I really,

really hope is coming to this soon is being able to call NIDEN's instance level MCP right here. If you haven't watched my video about that, I'll go ahead and tag it right up here. But in that video, I showed how I could use it in my own chatbt or claude. As you can see here, I have these tools right here

that let us search workflows, get workflow details, and execute those workflows. So, I can always stay in my cloud environment if I'm working on a project and just say, "Hey, use nitn to go do that or go do this in nit." And that would be really cool if we could have that plugged in here so that while

we were having these messages with whatever chat models we wanted in nit, we could say, "Oh, okay. I have an agent for that or I have a workflow that does that. Just go find it and go execute it for me." And so I imagine it will be super easy and by the time you're watching this video, it may already be

here because all you have to do is essentially give the client this server URL. And so we could easily just plug that in here. Or because this is an NEN product within your own, you know, environment, it should be able to just see everything either way and execute them. But anyways, that's going to do it

for today. I know it was a super quick one, but I wanted to update you guys about this new ChatHub feature. and I'd love to see some of the use cases that you guys are thinking about of actually plugging in your workflows right into this environment in NADN. If you're looking to learn more about AI

automation and NIDN, then definitely check out my plus community. The link for that's down in the description. We've got a great community of members who are building with NIDN and building businesses every day with NIDN. And we celebrate some awesome wins in here as you can see. So, just a great place to

be surrounded by like-minded individuals. But anyways, I would love to see you guys in the live calls in here. I'd love to see you in the community. But that's going to do it for today. So, if you enjoyed the video or you learned something new, please give it a like. It definitely helps me out a

ton. And as always, I appreciate you guys making it to the end of the video. I'll see you on the next one.
