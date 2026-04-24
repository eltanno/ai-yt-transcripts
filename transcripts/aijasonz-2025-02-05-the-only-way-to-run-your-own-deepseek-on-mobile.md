# The ONLY way to run your own Deepseek on mobile...

- **Channel:** AI Jason
- **Date:** 2025-02-05
- **Duration:** 20:34
- **Views:** 17K views
- **URL:** https://www.youtube.com/watch?v=lxae1AJverg

## Transcript

deeps show really exciting paths to run large L model on edge device directly meaning we can actually run state of art model on your mobile device or even Rasberry Pi to Power Smart hardware and this is extremely exciting because so far for people who are building large Lang model applications one of the key

challenge is that large Lang model is not a fixed cost most of us can't really introduce a subscription model like $99 per month for unlimited amount of usage like traditional s and I learned this firsthand one year ago I launched AI companion type of product with a free trial of 60 seconds chat and this

platform does get user all the time but I just never make any money because cost generated from this large Range model and tax to speech model is just so huge I have to ear at least $13 for those paid users at least to break even and I think this is really exciting part about the ability to run local model on your

mobile device directly is that your pricing strategy became extremely flexible you can totally launch an application using customer own computing power to run and support some kind of offline use case as well that's why today I want to take you through step by step how to build a mobile app that is

running deep seek purely on customer's own device break that down from how do you calculate the hardware requirement for different models text app for deploy on Android and iOS app as well as a case study of how to build a deeps chat app from scratch first topic is how to you actually calculate the GPU needs for

different larg Lage model it's a huge list of Open Source larg Lage model but you might have a question can my device run it and is it going to be too slow I'm going to show you formula of how you can calculate Hardware requirement for any model but first need to understand how does larg l model consume vram

typically larg L model mean consume vram in two parts one is we're going to store all the model parameters vam and this will take huge amount of storage already apart from that we also need to store the activation memory so the way life ler model works is that it has multiple layers and each layers there are

millions of different parameters and each parameter is doing its own calculation so activation memory will basically store the calculated result from each layer so basically need enough vrm to both store the model and also support activation memory and there are factors that really impact your

calculation but as simple formula you can get a proxy of vram needed by doing number of parameters multiply by Precision divide by a and multiply by 1.2 number of parameter is normally what you will see on the model name and on hugging face you will see the model size here while Pres

is basically what you normally see here like F32 and fp16 and what PR is that at default as we know large L model consistent of billions of different parameters and each parameter is doing its own calculation to predict the best next work at default this calculation is normally done in 32 bits format in

binary which means it can represent a number like this but sometimes we do something called quantization instead of using 32bit floating points we can use 16 digits eight digits or four digits to rep this number even though it is not as accurate but it might be good enough and it's going to save a huge amount of

computing resource and this is what you see here represent so this model can be run either as a original 32bit flow point or you can run the Quantified version with 16 bits so when you try to calculate the vram needed for this model you have do 13 bit which is number parameters in bildon multiply 16

assuming you are running the 16 Quantified version divide by 8 and multiply by 1.2 so should probably have around 31 GB each vram and with that you can choose the right Hardware that you will need if you try to deploy this model and you can also use that to choose the right model for different

device and customer that you are trying to Target so iPhone 16 is around 8 GB Ram if you want to get more accurate there also tools and platform like vram estimator that give you more detailed estimations you can choose inference the prision type as well a detail model param and those detail param normally

lives inside the f. Json file in each model you can find on hiking face so this how you can calculate the vram based on your hardware and next I'm going to take you through how can you bring those model to your mobile device and build an app around it but before we dive in I believe for some of you one of

the biggest challenge after launching the app is getting customers getting your first 100 customer is very different from getting your next 10,000 most advis that focus on scaling is irrelevant when you're just starting from zero that's why I want to introduce you to this free free guide and action

plan from Sam and Shem if you don't know Sam and Shen they're running one of the most popular podcast called my first million where they talk about building and scaling startups and this guy include real experience tactics and numbers about how Sam and Sean start their different business from cloud

Sushi beer hunt and mil where they all get S to a figure exit this give you Inspirations about where to find your customer how to build your distribution engines and at the end there are detailed action plan which break down the pass from 0 to 25 75 to 100 and above for you to start getting momentum

you can click on the link below to download this awesome guide for free and now let's talk about how to build mobile application that run lar model locally so to run deep seek or other lar model on your mobile device typically depends on OS you're using there different Frameworks and apps that can support it

on Android the most popular one is called turmo and on iOS you can use a free m called mlx and at this stage it's very easy for you to build an IOS app with local large L Modo inference because of MRX but on Android even though we have turno you can't really package everything into a APK file that

you can distribute on App Store but you can still use that for your hobby Pur so I'm going to very quickly take you through how to use terx on Android to run deep seek but I will spend much more time on deep diving into building an IOS app with MRX so with termix on your Android phone you can basically install

all Lama and set up local API and point for large L model inference and then if you have another Android app you can call this API that host on your Android phone directly to do that on Android you can download terx from Google Play in the terminal first the type in terx Das setup storage this will open this new

page ask for file access you can click on terx give access to all files then go back and next you were typing PKG upgrade so PKG upgrade will update termax package to their latest version then you will do PKG install get S make Goen this will install the necessary tools including get say make and

go so after that this environment has been set up what do we need to do is to get clone the AMA so you can install AMA on your Android device to do the large Range model inference and then we'll do CD AMA to go inside the AMA folder and then we'll type go generate dot- dot do dot to generate code required for the

project and then do go build dot to build AMA binary in this build process normally is going to take a while so you can just leave it open but don't worry it is not stocked and after that we will do do/ server and to start AMA server in the background so that you can call Ama from

any other apps and with the server running now you can execute the deeps R1 1.5b model on your Android device by doing do/ olama R deeps R1 1.5b this command initialize a deeps R11 .5 B model and start processing your inputs and after it is finished now you have this command line interface where

you can just type a message and start chatting with R1 model on your Android device so here I type this one and you can see start outputting the reasoning tokens as you can see the speed is not the best because my Android phone is pretty old it's like from 5 years before but if you're using the latest Andro

phone the speed should be much faster but as I mentioned before using this approach of terx that means the user will need to have terx installed and set up the old Lama server so it won't be very easy for you to distribute your apps that require local lar models but on the other side Apple has this

framework called mlx that is announced last year it is a machine learning framework that's specifically designed for apple cicon and mpu it lets you run large L model locally on your device and this is a package you can just add to any xcode project choose and load a model and start inference so in the end

you can just package an IOS app and put on App Store user just need to download one app and they can run influence on their device that and this is what I'm going to Deep dive in I sure the whole end to endend process in the end you'll be able to build an IOS app that Run unlimited amount of deep seek for free

forever so to get start with building a large Modo power app with mlx as first they open X code create new per choose app give per name click next first thing we need to do is going to add MX package to your X code project you click on F add package dependency pay taste the GitHub URL of the MX Swift examples here

and for dependency rules select Branch type in main here and click on ADD branch and then it'll show you a list of different packages that you can use you can see it supports things like stable diffusion vrm which is visual language model uh but the one we're going to use is mlx lar language model so I will

choose the project that you're in and add package then we can start implementing this to use mlx to load AI model in your IOS app the step is pretty straightforward you're going to import the library that we're going to need and then choose the model to use if you go to MRX sweet examples inside libraries

mlx large L model llm model Factory you'll be able to see a list of predefined models that you can just give a name and we Automatic download from hugging face and one of them you can see it's already loaded for deep seek R1 7B model if you scroll up it is basically loading models from hugging face which

means you can load many more models that is on hugging face and I will show you how to do that but for the model that is already in the list you can just do model registry do model name and then we download and load the model on the iOS device thatl and that's pretty much it after that you can just give it prompt

and use container. perform or tokenize the actual prompt into Vector then we'll pass the embedded prompt into this mlx LM common. generator and the result will be stream on screen so this how you can round the AI model on your iOS device with just fiz code so putting them all together this is a quick code example

we're import the library and at top we Define two State output from L model and another is the user prompt and the default value will be this one and the way Swift UI works is that the content view file here is almost like the main homepage of your app and you can constract UI at top but if you want to

do some basic functionality you can do extension content view to just put the function here so the top UI part you can also most consider as HTML versus The Thing below is like the JavaScript code so you can say that at top we're Define text field for user to give The Prompt as well as button to generate answer and

once the button is clicked it will try to call this generate function which we Define below that is using the mlx and load model for inference and if you're not familiar with that you can actually use cursor to open the project file either open the project folder click content View and ask cursor to explain

code further or you can also create a cursor rules and just copy the code example that we just went through where it give cursor a little bit context about what MX is as well as a stepbystep process then just go to content View and give a prompt I want to build AI app that can run large Range model on iOS

device using MRX detail dock in dock Serv help we build a basic chat app that can chat with a lar Range model at the top user can select which larange model they want to use uh could be this list for them to choose and at bottom users can input a text box with send button once the message is send with stream

results on the screen render the whole conversation chat history and the UI should look great and following iOS guidelines and I'm going to to use agent mode and click enter and again you can actually put the whole thing in actual instruction. MD file and then we can try to run this and to build IOS app with

cursor you need an extension called sweet pad if you don't know what sweet pad is sweet pad is a extension that allow you to automatically build a wrong IOS app and it will output arrows directly in your terminal so it became extremely easy for you to debug with cursor if you want to learn more in

depth about how the sweet pad works I have another video showcase the whole end to-end process of how to build iOS with cursor that you can check out in my channel but with this one I'm going to choose the destination of the actual iOS device I have because it does require iPhone mpu so if you just try to run in

simulator it won't work and then I'm going to click on build and run the command line will be sent and give us Arrow okay it looks like the problem is that currently the app is set to require iOS 18.2 but by iPhone is 18.1 so what you can do is uh go back to X code select app that you are running in

inside here there's a minimum deployment I'm going to change this to be iOS 18 and also you will need to go to sign and capabilities change team to be an actual developer team so that you can run apps on your personal device and if you don't see any Arrow here that means that should be all good to go so or go back

to cursor and click again okay but we got this arrow and I think the problem is here that we should actually Define the model register do the model name so I'm going to copy the arrow and say build failed you will see that cursor sometimes have the wrong linked arrows identifi for IOS

app so I'm going to give some additional instruction build fil uh fix it but also you can ignore some of linked arrows and Link basically refer to small mistakes or potential issues in the code that might not necessarily cause error but can lead to bugs and normally we will have linked check they're automatically

analyzing the source code but for some reason cursor is not great at identify of some of the Swift linked arrows so I'm going to accept this and just try again okay we have few more arrows so I'm going to copy this in build arrows so this app is running and we can change to any model that is pretty fine

here I'm going to change to llama 3.21 B model in command line you can see that it start downloading the model for the first time we can Implement that message on the UI later as well it load the model and give me the response here the response is bit weird cuz I think it is not handling streaming well so I give PR

model is working great however we are not handling streaming well it is repeating content instead of showing the latest content help me fix this it says the problem is that we are pending each tokens decoded Tex directly to the C response without considering that the tokenizer might decode overlapping

sequence as well okay still the same behavior so so I'm going to give feedback still the same behavior as before help me add a log and understand what is the rule cost so it add new logs and let's try to run this again so now we have this new lck we can type in this is the lock help me

fix the issue this is why I always ask it to add lock because now it really help you to communicate the issue back to cursor and let's try again cool so this is working out next thing you want to do is actually fix the chat history so lar lar model actually has context about what has been

discussed before and we will need to construct a chat history as example this llama 3.2 prompt format it will start from the starter header you can trct system message like this and then insert the user message we start a head ID as well as assistant message and put together we look something like this we

need to Define some message types format for this chat history using llama 3.2 form and build conversation history so whenever you send a message pen to history three after log model generary response we also append this as part of the message what you can do is you can actually copy this instruction I have

into cursor just create something called chat history instruction so I'm going to give prompt this problem that each time we are influencing log Modo has no context about what has been discussed before now build a chat history ability based on this uh instruction doc that we're putting here so now let's try it

again uh I'm Jason don't say anything else just answer what is 1 + 1 and then I can ask what is my name so you can tell that it actually has a full context of past history so now it's proper chatting experience and now let's also try the deeps model so I'm going to select deeps model and the

type a message you can see the app crashed if that happen to you that's because running those bigger larger dange model require a huge amount of memory and what we need to do is that we actually need to adjust the project setting to enable increase memory so you can select the targets and then in

signing and capabilities click on capability search for increase the memory limit and uh just like that then you should see this option show up now with that one we can try to run again so I'm going to change to deep seek model again and then say hey cool you can see now the Deep seek model

is actually working as well where it is output the reasoning token and as you can see this disted version is not that smart even though responding to hey it will just spend so much token on syncing and output this message and later of course we can ask cursor to render the actual syncing token apart from the

final message but this is how you can build a large L model app that is using powerful local model like deep seek R1 with this you can imagine a lot of interesting applications you can build and the last bit I want to touch on is that sometimes you might want to run a new model that just released but not on

the predefined list yet all you need to do just loging a new model under the model register like in this example you can just create a new model Quinn 2.5 coder 7B 4bit that is pointing to this new model on hugging face under MX community so if you go to MX community hugging face you should see new models

coming up all the time all you need to do just copy the model pass here open cursor and in your app adding extension to your model registry just pasting the IDE here and for the naming convention keep it consistent for the tokenizer here we are choosing the pre-trained tokenizer this means it will just choose

based on tokenizer that is on the huging face model and all you need to do just adding this new one to the list here and if you run again wait for a minute for you to download so you can see this new model is also loaded so now I'm going to publish this app to App Store to do that first thing making sure you have a

developer account and choose developer account here click on Peru archive this will take some time and then have this app click on distribute App Store connect okay so we actually need to add the app icon first so in asss app icon just add some CH generated app icon and then product iar

again now I can go to develop. app.com SL account account to see the apps that I have uploaded K on the one that I just submitted provide screenshots and some basic information the URL SL the latest View and I'm going to choose a category and for contact right I choose this no third party content and age

rating and also manage compliance the Privacy URL I also need to choose pricing tier and submit to app review cool so normally it would take one to two days for Apple get back to you so just making sure you are monitoring this and respond back to any of the comments so that's

pretty much it this is one example of how can you build an IOS app with local larange model building you can try and download this app if you want to get detailed tutorial as well as all the prom and code example that was showed in this video you can click on the link below to join my AI Builder Club where I

have step-by-step code breakdown of practical project that you can use to learn how to build software with AI and I share new learnings and tips at w basis I put a link in the description below for you to join I hope you enjoy this video thank you and I see you next time
