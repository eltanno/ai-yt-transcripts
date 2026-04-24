# "Make Agent 10x cheaper, faster & better?" -  LLM System Evaluation 101

- **Channel:** AI Jason
- **Date:** 2024-06-04
- **Duration:** 27:42
- **Views:** 20K views
- **URL:** https://www.youtube.com/watch?v=MGkByeDm-90

## Transcript

if you building AI products probably a great amount of time is actually not programming but literally staring at the screen and waiting for lar model to finish off task and pray to lar model God that everything goes well but quite often it doesn't there are millions of different cases where your large range

Modo system just didn't work or say something stupid and this problem becomes bigger and bigger in later stage after the large L Modo system goes into production majority of my time actually starts spending on evaluating monitoring testing because real world cases are really Dynamic and unpredictable quite

often when we build a system there are few task case in our mind that we are building towards but once it goes into wild customer will tell all sorts of different requests different ways like I was building a meeting scheduler agent where I was expecting requests where people say things like let's meet

tomorrow 9:00 p.m. s time but in reality the case would be much more complicated where people would say I'm basing UK but travel to Singapore next week and B China the week after once your L modor system actually put into your customer's hand it is almost guaranteed to break or perform really weirdly in certain cases

and this is when you want to start iterating the system and iteration of large range Modo system is extremely timec consuming because there are lots of different combination of things cuz large L model is not deterministic which means the result will be slightly different every time and there are all

sorts different combination of different settings like the prop itself the model you're using the temperature and how you break down the flow if you're building a agent do you use function calling agent or use react framework and most of the time your large L model system is not just one large Lage model call but a

flow of different lar model steps or agent who can autonomously decide what to do next with different tools so the biggest challenge is when you change one thing you don't really have a good confidence that it is actually going to improve the system for all the cases like you might put a special PR as

banded solution to solve a specific edge cases that you just capture but this prpt might actually make large Range model pay too much attention to this spefic spefic part of task but start ignoring some other parts of prompt so to gain real confidence you do want to test system in many different type of

cases and that's why live L model system evaluation is such a big topic it basically means how can you build a system to evaluate the performance of a large L mode system against the certain tasks so that you will have a benchmark to know if your new version actually improved and most importantly help you

find the optimal combination of all the different settings and system design for the specific task that you try to complete and there are huge amount of public EV valuation or on the Internet which is useful in some way where it give you a overall idea about which model is probably the best in certain

type of General task but quite often it is not that useful because the task they test is not exactly the task you want so most time I can't really trust the result from those public evaluation that people are sharing because I know almost certain when I test different models with my own system the rank will be

totally different that's why it's important to actually build your own custom evaluation process most rful one that everyone is doing is is human evaluation which means you basically look at a log of the large Range model system output and just eyeball the result to see whether it is good or not

and if you are a bit more sophisticated you probably will set up some logging system like Les miss or phix to have better interface to log and review every single step in those SL Range model system in most of cases human evaluation is still the must have and best thing to do especially while you're building the

system but the problem is once your system goes into production the volume of different cases to Monitor and evaluate is so big so it's almost impossible for you to do human evaluation on every single case anymore otherwise either you or the system going to break that's why the concept of use

large Lage model as evalu interesting and important and the idea here is pretty simple instead of getting human ibing the result to decide if the system is delivering good result or not we can build a large L model evaluate complete same evaluation task so that it can handle huge amount of volume and scale

very well and sometimes the evaluator can not only be just large Range model can also be code to write down some hard code rules and do heric evaluation like if the code generated has Arrow or if the answer or exactly match Mass formul so such a automated evaluation system is critical to launch any production level

lar Lang model system but it is not always clear how to build such system especially how can you build such large L model evaluator that almost as good as human to decide if a system is performing well or not that's why today I want to share a bit about how can you build such a large L model evaluation

system so you can really speed up the creation speed and increase the level of confidence for both you and your customers but before we dive into this I know many of you are going through a career change or looking at starting your own AI career but have you ever thought about how to leverage AI to land

on your next dream job so hopspot did a research about how the new generation of job Seeker are utilizing different AI tools or platforms to streamline their workflow and to be much more effective add job hunting process and they share a collection of all sorts of different AI platforms and St UPS in this job hunting

Market from how to script and collect all the job information using AI to find ones that suit you the best to craft a standout application that catch the eyes of recruiter and hiring manager using AI as well as simulating the interview process with AI so people can feel confident even before jumping on the

actual interview to even salary estimation to get a good understanding of how much it actually works so this was quite a refresh for me to understand two things one is all the possible ways that you can already utilize AI to help you land on next dream job and second it is also a good way for me to understand

what does AI stack look like for the job market which definitely inspired me a few different business idea that we can potentially build help job Seekers so I definitely recommend you to download this free report about how people are land on dream job using AI you can click on the link in the description below to

download this report for free now let's back to how do you build a evaluation system so there are few steps you will need to choose a metrix that is most important to your system and then you'll build a valuator that that can actually provide evaluation result based on this metrics and thir is optional but really

important you will also want to prepare a golden data set that you can use to really test and recalibrate your evaluator to making sure it can deliver the human level performance and after that you can start testing different system variations and compare the performance so firstly choose the right

metrix for your larange model system this is the first and most important step so you want to choose a metrix that you really care and most time the way I look at it is after doing some eyeball testing I start getting sense about which part of system can often break those are normally the ones that want to

design some kind of metrics around it to be able to get a benchmark and evaluate against for example if you're building a rack system two parts you probably care the most one is a retrieval whether your system actually retriev the relevant knowledge base at first place and second is Generation does a large damage model

actually generate a result based on the information provided or did actually hallucinate and if those two are most important things then you can design some metrics around those two things so you probably have metrics of contextual relevance where input will be the user quray as well as a retriev documents so

that we can decide is the retrieve knowledge actually relevant to the question second part will be faithfulness to test is a gener answer actually granted by the data that it retrieve or did they actually hallucinate different system can have really different metrics for example if

you are building a customer support chatbot where even though the majority of system are very similar to a rack system but you probably in this case also care about the realtime ux cuz you can almost always adding more kind of steps in the flow to improve the retrieval relevancy as well as

generation quality but you actually don't want to sacrifice the user experience and getting user just waiting for a long time then you probably put a latency metrix as well which is how long does the whole system to generate result for the cury if I'm building a research agent I probably care about couple

things one is this agent able to do as much of research possible to gather all the information relevant and second is whether the final report generat are actually grounded by the information collector and if you're building a kid tutorial app you probably have some special metrics is the answer provided

age appropriate so the key Point here is that the metric is very diverse and it should really look at which part of the system that often break or unstable and you really care and design a metric around it and when you design metric there probably different things you'll be thinking about for example you might

put a numeric metrix like getting large L model to provide a numeric evaluation for from 1 to 5 or you just getting a model to generate a binary classification is the answer correct not and the large Range model can only up output correct or incorrect you can even get large Range model to generate two

different outputs as well as some combination but from my experience the large L model is not really great at numeric evaluation it often fail to give very precise or Parada based evaluation but when we get lar model to do binary or even multi output it is actually performing really well so I often almost

go for the classification or binary type of evaluation when I use aary model and after you choose the metrics the next step is actually build a evaluator so you want to build a evaluator system that can actually evaluate the performance of large Range model system just like human to do that you will need

to decide two things one is what will be the data input that this evaluator should get the input can be as simple as a user query plus the output of the large L model system we can also include some reference data set if you are preparing a data set that with a predefined list of task that has ground

trues so the evaluator can use that to compare on the other side the input can also be the result of specific step like knowledge retrieval instead of the whole large L model system then the evaluator basic need to generate output which is evaluation metrics that you defined earlier so if you're building a rack

system where you want to measure the retrieval accuracy then you will have evaluator that the input will be the user query as well as a retrieve data and the evaluator will take this to input and generate output which is r classification that can either be relevant or irrelevant actual evaluator

here most likely be a prompt template that you have designed like for this one it can be simple as you are comparing a reference Tex to a question and try to determine if the reference Tex contain the information relevant to answer the question and here's a question this reference text and now compare this two

result and output only relevant or irrelevant you can give very specific description about what this relevant means and what this irrelevant means on the other side if you're not building a rack but actually agent that should follow specific process then the input can be the system prompt that you give

agent that contain specific soop or process that it should follow plus the full chat history that agent generated it can give those three different things to the evaluator and output the metrix to be whether the agent actually follow the instruction that it was given and second whether the agent actually

complete task and sometimes you can even get a to Output reason as well so you can understand better if the agent is not following the instruction which part did it Miss if I'm building a comy search agent where I want to test whether agent has ability to gather as much information as possible then input

can be the company and list of data point is should research about as well as the final result that agent generated pass on all those things to the large L model evaluator and output if all information gathered is yes or no and this is a problem that I used for this evaluator it will basically pass on all

those inputs and then say evaluate result from the research system decide if the system found answer to all data point per the answer can only be yes or no so how you design evaluator prompt really depends on the metrix you pick up at first place and the real question here is how can you making sure this

evaluator prompt actually give accurate evaluation just like you do so that you can have confidence in the result provided so that's where the third step is quite important to prepare a golden data set so this basically means you can prepare a list of testing case which including both input and output as well

as what is a correct evaluation result for example once you have this data set then we can basically still run evaluation by taking the input output and generate evaluation result but then you can compare this evaluation result to the correct evaluation result and decide if this evaluation is correct so

you're pretty much creating evaluation system for the evaluator itself you can run multiple different cases on this evaluator with your golden data set to get understanding about how accurate this eval is and the question here is how do you get this golden data set so there are couple of different ways the

most straightfor ways would be manually curate data so you can just create probably a small set like 20 50 or hundreds of those manually create data sets where you can just give the correct evaluation result as a reference but on the other side after your system going to production you will actually start

getting a huge amount of real user lock and with system like LMI or Phenix you can also go to those system look at user log and manually annotate your evaluation output as well and that's why in system like chbt they will give you some sumbs up and some down button to provide feedback if you're just getting

started you can even try to use large Range model to generate some data set as well for example if you're building a rack system where you want to really push the retrieval accuracy you can actually get large model to generate a bunch of different cases by loading website and gener list of questionable

and output result but no matter how you get this golden data set the idea here is you can evaluate your evaluator iterated it to a point where the result is pretty accurate so that in the end you can actually put a life and start testing against different variations of your system and compare the results

between different system in terms of the metrics you define the latency and cost and that's pretty much it this process might sound a bit curious but in reality it's actually very easy to set up with system like L and phix I'm going to give you a quick example of how can I create a evaluation system for a researcher

agent that I just created so I want to show you example of how I build a evaluation system of a web research agent that I built before all the details and source code in a different video so you can check out if you want to dive deeper and the key things I really care and want to test a lot is

about the research agents's ability to gather as much information as possible from different data source so the metrics I Define here is the info Gathering whether the agent actually found all the necessary information that user requests from internet so I'm going to show you a step-by-step example of

how I set it up and how I use that to compare the performance of using the old GPT model versus the new GPT 40 where they actually deliver better performance with cheaper cost so to set up there are really four steps first we want to use assistant to actually log the user request to your large model system and

there are multiple different platforms you can use com like L Smith or there also open source version like phix where you can host yourself and once you set this up you can start all the user requests and build a data set out of it by annotating result and then we're going to create the evaluator to deliver

the evaluation result so that we can start evaluating against different models and variations and compare the result so that's it but firstly the setup of logging system and the one I'm going to Showcase is SL Miss and the reason I I choose that is because they kind of have the both evaluation logging

and annotation kind of connect together which make this process a lot easier so I'm going to go back to my agent scrier project that I did last time which is basically agent that can receive a website URL as well as a few research topics and then this agent will go to the company website to research all the

possible information there and if nothing found it also go to poate internet to find more information and as I mentioned before I've demonstrated the source code another video which you can check out if you want to learn more but this is basically the agent I created before and as you can see here actually

didn't set up any tracking and to setup tracking is actually very straightforward so the way lens miss or any other logging system works is basically you can add some special decorator to the function that you want to track by adding this add Tris B before your function and they also

provide some help function to automatically track all the large range REM model core as well so all we need to do is just add this tras bow cre to every single function that we want to track the first step is we want to install lmus if you haven't installed that yet you can just do pip install L

Smith in your comen line after that you will need to create API key and then copy API key to your file one for L chain API key and also you will need to turn on this lanching Trac in V2 to be true so that it will start tracking and if you want you can also Define a specific Ling project that you want to

log all the information and at the four all the data will automatically go to to default project if you haven't specified yet and once you did that we can go back to our researcher. P file and firstly import two libraries from last miss one is traceable another is rap open a so I want to replace this open a. Cline to be

rap open a. Cline so all the lar ler Modoc code will automatically be loging LM and then for every single function that we want to track we can add add trable decorator so for the scripting function I can add this add traceable and you can define a couple things and one R type it can be tool it can also be

large L model basically the purpose of round type is identify them differently in the lens myth so some of will be large langage model some will be tools and at default will be Chang as you can see here each lck here has a different name this is name that you would Define here we can basically do add trow round

type equal to Tool and name equal to script I'm going to do the same same for the internet search function so just before this function I will add this Trace round type equal to Tool and name equal to internet search same thing for update data also add to this chat completion request as well to track this

agent chat completion for this help function where it is to log the information in my command line I don't really need to track this so skip it memory optimization I also want to track it so I just add decorator traceable name equal to optimize memory as well as call agent and same thing for the two

different steps tro name equal to number one website domain research and the number two internet search in the end the last one traceable for run research that's pretty much it after I set up all those traceable next time when I run this researcher agent it should automatically log information into L

Smith I can open Terminal to python researcher. py I can say start running okay so the agent has finished running on my end now if I switch back to LMI you can see this new session show up already and if I click on that you can see the four traits of every single steps agent did to complete this task so

firstly there will be a WR research which is top level function that we tracked here and then the first stage is website domain research which is one of the first stag that we track here called number one website domain research and inside that you can see every time when a certain function has been called it

will be automatically tracked from the agent chat completion and optimized memory I can also click on the top level number one website domain research to say the output of the first stage is that it didn't find any information on the website domain from Discord that's why trigger the second stage of the

internet search in the end it found the result for every single field eventually so that's pretty much it from this point every single time when a user have a research task the information will be automatically logged into the system from there you can actually start creating a data set that can be used for

evaluating the system so you can see there are two options here one is add to data set and another is add to NQ so n Play basically allow you to give your human evaluation result to create that golden data set set probably you won't see any metrics here yet because you haven't really connect any metric to

this project but once you set up you can actually give your human evaluation but on the other side you can just add this to data set as well so data set is basically a collection of different cases that you want to test including both input and output you can create a new data set let's say grab scraping

research agent click crate and you can also make change to the input and output here as well if you want and then click submit then this testing data set has been added for you to test later and if I switch back to data set tab you will see this new data set called Web scraping research agent if you click

inside this one example here from your user lck and you can basically just repeat this process to look at all the user lock and pick up the good ones that you want to use for testing later because for each one of those data set you can actually create evaluators so lesm miss do provide some U for you to

create a new evaluator you can choose some of the template that they already have but you can also create your own but I'm going to show you how can you create in the code direct so in our case as I mentioned before the key things I want to test is does this agent system collect as much information as possible

for all data points that it requested and for that purpose I will just create evaluator to test just that whether all data point user request has been collected so I'll flip back to our python code and first they import two new libraries one is evaluate this will allow us to run evaluation let's say you

have a few example in your data set the evaluate function will basically run your latest lar model system against this data sets and do the evaluation and we also import lens mist of schemas to import Rong and example so Rong means the actual output from your L model system example is where you can get the

reference information from the example data in your data set and then our first create a function called research evolve with inputs so first we will try to get a few inputs from the test data sets one is entity name website data points those are basically the input variables we have in the testing data set which is

website entity name and data points to search and then I'll do the wrong research function that we create above and return the data points as output then we're going to create the actual evaluator so evaluator I'm going to create is all data collected check and we have two input one is a wrong and

another is example so we need a wrong to get actual output from the lar model system with be and example will allow us to get the reference output as well as test case inputs so we'll get all those relevant data company data points result and gr choose which is reference output then we will put together a system prop

like this so I basically just pass it on both the research task the result from our research system as well as reference result from the human researcher and ask it to evaluate if all the information has been collected it can be either yes or no and then I basically use a model to do this evaluation and here I did

actually use the same model that I was using for the large L model system which normally is not the best practice most of the time you do want to use a different model to do the evaluation but in my case I'm actually not testing the model itself I'm actually testing the output of the whole agent system so I

still use the same model just for convenience and in the end I would do a transformation if all information found is yes then our set score to be one otherwise our set score to be zero the reason I do this is because in L Smith what the Matrix that number will be able to give us a overall score across all

the test case for example in this specific one one out of four case actually succeed and all the out three cases fell so it gave me a average score 0.25 so this quite useful to get a summary of the experiment and in the end I will output key to be only INF for Fone and score to be a score we output

and so far I couldn't find a Best practice about how to Output multiple different Matrix cuz unless seems like one evaluator can only output one score but if there any other good ways please comment below and let me know in the end I'm going to start a evaluate where I will put a system function that we going

to run to first par the data Cent name which is the one that we create here the evaluator point to the function that we create above and experiment prefix as well as metadata and that's pretty much it so first I do want to run a quick benchmark test with the model I was used before which jpd for Turbo and I will

open the terminal and run the script so you can see the agent start running which will take a while but if I flip back to LM miss you can see that there's a new experiment show up here called GPD 4 Turbo and if I click inside you can see all those two sessions are running in real time and showing us how much

token it consumed and how much money it cost on large motorite and if I click on this view Trace button it will show me the four Trace up to this point now you can see that the evaluation has finished if I switch back to the lens Miss so result you can see from our very small testing cases is one case succeed one

case fa and I can click on The View Trace button to see the result so test is basically I ask agent to search three piece of data about Discord about a certain company one is whether this company provide catering to the employees how many employees do they have and what different office locations

are and the result is that the agent didn't really find whether the company provide catering but it does find the number of employees as well as office location the other case is the same list of dat points but different company safety culture and this time it successfully find the company actually

offer in House Catering to the crew for breakfast lunch and snacks and there are roughly 696 employees and six office in total across those locations and you can see evaluation result also reflect that so the safety culture all info find is one versus Discord all info fun with zero and if you want you can actually

click inside and copy paste whole input so now we have this Benchmark about the GPD terrible performance with our system as well as latency and token cost and you can see that a roughly cost from $1 to 1.6 so let's say now we want to test whether new model gb4 actually improve the performance and ideally with cheaper

cost as well so I can just move up and change the GPT model to GPT 40 and run this test again so GPD 40 test also finished and if I go back to the last miss you can see this new one called GPD 40 experiment if I click inside great so both of them actually succeed if I click on the first Discord one I can see they

actually find some specific information for every single piece of information we need and I believe the overall cost to complete task is going to be lower as well cuz we can click on this add button and compare with another experiment we did in this case it would be gpq for Turbo so you can actually compare side

by side with the similar cost for Discord case the gbd 40 actually cost a little bit lower but completed task successfully and for cic culture test case they both complete tasks but gbd4 turbo complete task with much less cost and if you want you can even do another task with let's say GPD 3.5 turbo let's

change the model as well as Max token all right GPD 3.5 also finished and actually finished really fast the question now is did it actually complete task so so if we go back you can see that GPT 3.5 just completely Miss Mark even though it's extremely cheap and again we can add a comparison with all

the other two variation we just did to do this pop you probably need at least 20 or 30 different test case but you can see how powerful this one will be for your iteration process you can just change some combination and run the experiment to get understanding about what's the real performance of your

latest iteration across multiple different testing data set and if you know any other interesting evaluation system or best practice please comment below I'd love to try out as well I will continue posting interesting AI knowledge and projects I'm doing so if you enjoy this video please can

subscribe I will see you next time thank you
