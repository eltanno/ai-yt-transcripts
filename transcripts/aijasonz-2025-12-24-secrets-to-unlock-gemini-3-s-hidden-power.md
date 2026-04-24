# Secrets to unlock Gemini 3's hidden power...

- **Channel:** AI Jason
- **Date:** 2025-12-24
- **Duration:** 18:54
- **Views:** 74K views
- **URL:** https://www.youtube.com/watch?v=oL6bLQOXwAY

## Transcript

So let's face it, even though model Gemini 3 is great at design, there's still a difference between just a good looking website to something that feels like truly unique and stunning. And the key thing here is the animation and micro interactions. All those details makes your website looks just very

different from a template. And even though model default is not output this level of design and animations, they actually contain a lot of information knowledge about how to use certain libraries to output things like this. And all you need is the right process and prompt specs. And this is what I

want to showcase you today. How can you get your model to output stunning design and animation like this? But before I dive into this, animation is just part of work of designing a awesome website and landing page. There's so many other works that need to be done to go from an idea to an actual landing page that

convert really well, including things like research, the structure of the content, the messaging that actually resonate with people. That's why I want to share this awesome free resource from HubSpot. Their eight-step process for going from idea to a high-converting landing page, where each step comes with

detailed AI prompt for the right tool. This process help you break down into three different phases, from deep research about competitors, pull best practice to generating multiple variants of the copy and content structure, as well as visual guidelines, to eventually implement those things in the code. So

you're not asking model to build the entire landing page in one shot. You're progressively building the context. So the end result much better. But most importantly, they give you this collection of best practice prompt templates that already baking a lot industry knowledge and best practice

that they research from different companies. From how to get agent to very deep analysis that covering all different aspects to collect necessary information before you design the content structure, to the prompt that can turn the research results into a clear page structure, as well as

iterative process prompt that can optimize content and even do some AB testing. And in the end, it give you a structure to turn all those research into a PRD that you can send to a coding agent to finish off all the implementations. So you can actually ship, not just brainstorm. This is

extremely useful and practical. I'll put the free download link in the description below, so you can just copy and use. And thanks to HubSpot for sponsoring this video. Now let's get right to making awesome animations that going to really level up the landing page after you have the initial

structure, using GSAP. So there are two libraries that is very critical for you to achieve this level of animation interaction design. One is called GSAP, another is motion.dev. So most of you probably more familiar with motion.dev or Framer Motion, because it is the most popular animation libraries, which is

particularly great for UI animations. That is translate between different UI state, like those ones. It is also commonly used on all those micro interaction animations that you saw on website that's animating different UI component videos. We will get to that one. But on the other side,

there's one library called GSAP that is particularly great for more complex animation, especially scroll-driven animation, which means you can build very complex landing page where as user scroll, there are multiple elements mated together following a single timeline, which is extremely popular for

landing page and website. So as a rule of thumb, I often use GSAP for complex scroll-based interaction for landing page, while inside app mostly I would use motion.dev. And let's talk about GSAP first. So GSAP is library that you can use for all the cool scroll-driven animations. It allow you to

programmatically control the animation based on how much user scroll to proceed in the timeline of the animation, which means user can scroll in and scroll back and animation will just follow it. And that creates a much better interactive feeling, especially for things like landing page. And GSAP start with a

library that simply allow you to define a timeline of different animations. Like for each DOM element, you can say what a state it should transform to, what are durations and what are sequence. And they also give you a lot of useful tools like you can animate a paragraph of text word by word, line by line or even

character by character. And all those detail allow you to put together some pretty cool text animation as well. But the most important part is the scroll trigger. So scroll trigger is where you can define programmatically when user scroll into certain area, then trigger some animations. And this scroll trigger

have this thing called scrub. This is where the animation progress and timeline will directly tied to user scroll progress. And this is what creates all those amazing scroll animations and interactions. And there are a lot of things you can learn in GSAP to make a

super smooth animation, but you don't need to learn all this. But GSAP is not new thing. Model already have a lot of knowledge about how to use GSAP. But the challenging part with GSAP is is not really the implementation details, but how do you actually describe this animation? Even large language model

know how to use GSAP, it doesn't have a ton of really high quality example in its knowledge base about what a good animation and UI timeline look like. That's why the development process and context and unit here is pretty critical. Now one of the core thing here is creative work like animation

interaction is very difficult. You can't just give a generic prompt to the model like help me generate cool animation for X and expect it to work. Good animation like this requires a lot of thinking and planning of the whole timeline and how different elements should coordinate with each other in the timeline. And

some of task like even those SVG shape is not easy a task for model to do it in one shot. So you must go through a good planning phase, break it down into different small tasks and make the prompt to be very explicit so that the model just focus on the implementation of the animation rather than doing both

creative exploration as well as the implementation. Because otherwise model's default behavior will just revert back to something that's easier and common to implement. And this also what we mentioned as distributional convergence, because large language model predict tokens based on

statistical patterns in training data. And safe design choice that those works universally and offend no one just dominate web training data. However, with the right guidance, context and planning, you can actually utilize model to do some really creative work. Just a very quick example. So this very

mediocre interaction page is what I just got by prompting it help me create a super animated cool landing page with animated text and scroll interactions using GSAP. So model's default behavior literally just break down the text into different, you know, slide and sections with some sort of animation, which is

not that interesting, right? But once our prompt becomes more specific, it start creating something really interesting. Like here, I just give it more specific prompt where I actually break down the interaction animation I have in mind by saying create a horizontal scroll animation using GSAP

scroll trigger. And then I will talk about firstly the layout. Instead of using the full screen slides, which is default behavior we saw earlier, I want a continuous horizontal text flow. Imagine a single very long sentence. And use a single container so items flow naturally next to each other with

variable gaps. And I'll give content sentence and also some requirements that embed visual elements like SVG curves, icons in line with text acting like a punctuating or conjunctions rather than separating them into their own distinct sections. And again, this is just some prompt that I used to making sure the

whole thing should feel more fluid. And in the end, I just repeat again that it should feel like reading a long text rather than flipping through slide deck. And with this one, the interaction I got is just much much better and creative. You can see this whole thing just became a horizontal scroll text animation that

as user scroll, it will move from left to right with different text styles and some sort of animations. And we can actually animate it even further. I can start adding more effects. Like please add more animation to text using split text so things show up character by character nicely as user scroll using

ease. And here I'm using Super Design to build this because it's very easy for me to just generate multiple different versions, compare them and choose iterative one I like. But you can totally do that with Cloud Code Cursor as well. And here I actually have some special prompt about GSAP to making sure

it can handle certain interactions very well. Cuz even though model does has a good amount of GSAP knowledge, it will still make mistakes. Cool. So now we got this new version and let's try it. So if I scroll, you can see all those character is showing up one by one, which just add a bit more um

nicer animation feeling to it. So what we learned here is that model like Gemini 3 is actually capable to produce some really high quality animations using those modern libraries. But you just need to separate out the creative thinking and implementation into two different stage and give very specific

prompts. However, your challenge might be you might not have experience building animations and figure out how to explain the timeline. But this is where you can also utilize model to figure this out. On one hand, if you search for like GSAP or motion.dev examples, there a whole bunch of

examples that you can use as inspiration. And some of them even include the real code that you can paste to the model. But you can also get model to generate original creative work, too. And so you can use any AI to do the planning. Here I just want to showcase you how can you use like a Google AI

Studio Playground where you can have access to Gemini 3 Pro, customize the system instruction. So here we can give a special instruction like you are world-class GSAP motion designer developer. You think deeply about what's the epicenter of design and what are the one core interaction that can make user

wow and unforgettable. Try to tie back to the scroll scrub so the interaction feels live as user scroll. And think through all the animated elements timeline transformations one by one and making sure everything works cohesively. And try to design the animation that requires no 3D model, complex image

video assets and complex SVG. Something that can be achieved using just HTML, CSS and JS. And here I just need to mention those ones because otherwise model will just output something that so creative that the only way you can achieve that is using Nano Banana and video generation model to generate video

and embed it into your website. And if you're interested, I actually have a video covering how to use Nano Banana video generation model together with coding agent already, which you can basically build something like AirPods interaction. As you scroll, you have this kind of animated AirPod. And the

way you basically get those things work is that you generate video and break down the video into different frames with scroll trigger. And same as 3D model as well. You can build some absolutely stunning design using 3D model and 3js, but that does require you have a pretty good 3D model to be used.

And that does take some time. Like there are new models out there like Tripo 2 that will allow you to just upload image and generate a 3D model based on that. But the problem is that even the best model out there will just get some details incorrect. Like this one, it looks perfect. Like some part shape just

doesn't look 100% and things like text and texture are almost guaranteed to get it wrong. So, it's not quite there yet. It does take more work for you to do some editing and make it right. So, this is not the part I'm going to cover today. Same as SVG as well. Model today still can't do very complex SVG

extremely well. It is much better now and it can do some simple SVG very very well. But if it's very complicated, it still struggle and can take much more time for you to get to a version that you like. That's why I'm giving it those constraints here, but you can remove that if that's the kind of effect you

want. And then I can just prompt it. I'm making cool animation page for Coca-Cola with text this one which I just got randomly from web and help me design and planning the landing page interaction animation. And now it will generate this plan and the key thing here is that we want to

take a look to understand what it is proposing. Is this something that makes sense to you? And also something that can be achieved by code. So, here it saying it start with a massive red circle sitting center. As you scroll, the circle pops and explode into 50 smaller red bubbles. That's

interesting. And the bubbles begin to fall upward. This one looks fair and we can start experimenting it. By the way, we've been building this planning stage inside Super Design already. And we have some predefined prompts that going to make it better at

planning those animations. So, you can use But again, you can take this knowledge and work in any kind of AI agent. So, I'm going to copy this and pasting the prompt, click enter. So, now you can see this is a version generated. It start with this morph

effect that I think kind of simulate Coca-Cola bubbles and then the text start popping up nicely as I scroll. Okay, this part is a bit weird, but you can see the concepts are coming together and you can like keep prompting it to make it a few versions until it works well. And on the side another

version that it generated as well. So, initially it start with red background and with shape of Coca-Cola bottle, then text show up there and there also like some bubbles on the side as well. And then we get into this curved text which is really really nice. Um And in the end, you know, finish. So,

you can see that it's actually possible to get model to generate original interesting animations for your specific product and brand. It does require very careful curation scoping to making sure they actually can produce high quality animations. Here's another one that has some cool

hover effect for the text and then below that it give me this very cool scroll effect. And I can add more stuff to it as well. So, this is one example of how you can use GSAP to generate animations. Next, there's also this library called Motion Dev that probably is much more

popular and you can use that for stuff like UI state animations. So, motion.dev is basically Framer Motion. It became independent recently. If you were into animation, there's probably a good chance that you already use Framer Motion because it is the most popular animation library, much more

popular than others, which means model has a whole bunch more knowledge about Framer Motion. So, you have higher chance to get it right. And most importantly, it is designed for React type of project initially and is very good for UI animation. So, you can build very cool UI animation for different

components that you are building. And all those micro interaction just make your whole UI feels a lot more premium. And same as GSAP, model already has good knowledge. You just need to give the right prompt and right spec to making sure it pay attention to implement those interactions. For example, if I prompt

model to help me build a floating menu UI component, circle shape clicking on which will fan out a few options for me with smooth animation. And it will give me nice animated component like this. But it goes beyond just micro interactions of your UI component. Often on different cool landing page, you will

see those animated UI demonstrate product. And you can actually use Framer Motion to do something like this. I used same thing to generate this animation here for Super Design to prompt user to install the Chrome extension. And the way you do that is also pretty straightforward. So, here I can give a

prompt. We have this to-do app UI. Help me generate a self-playing loop animation for landing page showcase. And I'll give very detailed scenario. As I mentioned, the model itself is not that great to understand or think through the animation while implementing. So, I would say user should be able typing a

to-do and exit and also they should be able to complete a existing to-do. Which should disappear from the list. And the technical requirement here is the one that I think you need to mention a bit more. So, obviously I would say use Framer Motion and simulate mouse cursor so that you can actually get it

to simulate a real animation that there's mouse clicking or something. And the important bit is here. Like when I use mouse, sometimes they will get the position wrong. That's because I default to use hard-coded coordinates for the cursor movement. Instead, what you should use is that you should get it to

use use ref to get the bounding box of the actual UI elements and tie them back to XY coordinates. And in the end, making sure it is looping. So, I can send this one. Cool. So, on the right side, you can see this animation is generated. And as you can see that it animate everything, the cursor, click

interactions, and the mouse will just go complete the to-do app as well. And animation will loop. And you can imagine that you can just take this component, put on your landing page to actually showcase how your product actually works, which is very nice experience. If you're using Super Design, we already

have a lot of knowledge of Framer Motion baked in. But if you're not using Super Design, I also highly recommend you go add this MCP server from motion.dev as well. So, this MCP server come with two different tools. One tool is the documentation of the Framer Motion for AI. So, after you add that, it will just

give agent a whole bunch of documentation that it can read to making sure the animation generated is high quality and accurate. And it works with VS Code, Wing Serve, Cloud Code, basically any coding agent that support MCP server. All you need to do just add this MCP server by copying this part to

code.cloud.json, which open this gigantic JSON. You can just search for MCP servers, add to a project folder that you want to try out and save. Now, if I go to my Cloud Code and do MCP, you can see this Motion MCP has been added. And to visualize it better, if you see the UI on cursor, you

can see that it automatically add a whole bunch of resource into the model. But you don't have to worry because it's not adding 30 different tools to your agent. It basically just have two tools. One is listing all the resource docs. Another is read all the resource doc. Then agent can retrieve relevant

information. To test out, I can say help me edit App Store example using motion.dev on homepage. You can see that it firstly uses list MCP resource to list out all the documentations and then load two documentations about the layout animation and animate present. And it also has tool that can generate more

accurate CSS animation styling, which I don't know how much it helps, but it's there. This MCP tool. Then you can see the address page with a really nice and smooth animation for the cards. So, this is an example of how you can use Framer Motion to enhance your product's quality through micro animations. If you're

interested, we bake a lot of animation related knowledge on Super Design to making sure design agents really good at those popular animation libraries. So, if you want, I put the link in the description below for you to give it a try. And also include all the prompts and details about how I build those

agents in AI Builder Club as well, where we have a whole bunch of other top AI builders who are launching different AI products and may already experience problem that you are facing today. So, you can join AI Builder Club as well if you want to dive deeper into the building and development process. I hope

you enjoyed this video. Thank you and I'll see you next time.
