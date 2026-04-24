# WebMCP - Why is awesome & How to use it

- **Channel:** AI Jason
- **Date:** 2026-02-15
- **Duration:** 11:23
- **Views:** 58K views
- **URL:** https://www.youtube.com/watch?v=xQAYZBDV5jg

## Transcript

So Google released this web MCP concept for Chrome and is really interesting and I want to quickly explain what it actually is and why it is cool and also how you can start playing with it today. So at its core web MCP is trying to solve this one problem which is allowing agent to have deterministic behavior on

every single website. So let's take example if you are a owner of e-commerce website and you have this one goal that you want any agent to use your e-commerce websites. Assume in the future there were millions of different agents operating the web taking actual actions for human and to achieve that

today without web MCP you have two options. One is that you will build your own MCP server and hoping the agent is equipped with this MCP which likely is not going to happen because your website is not going to be the same every agent use every day and loading up the MCP in the agent all the time didn't make

sense. So this approach generally doesn't work for normal websites and the other option is that you relying on agent to have really good browser use capabilities and more and more agent already equipped with those capabilities like a manace where you can open a browser and do certain tasks. But the

problem with those browser use capability is that it's generally nondeterministic. All those browser use agent is extracting the row HTML which is gigantic doing some clean up and feeding to large model and sometimes they will take a screenshots with some annotated mark of the UI elements on the

screen. Basically try to do this translation layer to look at the HTML or screenshot to interpret what kind of core actions that agent need to make. And as we know most websites not well built and it's designed for human to consume rather than for agents. So there just huge amount of noise that is going

to be sent to large model that leads to nondeterministic behavior and that means agent will likely fail on using your website to complete tasks and in the era where AI agent will be the main consumer of a lot of web content or actions. If your website is easier for agent to complete tasks that means agent will do

it more and more people were likely to adopt it. And that's why this web MCP concept is quite interesting. So the way it works is that you still build MCP but you declare it in your code or HTML. So the agent who is operating the browser they don't need to do translation layer by themsel instead they just look at the

actions and MCP2 you register for each page like in your e-commerce example for the homepage you might register actions like search products get categories and filters and for the product detail page there could be actions like adding things to shopping cart or get similar products and agent can execute those

actions just like calling a normal MCP tools but this MCP tools will be loaded up the moment they land on a certain page. So you still get benefit of really deterministic actions the agent can take. And to demonstrate that let me just quickly explain how it actually works. So web MCP expose two ways you

can set things up. One is declarative which means you can add certain HTML attributes. Let's just take example. So this is example demo from Chrome team where you have this basic reservation page from just simple HTML. And in this HTML for elements like form you can start adding attributes like tool name

and tool description. And for each input that agent is able to customize you can also add this two param description. Once you set up those attributes with the latest Chrome version when agent visits page they will be exposed to this book table tool with description and input schema that automatically

transformed from the attributes you added. So that any agent that is supporting web MCP format will automatically equipped with this MCP tool that they can call. And if I send this request, the agent will automatically fill in the content to the form. And after agent call MCP tool, you

can also see some special UI elements popping up on the website as well like this. Please review and confirm floating tool tips and this also part of web MCP upgrades. So it has those special CSS class that I support that will be triggered when agent fill in certain form elements or before it's about to

submit this form. So this is how easy it is for you to make your static website agent ready. But the more likely approach you're going to take if you're building actual application is this imperative mode that allow you to register tools from JS or bind certain MCP tools when certain react component

is rendered. So basically the new version of Chrome browser support this navigator.register register tool and navigator.register tool to load up MCP and this is another example from Chrome's own demo. So if you have this react app for booking flight tickets when user is on this

search page there could be a exposed MCP tool for search flights and if I send a request here agent will be able to fill in the form and take action which redirect me to the search result page. And what's really cool is that on here you can see the expose MCP tool changed as I navigate to a different page. In

this search result page it has relevant tools like set filter, search flights, reset filter and list flights. And this is like the coolest part I've seen after using web MCP. Like each web page, it just has this special list of exposed MCP tool that will be loaded up contextually. You basically use this new

navigator.register and unregister to function and the rest is just same as how you build MCP tool where you would define two schema for the name, description, input schema, output schema and functions. Then for each component you can start register and unregister tools. So whenever the

relevant UI components show up, the MCP tools will also load it up accordingly. This is how web MCP tool works and the two ways you can set things up. I will talk you through a bit in details as well developer tools that you can use to quickly set things up. But before I move on, the most interesting part I see is

this web MCP concept. It just introduced this contextual MCP methods that I thought is awesome because when we look at how things evolved, initially we have this MCP concept which is great. It allow agent to extend his capability and also when agent run the tool it is guaranteed to pass a right schema to

evoke the tool. But the problem is that it just takes so much context no matter whether it's relevant or not. So it's not a good solution for those long tail scenario and then recently whole bunch of people moving toward this skill concept and the benefit of skill concept is that it didn't take too much token.

It only load up the title and description in the context window. The actual information about how to use this tool or how to use the skills is a contextual load up when it's needed. So it's much more friendly for extending agent capability for this longtail use cases. But the problem is that it

doesn't have those kind of strict schema guarantee because agent literally just receive a text prompt. Um but this web MCP tool just creates such an interesting pattern where depends on the context which in our case the web page agent is on different MCP tools will be loaded up and I definitely think this is

the future ideally we should always strive for those kind of contextual MCP setup depends the task that agent is doing relevant MCP tool will be loaded up I'm very keen to see what kind of new setup will evolve based on that but without going too far away from the web MCP itself I'm going to show you how you

can do that yourself so this web MC MCP require you have latest version of Chrome and to access that you will need to install this Chrome beta version and after you install you can go to Chrome flags and search for web MCP and you need to enable this web MCP flag and after that you should also install this

Chrome extension called model context tool inspector which you can download directly from Chrome extension that will be equipped with this web MCP tools portal and regarding a detailed implementation of web MCP in your application there are detailed step-by-step tutorial I have put into AI

at build a club so you can just follow along practice step by step and we also have a whole bunch of other tips that we share about agent skills and cloud code hooks as well as weekly workshop where we will dive into this latest techniques further but here's a quick version of how you can set up two ways of MCP

firstly let's try out the declarative methods let's say I have this contact us page that is static and if I open the webmc tool currently there's no tools register for this web page and I'm going to show you how we can make this form agent ready using webmc so this page is just one single HTML looks like this.

And the first thing we want to do is add this two name and two description attributes to this form element that will allow web MCP automatically pick up this S2. Then we add two parame description for every single input that agent need to fill in. Like for this in add two parame description of the name,

email, subject element and text area. And just by doing that, if I go back to this page and refresh, you can see this web MCP2 has been recognized by the agent when this page is open. If we trigger the agent now, it will be able to fill in the form automatically. But to make a full loop, we also need to

making sure proper tool response returned to the agent. So the agent will know whether the form is actually properly submitted. We can customize the event listener for the form submit action. Like if the validation of form failed and it comes with this agent.voked events and we use this to

know if it's agent executing this actions and if yes then we can send error message back to agent which also return the correct to response if there's no arrow. And now if I go back to page and after agent fill out our form I will click on send request you will see new log here that AI calling

this tool two response and two result returned. So agent can actually decide the next action to do. Then lastly, we can also customize it further by defining a special class for two form active and two submit active so that we can control the special styling while agents filling the form and ready for

human to review. This time after sent there will be some special UI show up that is waiting for the human to review. So this is basically how you can set up web MCP using declarative way. But the most common method as we mentioned before is probably this imperative definition. So next let's go through

example of how to set up webmc for a react or next.j JS project. So here I have this camb board app built up that is functional and let's say we want to add a web MCP support for this and at the moment you can see this node to register for this web app. We will use this navigator.reister tool and

navigator onregister tool to bind MCP tool to certain react components. First we want to create a file to contain all the web mcp. So I added this web mcp.ts file where we declare this register and unregister tool. And we'll also need this patch and weight function to generate request ID for client to listen

and track those events. Then we will start defining different actual MCP tools and functions for listing columns, add card, move card, delete card and delete columns. And for each function we wrap under MCP tool schema. Then we will wire up this web MCP tools into our actual UI component. And that's pretty

much it. Now if I refresh a page, when I open this web app, you can see all the web MCP tools just show up like this. Then I can delete all the existing task and let's say help me plan all the task for prep a dinner for three people. Each column be category of tasks and you can see it start in real time creating

different columns and for each category of task is start adding task autonomously. Now I suddenly just turn any general agents to be very fluent with the web app I'm building here and it's going to make absolutely zero errors because all action is taken through the MCP tool through

deterministic actions. If you're interested, I have add step-by-step tutorial in the AI builder club course which you can find in the web MCP section. So this is a wrap of web MCP. I hope you enjoy this video. Thank you and I see you next
