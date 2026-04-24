# The Design Mode for Claude Code...

- **Channel:** AI Jason
- **Date:** 2025-10-31
- **Duration:** 8:33
- **Views:** 42K views
- **URL:** https://www.youtube.com/watch?v=vcJVnyhmLS4

## Transcript

[Music] How can you teach agent about a specific design style you like and get it replicated super high fidelity UI that is not losing any details? So typically, when you try to teach agent about certain style, most of time you just feed it screenshots and tell it help me

build app with similar style. But most of time it only give you something feel like 60 or 70%. Lot of fine grain details are just got lost during that translation. The good news is that pixel perfect vibe design is not impossible. You just need the right process and right account text for the agent. And

there it will be able to achieve 100% of what you want. And there's a one very specific workflow that I have tried that works really well. We need to give agent more than just screenshots. And then co-create example design that meet 100% of what you want. In the end, we can extract a detailed and accurate style

guide that can be used guiding agent to generate also different design assets. But before we dive into that, I know many of you are building your own product and distribution channel. And there's one concept that is becoming increasingly popular called AEO or GEO. Which represent for generative engine

optimization. That simply means how often does your product and brand show up during people's conversation with ChatGPT, Perplexity and many other language model providers. Because reports has already more than 70% of consumer now use ChatGPT for search. And some company reported to lost more than

80% of traffic from traditional distribution channel like blog. So it is critical to really understand how your brand is performing and how to improve in this new world. That's why I want to introduce you to this free tool AEO grader built by HubSpot. It is completely free. All you need to do just

type in the company name, location, and product service. Then it will automatically try to fetch data from different large language model provider like OpenAI, Perplexity and Gemini. And give you detailed score across multiple different aspects, as well as a list of different market competition that is

showing up alongside your product and brand. But most importantly, it breaks down all the error improvements. So you got idea about what you can do to actually improve your brand exposure. So if you want to learn how to do GEO well, I would highly recommend you go off try out this free tool. I put the link in

the description below for you to use for free. And thanks HubSpot for sponsoring this video. Now let's get back to the process of creating 100% on brand agented design. And when I say high fidelity context, that means we need to go beyond just screenshots. Large language model today

is not that great and extract everything accurately in terms of color, spacing, font, and many other stuff. If you want to get the real CSS style from the website and send to the agent. And I'll show you where do we get those context. And with this information, agent would be able to replicate design much better.

But most of case still, it won't be able to get the 100% design in just one go. You want to co-create a simple page with agent that really represent the overall style and feeling. And then we can use some special prompt to get agent extract detailed style guide that can really guide real their further behavior. So

with this pipeline, you can turn any website into a detailed and accurate guide that can get agent to design UI, website, or even slide decks. And I'll show you my step-by-step process. So let's say I really like Mother Duck website style and I want to copy the same look and feeling. And if you just

take screenshot and send to the agent and ask it to recreate this UI, what you find is that most of time it will only give you something like 60%. Like this is a result it generated. It looks kind of similar, but the design itself just doesn't feel as high quality as it could be. And some color just didn't look

correct. And the thing with AI generated design is that whatever you have in the code now will be used as a reference to build more stuff. So whatever the first page you design just set a standard for the rest of pages that agent is going to generate. So how can you train agent on top of existing website that looks

really good and get it generate UI at similar level quality? And this one process I often use. Firstly, we want to give agent much more high fidelity context about specific style. So if I want to copy Mother Duck style, I would just right click, inspect, select HTML, and just copy the whole style here. I'm

still pasting screenshots, but instead asking it to build app with similar style that I think the first step I want to do is I just wanted to focus on UI generation. And I would normally ask it to start from recreating a single page. So that it capture the full essence I want as a reference. So I would give

prompt help me rebuild exact same UI design in single HTML as motherduck.html. Above is extract CSS. So it will try to create this page that looks kind of similar to the original design. And purpose of this page is like it kind of set a reference implementation about

what the right style look like. And also give you this playground to keep fine tuning the part that doesn't look exactly same. Cuz most likely, it will make some mistakes. And this is where you can feed agent more context about the right style and ask it to iterate. And there also free tools you can use

like VisBug. It basically allow to get style of specific UI elements very quickly. Like I can click on this and get the correct background color and give it to agent. The current background color should be like below. Now you can see the background color is exactly same. And you can keep updating it or

iterate to a style that is kind of more personalized to your own brand. But once it's finished, that's where magic can happen. can tell it great, now help me generate detailed style guide. In style guide you must include following part: overview, color play, typography, spacing, component style, shadow

animation, border radius, and so on. Then it will generate detailed style guide including the specific color plate, typography font, the spacing system, as well as common components. So give agent a really good reference. And based on that, now we can ask it to design new UI interface. So I can tell

it help me design personal to-do UI based on this style in todo.html. And with this, it can start generating really on brand design like this where every single details are very similar to the original design. Meanwhile, this is also one command I often used for UI design specifically where it include a

list of different design principles that can making sure design generated looks much better. So if I use the same prompt but with this command, and you will see now the generated UI still have same style, but it pays a lot more attention to the detail UI interactions. And once you got one page that you really like,

that's where you can start turning that into real application. So let's say we just create a new Next.js application in this design app folder. Then I can tell it great, now let's rebuild this interface in Next.js app in design app folder to be pixel perfect and has everything break down as reusable

components. Which means now you can ask agent to create new page and new functionality. And it's going to look very similar and consistent. For example, now I can ask to help me add a new feature to add description and due date for each task. The new UI generated going to follow exactly same style. We

can even ask it to create something more advanced and complicated. Like also help me add an analytics dashboard for the tasks. And the result generated fully aligned with overall design system that you have set up. But that's not only it. One of the main artifact from this process is this style guide.md file that

can be used not only for designing websites, but also all sorts of different artifacts. Like you can also get it to generate on brand slide deck as well. Like I can just prompt it and saying please make a slide deck based on this style. Then it generated nice slide deck using exactly the same style. And

we can export that into templates. We can even get agent to generate product demo videos and animation that is on brand with similar style too. There's one library called Framer Motion that can enable you create smooth animation with a real React components. And that animation can be interactive as well.

And all we need to do just give a prompt please use Framer Motion to create product demo animation where user typing task detail and add a new task using the real UI components. And for our application, it will start generating a nice animated UI like this. And you can embed in your own website or export it

using it in video as well. You can even use this context and importing other design tools as well. For example, I can copy the style guide and use Google Stitches which is AI design tools. Just pasting the whole design guide and maybe even a reference HTML page and ask to help me design all screens for a habit

tracker app. Then it will generate a full stack of UI within the similar style. Meanwhile, I also want to introduce you to this new tool I built called Super Design Extension. It is Chrome extension where you can open any web page you like and give a prompt like help me extract design system guide from

this web page. Then we will automatically clone this web page into a pixel perfect manner and scan through all the different style file within the page and generate high fidelity style guide. And if you export it, you will get a production ready React project with all the components break down as

well as this style guide.md file that you can use for any other projects. I have put the extension link in the description below so you can try out for free. I hope you enjoy this video. Thank you and I'll see you next time.
