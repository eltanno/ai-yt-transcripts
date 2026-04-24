# This is how I scrape 99% websites via LLM

- **Channel:** AI Jason
- **Date:** 2024-10-29
- **Duration:** 22:44
- **Views:** 381K views
- **URL:** https://www.youtube.com/watch?v=7kbQnLN2y_I

## Transcript

today I want to show you the best practice of how to script internet data at Big scale and even build a gentic web scripper that can interact with browser just like human to complete web scraping tasks on upwork autonomously so web scraping is one industry that is dramatically disrupted by AI especially

in 2024 traditionally loads of internet business especially like aggregator or e-commerce will spend huge amount of engineer resource on just scraping data from internet to making sure the price and offer is most competitive and the way they normally do that is that they will mimic the web browser and make

simple HTTP requests to the URL and get the HTML back then have real specific parsing functions written down to map out which Dom element contains the information that they want so it is very specific in custom build per website because each website structure is different and whenever this website

structure change the previous script will generally not working that's why this company spent a huge amount of engineer resource in just building and maintaining different scraping systems but apart from those big internet company if you just go to freelancer website like upwork and search for web

Scrapper there are huge amount of job postings every single hour where business want to hire someone to build a specific sripper that is really valuable to them and the use case across multiple different categories from Lee generation Le research or they want to Monitor and analyze competitive pricing doing market

research getting job listing and many more so there's a huge amount of longtail use case that small and medium business are after but couldn't really find a good cost effective solution before but with the latest development of large L model and agentic system the cost of building such web scripper has

been dramatically decreased in fact you can actually build a gentic scripper that can satisfy most of those upward tasks which just friction of time and cost of what it used to be and today I will take you through some examples of how can we complete some of the task here I would break that down into three

different buckets from simple and public website to some of scraping workflow that require very complex web interactions so first let's talk about the public and simple websites those are the websites where it is not gated by authentication or payment think about like Wikipedia page or different B2B

company websites those website traditionally is really hard to script because the structure is just so Dynamic so each one requires some kind of custom build still and this kind of first thing that large Lang model really change the game because it introduce two capabilities one is the ability to

extract structure information from Massy unstructured data which means you can just feed large Lang model Massy row HTML and it is able to race through hosing and extract useful information out of it and with open AI structured output feature this type of data extraction became really reliable you

can just Define very specific data structure that you want to capture and it will be always 100% follow that structure and on the other side apart from data extraction you can also utilize agent reasoning ability to build more sophisticated scripting behavior for for example if you're doing a B2B

company research sometimes requirement and flow is a little bit more vague you just have a company website but you don't know which specific page contains the data you want but with large langage model's agentic Behavior you can actually build a web scriper agent to be able to given website and then navigate

through multiple different pages until it find the information that you want and eventually aggregate all the information together so this type of large Lang model based scripper agent is really powerful but does that mean the web scripper problem has already been solved by this well not exactly quite

often you will have websit that require complex web interaction to get the information that you want for example a lot of news website will require subscription loging to get the content out and you might also have popups on the website that stopped you from getting the content not to mention all

sorts different antibond mechanism like capture and for some data it just require multiple different actions to gather result you need and for this type of website we need a way to really simulate the human interaction to be able to get data out and this is kind of second type of use case that I see those

are website that it's a bit more complex but the process of getting that data can be pretty specific and repetitive and this type of use case actually C for 70 to 80% different use case that I saw on upwork and I'm going to show example how do we do that in the end there are certain type of use case I see they

require not only the web interaction simulation but also complex reasoning tasks for example the user request here will be more vague like find me the cheapest fly for the next two months to Melbourne or buy a tickets of a specific concert within specific budget and time period this type of use case will

require much more sophisticated agentic reasoning ability and it is a lot more experimental from my experience but there are also platform that are experimenting this type of Frontier use case I'm going to take you through my best practice of how to implement web scraping for each individual categories

so first let's talk about best practice of scraping the public and simple websites as we mentioned before with help of open AI structured output feature we can extract structured information from the RO website HTML it also Builds an agentic system that can navigate through multiple Different Page

to get the information that you're looking for so before 2024 most of people are just feeding the row HTML to large L model and often it does work but because row HTML has a lot of noise the result can be inaccurate and also you will spend a lot more since it is burning more tokens but this year we

start seeing emerging of different service that is providing large L model optimized web content this category of service was started by fire CR so if I give the website URL instead of returning Ro HTML it can turn into markdown file that is a lot more human rable which means it will be easier for

large L model to consume as well and now there are few different players and service that providing this that's aimed to dramatically optimize web content for large Lang model and agents so apart from file C there also Gina Gina introduced a Raider API which is doing very similar things but what's really

interesting about Gina AI is that if your volume is small it's basically free to use they have API that do even require authentication you can just go to any website add https and add r.g. a and this will automatically turn the website page into a markdown format just like this it's pretty insane that you

can just use this for free without any kind API key I don't know who is paying the bill but unless your volume is bigger They Don't Really charge you and on the other hand there also a platform called spidercloud so when when I was putting file C and Gina into production I sometimes got a problem that there a

spike of usage Gina and filec it were just Arrow out and couldn't return any website content but spidercloud support script 50k pages per minute which is kind of insane amount of rate limit and on the other hand even though the content from each service are all marked down but there are still slight

difference for example I try to use both service to script a local restaurant near my place and you can see the result it returned from different service are slightly different you can see that filec has 116 lines of markdown file and Gina is 59 lines of markdown while spider cloud is 68 lines of markdown

from my observation FC tend to Capt as much information as possible from website there's a Gina API try to really focus on the main TX content itself and spider cloud is somewhere in between it will try to Capt link and also turn into really uh kind of human readable markdown format so in general there are

some different difference in terms of content return as well you can choose the one that suits you best based on use case and in the end they also cost so the cost per 100 page scripting as we mentioned before G is basically free Spider cloud is around three cents per 100 page and file cor will be around 6

cents per 100 page if you are on the highest here and here example agentic scrier I created before where I can use file C to get the marketown data from a website and then use GP model to exract specific information that I care about and it is able to race through multiple different pages to get the full manual

items across website into Json data like left side and there are more kind of features you can optimize for this type of agent like optimize how the agent memory should be stored so that it can script bigger and bigger amount data and remember what URLs it already script before so that it won't take the same

action again as well as integrated with new data source like llama PDF passer or EXA search if you're interested you can join my Community where I have ready to use agent template for web scraping and research with detailed code breakdown so feel free to click on the link below to join my community and get agent template

so this is the first type of website that is public and simple where you can simply build agent to scripts the content and next is this website that is not that simple and require some kind of complex web interactions where they might have pop up the blocking the content or require loging authentication

or you might need to interact with pagination to get the full content to deal with this website we need to mimic a human interaction with a web browser and to simulate those website interaction it is commonly done by package like like selum pop tier and playright those package are initially

designed for web app QA testing but now can be used for those agent scrier but hard part of building a gentic scripper that can simulate Webber interaction is how to locate the right UI element to interact with for example if you want web agent to be able to type in the search box for your location you need

effective way for the agent to communicate with web browser which input is the search box and some of the website can be even more complicated like this login page of LinkedIn it has three different sign in button so if you just simply give large L model the whole web page and ask it to extract the right

UI elements to interact with it often didn't work and this where I found a package Called Agent ql comes really handy the basic building model to be able to identify the right UI elements to interact with as well as the right Dom that contain the information that we want so that we can give the WR

instruction to play right to simulate the web interactions and this allowed us to do a whole bunch of web automation like close different sorts of popup window and cookie dialogue as well as logging website that require authentications all I need to do is just using their SDK and pass on the UI

elements that I want to get back with natural language and to Showcase how can you fully utilize agent ql to build such web scraping I saw it would be interesting to Showcase how can we deliver the scraper for some of upper workk job here so this one from three weeks ago where they want to build a

scripper for a website called ID list which looks like a job market for nonprofit and volunteer work and they want to pull all the jobs that has been advertised every week and get a big list including the or name job title salary so that they can easily sort by type of role and location to help clients do a

better job in terms of setting salaries if I go to idea list uh you can see this website actually required you to log in to use the populate so I we quick create account and loging firm also has a bit kind of anti-bot practice with a I'm not robot checkbox and we were also showcase how can you gu through that as well and

after we get into it it has a list of different jobs with pagein naations so we need to learn how to use agent ql to extract the job detailed data here and navigate through different page ination so to get started we can create a account engaging ql and first let's download their Chrome plugin to get a

sense about how does it actually work after we install the extension we can go to the website that we want to script and open the inspection by right click now you have new tab here called Agent ql we need to put our API key here which you will get from agent ql website and now we can start experimenting so we

just need to pass on query of the items that we want to capture for example if we want to get the number of jobs results I can just put something here called number of job post total and fash data then you will see that it return the data 3,258 which is what do we have here but

on the other side we can also Define array as well in this case I can Define jav posts and putting the array symbol here and inside each job post I want to know about the orc name job title location salary contract type and remote type and for some of the items that might not be self-explaining enough I

can add further description as well so for contract type I can Define fulltime or contract or parttime and click on fetch data below that you can see the result extract all the job post on that specific page with company name the job title location salary and contract type remote type so this plug-in allow us to

just debug and test what type of query can actually work and return the result you want on the other hand we also want to test whether they can locate the whole login flow UI elements so this time I'm going to try login form email input and continue button so it will be useful to give a structure so that agent

ql will know that it need to get the continue button within the login form instead of or any other buttons so let's try to fet web elements okay great so you can see that it return two UI elements one is email input one is continue button successfully so this looks really promising now we can start

actually go to the python to build out the automation that it can log in to the website so I start at GitHub rippo and open the folder in cursor let's firstly install agent ql so I will set up a new virtual environment first so since I'm in cursor I can do Comm command K set up new python environment then it will

automatically generate the command line for me or enter so now we are in this new environment and first thing I will need to do our will copy this to install agent ql and initiate the project and then I'll create a EMV file in here I will put the agent ql API key as well as the email and password for logging the

ID list and after that I created scripper py or import a few different libraries we're going to use and then load the environment Val Ables that we just put in here so first we want to build a script that can look at the email input and type in the email input then click on this I am not robot

checkbox and click on continue to do that I first Define the initial URL as well as query called email input query so this will requir a login form with email input and continue button you can see that I didn't really include it I'm not robot checkbox because at the beginning that UI element is not showing

up on the screen so we actually need to create another one called verify Curry to get this verify n robot checkbox so now we can try it out I will start a web session first in play right and then start a new page with agent C firstly do page. go to to go to URL and then try to Curry the email input form then I will

ask you to put email address into the email input field wait for 1,000 milliseconds for the verify human UI element show up uh then we're going to quy that specific element then ask AI to check that I'm not robot checkbox to see if it works works and in the end click on the continue button to login so let's

try it out I will save this and then open the terminal python scripper py and looks like I need to install the EMV so I can again open the command K and give Arrow message no module name. EMV and C submit and now let's try to run this okay I got this Arrow uh looks like I need to install play right so I do play

right install and again play right is a library that we're going to use that can simulate web browser sessions okay now the installation is done let me try to run this again so you can see that it open a new browser and also locate the email input and type in the email address and after

the I'm not robot checkbox show up it try to select the checkbox and click on the login button next the password input show up so this is working and it's actually kind of hilarious that it is able to click on the I'm not a robot checkbox either so if you're building website don't rely on that as a

mechanism to antibot so I'm going to add the last query for this login function called password input now try to query the password input F in the password there wait for a second and click on continue button and in the end it will wait for the loging to finish and after that I will also add something called

browser. contacts uh storage state to save this login State as a file that we can load in later so that we don't need to repeat this kind of loging process again again and just for demo purpose our ask on waiting time in the end so we can see the result so again in type in the email address click on I'm not robot

button click on login the password click on login again great so it has log to this platform successfully with my password and email and you will see that this a file called IDE list login. Json which will start the login state so that we can load in later and I'm just going to wrap this whole thing under a

function called login and start a new session for the main function to script job posts and then I do if the file didn't exist then call this login function if it does exist then we want to load the file directly so we don't need to log in again now we load the state and then go to the URL which is

something we Define here to job posting page so that's pretty much it and then we're trying to call this function that we just Define here now we can build the rest of script to get the full job posting content across multiple different paginations so I create two new query one is job post query that we

tested in the Chrome extension before another is pagination query because we want to get the next page Button as well so the agent can go to next page and then our first setup status equal to true and get a current URL before we click on the next page button and we firstly try to get job posting data from

agent ql and after getting that data we also want to get pation and click on the next page button and after we waited for finish then we'll check if the UR L actually changed cuz if the URL changed that means we are not at the last page yet so it will continue going until we script every single page so that's

pretty much it we can try to open Terminal and python squ per py in the end for the job posting data I also want to save it to air table or Google sheet so I'm going to add some new credential for air table inmv file which is API key base ID and table name if you're not familiar with air table API you can

basically create an air table base ID is basically this part of the URL and table ID is the one after Star Wars TBL so you just need to copy these two things over and then go to the Builder Hub create new token given name agent ql add scope we will need the write and read and access to the full workspace and can

copy over the API key and put in here then I will import a new package called py a table if you haven't install that making sure open Terminal and do pip install then Lo those credential in and we're going to create a one function called push data to air table where we will take a list of Json and save the

data to this air table and then we're going to go to the main function and call this push to air table function um that's pretty much it so you open the idea list and should be start scripting and meanwhile just let me open air table to see things side by side whether it start adding information okay great so

on the right side you can see the information is automatically pushed in while some of them salary seem to be empty uh but looks like there are some jobs actually didn't have the satary data that's probably why and and once the one page is finished it will navigate to next page and keep adding

new data in until you finish all the pages so this a pretty dope automation that it's actually pretty hard to do since it Touch model different parts and the best part is that the script we build here can automatically apply to other job posting websites because process and workflow going to be very

similar where it will do the login and handling the pagination to script is a full job posting data and what you can do after is just schedule a job every hour or every day to keep updating the data in the aor table but this is just one example you can imagine there's so many web automation you can do like

collecting and comparing pricing data from different e-commerce website and many more so this is the second category of those complex website but has a pretty predictable and known process as I mentioned before this second category publicated for 60 to 80% of different jobs and requests that I saw people

posting already but the last category is those type of scenario where users request is a bit vague not a very clearly defined step-by-step workflow for example you might wanted to go find the cheap is fly for During certain period of time for you so this type of workflow is much more complex and requir

some kind of reasoning and planning ability to decide where to go next and from my experience this type of workflow is very hard to do but there are our companies are exploring those kind of Frontier workflows and the best one is probably multi- own whereas they focus on building those type of web agent that

is autonomously operating the web browser for example I can actually go ask to book a ticket for me and complete the whole workflow so I can just copy this URL over and then say book is a ticket for me so you can see it automatically choose the Vue and date click on next button go to this ticket

selecting page and it was able to select a ticket and adding a ticket for me as well at top and move all the way to the bottom and you can see they try to find the next button but for some reason stuck there okay and eventually find the next button click on it and then start at this page so you can see that this

type of fully automous web agent still have long way to go to be super useful but it is actually pretty impressive it is able to go through mod with different hurdles of this webform and they also offer an API for you to use as well so there are loads of opportunities most of people didn't realize how easy it is to

build at moment those are my best practice about how to use agent and large Range model to do the web scripting in 2024 but definitely recommend you go and try out on the other hand if you want to dive a bit deeper into this topic or have some specific question that you need help

with you can go join my community where we have full detailed stepbystep code breakdown of those different type of web scripper agents with ready to use templates that you can just copy paste plug and play and more importantly you can join a community of other top AI Builders who might already experience

problem that you are having now so you can just post and get some help or continue posting interesting AI experiments I'm doing so please like And subscribe if you want to get update thank you and I see you next time
