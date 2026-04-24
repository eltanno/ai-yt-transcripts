# 1000x Cursor workflow for building apps

- **Channel:** AI Jason
- **Date:** 2025-01-07
- **Duration:** 27:54
- **Views:** 76K views
- **URL:** https://www.youtube.com/watch?v=jzhANqD_VhM

## Transcript

how can you build IOS app 10x more effective with AI IDs like cursor and wind surf so AI coding platform like cursor and wi surf has became extremely popular past few months we saw people building all sorts different applications some of them are very sophisticated but it was never easy to

build an IOS app with cursor or one of the reason is that if you're building IOS app you have to use xcode as a development environment even though you can still open the project file with cursor there's still a lot of contacts that cursor won't have for example if there are Arrow message it's very

difficult to bring all those Arrow message as contacts bad cursor so that it can debug and fix issue and as we know clear and precise context is one of the key to make AI coding assistant effective on the other hand there are also Frameworks like react native and Expo which is a framework where it help

developers to just build codebase once and it will transform into Android iOS and web applications the problem is that the best lar L model out there like Cloud 3.5 don't really have much knowledge about Expo and react native so often the code it right is just not good enough so both those two challenges made

iOS development quite challenging but the good thing is for the past few days I learned some new workflows and tips that going to make your iOS development 10x more easier you can almost develop IOS app just like how you build a web location I will show you step by step what does my workflow look like and also

take you through example of how can we bring jinen Seafood app idea life what will you say if I told you there is an app on the market we're pass that part just demo it okay let's start with a hot [Music] dog holy yes it works mother do pizza let do pizza pizza okay Pizza

[Music] not hot dog wait what the H that's that's it it only does hot dogs no and a not hot dog yeah this EP idea where you can just get AI to tell what food it is V the picture just seems so magical a few years ago but now it's actually very easy to build and no we are not going to

build a hot dog not hot dog app I'm going to take you some example of how can you rebild the Cal AI app which is app where allow user to take picture of food and automatically analyze the calorie intake using multimodal lar Range model if you don't know CI it is apps that buil by 17-year-old high

school students they already made more than 1 million monthly Revenue so without further Ado let's get it but before I dive deep into this one question I got ask a lot is what does the road map look like for learning programming that's why I want to introduce you to this free ebook that

did by Google's principal analytics lead and data scientist some that scalette where she wrot down all the secret tips and methodology that she use to learn coding and design a personalized learning role map that cater for your needs it cover all the fundamentals and basics of coding like how to choose the

right coding language to starway for your purpose best practice prompt for different coding scenario like debugging and optimizing the code as well as detail road map of how to master python in just four months with a purpose buil custm gbt that contains a lot of Learning Resource and detailed video

tutorial showcase step by step of her workflow so I definitely recommend you go take a look if you just getting started with your coding journey I put a link in the description below for you to download for free and thanks hpot for putting together this awesome material for free now let me take you through my

new iOS cursor development workflow the first thing we're going to do is that we're going to transform your cursor wi serve into a proper iOS IDE and one of the key components you're going to use is something called sweet pad so sweet pad is a vs code extension it will bring all sorts of X code functionality into

vs code directly and because cursor and wind surf or build based on vs code you can just install this extension directly to do that first step is that you can open cursor and click on extension button here and search for sweet pad this should pop up and you can click on install button and after you install you

should see sweet pad showing up here and you can just pain it as well so it'll be easier for you to access later and this is where we're going to run the project and open the iPhone simulator later so with sweet pad install your iOS dment experience with cursor is already 10x better but there are also few things you

can do to bring it even further one that you can install this xode build server so XB server enables Advanced code navigation for feature like autoc complete where it can show all Thea variables and things like Arrow highlights so you can just go to terminal and then do Brew install X code

build server and we also need to install the iOS deploy this will allow you to run terminal command to to install mobile apps in your iOS device or simulator and on the other hand there also another packaging you can install called XC buy this will makes xcode output much easier to rate in vs code

and this is particularly useful for things like Arrow logs so again you can install this by doing Brew install XC beauy and last one you can also install this bre install s format and this again is a tool for automatically formatting your Swift Code follow consistent Styles and last but not least if you haven't

install Swift language support in your cursor you can go to extension and install it so with all those setups your cursor now is becoming an iOS ID and I will show you what I mean so to get started let's open X code and create a new project and I choose app you can give a name and I give a name SE food

and for testing system I'm just going to choose n for now and click next create and after this is created we can go to cursor and open the folder and now the first step we're going to do is we're going to do command shift p and this one option called sweet pad generate build server config and this will create build

server. Json file that allow the X code build server to work with your project directory so you can choose a project here and after finish you should see a build server. Json file here and this pretty much it you can now start running the application directly from cursor so if you go to sweep hat Tab and click on

this play button for the first time it will ask you to choose the simulator and you can choose any simulator but on the other hand you can also connect your iPhone or iPad and then open the destination and then just refresh the destination iOS device here and you should see the device show up if you

didn't see that making sure you go to x code and set up the device properly so in this case I'm going to open iPhone 6 16 and below that you can see that the app has been running you can see simulator is open and running our test app automatically now we can open the GitHub so I'm using GitHub desktop app

and I will click add existing app and choose folder where we create this xcode project now let's try to build and launch an IOS app the one I want to showcase how to build is this app called cow. that allow users to take a photo of food and automatically analyze and log calorie consumptions this app is

generating more than 1 million monthly revenue and this is just classic example how can you bring any Niche idea you have to the market so firstly this is one setup we do need to do uh if we go back to the X code click on the project icon you have here and go to info so we need to do something here to actually

generate a file called info.plist This is where we will write the device permission access to things like camera location and X code at default didn't really expose that file so we just need to open anything like document types add a new one and leave it empty but now you will see that's a new file created

called info and if we go back to X code you can see that here is one info. PDS file created so now cursor will be able to update this file to manage permissions and on the other hand before we just ask cursor to build application directly there are some best practice set up that I often say people didn't

really do one is cursor rules so all major AI ID like cursor Wier vs code all have this component Project Specific rules all you do is basically create a new file called do cursor rules if you're using cursor and then information you're putting here basically become a system prompt for the cursor agent so

for example you can put a random instruction here that always start with yo and you can open the side panel and just say hi and you see that it start with this random phase that we put at top but to make your cursor rules actually effective you want to making sure the rules you're putting here is

concise and necessary I know there platform like cursor. directory that aggregate also different cursor rules that people have been putting out there but one mistake I saw people doing is that they would just copy whatever cursor rules other people have and use for your own Pur this often didn't work

very well for a couple reasons one is that you want to keep the cursor rules to be as concise and necessary as possible because the more contacts you feed the AI agents the more likely it will forget details and not following the rules so by just copying other people's cursor rules very likely you're

going to include some stuff that is not necessary for you and the way I would structure my cursor rules normally look something like this our firstly give a oneline description about the context project and here I won't dive deep into specifications about all the requirements of the project because I

will create a new file called instruction MD later for detail requirements here I will just give a quick context and there are two things I almost always put in one is that I will ask agent to always add debug logs and commands in the code for easier debug and readability and second one is that

every time they choose to apply rules explicitly stay the rules in output cuz quite often it's hard to tell whether agent actually are adopting the rules that you list out here or not and by doing that it will make it clear and next I will have a section called existing purchas structure this is where

I would give the pur structure so that agent will know which file already exist and which file it didn't and to get the information again just open Terminal and then do tree okay so tree is a package that can generate the file structure of your current file and L3 means it will go down three layers deep so I can just

copy the pur structure and paste in and next I will also put TX stack so this text session is particularly useful if you are using serd party library for certain functionalities meaning prevent cursor from implementing a functionality with a different package which my messing up and in the end depending on

type of project you're developing I will also putting some Swift specific rules and again in here I normally just put in situation where I observe agent often make mistakes if you never saw agent make certain mistakes there's no point to including the rules here so with this cursor rues it should give us a pretty

good starting point the next one is that I will also create a folder called instructions and inside instructions I will create instruction. MD and here is where I created specific product requirement dos normally including like the scope and purpose of project and then list out the key features and for

each feature I will number it so I can dive deep into the specifications if you don't know how to build it I will also show you how did I get this prod requirement docks ready so typically I will use powerful model like 01 to generate this part requirement docs I do is that I will take a screenshot and

then I'll give instruction I'm trying to build an IOS app called Seafood they autoc calculate log calories it should have key functionalities like below take a picture of food analyze food and history view help me think through how should I build this and how should I structure PRD DOC for engineers and PRD

should have sections of project overview feature requirement for each feature data model API contract it be explicit about dependency variable name API to call so it Lees no ambiguities and it will generates P requirement dock you should always review the stock and see whether any part does really align with

what you were thinking so it is breaking down into four different features capture food image analyze food edit and confirm result view history looks good the only thing is that I plan to use open AI multimodal model ability and together I normally need to provide some kind of code example of how can you use

this API point and the easiest way to do that is I can go to the open AI playground or choose the right model and then the response format I will use the Json schema so this is where we're going to use a structured output feature from open a just click on this generate option your AI calories calculator you

will be given image of food and output what ingredients does it contain and calories for example the TI description of image ingredients which I will use this to indicate that it is array and total calories Health score and I'll click enter Then This Will generate at the Json schema and I can update it a

little bit uh to my food calories analysis and here our change to be image description describe what do what food do you see in image and reasoning then ingredients which is array and for each array it has title calories per gram and total gram total calories and since I Chang the title here I will need to also

change here and click save going to just take a picture of some food uh like this is a pancake uh so I will go back here and do a test okay so you can see that it output the information properly it identify it is French toast and all the ingredients it contain so this looks pretty good and what I need to do is

choose a code option and change to crl copy this and go back to our PRD chat GPT session so I'm going to paste in here for the lar model API service we'll be using open latest model with structural output function below is the latest code example and this is where I paste in this code example here and also

copy this example output and tell you this example response now help me update doc to reflect this making sure you use the latest in taxing the Cod ex that above and here it didn't actually return me the full PRD so I'm going to ask it to return me the full PRD cool so now it return me the full

PRD what I will do is I will copy this and paste in the instruction MD if you want to get a full prompt as well as the cursor rules I'm using here as a reference you can click on the link in the description below to join the a build Cloud where I have full PR pasting here you can just copy paste as well as

ton other practical AI coding examples that you can take as reference but more importantly there's a community of top AI Builders who might already experience problem that you have today so you can just come here and post any questions and channs you have and both me and other Community member will just come

and provide advice so that's pretty much it we can getting started I will open the cursor composer in the right side panel here and arive problem how we build IOS app based on instruction let's first say do step one capture food image and or accept all and again for

all code that generate by cursor I think you should try to look into each file to understand what is implemented so on one hand it will help you to be better developers but also it will allow you to just quickly check and see if there any issues so you can see here it create two files one is camera view this a code

where it will it will Define the UI you can almost think this as HTML so you can see that it shows a camera preview view add a space and also add a button and also create a camera view model so this common structure for IOS app called model view view model you basically use the code under views to render the UI

and the view models is where you will process the data that will be rendered on the UI this will make the code easier to maintain without further ad do let's get started I'll go to sweep pad and click on this build wrong button so you can see we got some and this is the best part of using sweep pad we can just copy

those arrows from build fil to the end and then paste those arrow in and accept this and I will run again and this time you can see that the build has been run successfully and if I open the simulator it has this app with this button click on scan food it will open the camera view but one thing is that simulator you

can't really test out the camera feature that's why I will also try to install and test this app on my phone and I'll just open Quick time for you to be able to see on screen after you connect your phone to the X code you should see a option here and we can try to run this and here it says the OS version didn't

really match and this is where we can go to General and change the iOS version to 18 and now the arrow is gone and now I will go back to cursor in destination you just see an iOS device here if you click refresh this option should show up and what I will do now is that I will do command shift p and select s pass SL

destination and in here you should see your device showing up you can click on that and click build and run and that should reinstall the app on your mobile phone and run now I can try to use it on my phone okay so here's one problem even though I can see the camera view pop up there's no actual live view of the

camera what I do is I will copy those commands in and then open the cursor give promp the app is installed and running however after I click scan food it brought up sheet of camera with camera button but it didn't show me actual live camera view below is a log help me adding more debug information

and figure out what is the issue so here is one thing I often do every time when they're arrows I always ask it to add in more debug information and here we found issue the camera view isn't showing because we need to propably set up preview layer and it's frame okay I'll click accept and let's try again okay so

the issue didn't seem to be fixed but now we actually have more debug information so I will copy those things in paste it the issue is not fixed still the same behavior here is the logs and now it says that the issue it found is that preview layer frame is zero which means the view isn't getting properly

bounced and I will try it again so here you can see this is benefit of always asking to adding more debug information cuz it will really help you to identify the rot cost okay great so now you can see this camera view is working publicly now we can move to Next Step but before we do that I

will just open my GitHub and give a commit Implement camera view and then I'll go back to instr instuction and and currently after I click on take camera button it didn't really take me to the confirmation screen so I will ask it to implement the rest the camera view is showing up poply but it didn't take me

to confirmation after I take a photo help me finish the rest of capture food image requirements so this time it meaning create new view called confirmation View and now if I click on the camera button it will take me to this confirmation screen where I can use a photo or retake

all right so now let's do this step two so now we add a new commit add a confirmation screen and then go back to cursor created worked now let's do step two cool this time it create a folder called service where it create open AI service here and it also create endless view to present the result from open AI

API API it also update camera view model to uh include this nless functionalities and one thing I would do is that I would check open AI service to see if it is implementing things properly and as expected you can see there are some parts is not working well it's using the old model which I change full old model

and the last thing is that I will also need to replace API key uh so I'll just search and I'm going to replace my API key here so I'll click accept and let's run the app again okay and this time we got some more arrows but the good thing is that we have those Arrow message here directly so I'm going to paste this in

and take got Arrow cell to build and let me run again okay so this time we got some different build fils uh so I just again paste this in more build fil okay now we have more arrows so I'm again just going to copy those arrows in paste in here more good fail okay great so this time it succeed

and let me try I'm going to pick up orange and it's showing the small tax analyzing food and I can also see the lock here but it showed a failed message so I'm going to copy those arrow in the app build successfully but got this Arrow after receiving the response from open a so here I think the arrow is

because a model name and uh I know for sure it is not the case so I'm going to update the message here a little bit so the app buil successfully but got this Arrow after receiving response from openi the model name is not the issue it should be gbd4 help me add more deer log to understand Ru

cost okay so this time it gave me the proper error message as you can see missing the required parameters response format. Json schema if I check the original code example you can see the key here should be Json schema so probably this is issue I will change this to be Json schema here uh and let's

run again okay and this time it give me more arrows about the Json schema uh let me just double check so here we put Json schema into full Anis schema and it has Type properties and if we look at the proper schema it should have name strict so I think the problem is that the

schema here isn't correct what I would do is that I will go to the instructions and I will copy this example code response and put in here I will also do add menion open AI service I still got arrows so see I think the Json schema food and schema is not find properly it has to have same structure like code

example I pasted Place update a code okay so let me accept this and we can run again okay great so now we get response from open pop the an icon stream directly on the screen but you can see on my phone it is popping up a proper Anis like this great so I'm going to make a new commit uh the open AI

integration and then let's do the next step now let's do the step three I finished it created a new file called editable food analysis which is data model so as we mentioned we are using this model view view model structure and model is where you're going to store those data structure so in this case

that means for each food analysis we will have those data which is title image description ingredients total calories and health and this will help system to validate the data type making sure all data is in the same structure and also create a view for editing and now let's try try to run this okay and

we got this arrows I'm going to copy those in got failed boot arrows so I can run this take a photo and here one thing we can optimize further is the image compression So currently it's in the original image to open AI which is probably too big uh if we compress it it can makes the image

processing much faster from open AI so this is one optimization we will do after uh we finish the whole application Okay cool so I can see this adding button if I click on that I can go start editing the view but there are some changes I need to make so I'll give some feedback a few things to fix one editing

view user should be only be able to edit the gram of each ingredients and calories per gram they should not be able to change total calories that should be calculated based on the value above if they change gram or calorie per gram the total calorie calculation should be updated automatically and

second issue that the editing experience is not great the UI looks crowded and after I type in character the key keyboard automatically close help me fix above okay and I click now accept and try again so let me try again I'll take photo of orange and waiting for response and go response back and I can click on

edit so now if I change the gram to be let's say this 80 instead you can see the carry calculation will be automatically updated and I can add a new one let's say I also had mute so this part is still not fixed but in here if I change the carry to for per mute to be 0.2 and amount is 100 G the total Cal

will be calculated uh but there are still some issues the user should not be able to update the total calories and health score and when updating ingredient names after typing each character keyboard Clos automatically which made the editing quite difficult and let me try again and one thing up to

this point is that I actually didn't care too much about the actual UI cuz I'm going to come back and fix all the UI later okay let's try again and I click on edit so now I can change the caly here and you can see the top caly will be automatically updated and I if I add a new one with Okay so

this typing experience still not fixed which we ask to fix but if I add a milk to be a new ingredient the total c will be automatically updated so that's pretty good I'm going to just ask to fix the one last thing the C calculator is fixed now however the editing of ingredient name is not fixed after I

type in any character it will automatically close keyboard and help me fix this and this time it added a temporary title to handle this and also unchange modifier to maintain the focus and it got on Arrow again um so we're going to repeat the same process try again take photo got and I click add it

if I try to change this this weird still the same behavior um this is very strange so I'm going to give debug information still the same behavior of autoc close keyboard while editing ingredient title help me add debug locks to understand the Ru cost okay so now we have some new logs I

can copy those logs in here and then say those Behavior still the same and above is a lck so this time it found that issue is because a view has been recreate every time when Title change which is causing this folks loss and now if I try it again I think this issue should be

resolved okay great so now you can see that this editing behavior is also Implement properly the last thing is I want to ask it to the view history so I will say great now it worked let's add feature based on instructions and let's try to run again okay again we're going to copy those Arrow messages

in Okay cool so you can see now the home screen became the calendar view and for each day I can click on scan food take picture analyze it and save this the problem now is that after I click save the log is not showing in history view so I'm going to give prompt after I click save for for M analysis the log is

not showing in the history list view what could be the issue help me add debug log to find the real cost and got build error again okay let's try it so this time I'm going to promp a stilling behavior no mail found after click done in history view is it because

data was not saved let's try again okay great so this time you can see that it is working with proper saving Behavior so this is my workflow of how to use cursor to do iOS development if you enjoy this video I will also make some content about how can you build Android app with cursor and Winger as well as

how to make beautiful IOS app UI using cursor so please comment below if you want to see more of this type of content meanwhile if you want to get the full prompt as well as cursor rules that I am using for this type of iOS application you can join the community that I'm building called AI Builder Club where I

continuously posting in depth content about how you can use Aid like cursor Wing serve to build production ready applications as well as large L model agents but more importantly we have this community of top AI Builders who might already experience the problems and challenges you are facing today so you

can just come to a community ask any questions and challenges you have as well as learn from others tips and tricks I have put the link in the description below so you can click and join our continue sharing interest in learnings and project I'm doing in AI if you enjoy this content please like And

subscribe thank you and I see you next time
