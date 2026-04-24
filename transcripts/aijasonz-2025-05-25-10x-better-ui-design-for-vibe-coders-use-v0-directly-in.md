# 10x better UI design for vibe coders - Use v0 directly in Cursor

- **Channel:** AI Jason
- **Date:** 2025-05-25
- **Duration:** 3:35
- **Views:** 53K views
- **URL:** https://www.youtube.com/watch?v=0KYWJWY62d4

## Transcript

How can you dramatically improve cursor generate UI from something like this to something like that? So v 0ero which is application you probably have been using to generate really high quality UI for web application now just released their own AI model that you can use directly inside your cursor. They also introduced

some new AI coding workflow that can make the UI generation much better. Here is my workflow and setup. So to use V0ero in your cursor, you actually need some setup because cursor unfortunately don't support VZ model natively yet. And to set up, you will need to go to models in your cursor settings. For the open AI

base URL, put in api.vzero.dev/v1. Save it and then go to your v 0ero chat. Go to settings, generate API key here, and paste over into cursor and click verify. You'll probably be prompt to confirm to enable open API key here. So from now on, every time when you choose a GPD based model,

behind the scenes, it actually calling v0ero model. There's also a bug you will have that even though you're calling cloud model but if you have this open AI API key turned on it will have this arrow. So making sure you turn off when you try to use cloud model and turn it on when you want to use the vzero model.

So as a quick way to showcase the capability if I just use a 3.7 model and give a prom make a beautiful calendar app the result you will get probably look something like this fully functional calendar app but the UI of spacing font color just doesn't look 100%. So instead we can switch model to

GPD 4 and making sure we turn on this open AI API key here and give the same problem make beautiful calendar event app but with one caveat I will just ask you to build one page to start with cuz even though vzero model is extremely good at UI generation it is not as good in terms of scaffolding the whole

application and complex functionalities. When I ask you to build a whole application it often just fail and stuck in the loop. So I would just ask to build one page to start with and then switch to different model. So this is the result you get one shot from the Vzero model in cursor. You can see the

UI outcome just looks ton better. All the spacing font color looks right with better taste. What's really cool about it is that you actually don't need to use Vzero model through the whole DM process. You can just use that to set a foundation of how the application should look like and then we can switch to a

better model like cloud 3.7 or cloud 4 if you want to keep adding new feature on top of this page. And you might have this arrow just making sure to turn off the open API key here and try again. What you will find is that even though you switch to different model because VZ already set a example of what type of

style, spacing, color it should follow, the new UI generator will follow the same style and build out all those other screens that also looks really good. So this is my current workflow. I will try to use Vzero to initially set up some main screens and then use cloud 3.7 or cloud 4 to build out more functionality.

But if I need to set up some new screen again or switch back to Vzero to build out that new screen. This is probably one of the key benefits I see of Vzero releasing their own model instead of just using their chat app because now you can just switch back and forth between different model for specific

tasks. So this is a quick example of how to use the Vzero new model. If you want to learn more in depths about AI coding, you can join AI builder club where I have more advanced tips about AI coding and building production ready large learning mode application for myself as well as industry experts. And we also

have tools that can bootstrap your building experience from SAS and MCP template as well as tools like 10X coder that can turn your vague idea into wellcraftraft person prd and rules. But most importantly, we have the community of top AI builders who are building and launching their own AI products. So you

can come build with them and get advice. If you're interested, I put a link in the description below to join. Thank you and I see you next
