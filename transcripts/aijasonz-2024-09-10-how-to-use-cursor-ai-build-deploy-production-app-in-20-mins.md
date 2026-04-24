# How to use Cursor AI build & deploy production app in 20 mins

- **Channel:** AI Jason
- **Date:** 2024-09-10
- **Duration:** 42:31
- **Views:** 216K views
- **URL:** https://www.youtube.com/watch?v=bAAbrhb3QoM

## Transcript

today I want to show you how can you use cursor to build not just demo but a production ready full stack application without any programming knowledge and I'm going to show you from id8 setup building front end backend o as well as deploy online if you don't know what cursor is it is AI code editor that

everyone is learned to use and adopt this AI native code Ator enable almost anyone to build whatever application that you want even a year can build a fullon web application in just 45 minutes and we already seen people build some really high quality production level application like video editor

Chrome extension and even crypto exchange and there are loads of video about cursor already but most of them are just showing you how to build simple demo instead of actual production ready application and that's why I want to make this video to show you full potential end to end and application I

want to show you is how can you turn any interesting AI model like this Emoji generator model into a web application when people can just type in any type of prompt and generate Emoji based on that and everyone can see everyone else Emoji they can like and download image and it has a full authentication flow building

as well where things are feature gated and this will have the whole backhand set up where you can keep track of every single Emoji generated as well as all the users you have so first thing you want to do is set up the project instead of getting curs to create a whole web app from scratch we can utilize Library

like nextjs or react which will make development a lot easier and I will also utilize UI component Library like sh C in where they provides loads of beautifully made UI components that is ready to use as well as twin which is CSS or style libraries that will make the code a lot easier to read and to do

that I will go to the chn SEL nextjs and there's one command L that we can use to set up the nextjs project with chn and tellin so I will go back to cursor open Terminal and do MPX CH in at latest initial it will ask me whether I want to proceed I will type in y and enter and then it will ask me whether I want to

set up a new nextjs project I would type yes and the name of the app will be Emoji maker and'll ask me what kind Style I want to use I would just choose New York which kind of more condens View and then the color scheme you can just choose whatever you want I will just choose neutral and CSS varable for

seeing I will click yes so on the left side you can see that it created a folder with bunch of different files and while I'm doing this I know it's quite confusing as we throw a bunch of different terms to you but at high level the things we mentioned so far like JavaScript and typescript are the

programming languag just like python where tab script is like an upgraded version of JavaScript where it has extra safety features to catch mistakes in your code before you run it making sure you don't accidentally break something react and nextjs those are the web application Frameworks that helps you

build web app faster it allow you to break down a complex web application into different components nextjs is variation buil on top of reactjs where it optimized for the web application speed and things like chassi in and tellwin those are just UI components or style libraries where they

already have a bunch of pre-build UI components that you can just use and grab instead building from scratch as well as CSS styles that has been predefined and in the end when I use mpm or MPX those are just package manage command line code that allow us to download those package and if you open

the project folder you can see this ton of different files has been created already this might feel quite confusing and overwhelming but this is kind of common structure of nextjs project look like so the app folder is normally where you define all the pages of your application page. TSX you can consider

as your like index.html or the homepage and the library folder is where you can store some kind of utility functions will create a components folder as well to store all the kind of UI components that will be reused across Different Page and a bunch of other files that you don't need to worry about that now and

you can already try to run this and first thing you want to do is actually just open the nextjs project folder instead of root folder because otherwise cursor can always confus about where they should create certain files and to do that you can either close this window and open the specific sub folders or you

can click on the bar at top and do install cursor command which is first one if you click on this click okay type in your password and then now you can do cursor Emoji maker which is a folder name here and click enter and now you can see that it opened the actual specific project folder now I can do mpm

run def so this command line is defined inside package.json where it has this ST which is next St and this basically means that we start the developer server to try to run the web location on your local machine so if I click enter you can see nextjs project has been set up properly but one thing to know for sh is

that at default it won't add all the components into a project RL you actually need to select and add the components that you want to use so you can either do MPX just at the latest add the component name the outlay or you can go to terminal open new terminal do MPX chass in at latest and click enter then

this will show you the list of all the components that can be added and you can just move to the one that you want to use and uh use space button to choose those the one that you want to select I want to add the button card and input and click enter so now you can see a components folder has been automatically

created and inside components folder this UI folder it has import all the components that we're going to use so now our project has been set up pop okay finally using cursor to start building out the web application based on your requirements but before I get into this I know many of you just getting started

with your programming and AI development Journey or try to figure out what does a road map actually look like that's why I want to introduce you to this free ebook as an introduction to JavaScript because JavaScript is a main language that you need to learn and master to build web applications which is type of

application that is easiest to distribute and this ebook is introduced by hopspot who is sponsoring this video in this ebook it will cover all the fundamentals of JavaScript and objectoriented programming in general including basic syntax and Concepts how do you define classes method and build

complex Logics into your application as well as some more advanced tips like how to manage different type of Scopes and even comparison of some most important and popular Frameworks it'll also show you example of good code and B code with practical code Snips that you can just copy paste in so if you're just getting

started and want to fully utilize tools like cursor to build out your dream app I definitely recommend you go and learn some basic understanding of web development and this is a great place to getting started you can click on the link in the description below to download this ebook for free now let's

get back to how can we use Cur cursor to build out this whole web application and to do that we're going to use the cursor composer which is really powerful feature that can interact with your project folder directly and has context of your whole project file but instead of giving direct simple instruction like

help me build this we application what I commonly do is I will create a kind of prodct requirement doc where cursor can use as a reference about what are the key features that it needs to build so I'll create a requirement folder and then inside requirement folder I'll create a uh markdown file first called

front and instructions so I tend to get a cursor try to build a part of the application progressively and inside instruction folder a structure I normally follow is that I will give a overview about this project so it has context about what I would try to achieve and then I will have very

detailed feature requirements uh and in the end I will also include some relevant documents for either API end point that we're going to call or new library that you're going to use cuz quite often the model didn't have access to the latest documentation for different librar that you going use and

in the end I'm going to tell the model about how does the current file structure look like so that it can create files in the right place and I would explain this part a bit better soon so for this project I'm going to use a model host on replicate called sdxl emoi this model will be able to

take in a prompt and then gener Emoji Style file so I'll come back to the project file the project overview I just say use this guide to build a web application where users can give text prompt to generate Emoji using modo post on replicate and then for feuture requirement I will tell you we will use

next.js chassen Lucid which icon Library they're going to use and super base which is what we're going to use to build up the backand and clar clar is Library they're going to use to build up the user authentication and then create a form where user can put in prompt and clicking on button that cause a

replicate model to gener Emoji having nice UI animation when the Emoji is blank or generating display all the images ever generated in Gra when hover each emoj image an icon button for download and icon button for like should be show up here you can see that our basically talk about which library that

I want it to use and then detailed uh requirements about what kind feature interactions that the user will have and here normally you want to be as specific as possible after that there will be relevant docs so since we are using this model I can go to API Tab and then copy the content in the uh node Jaz and

create a subsection how to use replicate Emoji generator model then pasting the documents so the model knows how to call the endpoint as well as all the input that is necessary in the end I feeling this section called current file structure this is actually quite important I found that cursor in general

is not that great at understanding the file structure and quite often it can create files in wrong place or not really following the file structure that I'm following here I'll take a screenshot of the file structure on the left side and then I will open the chat on the right side past in the screenshot

and ask it to help me generate the file structure and I will do command enter so that it can rate the whole codebase as well then you can see that it generate this whole file structure for me which is extremely useful so I can just copy and paste in here and also in the end I will enter specific rules all new

components should go into the/ components folder and name in specific format and all page should go into the app folder and with this context cursor should be able to create a files in the right place so now I can start getting the cursor to build up the whole project and while I'm doing this you probably

notice that cursor can actually take in image as input as well which means I can actually add in a figma mup into this project as a reference so with this one we basically have everything that we need and the last step is I will create a new file in the project folder called env. loo so this is where we're going to

store all the credentials like replicates API key and you can get replicate API key after you create account if you haven't install replicate yet you will need to do this mpm install replicate so I open Terminal and paste it in and now we can use cursor to start setting up the project I will use

command I uh and I also select page. TSX then say help me build the whole Emoji maker app based on the instruction so I can add instruction macdown file that we created earlier as reference and the UI needs to similar to the mup so I can reference a image file as well and then I can click enter so you can see that it

create two new components one is called Emoji generator which has form that allow people to point in the prompt and call replicate model as well as Emoji grid which will display all the Emojis ever created also create a folder called API inside that called generate Emoji folder with route. TS which will call

replicate model and in the end it also show show you what are the next action that it think it should do like create backend to store a retrieving emojis uh Implement download functionality more styling so you can use this to keep prompting the model to build more and more features but first of all let's

accept all okay looks like this the arrow it seems that we didn't put use client in emoji generator to debug this you can either give the arrrow message here and click enter but quite often I found it's better to actually use the chat UI for this because cursor will automatically start creating files and

sometimes it will messing up versus in the chat I can actually control things a little bit better so in here I can see the part of the arrow out is the Emoji generator or go to components Emoji generator. TSX putting the arrow file here and then give a prompt call this Arrow what will be the rule cost sync

step by step and the command enter it will give you very specific explanation about what is going on on and what issue and in the end it will give you this uh resolution so all you need to do is basically go to the emote generator and at top add use client so use client is basically a kind of TX set to indicate

nextjs that this file has some functionality that need to be wrong on client side instead of server side so the next J know how to render this application and optimize for Speed and if I save this okay so now I have a new Arrow but looks like the same issue I just need to go to Emoji G

and do use client okay so now you can see this app UI looks very close to what I want it has this place where I can put in prompt it have button where I can click it to generate Emoji which assume we're called replicate model it has image grade which will be used to display emoji and if I hover those ones

it will show me a button to download so this is awesome even though Emoji here is not display populate because I believe currently just put some placeholder image now let's give a try so our put in Doc and click enter so it has this nice loading State as well okay so we got this Arrow uh and we're going

to do the same thing just copy everything and then paste in the arrow in the end I will say I got this Arrow after calling replicate and generating Emoji what could be the root cost let's sync step by step so I do found that this kind of chain of s definitely help in terms of solving accuracy so I almost

like to adding this instead of getting it to solve that right away and command enter again it will start analyzing the root CA this Arrow so the main reason it Arrow out is because we are using a special kind of image component from next.js but at default for security reason nextjs only serve image from

trust sources only so to resolve that we actually need to go to this next. config MJS file and adding replicate as one of the trusted source so I can just copy this and paste in at replicate do delivery as a trust domain and save this now I can go back to the Local Host refresher page and do this

again okay great so you can see the image has been generated and display here though one thing is that the image didn't look like a Emoji so wonder why okay I notice that inside the promt it normally have this prefix a took image of something so maybe this what's this missing I will go back to cursor and I

think that part is down in the general Emoji ru. TS so all the actual external API call will be under this API folder So currently it will be called prompt let me change this add this prefix a token Emoji of save this again and I'll refresh the page and put a cat and generate again okay great so now it's

generating actual Emoji Style but one problem I found is that the newly generated image didn't really add to the image grade so I can go to cursor and ask to add that but before I do that I will just go to GitHub and add submit basic layout plus called replicate model successfully commit and push then I can

go to cursor and and open the composer tell it the functionality of generating emoji is working however the newly generated uh should be added to the image grade what will be the steps what will be steps to achieve this functionality let's sync

step by step so first we need to create a share State and then update the Emoji generate components to update State as well as update Emoji Gade component to I display the image based on State and here it is using a state management Library called zustand uh so I just do what it told me to do do npm install Z

stand okay it has been done so I will accept all got this Arrow again our copy arrow and paste in okay so looks like I need to update the next confit MJS file again or just copy and save I will also try try to rebild the project as well so I will do contrl c and mpm run def okay got

another arrow and I can actually just copy this whole Arrow message here and paste in I got this Arrow after running mpm run def help me resolve it so I will paste in here so it basic change the requir to be process false and save it again and then and do mpm wrong dep okay so now let me try doc okay great so the

new image will be showing here and also added to the image Gade and if I add another one now you can see that all the image will be added to the image grade automatically and next we just need to implement the two last feature one is download image as well as like image but again the same thing I go to GitHub and

add a commit display image grade po play I will go back to the cursor composer and then skip prompt now let's implement the feature for download image and like image so clicking on the download icon button it should download image to low computer and clicking on the like icon button it should Auto turn the button to

field style to indicate that image has been liked by this user already and also increment the count of number of likes which is what display at the bottom so I will click enter it update the Emoji store file to increase functionality the count likes and inside emoj grade it Implement download and like

functionality and I will click accept and go back to the Local Host try to run again okay so after image generated if I click on the download button it'll open this download if I click save this image has been downloaded perfect and if I click on like you can see that the likeon has been updated and if I unlike

it it will reduce the number of likes perfect so all the core functionality has been created I'll push this implemented like and download and next thing we want to do is that we want to set up the user authentication which means people will need to sign up to use application and

then I can also build credit system or a payment system to actually charge the user there are few ways you can build the user sign in and offlow super base also provide default o integration but you still need to build our lot of UI yourself that's I'm going to use Clark which kind of outbox user management

platform that you can integrate into a system very easily and it support all sorts different all mthods and this process going to be pretty standard across all s different web applications so I'm just going to show you how you can do that you go to Clark and create account there and then it'll ask you to

create application give it a name called Emoji maker and they provide also different sign options outo Boxx and then I click on create application then we can just follow instruction here first we need to install the Clark package so I'll go back to cursor and then do

mpm install Clark SL nextjs and then I'm going to copy the credential and put into env. loal and last part is that we want to create a file called middleware dots so middleware you can consider this as piece of code that will be around every time whenever some kind of function is going to be called and this

is commonly where we Implement authentication because otherwise you want to implement authentication and feature gating on every single piece of code default one they provide here is pretty basic so I'll copy this and go back to cursor on the root folder I'll create a middleware dots file um and

again you you probably can also just copy paste the whole documentation into a markdown file and ask cursor to do that but consider authentication is pretty standard one across different type of web application then I will just show you how we can do that so now paste this in this is pretty standard one if

you don't understand specific part code you can just highlight this code and add chat then it will explain the code to you but at high level whenever any URL arounde me those patterns then this middleware code will be R but at moment it didn't really gate anything so I'm going to update code a little bit here

first I create a mat for what are the page that want to be gated for only sign up user and add default and point to every single page but you can also change it to get only specific Pages then I will write logic that if the user ID didn't exist and they are try to visit to those typ agative page and I

will redirect them to sign in and after sign in success L I will want to take them back to homepage and on the other hand if the user ID exist then just proceed to next action and next I also want to create a component where it will show sign in button if they haven't signed in and profile component if they

already signed in so I'll go to components folder and create a new file called headers ttsx you look something like this again you can just highlight this code add chat to get cursor to explain code to you last thing is I will go to the layout. TSX import two things Clark provider which is thing that can

enable Clark for us as well as a header component that we defined earlier and to activate Clark is actually really easy we just need to wrap this HTML Under the Clock provider and that's pretty much it clock will automatically handle everything else the last thing we want to do is insert header component here

and save so now if I try to access Local Host again at default it will automatically take me to the sign page sign to Emoji maker and I can sign with Google or email address and after I log in it will take me to the actual app and on top right corner I have this profile icon where I can manage account or sign

out so the authenication also working last thing we need to do is connect the database and storage to super base so that you can keep track of each user how many credits they have what kind of emoji they created and for each Emoji how many likes have been added for the backhand we're going to use super base

so super base offer complete back end for both mobile and web applications it was created back 2019 as a open- source fire B Alternatives before s base the two major ones people use are Firebase and AWS amplify both works but the problem is that each one of them will lock you in a specific vendor from

either Google cloud or AWS that's why superbase was built and got popularity very quickly and they offer four stack backend that cover both database authentication file storage and even vector embeddings and their database is built based on postcat which is one of most advanced open source relational

database they offer frontend SDK to connect to all those backend service quite easily for different web and mobile application Frameworks if you haven't built any backend or database before this might sound challenging but it's actually pretty straightforward to get start with you normally try to

figure out what kind of data table you actually need to create so almost think about you have some Excel file sheet to store all the necessary data for your application to run so in our Emoji maker I basically need two tables most of the time you will need a users or profile table to store all information about

each users and for each user you will need to think through what kind of columns of data that you will need uh for like user ID which pricing tier they are on how many credits do be left and stripe customer ID or stripe subscription ID if you want to implement the payment regarding all the emojis

that we have I will need to store the ID the image URL The Prompt that has been used to generate Emoji the number of likes as well as a user ID of the Creator and for the image J we will use superbase storage to store all the image files to start setting up the back end we'll create account as super base first

and after that you will create a new project give a name Emoji maker and put in password and click create and after you create it you can click on comeet button and go to app framework we will copy this credential into the env. Lo file so step we're going to take for this Emoji maker is that we firstly

create relevant super based tables and buckets and then implement the backand feature one by one one is for connect and create the profile table Po from Clark and the second is we want to upload image to the storage bucket so that we have image URL that can be accessed then we will set update emojis

table whenever user generate new emojis or whenever they update likes button so first let me set up the user table there are two ways you can do that one is you can go to table editor and click on a new table and they provide nice UI for you to uh give a name like profiles and then Define all the columns that you

need like the user ID tier which can be tier and for each column you can Define the data type like for tier I will choose text and you can also Define the default value so at default it will be free and in the speci settings there is norble which means whether this field is optional and for me this field is not

optional so I will uncheck that as well as credits so if each user you only want to be able to set let's say three credits then you can set up a credit like this and again it shouldn't be normal so you can create table using UI like this but what I would recommend is you

can go to SQL Editor to set up the table there so here I can paste in this SQL code where it will create table called profiles with user ID which is primary key the credit at default will be three the tier default will be free and can be both free and pro the stripe customer ID and stripe subscription ID in case later

you want to set up payment and the date will create it and update and I can click on and then it will return this message success no Road post return if you go to table editor now you can see a table has been created with user ID credits tier subscription stripe IDs and date if you want to add new column you

can just add a new column here as well and next we want to also create Emoji table so add a new one emojis the ID which is the primary key and the ID will be automatically generated the image URL the prompts the likes count the Creator user ID as well as create a date and I'll just click okay so it succeed as

well and you can see the Emoji table has been created and the last thing I want to do is I also want to set up a storage so storage is where we will upload all the image OS I will go to start and click on new bucket and uh give a table and give a name emojis and in my application I actually want the image to

be public accessible for everyone that's pretty much a setup and next thing is that we want to prompt the cursor to set up backend features so inside requirements folder I create a new backhand instruction where I give a per overview the TX stack we're going to use as well as section called tables and

buckets that we already created so that the cursor knows what does the schema look like and this is where you can just basically copy paste a SQL query that you use in super base here directly and there have requirement section where I will list out all the backand functionality that I can sync of and

there are few functions one is create a user to a user table so after user signning about Clark we should get a user ID from Clark check if the user already exist in the profile table if it didn't exist then create a user in the profile table if the user already exist then proceed and pass on the user ID to

the functions like generate emojis then we also want to upload emojis generated to the star bucket and then add a row to the Emojis table we want to display all the images in the image grade as well and also Implement like interactions and in the end you can add some documentation as well but super base is

pretty popular so I didn't need to add too much things I was just adding this one as example and then click save and now I will go back to layout. TSX and then do command I so I'll give you this instruction of building Emoji maker web application front end based on MD Now help me build the backend feature based

on backend instructions let's firstly set up the create user to user table syn through steps to implement this let's sync step by step and then click enter now you can see that I create a new API route to handle the user profile creation and verification and it also create a component called user profile

initializer which will check Clark and see if the user already signed in if so then continue to verify the user and also add this component to the layout. TSX um but here's one arrow that looks like it forgot to add the used client um so whenever this type of issue happen you can either just ask in the chat but

this one is pretty straightforward you can just go to the user profile initializer and add use client and this another arrow that that model not found and to resolve this Arrow again you can just copy arrow and into chat and let AI tell you how to resolve this one but this one should be pretty

straightforward we just need to install the super base so I will click on new terminal and install the package so this time I can see the app is running successfully and the user is log in so let's check but there's no user actually created in the profile table and we want to understand why so to do that or go

back to terminal and you will see this Arrow it look like it is something around the clock and again I'll just copy this file in and then pting the arrow I got this Arrow help me sync sir what is the rule cost and how can I resolve it it looks like we are importing it wrong so I will

copy and PAs in this okay and now it looks fine and if I refresh the page you can see that this user has been created successfully and if I log out and log in again with a different email address and this time you can see a new user has been signed in and if I go to the table a new user will be created so user

authentication part is working and I will do a commit connect Clark to super base user table and next feature I wanted to implement is upload Emoji to Emoji super base storage bucket so tell it great next let's implement the second requirements based on the backend instructions let's sync step by step and

I will add root file to this and enter so it did a few things it first create a new route for General Emoji with functional to download image upload to sub base get a public URL and then add a new row to the super base emojis table and also update the Emoji generated TSX component with this latest code so I'll

click accept and the only part I found is that it remove the prefix I added before so I will add it back the to Emoji of the prompt and click save and now if I add a new one and generate okay looks like there's some arrows so our again go to terminal and copy paste the server side Arrow into chat but I can

see the arrow is the same as last time I actually need to use the superbase service row key which is what do you have here then this key will be able to bypass all roow level security and I we adding this service row key here and if I refresh the page and try to generate a new Emoji okay nothing show up here but

if I go to super paace you can see that this is one emoji file has been created with this file URL and if I go to storage emojis you can see exact Emoji file has been uploaded here great so this part has been working I make another commit upload Emoji files to super base and now we just have two

features left display all the image in emoji grade and likes interaction I pretty much do the same thing help me implement the insert requirements for display all image in EM Emoji grade let's sync step by step so firstly it create a a route to fetch all Emoji data from superbase and then it update Emoji

grade uh components and also update Emoji generator as well as the main page so let's accept it okay now I get this Arrow which I can copy paste into the chat I got this Arrow after loading the page help me find the rule cost and how to resolve it so this is arrow that normally nextjs for safety purpose will

only load image from trusted URL so what we need to do is basically go to uh the next. config MJS and modify this part let me try again okay looks like the image that we created in the table didn't really display here so I will need to go back to the composer and ask it in super base emojis table I

can see there are one emoji entity however nothing is shown on the UI let think step by step what is a rule cost and how can we resolve it so this time just add a bit more console log for debugging so I'll just accept out for now and refresh this time it actually show up so so that's great and will try

to generate again so the new image has been created and display here if I go to super base the new image also display here that's great but one thing I found is that it somehow removed the like and download feature which is annoying and it also didn't display how many likes it has and also it has kind of weird

counter at top so I'm going to go to composer and tell it looks like it's working however some features and UI are tweaked help me fix things below one when hovering the image card it should show two icon buttons one for download image one for like at the bottom of the image it should show prompt which is

left align number of likes returned from the Emoji table right Aline and thir is that remove the total count and I will also add the backend and front and instruction file here so it has some additional context and accept all okay perfect so the app has been updated with prompt and number of likes and when I

hover it the two button will be showing up I will commit this as well add a feature for displaying all emojis from super base last but not least I wanted to implement the like interactions so great now help me implement the last uh backend function likees interaction based on the backend instruction here so

it create new route for the like interaction and update the Emoji grade component to use this endpoint so let me accept and refresh page if I click enter I can see a number here increased if I go to subbase you can see that the likes count increase here as well the only thing is that in here that user can like

the same image multiple times which is not what we want so I will give the feedback one user can only like one emoji once after after the Emoji is liked the like button should be toggled to active clicking on active like button will decrease the number of likes so it figure out that we actually need to

create new table called Emoji likes which makes total sense now we go to subbase and create a new quy and run so a new table should be created here and then it also ask me to create a new subbase function so I copy this and uh round this okay and then I will click accept all and go back to our web

application so now if I click like I can see the state has been added and if I go to the table Emoji likes it is also updated here so if I like two of those emojis it'll add both records here however it is not displaying the number of likes properly so I will need to give it more feedback I can see the Emoji

likes are updated correctly in super base face however the Emoji grade is not displaying number of likes properly the number disappeared after I click Like help me fix this let's sync step by step so it looks like the issue is in handle like if I go to handle likes and copy paste this latest code in replace the

old one save this and refresh page okay I can see that number is displaying public here and if I uncheck that it didn't have any if I check it again now this time I will come back with more specific behavior so notm only the more specific can be the better so the issue is when I load a page the number of

likes display properly however after I click like button the number of like disappeared help me fix this let's sync step by step so now it spit up a bit more information but as you can see this is why I normally prefer to do debugging in the chat UI instead of composer because uh if I doing composer then the

composer chat history will be filling with all those debugging information uh versus in the chat I can just clean up pretty easily if I copy paste Chang in then you can see that it has been displayed properly each user can only like the ones and number will be displayed on the bottom right corner

okay this perfect and the last part you need to add is some sort of Time Out setting so in verel environment at default the time out is quite short and this will cause some kind of weird behavior that it failed to actually create image so you want to add this to some of the endpoint that would take

long time to fetch like generate Emoji so whole app is running now I can add that implemented like feature the last step we want to do is put this app live and the easiest way to deploy the nextjs app is using verel so you can create account on verel just loging V your GitHub and then create new project

making sure upload the latest code to GitHub already and I will choose this Emoji generate cursor I need to change rot directory to be the Emoji maker project folder and I also need to put in environment variables which is everything that you store in env. Loco and click on deploy this will take a

while and normally you will have some sort of Arrow which we will also use cursor to kind of debug okay so I got this Arrow this weird it looks like I haven't really installed replicate so I just install it add to package and then push again okay now I got a few more arrows easiest way again you just copy

paste everything and put into the cursor chat where it has context about the whole code base we should remove this variable that has been declared but never used to something like this and then in the user likes also remove this line to be something like this because the request was never actually used and

then in the Emoji generator we remove this import that is never used all right so I update everything based on instruction and then add a new commit add a fix and remove um on used Imports and with cursor every time you publish a new commit to the main branch it will automatically redeploy and you'll

probably just have more and more different arrows that you need to go through and you might wonder why the application works when you're running on your local host but has so many new arrows when you deploy it that's mainly due to difference between local and production environments ver might use

different node ja version different file assistance good thing is that process of debugging is pretty similar you can always just come back and then adding Arrow code here into chat and get a cursor so I can either copy paste or just click on apply and accept everything click save and commit and

we're just going to repeat this process a few different times and quite common is like type arrows where versel prefer us to Define very specific types instead of any so now the department has been successful I can click on vit it will Tak me to this app so at beginning since no one log in I will log in first then

it will take me into this app that we created earlier and it's 4 functional user can generate new emojis or like dislike download imag so this kind of whole end to end process of how can you build an actual production application with both front end backend authentication deployment with cursor

and as you can see I'm not a front end developer but I was able to build such application in just less than hour and there are lot more tips I want to share as I use cursor more and more and if you want to dive deeper into what we have talked about today you can join my AI Builder Club Community where I have

step-by-step detail code breakdown and prompt of every single example that we mention in this video where you can just copy paste the code directly and share question and challenge you have in a community of all the other AI Builders who might already experience the problem that you are having now you can click on

the link in the description below to join the community today and if there are any other type of cursor tips that you see can speed up this process even further please comment below and let me know I will continue sharing new interesting curs tips about how can you build production applications for your

dream app so please like And subscribe if you want to keep update thank you and I see you next time
