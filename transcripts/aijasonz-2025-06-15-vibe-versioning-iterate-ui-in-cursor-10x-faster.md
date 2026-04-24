# Vibe Versioning - Iterate UI in Cursor 10x faster

- **Channel:** AI Jason
- **Date:** 2025-06-15
- **Duration:** 5:55
- **Views:** 23K views
- **URL:** https://www.youtube.com/watch?v=JfMcFjD-tIA

## Transcript

I want to show you how can you iterate UI implementation in cursor very easily and effective as we get new model like cloud 4 models coding capability for UI is become much better but once I really miss implementing UI in cursor compared with platform like v0ero is the versioning it will lock all the

different versions as it goes so I can jump in between different versions compare the difference and forks from the ones I prefer more and the nature of design is that we often will iterate multiple different versions of the same screen until we find a version that we really like. I just found this open

source plugin recently called Yoyo that allow you to do this version control directly in the AI ID like cursor wins serve and cloud code and this speed ups the UI iterations much faster and it's also very good for code maintenance as well because quite often when you prompt cursor to do something it might just go

off rail and break a lot of stuff. So you almost want some sort of quick snappy save that you can easily go back something more lightweight than git. And here is my UI iteration workflow with yoyo. So I can just click a button to install extension. Normally I firstly go to different platform to find design

inspirations. Their platform like dribble where you can just go and find some good UI reference as well as mobile where they provide you real mockups of applications or specific UI elements. Let's say I found a UI that I quite like. I can just take screenshot here and paste into cursor give from UI

senior front end engineer designer we want to build a digital web application UI just like attached moch please first break down and analyze design system style font and components and let's firstly build a UI mo with mock data on the first page so it will try to analyze the design style font and colors okay

now it has first version built in and we can copy this URL and do command shift P uh search for simple browser and paste in the URL. This will allow you to just preview the UI here directly in cursor which is very helpful. So this is the first version of the UI. As you can see it's kind of 80% and got essence of UI

but it's not like 100%. And I also want to like experiment with a few different versions of styles. And this is where this version control is really useful for iterating UI. So I can create a new version by clicking on this button. This will create a snapshot of the codebase at this specific point. Uh and I can

give it like initial UI. Then I can start iterating the UI. Let's say I want to iterate the component cards at top. The cards at top should look like a moch here. But currently it is not even aligned and the color is wrong. For the event card, I can copy paste and give a prompt for task car. Please polish your

UI to look exactly same as the screenshot. So we did some finetuning and polish of the UI. I can click on save new version here to save a newer version of the UI and this how version going to help on the UI iteration. I can click on the V1 again and refresh the simple browser. This allow me to see

what the original version was and I can click back to the V2 and take a look at the latest version. So you can like go back and forth between those different iterations very easily and see which one is your favorite. And I can make a few more changes now. Help me make a light mode version, not dark mode version. So

I got the light version here. And I can still again save the version. And I can also add some custom nodes here. So this will be the light version. Previously will be polished dark version. I can switch different type of UI quite easily to see which one do I like. And I can even make some more dramatic change. For

example, Apple introduced this kind of liquid glass type of style recently. I can just go find some liquid glass implementation on GitHub and here we got a one. So I can go to the CSS here and just copy the whole style here and give a prompt. Please help me update the whole UI with Apple's new liquid glass

style. Below is some reference which is CSS I just paste in. Now we get this type of new liquid glass type of style application. Obviously, you can keep fine-tuning the UI to make it looks better. And again, I can save the version and you can see some description be automatically added about liquid

glass. And what's really cool about this new version control is that it manually kept a lot of different versions. You can actually chat to extension to understand what does each version contains and find a specific branch that made certain change. Like here, I can just give a prompt which version was

initial light mode. it will automatically return me the right version as well as some description about what exactly we did in that specific version. And this I think is just touching what the new git or versioning experience could be in the era of AI coding. There's also a very

interesting interview between YC and the founder of wingsf where they talk about how git might be different. Have you thought at all about whether doing git commit all the time is the right move or whether there needs to be like a deeper infrastructure change? Yeah, I think we have. So, you know, one of the things

that we always think of is in the future you're going to have many many agents running in parallel on your codebase. That has some some trade-offs, right? If you have two agents that kind of modify the same piece of code at the same time, it's hard to actually know what's going That's another thing is that like it's

hard to have multiple branches checked out at the same time with different agents working on them independently. All the merge conflicts. Oh god, there's a lot of If you're interested in this topic, I definitely recommend you go check out and imagine what the future might look like. Meanwhile, if you want

to learn about AI coding beyond basics, I'm building this platform called AI builder club where I will share the latest workflow tips and learnings about AI coding and building production ready agents both myself and other industry experts as well as tools that can help you get start with your AI software much

faster like SAS launch kit and MCP boy play. If you're interested, you can click on the link in the description below to join. I hope you enjoy this video. Thank you and I see you next
