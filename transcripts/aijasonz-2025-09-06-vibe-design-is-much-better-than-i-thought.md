# Vibe Design is much better than I thought...

- **Channel:** AI Jason
- **Date:** 2025-09-06
- **Duration:** 6:41
- **Views:** 18K views
- **URL:** https://www.youtube.com/watch?v=4j51FMU-SUQ

## Transcript

For the past few days, I've been exploring different workflow from Figma to cursor and cloud code to get a generate super hype daily UI based on the Figma mo as well as this new chassen MCP that allow you to access different source of UI component libraries. So you can get a generally sophisticated UI

animations and components from all sorts of different styles instead of just the default chassis in and I'm going to talk you through this workflow in just 5 minutes. The effectiveness of Figma MCP can't exceed my expectation. I can take a pretty sophisticated design like this, copy link to selection and just go back

to cursor or cloud code, ask it to implement landing page section 100% pixel perfect and the cool part is that the Figma MCP tool also allow you to download image and SVG assets. Then it will generates almost pixel perfect design. Obviously there will be some like difference and I can just copy

paste over. I can give it a prompt. Overall looks great. Just make two changes. one image and it says on the right side should have some color background and there should be border line between the left and right section. Great. You can see the left side is original Figma mo, the right side is UI

generated. Looks almost 100% pixel perfect within just two prompts. And all that is thanks to this awesome Figma MCP made by RAM is open source. The real killer feature in my mind is this download Figma image feature allow you to just download both image assets as SVG logos. And to install this MCP tool,

you can just put this MCP to your cursor or cloud code. So you need to replace your uh Figma API key here. And to get Figma API key, you can just go to Figma, click on settings, security, and generate new personal access token. You can set expiration date to be a bit longer, give a name, and probably just

give access to most of those stuff, especially read permission for your files and then generate this token, paste over here. Meanwhile, another really cool MCP tool you can try is this new chassen MCP server. So this tool allow you to connect any of those chassis based UI component library which

means there will be more than just chassen. There could be new UI component library built upon chassen as different style that you can just connect to like chassen form tark and magic UI. And what's really cool about this MCP server is that it will help you retrieve whatever component available in each UI

component library that we import there and automatically retrieve the command line to add those relevant components and blocks to your project and get example code of how to use those components. And the best thing is that if you're designing Figma is already using chassen based components with

correct naming then between the Figma MCP and chassen MCP you can almost design 100% pixel perfect UI. And to do that you first need a project that has chassen set up already. Then you can run this MPX chassen latest MCP initiate with a specific client you are using. If you're using cursor you can run this but

also cloud code and VS code. And once you run that should add the chassis and MCP to your pure level. So this is very important. This MCP service need to be per level because it will read the UI components library that you imported in the registries. And meanwhile you're also adding this agents.mmd file to add

additional rules about how agent should be using those tools. If you set up the chassen public there should be a components.json file and you will need to add registries. So those registries are new UI component library built upon chassen and they will all follow similar structure as URL where they host this UI

component library and / r which represent for registry the JSON file that including the component. If you don't have your chassen um like template already set up, upload that to MCP classrooms chassen MCP and Figma MCP session. So you can download and use and just customize the registries part. So

here I have both a Figma MCP and chassis MCP and activate it and I can just do the same thing. Go to the Figma. Copy the link to the selection of frame where we use chassen components. Paste in from help me review this UI from Figma using chassen to be 100% pixel perfect. Retrieve the data from Figma. Check all

the UI component library already connected to this project and search for relevant component for data table badges and cards based on the Figma layer names. Add those components. Create the UI. So now this is UI generated from just one shot and you just compare with what's in Figma side

by side almost look 100% pixel perfect. So this basically power of chassis and MCP plus the Figma MCP for you to get really fine-tuned pixel perfect UI but the power of this chassis and MCP is not just there. The really interesting part is this ability to allow agent search components across different registries

and automatic import download to use those examples. And let me demonstrate this. At moment, there's no directory of public registries that you can use directly. There's a few I found online that is pretty cool. including this fancy component that's specialized in all the different animations to this

animate UI that has all the like animation that it added as well as this one that focus on kind of chat UI where I give you things like modal selectors and this one that has a whole bunch of really cool stuff and and also there are specialized shing component like focus on just one thing like text editor that

provide a whole bunch of things that allow you to build all sort of different text editor experience. So as an example I can just add those components registry in and for the ones we test we use PL UI I can ask what's in PL UI it will check the components a list of useful components inside this library then I

can just ask it to help me build a text editor UI then it will start adding the components and build up the UI. If you check out it will add all those component directly into your project. If we check out now we have this pretty sophisticated text editor experience directly implemented. you can swap out

to a different library to add some like fancy animation to make this UI look better as well. So you can mix match different components. So this is the power of the new chassis MCP and you can even build your own UI component library hosted somewhere so you can import for your future purchase. If you're

interested about that, I can also make a video talking about it. So comment below if you want to learn more. I have added all detailed instructions to AI builder club about all the MCP tool that we talk about as well as a chassis invite template that already have this component registry set up. So you can

come just modify, edit and start using right away. Meanwhile, we run weekly workshop talking about the latest tips and workflows of vibe code in production. And this upcoming week's workshop, we're going to specifically talk about UI generation workflow. So if you're interested, you can click on the

link below to join AI builder club in our upcoming weekly session. I hope this is useful. Thank you and I see you next
