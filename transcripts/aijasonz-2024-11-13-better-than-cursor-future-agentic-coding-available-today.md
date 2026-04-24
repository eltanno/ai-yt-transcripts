# Better than Cursor? Future Agentic Coding available today

- **Channel:** AI Jason
- **Date:** 2024-11-13
- **Duration:** 27:32
- **Views:** 64K views
- **URL:** https://www.youtube.com/watch?v=824Fyh146_w

## Transcript

so I've been playing with this new AI ID called Wier for the past few days even though it's looks familiar like any other e IDE it does feel very different when you actually use it one of the key things that wi serve doing particularly well is the context awareness if you ever use cursor to implement some

feature to existing puras one thing you will quickly realize is that cursor often didn't really understand the project structure very well even though you set up project and ask it to build app it often has noide IDE about what type of project it is and where it should create the right project file not

to mention if you want to ask cursor to add a new feature to your existing cbase it almost guaranteed fail because you generally didn't really understand the dependencies of different files so how is a wind serve going to be different so this a wi Ser interface it looks pretty familiar like any other Aid you can

build any files try to do things like autocomplete but what's really magic is this Cascade feature so Cascade to some extent you can consider that as like cursor composer it is Agent that can create files run commands and understand your project structures and it might look similar to any other chatwi code

based interface but once you try it it does feel a little bit different as it is really aware of the whole project structure the environment it is in much better as a quick example I have this nextjs project already set up with certain file structures I can just prompt wind serve cc to build out the

web app and without prompting at the current file structure it will be able to create file in the right places for example if I wanted to create a basic text to image platform I can just take a documentation from flux model that is hosted on replicate copy paste whole dog directly and then add a simple prompt

above is a text to image AI model posted on replicate help me turn it into a web app using nextjs and chassin I already set up a project in my app folder and you will see that before you implement any code it will firstly try to analyze your project structure to understand where to create which files it identify

the the nextjs project and chassin components already set up and next it will also show this UI ask me for approval to run certain terminal commands so it is able to actually run command directly if I click accept it will run command and get a result if there's no Arrow it will continue but

you can imagine if the command line return arrow it will also be able to self reflect and fix issue if you check the project folder on the left everything has been created in the right place as expected and you will know that there's a components folder already so all the new components will go under

that folder and if we open this app it is also running too and apart from this Pur structure it actually keep track and understand all the change that human is making alongside the AI for example I can go to this component and change the name of this function to be text to image form instead and save this and

obviously this will cause error since all the variable name is wrong but I can actually just go to Cascade and and say continue without giving any prompt it actually understand and notice that the component name has been changed from image generated form to text to image form then it start refactoring the whole

code base to making sure everything has been updated and using the new name and it also proposed update the file name to reflect change as well so this was really big H moment for me and that made me realize why it is important to build an IDE instead of just a visual studio plug-in because now they can understand

so much better what the user is doing and get a lot more contextual information like the change they make which file they are on at moment or even have sandbox environment to get direct feedback from the console and another thing I experienced while I was using wi serve is that there's one time I got bug

in the application that I'm trying to build and they ask wi serve to fix it then what I observe is that it actually start reflect and iterate its own solution so it generate a fix at beginning and then later it said let me try another approach since the previous one might still have issues so it tried

another version but after that it tried again it says let me try one Final Approach that should work more reliably and in the end it does fix issue so this was really interesting cuz quite often when I use other platform like cursor or co-pilot while you're debugging many times it feel like it is just running

circle and try to do the same thing again and again and not fixing the issue but this ability to actually reflect and think about different ways it can solve the problem can probably dramatically improve the result and output though it's a bit mystery to me about when this will be triggered and how does it decide

there are actually still improvements and iterations it should do but this Behavior definitely feels very gantic and smart so as I mentioned before even though this Wing serve UI looks very familiar behind things there a lot of work seem goes into improve the code quality as well as the contact awareness

and to understand why Wing serve is doing so much better in terms of context awareness I reach out to the codent and Wing serve team to understand what their secret Source are and they share a lot of interesting source of how does Wing serve actually work behind the scenes but before I show you those insights

interview Clips I know many of you just getting started learning how to code and one question I got asked a lot is whether it is still needed to learn coding if so what does a road map actually look like and that is why I want to introduce you to this free ebook did by Google's principal analytics lead

and data scientist Sunday scet where she wrote down all the secret tips and methologies that she used to learn coding with platform like Chad gbt and design a personalized learning role map it cover all the fundamentals and basics of coding like how do you choose the right coding language to start with for

your purpose best practice prompt for different coding scenario like debugging and optimizing the code as well as detailed road map of how to master python in just four months with a purpose build a custom gbt that contain a lot of Learning Resource and detailed video tutorial showcase step by step of

her workflow so I definitely recommend you go go take a look if you just getting started with your coding journey I have put the link in the description below for you to download for free and thanks hops ball for sharing this awesome material for free now let's get back to Winger and here is the interview

Clips between me and Codi and founding engineer Andro where he Shar a lot of interesting learnings and thoughts about how wi Ser is building this context aware IDE the way I always kind of explain casc is we've given the AI access to three things right knowledge tools and the human acction and I think

there was kind of research along each of those three things that we realized that we were at a depth within each that combining them actually made sense to do larger and larger tasks so on the knowledge side we've been investing a lot of time into building what we like to call a context awareness engine right

systems that can truly actually take large code bases as Parts them embed them index them combine full repository awareness with the code structure so we've been spending a lot of time building those systems that are orthogonal from the llms themselves that's one part of the codium story we

support over a thousand Enterprises including a number of the Fortune 500 and the only way that we're truly able to give a a company of that kind of complexity of code is if we've done a really good job at understanding their code base that's the first access so that there's kind of constant research

there that we've already all always been doing be powering the codium extension so far but then the tools and the human actions part I think we're more recent and I think that's when when things came together on the tool side we we recognized there were some like tools like okay make an edit to a file or add

a file or GP or list a directory like these were kind of obvious tools that we wanted to give the AI I don't think these are necessarily groundbreaking kind of ideas but we'd also build other tools as well and and one of them was actually covered by the press a few months ago um it was this idea that

embedding base retrieval had some fundamental limitations right if you have a lot of Code false positive rates for embedding based retrieval simply means that the number of false positives increase and if you have a lot of garbage coming in you have garbage coming out and so we've come up with a

new way of actually leveraging compute to actually massively parallelize a bunch of llm running at once across a large amount of compute to essentially retrieve more relevant Snippets at a much higher accuracy than any embedding based method right if we if we just go back to embedding based methods right

you're taking raw code Snippets you're putting them into a lower dimensional space um by definition you're losing some of the Nuance of the original raw text that's just part of it so pending embedding BAS system there is a fundamental limit to it on kind of the accuracy and how low your false bitor

rates can get but what if you flip the question a little what if you say okay what if we can actually just instead of doing embedding based search because you do embedding based search because it's fast what if we actually trained a proprietary LM that was really good at asking the simple question is this

snippet of code relevant to the query that I'm asking it doesn't have to be a very large model but it's like a purpose build model that's really good at that one question and then you take that model you paraliz essentially thousands of those calls across a ton of compute for a really burst period of time then

essentially you can get a really much more higher you know quality score on the relevance of each code snippet to the query at hand actually captures the full Nuance of the raw Tex and then we've essentially figured out by using that as a signal and using that as an ability to do search it is

significantly outperforms any embedding based state of the art method possible yes you're doing a trade-off of compute but like we'll take that trade-off any day if that actually means it it creates significantly so was like some breakthroughs there and then on the human actions part I think it was just

really trying to figure out what's the right granularity of like a trajectory are we able to actually pick up on what the developer editing or where the developer going into the edit and how they're navigating a directory or doing commands in the terminal and understanding the granularity that was

required there to really get a true picture of what a developer was doing at all times and I think that was the third reason and that was the most recent one where it's like okay we really do want access and control over the editor because we want to see what a developer is doing because if we can understand

what the developer is doing we have a much much better chance of understanding what their intent is and then they therefore giving them relevant results so there's a lot of can't say it was just like ah yes we had one magic bullet that unlocked everything right it's like multiple years of of actual work that

came together um that made it really clear that if we just developed our own surface our own ux or our own IDE we could expose this in a pretty magical way and to best demonstrate how can you get the most out of wing surf let's build a real application together and while I was looking for use case to

build I saw this tweet from Greg Eisenberg where this a micro set called bank statement converter basically just do one thing taking the PDF and convert them into Excel but this simple application itself is generating more than 30k Revenue per month and this is really interesting because extract

structure data from PDFs is a job that large Lang model is really good at and there are so many different niches you can potentially build like for accounting firms lawyers marketing agencies many of them spend hundreds of hours every month to do this data entry and converting job so I use wi serve to

build this PDF to excel converter where we can drop any sorts of different type of PDF files and Define all the data part that you care about and it will do the rest of work to extract information and convert them into Excel file that people can download with this one you can easily tweak into specific vertical

solutions that you know well and maybe get a smaller model to F tune and drive down the cost and I'm going to show you step by step how can you build this in Wind serf so I'm going to set up a new project in GitHub so we can keep track of version and firstly I want to set up a nextjs project using chassis

in and then I'm going to do CD converter MPX CH in latest at input S car label button which is a list of common components we likely going to need to use and to build this PDF converter the pipeline looks something like this the app will take a bunch of different PDFs and then we're going to use llama Parts

which is probably the best PDF to markdown converter we have on the market it's basically service that can take Massy PDF files extract information into markdown which is a format that large Dage model is really good at reading you might wonder why do we need a special PDF converter well that's because PDF is

really complex and messy there are all sort different structures like tables or diagrams and even equations and sometimes the reading order is also different you might have PDF file that contain text that has to be read in certain order to make sense so there are whole bunch of optimization need to be

done to making sure large L model can actually read the PDF file properly and this is where llama pars is really good at so we're going to use llama parts to actually extract structured markdown text from message PDFs and then we're going to feed this data to Lar model that support structured data extraction

like GPD 4 o model then we can flatten those data into Excel file and as we mentioned before we're going to use nextjs as a framework and if you're not familiar with the front end development nextjs is a type of front end framework instead of building from scratch they will provide a lot of components

building already with specific project structure and chassen and twin is just the UI component and CSS library to make your app looks better and we also going to use npm npx they are like the package manager to install third party libraries so let's get started so create instructions folder inside this project

folder and then create instruction. MD file if you ever watch my other AI coding videos you will know my process normally start from defining a product requirement dog to align with AI so that whatever it is building is going to deliver the result I want and the common structure normally look like a project

overview to indicate what does the project do the core functionality that I wanted to deliver the relevant doc implementations and important implementation note to cover common mistakes that AI model make as well as the current file structure but one really good thing about wind serve is

that it is really good at understanding your project structure so I actually don't need to do this hack anymore to include the current file structure because wi serve just gets it but the rest of content still remain relevant and I have asked wi serve team to confirm that as well and this is their

recommendation about how much information you should give up from so in our case I will give this project overview that your goal is build a nextjs app that allow us to upload multiple PDF files and use open structure output to extract information and convert to Excel file you'll be

using NEX js14 chassi and Tailwind Lucid icon and then I'm going to write down the core functionalities in my mind for this app there are four key components one is we need to allow user to upload file and Define the data points that they want to extract then we're going to use the L parts to extract the text and

send to open AI to process those data and in the end convert into a Excel file so people can download and I normally tend to specify very detailed behavior that I want so here is what I put for the file upload and schema definition so user should be able to upload one or more PDF files and they should be able

to Define data point they want to extract it can be either individual fields or can be groups which is like array of objects that they want to extract and this could be useful for things like bank statement or invoice where you might have a list of information with similar structure that

you want to capture and for each group users can Define multiple Fields inside as well or even other group to create this kind of Nast structure and there should be a button star extraction and I also want to set a default schema to Showcase how does this software works so I'm just going to give a uh default

value in then here I mentioned that it need to be server side file processing basically in front end rment each function you can do on the client side or server side and server side action are good for task that require either security data preloading and file processing

typically is something handle on server side the majority of Doc here you can see basically just split out the requirements of what kind of feature that you want to build then for text extraction I will say use llama for PDF Tex extraction and again it is server side and for each file combine all the

documented chunks for complete TX making sure return the four TX so this is something I noticed when I was using LV Parts before because it will break down the whole PDF into multiple different chunks and quite often large L model didn't know that and only extract the first chunk which means we're are not

getting the full PDF data so I'm just adding this instruction here and this text extraction should happen immediately after user appro the file to the UI instead of waiting for the button to click so that we can make this process a bit faster and strictly following llama procor documentation as

code implementation example so this is actually pretty important because llama parser is a fairly new package so model like cloud or gbd4 didn't really have much knowledge about how to use that and typically what I do is I would just go to their documentation and copy paste the file here into my instruction Doc

and I we making sure the name here is the same because this I believe will actually help wi serve to pay attention to the relevant parts of documents if the identifier here is saying and after each file uploaded it should be displayed as an item on the page so that users can click to preview the text

extracted and they can keep adding files and this should be a server side processing only and then data processing so after user click on the start extraction button the data should be sent to open AI to process all the files use open AI structure output for information extraction and straightly

following uh the documentation that we attach for open AI uh structure data output and I would basically do the same thing to find a relevant code example that I can put in for this specific One open I provide example for structure data extraction so I'm going to copy and paste in and one thing I will putting

here is is also a note that making sure you use gbd4 all model and Zod for defining data structure this is something I found when I was using cursor it almost guaranteed fail with this open a functionality because structure output is very new feature that open a released and large L model

didn't have that knowledge when I using cursor it wasn't that great in terms of fetching the right code example inside the documentations so it tend to implement in the oldfashioned way and this is where you will see wind server that is really good at and last part we will also put documentation for file

download so combine all typ data process from multiple different file into one Excel when there next structure flatten them and we should have proper error handling and enable Excel file download and we also want to implement tempor file clean up because otherwise all the Excel file uploaded will just keep ping

up and that's pretty much it um the last thing I would do is that I will also include some important implementation notes so in my AI coding workflow I tend to keep track about list of common arrows here so that it's less likely it will make those mistakes so with this one it's pretty much ready to go we can

start let wi serve to implement this app for us I'm going to open Cascade which is a coding agent in wi serve and then give instruction I want to build a nextjs app for user to upload PDF files and convert into Excel Implement strictly based on this instruction that I give I've set up the project already

in this folder now let's build this uh first feature which is file upload and schema definition so there are few things that you will see happening if first say go inside the instruction file and then look up the revant chunk you can see which lines of code it actually uh looks through then you also check

what kind of components already exist in this project to making sure it is creating file in the right place and what you will see here is that compare with cursor composer after every step here it can reflect a bit of what has been done before and then move on to the next step and after this is done you

will also see something cool in the code it generate it used a few UI component library that we haven't installed yet so it will generate the terminal command and ask ask for approval and if I just accept here it will run command line and move on to next step and this is really good because if your command line has

some arrows it will also get as feedback so they can iterate and design Next Step based on that and let's try to run this our open Terminal and then do mpm run def cool so you can see this app is already already build where I can upload files and can also Define the specific data point that I care about I can give

a name data type the description here if it's group I can Define information further as well great so now I'm going to move to Next Step let's do step two and what happen next is it actually will go back to instruction. MD and look for the revant information as part of context and here notice that I need to

install new libraries so I will just accept that okay so it finished uh but it got Arrow this Arrow basically means that we haven't really add this dialogue component from the chassis in you can actually copy paste this in and then it should be able to round the right

command for you as well but one thing to know is that at default I think cloud 3.5 uh is still using the old syntax which chass and UI and that will cause issues so just making sure you add special instruction like this if you're using chassis and into documentations and what's really cool here is that

because of this Arrow it also kind of reflect to say oh we need to check if other components that required also install and also look up the file dog to double check now next two things we need to do based on previous instruction is one is ADD llama paror API key another is I need to create a folder uh inside

project route for uploaded files so you can either just create a folder here for plose dat but you can also ask insert to do this for you if you need but I'll just create a ARL here and we also need to get llama pars API you will create account on cloud. Lama index. a and then go to API Keys creating new API Keys

here and go Tov paste your API key so now we can refresh the page and give a try I'll upload this example PDF files and once finished there will be a view text button if you click on that you can see that the text has been extracted properly into markdown file based on the original invoice PDF great so so now we

can move to Next Step let's do the step three and this is a part that I'm very interested in because as I mentioned before Cloud 3.5 has no idea about the latest structur output functionality but you can see here in the wind surf the first thing it does is go to the relevant part of instruction so you

understand what's the latest syntax then decide need to install this open Ai and Z components which is bredent that means it probably will Implement in the right way and then it'll also try to use a chass in table and what's brilliant about this is Wier somehow just remember those things a lot better and use the

right syntax and this release much less arrows as you can see all right this function is done all we need to do just adding the open AI API key here in the EMV file as well then we can try to run this go back upload the file and I just want to go quickly double check if it is

implementing the right way so if I go to process data you can see that it is using the right model and using exactly the right format that we asked to and as a result it showed us the table that we were looking for so this is a brilliant I'm just going to ask it to do the last part which is uh file download and again

it will ask me to install this package all right so this part is done as well we can go back to the application upload the file and then do the extraction and once the data is extracted you can see this download Excel file button if I click on that that the result is showing in a proper

Excel table so this whole functionality is done already as you can see wi serf did a really good job in terms of extracting and referencing to the latest stock because both llama pars and the open AI structure output are not part of the lar n model's knowledge but it was able to reference to the ride dog that I

putting here and last bit I just want to do some quick UI touchup because now the style looks a bit kind of boring and one thing I did learn from our community member Garrett in the AI build Club is that we can use v.d Sims to control much better UI for example if you go to vz. d/s you can click on same to clone same

and playing with different styles on the left you can even get AI to generate a special same that you want but for me I kind of want to use this kind of Windows 98 type of style and once you finish you can copy code uh and just paste those code into your nextjs project one by one so I will paste this CSS file which is a

global CSS paste it in and then the fonts file in the layout. TS which is under your app folder and then tailing config which should be in your root folder and now you can try to run this uh okay looks like we got some arrows that I need to define the font weight uh so you can just paste this uh Arrow

message in and one really cool things about wind serve is that you can see that it actually knows what kind of modification you made recently without prompting it so that it has more contacts and are able to fix those things directly for you cool so we got this kind of Windows 98

style UI here and another thing I do kind of curious to try out is that how good a wi serve is in terms of understanding your existing Pur structure and adding new feature to it so I would just start a new Cascade and I assume it probably didn't have contact or past chat history to understand where

we create which file so I'm going to just give you instruction without any context makes the app a lot more mobile friendly and I want to display upload file UI and schema definition UI side by side and make a star extraction button sticky at the bottom with primary color Windows blue so you can see what it does

is that it firstly analyze it look into our page. TSX which is main file try to analyze file and understand what all the different components available there and then try to identify where the right place to implement those Chang and if I go back to the application you can say just transform the UI for me without me

prompting it at all and it is fully functional as well so that's pretty much it if you are interested in how to use VZ same and how to build UI part a lot better G actually did a course inside our AI Builder club and if you don't know what AI Builder Club is it is a community that we're building where we

dive deeper into all sorts different AI coding and agent building courses with a step-by-step tutorial and code examples and most importantly we have this group of top AI Builders who might already experience the problem that you are facing with so you can just come and ask questions to so feel free to click on

the link in the description below to join this AI build Club I hope you enjoy this video so this pretty much how we can use wind serve to create applications as you can see just making the agent much more context aware even though it is still not type of platform where you can just go give one single

instruction and it will work out everything for you but the code quality is much better I'm very excited about what type of interesting tips and tricks you guys start finding using wi serf so please comment Bel for sharing any interesting insights you have thank you and I see you next time
