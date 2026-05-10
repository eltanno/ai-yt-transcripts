# I used /goals command wrong... Here are all tips & mistakes

- **Channel:** AI Jason
- **Date:** 2026-05-09
- **Duration:** 12:17
- **Views:** 6K views
- **URL:** https://www.youtube.com/watch?v=rIs802-bXDY

## Transcript

So, OpenAI released this goal feature in codeex which allows agent to continuously working for hours and hours on bigger and complex projects and we already saw people getting pretty phenomenal results like one prompt to generate fully functional game to building and testing an iOS app by

itself for 6 hours and key developers from codeex team also mentioned this is probably the most consequential thing they have shipped in codeex this year and very quickly Hermas agent also released this persist ghost feature which is similar type of feature that allow you to set a standing goal for

Herm's agent to walk across turns until it is achieved. So how exactly does this go feature works and what are the best practice of actually using this. So what is the problem this goal feature actually try to solve? So even though modto has getting significantly better where it can consistently finish well

scope tickets but as we let it take over more and more complex projects you probably experience yourself that the model can sometimes get lazy and declare the victory too early. For example, you might ask agent to just fix all the failing test in your ripple and most likely agent will do some work maybe for

10 or 15 minutes and then come back saying it fix all the issues which most likely is not exhaustive. You need to prompting the agent say hey there's still XY not done and you need to keep doing this for some complex tasks and there were a very popular project earlier this year called rough loop

which is basically running your coding agent in for loop where every time when agent finish it will write the output of it work in the file system and programmatically trigger the coding agent again and very quickly it was implement in cloud code three plug-in as well but fundamentally rough loop is a

pretty simple or kind of dump programmatic loop you're just running the cloud through specific say prompt in while loop and define the max amount iterations. And this go feature in codeex and hermas is an iteration of this rough loop where it is no longer doing a simple dump programmatic loop.

Instead, it use large lang model to decide and judge where the task has been satisfied. So when user send out a goal command, it will trigger the agent to do things and once finished there will be one large language model call to decide whether the goal has been satisfied. If yes, then finish the session. But if no,

it will trigger the agent again with some prompts. And this means instead agent prematurely claims the task has been done, it will have this larger mode call identify and capture the scenario and guide agent to continuously working until the goal actually satisfied. Meanwhile, it also made it good to

handle ambiguous tasks. So instead of a list of tasks that has well scoped out, it can handle things like just cut a docker image size by 60% where you probably at beginning don't know exactly how to do this, we can get agent to start exploring trying out multiple different methods and approach and step

by step adding the improvements. This is somewhat similar to the other very popular project earlier this year from Andrew Copsy like auto research where fundamentally it's also a for loop that getting agent continuously working and save the state result. So this go feature is really good for those type of

complex longunning coding work like code migration larger refactories as well as ambiguous goals like experiments where agent can keep making scoped progress. So compared with original rough loop the stop condition instead of being a programmatic menu limitations it will be using large model to judge and decide

where the goal is finished and when new loop start instead of feeding the identical prompt. MD into the agent loop. This go feature has this continuous prompt about go context as well as a state and the way it works as we mentioned before is this loop that is running and once finished it will send

to this large model call with a prompt here that define the definition of done the output format as well as a goal and response and this large model call can output status as well as reasoning. And if you judge the goal is not finished then a message will be sent back to the agent. You will see a status like this.

But in reality, the agent receive a message like continuing toward your standing goal that list out the goal file and a special prompt to continuously walking towards this to goal. Take the next concrete steps. If you believe the goal is completed, state so explicitly and stop. And the codeex

continuous prompt is a little bit more sophisticated where it has things like do not accept proxy signal as completion by themsel. It only marks a goal achieved when the audit shows the objective has actually been achieved. No required work remain then uses update goal with the status complete. So codex

go feature actually ask agent to mark the goal as complete by itself whereas her agent will have special larger mode called judge the result and to activate this go feature in codeex. You can do codeax features list. This will list out all the experimental feature that codex has and you will say go feature here.

Each one labeled as stable or under development and whether it has been toggled on or not. And then you can just do codeex features enable ghost. You should see a success message here. Now if you run codeex and do /go you should see this go command and then just type out the go here. Help me migrate my

codebase from javascript to typescript and making sure all screen stay exactly the same visually using playright interactive to verify the output. And once you sent it will receive this go active message and then the agent will start working. And while it is working, you can always just run this go command

again to check the status of the go in term of how long it has been running, total amount of token has been used. You can also run go pause or go clear to stop the work anytime. Meanwhile, if you want to let's say ask it some questions or branch out a conversation while it is working, you can also run this side

command which will basically fork the conversation from this point. With this, I've been using codecs to run some migration work for 9 hours overnight and it is still going. But there are some rules you should put in place to making sure the goal actually apply. So the common prompt will look something like

this like complete a certain objective without stopping until verifiable end state. So a good goal prompt should be bigger than one prompt but smaller than open-ended backlog. It should define what codec should achieve, what it should not change, how it should validate progress and when it should

stop. And the most important part is that codeex should know what done means before it starts. For example, if you ask it to do a migration task, the goal should look like migrate this project from lack stack to a new stack and making sure all screens stay exactly same visually and using playright

interactive to verify the output. So you can make scope progress step by step. And if it's a prototype, then you should probably point it to a plan MD file or PRD file. creating tests for each milestone and verify the output with playride interactive. Even include reference screens as needed so you can

verify whether the game UI looks exactly same as design and if you have evaluation set you can even run it like a auto research loop. Give a go optimize the prompts in the prompt file until the evalu reach a target score and after each change run the evolve command inspect the failing cases and keep the

prompt at its minimum and targeted stop when the target is met. So what you see here is that you have to define very explicitly what does done and finish means. So the agent will know when to stop because without defining that what you see is that Adrian will again just get lazy and decide okay this task has

been done and finish out very quickly. And there's some similar learnings from Vincent who is one of the maintainer for open claw. He has been running go for three days on open claw across 30 rounds gazillion tokens and many many PRs. One of the learning he had is that you should spend time to align with agent

early on. Most time if you just simply paste in a prompt and ask it to do it is likely give you garbage. So instead he will have a conversation with the agent about all the context like what is his project is what are the things he care about what bad looks like for user what he already tried and lured out and kind

of bugs he keep missing and ask the model to ask anything before he start. So an initial interview alignment conversation is very critical here. Meanwhile it will also try to quantify down as we mentioned before. So you should not prompt it to something like keep going until everything is fixed.

Once the definition of done is fuzzy like this then model will either quit too early or spiral into nonsense. You have to give it some quantifiable number. And here is one example QA prompt that he has been using. It will define the path and has very clear stop conditions which is once it found 20

discrete new issues and for each issue produce repro proposed fix push fix to a branch as you go and log the result to run folder or this prompt he has been using for new projects like we are building x reference implementation to different ripples and also point out to a list of files including anti patterns

logs and design pattern you wanted to follow as well as what my user will expect. So here you can see that even for new project it's very important to list out the expected criteria and behavior rather than a loose goal that optimize or improve our app UX. So having a good goal prompt is quite

critical to decide whether you get good results or not. And there's a one open source project called go body which is basic skew that help you construct a good prompt. The way it works is that you can run npx go body and then run codeex. If you do dollar sign it will list out all SKs and plugin and you can

type in go prep. This will load up a workflow to trigger codec star interview with you and construct a good prompt folders. So even though I give a pretty vague like build a raen type game using image gen for image assets and beautiful graphics verify it on desktop and then go body will start creating some files.

One is this god file. This will turn your go into a well-written md file that clearly describe the requests the constraints the stop rules and detail loop. It also has this state.ymo YAML file that's listing all the tasks based on the code. So instead of running a go plus your prompt, you can do /go and

point to this go. MD file and then codeex will start working on the task update state.mmo file to keep record and reference to go.md file on every single loop. With this in just one single prompt agent is able to generate image assets for the game and stage together a fully functional game. So this is codeex

and herms agent's goal feature. It is really good for those complex coding work that will require not just minutes but hours to complete and we'll adjust some models default behavior where they will stop things prematurely. However, this feature still has limitations based on our testing. For example, it's mainly

designed for longer coding sessions that runs for hours. But if there are things that you wanted to do for weeks or months like improve your SEO or go strategy, optimize return on ad spending, it didn't quite work. especially the scenario that don't have immediate verifiable results or

feedback. And my team has been experimenting with this concept called mission. The way this mission works is actually quite straightforward. It will basically capture those long runninging goals or missions into a mission.md that clearly define the metrics to optimize. It will trigger agent run where agent

will try to form a hypothesis about a few strategy it should try to complete the mission. do one step and output this work as artifacts and at the end of that instead of just keep running a for loop it will schedule next run could be in hours or days or even weeks depend on situation and every time when next run

is triggered the new session will receive the mission MD as well as the previous step summary so you can always iterate and improve and learn from previous steps and for this type of really long runninging missions we also found it's quite useful to have those human in the loop experience if agent

realize want to try something really dramatic IC or realize a goal or mission is unclear or not verifiable. It can send message to human and change mission status. We've been reexperimenting with long run mission like grow trader follower to 10,000 let agent to iteratively take actions run experiments

and at each step it can output artifacts like a certain type of post as well as specific analysis report and based on that form certain hypothesis and schedule next action. It already delivered some quite interesting results like for K's own Twitter account initially made the first tweets like

this which got kind of average performance but then based on the observation it decided next tweets we should probably do a strat and use kind of founder voice and next one immediate got pretty good performance and based on that observation it decided to double down on this type of content and post

the next one which is not explosive but already the performance is much higher than the original baseline and we found same type of setup can be used for like optimizing ads campaign go and even product growth. We currently open closed beta. So if you're interested, you can join early access program. I have put

the link in the description below for you to join. I hope you enjoy this video. Thank you and I see you next
