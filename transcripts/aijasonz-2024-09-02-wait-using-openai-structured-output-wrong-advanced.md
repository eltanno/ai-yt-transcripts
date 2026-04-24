# "Wait, I'm using OpenAI Structured Output wrong ?!" - Advanced Structured Output tutorial

- **Channel:** AI Jason
- **Date:** 2024-09-02
- **Duration:** 20:27
- **Views:** 33K views
- **URL:** https://www.youtube.com/watch?v=YtBEc6yZCkQ

## Transcript

most of people really missed what can you do with 100% guaranteed structure output from open AI so open AI released this new feature a few weeks ago where they promised 100% guaranteed performance for structured output and this just totally changed how I develop AI application for example if you're

building AI agents as the agentic system became more and more complex it is really challenged and painful to get agent perform consistently so one out 100 time agent might behave totally different and this structure output feature is going to really help and change that it is basically a feature

that going to G and force lar orang model to Output the result in specific data structure which kind of promis a lot of interesting use case like enhance the reasoning ability by forcing it to syn step by step extract data from unstructured information or even dynamically generate UI based on the

user intent but getting large langage model generating specific Json output is not really any New Concept what's really mind-blowing was open AI promised 100% guarantee for the output structure score with the latest GPD 40 model but is this actually that good and when should you care to use it at all so for the past

few days I've tried to experiment with different ways I can use this structured output feature and explore different use case including web scraping for very complex data structure building generative UI application as well as a gentic application that can automatically finding the highlights of

video and Str shorts clip so I'm going to show you with my learnings what worked what didn't work and when should you Leverage The structured output feature but before I dive into this I know many of you are building voice related lar model application and one challenge you might find is getting

extremely accurate audio transcription in multiple different languages that's why I want to introduce you to assembly AI they are leading speech to text model provider they can provide extremely accurate transcription for both audio and video whether you are dealing with English Chinese French or even Spanish

and it does more than just transcription but also out box audio intelligence like automated topic detection summarize the content as well as speech recognition and it's extremely easy to getting started they provide SDK that you can use right away and my personal favorite is that they allow you to Define Cosmos

spelling for domain specific words that is not that well known like I can Define special words like land graph and land chain and then the transcription will be able to to identify those words accurately and if you're building realtime AI System Assembly AI offer low latency realtime streaming it is

extremely fast and you can get things transcribed as they happen I have put a link in the description below where you can click to get $50 worth of credits for free and I also utilize assembly ai's accurate transcription ability to build an AI video editor that can turn any long YouTube video into small shorts

you can jump to that to get example of how can you set up assembly Ai and now let's get back to open AI structured output firstly let's quickly talk about how does it actually work and why is this such a big deal as I mentioned before getting large L model to generate structured output Is Not A New Concept

because real world scenario is full of structured data if you are building a large L mode application to automate data entry and data extraction work it has to follow specific Json schema so that you can put them into a CSV or database on the other hand if we are building a gentic software where it need

to interact with different Sy to call those apis we also need to making sure the answer follow specific API schema and people also found structured output means structured reasoning so you can not only get large Lang model to think step by step you can even teach it to think in specific ways and process by

defining the specific key in the output structure and previously we kind of hack our way through by adding specific prompt about the data structure that we want in the Json mode and there are also open source Library like instructor to enable large Lang mode output of structure data more reliably with

mechanism like retry if it didn't generate intended result at first attempt but the problem of this existing approach is often that it is not 100% reliable there will be one 100 time it will output something not following the specific structure I Define especially when the data structure becomes more and

more complex and this is why this 100% guaranteed output score is such a big deal and to achieve that it was not just based on model the mention no matter how much they try the GPT 40 Motel itself can only achieve 93% in their Benchmark and to get 100% guaranteed performance they took a deterministic engineering

based approach to constrain model's outputs if certain symbol like Curly bracket has already been used then the curly bracket is no longer a valid token to be used and this is exactly the constraint that they add to the model so they turn every Json schema into a specific grammar the large langage model

has to B and their inference engine will determine which token are valid to produce next based on the previously generate token so it is really interesting approach they're taking so how exactly can you use it basically there will be a field called response format where previously you can only

pass on Json object type but now this response format can take in specific Json schema and inside Json schema you can Define very specific data structure like in this case you want to extract person where each person will have a name email and account ID and there are two ways you can Define the structure

you can either writing the whole Json schema like what you just saw earlier but you can also use a library called pedantic and pedantic is one of the most popular open-source data validation package on python pantic library is initially used to solve the problem where in Python there's no concept of

static type which means each variable can be any type of type like string or integer at any given time and this nature of lack of type it's good in a way that it make it really easy to getting started but also causing a lot of problems later on like you might pass on a variable value to be string while

the expected value is integer but with pantic you can create specific data structure and for each view you can Define the data type and even add description so that you can add more rules and requirements about how you want this data to be added it's very extendable to create more and more

complex data structure by wrapping different Panic model together and can also limit specific options certain key can has and pan model will automatically validate if all value has been generated in the required format and there also Advanced usage where you can build custom validator if certain field not

only follows certain types but also customer rules that you can program to get more deterministic Behavior like making sure the account ID or the price tag generated is within certain range so as a quick example I can create a panic model called person with name email and account ID and for each field I can find

the type as well as adding a description to further prompt lar langage model about how this data should be generated and you can also put a custom validator here to check if the length of this account ID is not four digits then Arrow out and then all you need to do just set up a response format to be this padan

class that you define and run it so if I run it here you can see it return me the format in exact way that I want it as a contrast you can remove this description and generate again and this time it will aor out says the account ID must be four digits so this this is how the open AI structured output works and next we're

going to dive into when should you leverage this structured output feature to build a much more reliable and Powerful life Lear Modo application I'm going to break down into three different categories complex data extractions and boosted reasoning ability as well as building more reliable a gentic workflow

so firstly complex data extraction and web scraping one of the most wonderful ability large Lang model provide is that ability to extract structured insights out of unstructured data like website content PDF file or even books and people can already use large langage mode even Json mode to do simple data

extractions like looking a website and getting the company name address City phone number pricing and this structured output function obviously going to make this simple use case more reliable but when it really shine is those complex data structure like if you want to scrip a e-commerce website where it can be

hundreds of different products and each product can have information like product name rating pricing material and sizes or you are scraping a restaurant website where you want to extract the manual item and for each item you want to GA the name ingredients and price so for this type of complex data structure

with huge volume it is typically quite a challenging task for lar langage model to deliver reliably and consistently and this is the first thing I want to test out to see if it delivers the relied promise so I quickly set up a stream L web app where you can take any web URL and extract data in any specific type of

format you can Define above our showcase full code of how you can set up this PO app in the end of video so you can jump to that if you want but as a quick example I want to scrip some restaurant menu data so I passing on a small restaurant's website it can has loads of different items for food wine and drinks

you can see here there probably around uh 50 to 100 items so it will be pretty challenging for the normal L Lang model I would Define data model where it a menu for each manual item it will have the name of this item the ingredients that goes into this dish as well as price and each item can have different

type of price by different type of size so it's a fairly complex data structure if I passing on this URL to the Stream app and click script now you can see that it extracted four manual item and for each manual item it has name ingredient size and price where size will be optional fi and we can quickly

verify if it's correct so the first item here is garlic bread which if I go to this webside the first item is garlic bread two pieces $11 and that's exactly correct and the last item is this canal which has Roda and pistach with $8.2 so if I scroll all the way to the bottom it is also exactly correct so this is doing

a pretty good job in term ofing large Mount of content but if you want to scrip something different like e-commerce side or car dealer information you can just load a new website and then change the data model here and this time the model will be a list of different products with product

name description location price and list of imag and all we need to do just passing on the different data model and if we compare side by side with the actual website you can see data is correct with the right name right price right per description and captured every single car on the page and second

category is improving large Range model reasoning ability so most of you probably pretty familiar with the tactic of chain of SCE if you ask large Range model to sync step by step large Range model can generate much better result the problem using chain of sort is that it basically output a huge amount of

reasoning steps together with final answer so to get the final answer you normally need to go through another data extraction or another large L model step to get the final answer and this additional work for my opinion can't stop developers from adopting chain of s for many tasks that could have been

optimized but with the structur output you can force SL Lang model to generate list of reasoning step first and only after that try to come up with the final answer and you can just grab the final answer directly by getting the value of that key it became extremely easy and simple to set up those additional

reasoning steps to improve the quality and you can even teach the large Lang model about what are the steps to think through before they come to the final answer as well and last but not least how can you leverage structured output to build more reliable agentic workflow the best practice of building AI agents

kind of switch from a free form agent where you just give a list of tools and letter figure out what kind of process to follow more towards kind of flow engineer type Paradigm where humans do control and Define what are high level steps and process but use large L model to make certain decisions at speciic

points to decide which speciic sub pass to take and to have this type of workflow Works reliably you need this ability for large L model to Output only specific answers for example you might want to build a marketing agent where it were take a step of generate the block first then go through a large langage

model step to say if the content is align with what user is requesting if it pass then go trigger the web flow to publish content if it fail go back to the previous step to regen generate blog again based on the feedback so with this structured output format we can define a pedantic model where it'll firstly do

some reasoning to create ticket block content then come up with a conclusion which can be either passed or fail because structure output format is 100% guaranteed this means this flow will also be 100 guaranteed reliable so now I'm going to get into details about how can you build three example L Lear model

applications from web scraping automated video and AI as well as dynamic generated a UI based on the user intent so the first example I want to take you through is a video editor AI I basically want to build an AI video editor that can take any source of YouTube video understand what does this video actually

talk about and create multiple different shorts that represent the core highlights of this video and hard part of building such system is actually identify the right timestamp of highlighted clips and this is where the open a structure output come into place so we can Define this specific data

structure that one one force the lar Lang model to sync things through before it give us a random time stamp and second to making sure the format of time stamp is returned is proper and this should return a data structure look something like this it will identify multiple different highlights and for

each highlight it will identify the mean points it talk about the title as well as specific Clips so that we can first use service like assembly AI to get the full transcript of the YouTube video with Tim stamp and using open a to extract specific Clips in end creates a short video so to do that we will

firstly import a few different libraries and also in theile we were adding assembly AI API key as well as open AI API key and there will be four different functions the first function to download the YouTube video from URL we're going to use a library called YT DLP and then we will use assembly AI python SDK to

get a full transcription where I can turn on the speaker label Auto chapter as well as IAB categories so it can provide some sort of intelligence out of box now we're also pass on some special words that are not well known like Lang graph or L chain I can get a transcription from a service and then

get full transcription in the SRT format which had all the time stamps then I will use open structured output feature to define the pagon model that we explained earlier where I can Define very specific format of the timestamp by adding descriptions here if you want you can also add in custom field validator

but I found the performance pretty well so I didn't really add it I pass on transcription get all the highlights and return the four highlight clips and in the end I have this function called Tri highlights going to Tri the video and put together all the highlights clips into a highlight video shots and that's

pretty much it I can try to transcript this video that I just published last week by running the script you can see it will download the video first and assembly AI will return the full transcription with Tim stamp and then we'll gather response and try to generate video clips and if I open

folder you can see there are three different shots that has been generated from the original video you can do something similar to generate a full blocks with both screenshots video clip and content and next I want to show you how can you quickly build a universal web scrier where you can take a URL of

any website and script structured data format in your table to do that we will load a few different libraries we're going to use set up open AI as well as Define model to be the latest gp4 model and we have a few different functions one is our use spider Cloud which is web scripting service to get markdown format

of the web HTML and then use open AI to extract structured data in then I'm going to do some data transformation to making sure everything can be displayed popular in a table format so firstly I will create a function called spider Cloud script spidercloud is web scripting service that allow you to turn

any website into markdown format with really high rate limit I personally found it is better than the serer service as well as the fire CR so I would just use the Pyon API to get the website content into markal format and then I will use this extract data function which we taking the row data as

well as a response format that we Define somewhere else so it's a pretty General solution that can extract structured information and in the end I will create a function called flat and Json as well as flat and Json array to transform the Json data in a way that I can display in a flat table and that's pretty much it

now all I need to do is Define the data structure that I want to capture in this case I want to extract the manual item from those restaurants so I Define a menu and for each menu item there will be a name of the item ingredients and price and you can also Define different price for different size I quickly use

streamlet to build a UI and this end result you see here so it's a pretty powerful Universal scripper depends on type of data you want to script you can just change the data model here as well as specific data that you want to display and last but not least I also want to show K example of how can you

build a simple web app that can dynamically generate UI based on the user intent and prompt with panic model like model reboot and that means you can output structure where it can be a child component WRA under a parent component and this useful for dynamic gening UI by just giving large Range model a few

predefined components there already people on Twitter utilize this functionality to build some sort of automated form Builder where user can just give a high level instruction about what information they want to clect and large Lang model will generate the whole form based on the user intent and I also

build something similar in Python utilizing the fast HTML Library so fast HTML is a new library that allow you to build fullstack web application with buing python you can build a UI component with complex interactions directly in Python which is great news for many people who are not familiar

with JavaScript so to use fast HTML we can basically set up app server very easily different sours of endpoint you can easily create the HTML format by using those TXS so in here I load two script first from tail wi and Di UI which are two popular component libraries and put together a quick UI

where it will have title as well a text input for user to give the prompt and a button which trigger SL ji and point that were defined here so every time when the button is clicked the function we Define under ji will be called and the return value will be changed to the Target item which is div with ID C UI

and fill in the inner HML with what we generate from this endpoint and under the ji endpoint I Define a function which will take a data that we receive from the form which is prompt and I create two simple data structure which I basically ask large L model to generate plan first and then create cre HTML

immediately and once it return response you will get just HTML and then put it back and you can do server to start the server very easily if you haven't installed fast HML yet you can do pip install python but if you already did you can just do python i. POI to start a server directly so I can come here and

then ask to create NPS survey popup click on button if you open Terminal you will see that it receive a prompt and return back to do so if I go back here now it show me this model about NP P server I can also try another one called a weather UI carard which it will return me a UI carard for display weather even

though the logo here is empty but we can imagine later we can just replace this with real image URL so those are a few quick example of how can you utilize open structure output feature to really improve the reliability of your large L model application and also start exploring a few new use case that wasn't

very easy to do before if you do want to dive a bit deeper into the code example that I showcased earlier you can join my AI Builder Club Community where I will showcase step-by-step detailed code breakdown of every single example that I've showcased in this video plus you have chance to collaborate with other AI

Builders who might already experience the challenge that you are facing today I have put the link in the description below so feel free to join I'm really Keen to see what type of use case that you start building with this structured output feature this a very exciting step for the h gen future if you enjoy this

video please give me a subscribe thank you and I see you next time
