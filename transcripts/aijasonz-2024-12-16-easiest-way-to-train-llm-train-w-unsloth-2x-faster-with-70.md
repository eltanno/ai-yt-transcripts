# EASIEST Way to Train LLM Train w/ unsloth (2x faster with 70% less GPU memory required)

- **Channel:** AI Jason
- **Date:** 2024-12-16
- **Duration:** 24:56
- **Views:** 135K views
- **URL:** https://www.youtube.com/watch?v=jFl5Fewrieo

## Transcript

so today we want to talk about large language model fine tuning so for the past 12 months one area has been improved dramatically in 2024 is a gap between the top close Source model like GPT and best open source model has decreased dramatically as meta introduced llama 3.2 and all the model

Mist has introduced and this is great news for AI developers because that means you can take those open source model find it to optimize for whatever use case you care about and deploy anywhere you want however fine tuning is a topic that has been discussed and bring up a lot but in reality not many

people knows how to do it properly cuz the process is quite complicated you might see so many different models on hugging face and didn't know which one is best one for you to get started it also requires lots of knowledge apart from just fine tuning like how do you prepare your training data popularly how

do you actually deploy and use a model in production quite often in my Feld overwhelming but don't worry I will take you step-by step what is the full process look like to fine tune the model from prepared training data all the way to deploy the model and I will also show you how do you use onslaughts to open

source package that allow you to find T the model two times faster with 70% less memory required which means you can actually fine tune it on a consumer grade GPU so without further Ado let's get started before we dive into fine tuning we probably should talk about another method that people has been used

to bring private knowledge into large L model which is rack and many of you probably didn't find tune any model before but you almost definitely have tried to build rack before because it is the easiest way to bre bring new knowledge to large langage model so instead of getting large Lang model to

generate answer directly R which represent for retrieval augmented generation or basically turn your private knowledge like PDF website into Vector database that allow us to retrieve most relevant information based on certain query in natural language and just append them as part of the prop so

that when large language model generate information it will has additional context so this is extremely simple and easy to get started compared with fine tuning where it actually change more model itself you can almost consider some base model like GPT 3.5 or llama 3 as a new graduate it already have the

fundamental skills like reasoning logic and common sense but to put them on a specific job you will give this model some additional training to baking the knowledge directly into the model so that when user ask a question that didn't exist in the original base model it can still provide the right answer

without rely on external data source so both Rag and fine tuning can actually achieve the result in of bring your domain and private knowledge into the model and in many cases rack is actually the better option because with f tuning the model's knowledge is Frozen it's latest knowledge will be based on the

training data you provided during the F tunity stage but if any of those data has updates won't be able to handle properly where with rack it's much easier for you to update knowledge base and even bring realtime data into Po and that's why in most cases rack is actually the default option you should

go for however apart from domain and private knowledge there are use case that rack is is often not enough for example the default multimodal model like GPT 40 even though it can read image it can't really handle specialized task like reading and analyze medical imag and even though you can use rack to

retrieve a few example and put into the prompt as few shop examples to get really good quality result you almost want to Bon those instincts into the model similar if you're building in legal space where you want the model to follow specific process instead of prompting the model it would probably be

much better if to train the model to be specialized in those tasks as there are just so many different cases available and even for simple and basic use case where you are building AI companion or try to mimic the way certain celebrities speak like being sarcasm or a bit rude where default model simply won't have

and you can prompt it to maybe 80% but to get a really high fality in of mimicking the way someone speak you actually want to fine tune it so fine tuning is really good method to train the model in his very specialized task and behavior apart from that funing is also a great way to to reduce your large

Lage model cost dramatically many of you has worried that using model like GPT 4 for your production app is too expensive however you can totally accumulate certain usage and then you can use those data to find you need smaller and faster model to dramatically decrease the cost so in general there are different use

cases where Rag and fine tuning is good at and you can choose the right method based on use case as a rule of some if your use case is just bring private knowledge like website PDF into large Range model rag is probably a much better place to get it started but if you found base model struggling to

complete specialized tasks in your domain or to play with also different Weir pomping tactics to get it work then fine tuning is great option for you to try out the process of fine tuning and deploying your own large L model looks something like this you first need to prepare the training data you can use to

fine tune the large Range model and after that you will choose the right base model to use as well as the right fine tuning techniques to actually fine-tune the model but most of the time fine tuning is not a straightfor process and you normally don't get it right at first go you need to evaluate the model

that you f tuned and then try to iterate a few times you want to set up a proper evaluation Matrix against the model that you just F tuned and iterate towards a state that you are happy with and in the end you need to deploy on the right platform write hardware and write inference methods first and most

important step is actually prepare the train data the ability and performance of fine tun model it very much depend on what type of data that you are giving to it and based on use case there are kind of three ways you can try to prepare the training data one is that you can get existing data either from your own app

that you has been running for a while or you can also go and find public data set that other people has created there are platform like KGO as well as hugging face data set where there already bunch of public high quality data set that people and company has been maintaining and very likely you will be able to find

something for your use case for example if I'm building a customer support agent and I want a model to quickly classify the sentiment and priority of the ticket the I can just come and search for like customer support and there are existing ones like customer complaint sentiment and priority data set that exist already

and same thing on hugging face there are existing data set that has a pair of medical image and the right caption and diagonosis of the problem so yet you can take this data set to fine tune a specialized model that can read and identify problems from medical image but of course you can also manually create

data set CU many time you probably have your PDF documents websites or even videos meeting recordings that contain huge amount of company data that you want to train the motel on that's why I want to introduce you to assembly AI there are leading speech to text model provider they can provide extremely

accurate transcription for both audio and video whether you are dealing with English Chinese French or even Spanish and it does more than just transcription but also outbox audio intelligence like automated topic detection summarize the content as well as speech recognition and it's extremely easy to get in

started they provide SDK that you can use right away and my personal favorite is that they allow you to Define Cosmos spelling for domain specific words that is not that well known like I can Define special words like land graph and land chain and then the transcription will be able to identify those words accurately

and they just launched a new model called Universal 2 which is an action speech text model that has the best inclass accuracy particularly in tricky scenario like special nums improve text formatting and handl offer numeric accuracy much better so it is model that can really handle complex real world

audio and video data with that you can take all the videos meeting recordings into Text data that can be used for fine tuning model but one thing to know is that to fine tuning normally data set need to follow a specific structure where it has a system message the user query as well as AI response what this

means is that if you have a PDF file or website of your private data you actually need to convert them into this specific structure for example if the one knowledge is your office opening hour is 9:00 a.m. to 5:00 p.m. you need to turn this into a specific kind of Q&A structure where user ask what's your

office opening hour and assistant says it is 9:00 a.m. to 5:00 p.m. and similarly if you are trying to fine tune 01 type of chain of s model where it can do very complex Mass calculation it will also follow very similar structure user will give input like what is answer to this mass formula and assistant would

generate response which will sync step by step with high quality analysis so quite often we use large L model or code to transform your existing data into a format that we can use to train the lar L model which I will showcase a example very quickly but on the other side one thing start BEC more and more popular is

this term called synthetic data this basically means that we can use large L model to actually generate more training data that can be used to F tuning specific model commonly the process is that we will use a very large but smart model to generate data that that we can use to find tune smaller model for

example you can use a extremely large powerful but slow model to generate CH of Sol data for solving Mass questions normally it will generate multiple different versions of answered and on the other hand we will also have a reward model which is not model that has been fine-tuned to score and rank the

answer provided by the other L model so that the better version of the answer can be saved as a data set and this has a lot of benefits one is that you can actually use large and Powerful model to trink smaller faster and cheaper model that special izing specific tasks also enable us to be not restrict by the data

we have in hand Nvidia introduced this Moto family called neotron which has 340 billion parameters and it has both instruct model that you can use to generate training data and also a reward model that has been fine-tuned evaluating and score the response so that you can use this flow to generate

very specific training data for use case in a very big scale and there very detailed tutorial as well as code Works through AI Builder communi and so if you're interested you can click on the link below to learn more in details about how to do synthetic data generation and as a quick example I'm

going to show you how can we create a training data set for a specialized large Range model that can enhance your mid Journey prompt so for this use case we actually want the training data into specific format where it has pair of Original prompt which is pretty simple and basic and improv prompt with a lot

of details added in so that we can take this training data into this type of format that we can use to find find to the model and to do that you can either collect a list of really good mid Journey promp yourself or find some existing data source on the internet then we can use existing model like gbt

40 or other ones to generate what does a simple and basic original promp could look like so that we can generate this data set pair in bulk and I'm going to Showcase how can you use hugging face or KGO to explore existing data set that you can leverage to so in huging face I will go to the data set page I will

choose task there should be a text to image task already and I can search for a mid journey to see if there any existing ones so you can see that there are few existing ones already and this one called M Journey prompt high quality which I assume is kind of filtered out prompt that generate higher quality

image and if I go inside in this table you can see that they actually do contain a pretty detailed prop for each image to do that data generation pipeline it's actually very straightforward we install the open in data sets data set is a package that allow you to download data set directly

from huging face then we're set open API key so we're going to use4 O model to generate data set so here we're going to actually download this data set with that specific data set name that you can copy paste from huging phas and split train is referencing we're getting this training data set and I'm going to just

take the first 1,000 which I think should be enough for this fine tuning now try to extract the actual enhanced prompt data from this data set because it does do have some other stuff that I don't really care I just want to extract the stuff that is wrapped inside this star signs and this function does that

then for each enhanced prompt I will go through this GPD 40 model to actually generate that data where I give example of enhanced prompt and a simplify from and in the end I'm going to save the string data so I can download and use later so that's pretty much it I can run this it probably take roughly 15 minutes

if I'm using the GD 4 mini model and if you're using the 40 model it probably take longer okay so this one take 8 minutes in total and then we can save this data into the training file that we can download which should have around 1,000 examples and then we can use this data later turn them into a format that

we can use to f t the model so after get initial training data ready next is we can start fine tuning and there are few different options that you can use you can use those close Source model platform like both open Ai and entropic provide platforms where you can just upload training data in the right format

and they will do all the fine tuning for you as well as the deployment and open AI support all the GPT 40 model as well as 3.5 turbo where with entropic you can f tune High cool model but one of the core consideration for this cros Source model is that you actually don't own the model they just provide your API for you

to do the inference so you kind of just lock it into that platform you can't really download the model and host someone else and because of that one of the key consideration would be the price for inference because once you findun your model on those closeup platform you will have to use their API for inference

so you have BL control to optimize cost here the other option is that instead of using those close Source model you can try to find your open source model but the problem with fine tuning this open source model is that you will need to build the fine tuning pipeline yourself and after you fine tune it you also need

to do the deployment yourself which is not easy to do and require a huge amount of engineer work if your user base start growing a lot that's why there are also platform kind of sitting in the middle that allow you to find to open source model and can help you deploy the model on their platform directly for the

inference like together AI or fireworks AI for those platform typically they will handle the pipeline can do deployment but also they allow you to download Fine tuna model so that you are not really locked in so if you just get started and you don't want to use those close off model those type of platform

are actually pretty good choice but if you really want to have 100% full control you can just train and deploy your own and there are platform like Rod or model that make a deployment actually a little bit easier in our case I'm actually going to Showcase you how to do the train and deploy your own mthod so

that you can know the full process end to end and then it became easier for you to go close Source platform or open source platform and one question you might have is how do you choose the most suitable base model to find T you kind of also need to consider two things one is the cost and speed for the inference

so at default you might think why not just always use the largest model since they are the most powerful one well the largest model normally means it will be much more expensive for you to run later and the other side it is also slower so if you are building some kind of realtime Chad B use case the problem is

not bad as one to go and the smaller model is actually getting better so as a Ru of sum I normally would choose a smaller model to start with like 3B or ab and based on that find two models results I can decide whether I want to go to bigger model to get more accurate answer or I can go even smaller model to

make the experience faster and apart from the cost and speed for inference another thing to consider will be the use case so general purpose model like llama or mistro those are kind of general purpose model that is good at many different things if your task is more specialized let's say you want to

build a data an agent where it can turn user's query into a SQL that you can run to get data from database you can actually just search for test to SQL there are a bunch of specialized model just for that task and you probably get more cost effective solution just find you need those very specific model and

see for coding mass and many other tasks that you can find so at the beginning you just want to figure out what's the most suitable model for your use case but apart from base model to use the other thing to consider is the fine-tuning method and there are kind of two popular ways you can use to do fine

tuning one's called Full fine tuning another is called Laura and if you haven't heard about Laura before and don't know what it is the difference between full fine tuni and Lura is almost like if you consider lar langage model as a book full fine tuning basically means you are rewriting the

whole book which takes a lot more efforts than time versus with Laura you actually don't rewrite whole book you kind of just add post notes on the book so that when people reading the book they can get additional information and Laura fine tuning has became more popular C of fine tuning and time span

is multiple magnitude lower it might take you way to do the full fine tuning but with Lara it can compressed to just a couple hours and consumer grade GPU but because we are not changing the weights of base model most time you will use Lara for fine tuning and aligning some very specific behavior and to just

get into technical part a little bit more three blue one Brown made this amazing video explain how this large L model weights actually works behind the scenes so at high level large L model you can think about a blackbox where it will be able to predict what's the next word based on the sentence it was given

so it's basically a calculation machine that is able to calculate the probability of the next words and when you look inside lar langage model the way it is predicting next word is you can almost consider the billions of different parameters or what do we call weights inside the lar Lang model and

each indiv parameters you can consider them as a dow that is doing its own calculation and accumulated result of those billions of parameters calculation lead to the prediction of the next words so for each parameter the original base model is calculated like x equal to weight multip y with four fine tuning we

basic have new weights for each parameters to do this calculation but with Laura we actually don't change the weights of the base model instead we're try to add some factors that impact the calculation result but the base model weight is not really changed that's why if you're looking at L normally you just

have file that is much smaller but will be used together with a base model but in general call C of time resource and amount of training data needed is so much lower normally you can start from just lar of fine tuning see the results and decide if you need to actually go for f tun today I will take you through

example of using Laura because there's one package that became increasingly popular called onslot so onslot put inl is a open source package that help making training AI model faster cheaper and easier even if you don't have the most powerful GPU so with unslot you can actually fine-tuning model up to two

times faster with less than 70% memory usage on a consumer grade GPU so I'm going to take you through the example of how can we take the training data that we just generated from this awesome mid Journey prompt into a model that can actually help enhance the mid Journey prompt that user get and this whole

training process can be running on T4 GPU which is free provided by Google clap and you can get results in just roughly 15 to 20 minutes so let's get it I'm going to do the whole fine tuning process on Google clap with a free GPU they providing with T4 first they want to install unslot package here is the

list of all the possible model that you can use to do the unslot fine tuning in this case we are choosing the Lama 3. 23b model and here is one option called load in 4 bit or in other place you might see things like 8 bit and those is concept of quantization and quantization is a technique to shrink his model size

and speed up his computation by using smaller and less precise number that represent model's parameters and at a default each parameter could be 32bit Flo point which means its calculation will be number like this which can be represented by 32 bits binary number and four bits and eight bits basically means

that we will try to use smaller and less precise number to represent each parameters so it is not that accurate but the amount of computation needed will be much smaller so 4 bit basically means we're using four bit integer to represent the number in binary next is we will start setting up the Laura

adapter and there are few different settings so op means how many parameters going to be impacted by the Laura the bigger number means more parameters will be impacted but also takes more space and and resource so normally you can start with 16 and Target module basically means that if you think of

base larg model as robot it already trained to do things like walking running but if you want to teach it how to dance you actually just need to focus on training the lag module and Target module is exactly the same each module here kind of represent specific part that you want to find you and improve

but if you're not sure you can always start with everything here and L arpha bigger this number means more more impact this Laura fine tune Behavior will be on the model and often you need to find a balance here if you set this number too big then you might have the problem of overfitting which means model

can only do the task that is within the training data set and everything outside the training data set it will suck and same thing if you set this number too low the model might not have enough significant Behavior change after the fine tuning and if you're not sure you can always start with 16 so those are

core settings that you will need to set up a lower fine tuning adapter the next thing we want to do is actually we want to prepare the data so from previous notebook all our training data looks like a pair of simple prompt enhanced prompt but to be able to actually find you in the model we need to turn them

into model specific syntax so for llama they have very specific syntax look like this we will have a user attack the actual message from user yeah assist the message so for us to be able to find tun Lama model we actually need to turn the training data into this specific format and to prepare data we're actually going

to use a feature provided by onslaughts called standardized share GPT and this is a feature we can just have the training data set in this unified format with form and value and it will be automatically turned into the right format for different model so in my specific case I would drag and drop the

training data Json that we create earlier load it and put them into this unified format then I will load the chat template and run the standardized share gbt function to get the right format for different model and now we can see if I run data set conversation the result it g me will be in similar format to open

AI F tuning data set but if I do text then it will return me the specific format where llama 3.1 we need and that's pretty much it now we can start fine tuning since we have a Data before we start fine tuning let's just quickly run the default model see what kind of result you will get and you can see that

this is default result and it's not very good it just looks like more expanded paragraph but it didn't really have all the Nuance of how you're going to write a mid Journey prompt this is where we're going to start the fine tuning process so we will use this fft trainer which is a package provided by hugging face they

already have the fine tuning proper plan set up then we'll also use unslot train on completion method to only train on assistant outputs and ignore the loss of the user inputs it will basically try to remove the inputs from the training data sets and only focus on the output and that's pretty much it we can just click

on this button and start the training process you can see that this whole training process finished within just 2 and a half minutes and now let's give a try I'm going to give a same prompt and we will see what the result get so you can see that this looks a lot more like the Journey prompt that you will see

from the website and if the result is not good more likely there are few things you can do and most straightforward and likely result is that you might need to provide more training data in here I provide 1,000 training examples but if your model is bigger you probably need to provide

bigger data set and second one is that you can also change the model if your task require more reasoning ability no matter how many training data you provid it it might still struggle instead you can try a bigger model and after you f tune a few times and get the result that you want next you can export model and

deploy somewhere and when you export the model you can either just export the Laura adapter which will be a very small file and can be used together with the base model itself or you can export the ggf which is specialized file that include the base model as well adapter and you can just run it right away and

you can also push to by putting your API key that you get from the hugging face and you can get the access toen on hugging face access token and then put your username here and Define a ripple and after finish you will see a new one has been created here with the adapter file and next time if you want to use it

you can just use this code to load the model that you put on hugging face but on the other side you can also explore ggf file which can be used on llama CPP or AMA directly so this pretty much how you can fine tune lar Lage model using unslot if you want to dive deeper into the topic of fine-tuning you can join

the AI Builder club that I'm building where I work with industry fine tuning experts di much deeper into the fine tuning topic like how do you take the fine tuning model and deploy it and how to use platform like together Ai and how to evaluate the fine tuning Pipeline and I will share interesting learnings and

practical project you can build to learn more about building AI products and more importantly we have group of top AI Builders who might already experience the problem that you are facing today so you can just come here and ask any question you have me and as Community member can just jump on and answer your

questions so this is today's video and if you find this useful please like And subscribe I'll see you next time
