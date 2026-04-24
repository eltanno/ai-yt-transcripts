# Claude 3.5 struggle too?! The $Million dollar challenge

- **Channel:** AI Jason
- **Date:** 2024-06-26
- **Duration:** 23:31
- **Views:** 17K views
- **URL:** https://www.youtube.com/watch?v=kZap-tDA1i4

## Transcript

if I ask you to identify the pattern of how does a matrix on the left side transform into Matrix on the right with as little as just one example you'll probably be able to figure out the pattern and generate output on the right side which looks something like this and even for some more complicated example

like this with as little as two or three different examples you'll probably be able to identify the pattern that it is taking the smallest rectangle shape outp put just said which means now you are able to answer this new question those simly intuitive and simple task that you can answer is something that statea of

art large Range model like GPD 40 will be very struggling to answer because those information are not part of the training data set even though large langage model has shown impressive ability to solve problems especially with the recent agentic Behavior where it is capable to generate complex code

or explain deep Concepts it is fundamentally very poor at handling new things that it wasn't train on because the way large language model works is basically trying to predict the next word based on the probability within its massive training data set and the reason it can answer some basic math question

or things that require some logic and reasoning is not necessary because they actually think things through but you just memorize it and spit out the answer based on its memory and some might argue that this is not a Showcase of true intelligence but more a Showcase of strong memory ability and and that's a

big difference because many believe the definition of true intelligence is the ability to adapt and learn new things as a s psychologist Sean mentioned intelligence is what you use when you don't know what to do if we always just rely on past experience and knowledge no matter how big the amount of data we can

ever have it will always be limited by past experience as human we won't really have breakthrough to learn how to use new skills and tools never seen before because it was not part of training data but if you put a baby or kid in a new neighborhood even though they never go through any training able to adapt the

new environment or language without pouring millions of training data in and that is ability to solve problems that never seen before with very little training data this exact problem has been described by Franc charot back 2019 where he published a paper code on the measure of intelligence where he

introduced a benchmark that we can use to measure the efficiency of AI skill acquisition on unknown tasks called Arc which represent for abstraction and reasoning corpse this Benchmark is basically a collection of unique training and evaluation tasks each task contain multiple inputs and output

examples to Showcase a pattern and the puzzle like inputs and outputs present a grd where each Square can be one of 10 colors and goal is build a AI system and will be able to predict exact output based on a new input some of them might feel simple and straightforward but many of them are actually not that

straightforward and can be quite a comp complex and also cover a wide variety of different type of tasks that is fairly unique compared with each other and those tasks didn't require any power knowledge it's a pure test of its D intelligence and ever since this Benchmark was introduced back in 2019

there were many people tried to build AI system that can complete those puzzles back 2020 the best performing AI system was able to answer 20% of those task correctly and the latest version to now June 2024 is 39% which we dive a bit deeper into their messes but Meanwhile Back 2021 New York University actually

did a study to get a human Benchmark according to that study an average human is able to answer 84% of all the puzzles which means if we have ai system that can achieve similar level of performance as human that means we actually build a system that can learn and adapt to all sorts of different new scenarios just

like human do and that is basically goal of the arkhi competition that is happening right now it is global competition everyone can join and whoever build a AI system that can achieve super human level performance which is 85% correctness of the AR testing data set will be winning the

competition there's total amount of 1 million price pool for the winning teams and what does this actually means let's say by the end of this year let's someone build AI system can actually achieve this and this is what French said given that Arc is a minimum reproduction on of general intelligence

how important is it once we discover a solution so at the very least I think a reliable solution to Arc would be at the very least it would amount to a new programming Paradigm if it works on more the mains than just Arc then it means that you found a way to given just a handful of input output pair

demonstrations produce a program that matches what you described with your examples and because you only need a couple examples but it means that anyone is not able to program computers just describing here's my input here's my output and and do this twice or three times uh and now they have a program

that they can run and that will generalize to new data in very much the same way that the human that has seen the same examples would generalize and hopefully that's a gii but if it's not I think it's at the very least revolutionary new programing Paradigm that will make everyone a program in a

much true way I think than llms that basically speedback code Snippets that are similar to things they' WR on GitHub or stack Overflow so this is really exciting project and going to help on the progress towards AGI massively but what are the all different type of approach and methods people have tried

so far to build such AI system that can adapt and learn new things so I'm going to share a few examples about how different teams are trying to tackle this problem as well as how can you participate but before we dive into that I know many of you or your company actually have have a huge amount of data

that can be analyzed or can be leveraged by AI to extract additional insights but not exactly sure how can you do it popularly because there are just so many different unknowns and it's not very clear what is best practice in terms of like choosing the right data set to use project to prioritize or how can you

pach those project internally that's why I want to introduce you to a research that hpot did where they interview lots of different people from top companies about best practice of how they are integrating a AI into their data analysis workflow it showcase common challenges and pitifuls that you might

experience when adopting AI into your data analysis process as well as some best practice process about how to start and plan such projects within your company it even include a comprehensive checklist for specific things like how to ensure data privacy and security while you're sending data to different

large L model and AI systems so if you're planning to leverage AI to analyze data in your company I definitely recommend you go download this free research and get more prepared about things that you need to do to launch such project you can click on the link in description below to download

this report for free and now let's get back to the arhi project so how does it actually work and how can you participate if you go to KGO and search for Arc price 2024 you have this page where you can join and submit prediction in this project it has data set if you're look into this data set it has

both evaluation training and the tests and evaluation and training are basically two different data sets us that you can use to build the AI system where the training is a bit easier and evaluation is bit harder and more difficult tasks each challenge in those file has both test and train and if you

open them they are basically input and outputs and each are a matrix of numbers that is representing the chart so basically each visual chart is represented in list of array like this so that you can feed to different system like large Range model and each data set look something like this where the

training basically just three or five examples that is provided to help you identify the pattern where the test is actual challenge so you can use basically all those training data set and input from test as the input for the system and the goal of system is to be able to generate an output that is

exactly 100% match to the correct answer that is provided here there are loads of different challenges that you can use to train and test the system your building and that's pretty much it you can start trying different approach and methods to try to tackle those testing Thea sets and I'm going to show you very quickly

how can you set up some basic environment to start building the system so if you go to KGO and click on create new notebook you can click on ADD input and just search for Arc price 2024 and there will be one of them you can click on that to add to your notebook if you close that you will see that this one

input called Arc price 2024 which has all those Json file that we will need and what I'm quite curious is I want to test what's grow ability from large Lage model to try to solve this problem even though large langage model itself is system one fast thinking with just pre-train data but there are a lot of

techniques that could be used to actually increase the reasoning ability so I'm quite curious to just try it out and see what kind of roll ability output will look like and that's what I'm going to do here so first thing we want to load data so I will import a few different libraries and create a

function to split task that have multiple different test input output Pairs and this will make handling a bit easier then I just run a quick function to load the evaluation data set and here what I'm loading is the evaluation dat data set which is the one that's a bit harder and in the end I will create a

pan a data front Okay and last we can just try it out to see how data set look like so if I do data set zero you will see that each data set looks something like this it has training with input outputs examples as well as test data including output that we can use to verify and that is what we're going to

do next I want to create a quick function to be able to validate whether the generate answer is correct or not as well as some help function to extract the answers and to do that to install a few libraries I'm going to use open AI for this test but just be aware when you actually participate the competition you

are not allowed to use openi model because there won't be internet access so you have to use some open source model so I create a few different functions to extract the final output generated by the system because if I'm using large L model the answer might include all sorts different things like

the reasoning itself so I need one function to do exactly that and then I'll create a function to be able to compare the result result generated by the AI system versus the correct output from the data set and output if it is 100% correct or not and that's pretty much it now we can start building

functions that can take in the testing data set to generate answer compare the result and firstly I'm just going to try some basic vanilla L model call with GPD 40 so I create a function called Soft single L model where it will take in the task a few short examples if I have any so I create system prompt where it will

taking the few shop example if there's any uh and then show the training data and in the end input data and here I didn't even ask it to do the train of s so it's very basic large Lage model call and then I just take one challenge data set get the true solution generate answer from lar Lage model and then

compare the results in the end output the final result I click this okay so we got answer so this is s process from gbd 40 the final output this one and we can see that it actually answered correctly correct percentage is 100% And if we check this file name which is 0576 224 this the actual visualized

challenge you can see basically it will just repeat the pattern multiple times and it is actually answer correctly so that's pretty good start but let's try a next one to see how well it perform and this is the second one from what I can see it basically just takes the biggest shape and the color is differently

assume the color is based on the actual number which some transformation if we go back to the notebook you can see that the answer here is incorrect and gbt 4 or vanilla Al both shaping as well as color real so obviously there's some limitations with direct large L Moc in my question now is that were some

tradition prompt engineer tactics like multiple l m chain or agents or even multi-agents going to help in this situation so I'm pretty Keen to just try it out so this second thing I'm going to try basically the idea here is instead of just getting through one large L model call can I increase its

intelligence by break down into two steps the step one will be just looking at the um examples and trying to identify the pattern and step two will be trying to solve that so I would have first large L model call to identify the patterns and explain the transformation that it that observe from input and

output and then I will put this rules as part of prompt to second large L mod call and this is basically the and let's see if it actually improves the reasoning so I would basically do the same thing but swap the function to be this new function that I created okay so now we get the answer and if I look at

it now I can see the reasoning actually improved compar this previous one because if you see the result it does remove all small symbol from the output which in the previous one it totally ignor this rule but the part it got wrong is the color of the actual shape and this to be honest it's a bit

challenging I don't even know what rule here is because it looks like there are different colors based on different shapes and if you look at reasoning stab it did actually capture that so it captur a few different rules one is number a represent some particular structure that need to be transformed

but it just wasn't sure what the rules there and each input grid that contains one which is smaller one that should be removed from grid after and what I want to try next is I want to see whether a multi-agent system can actually help in this situation and in my mind that the next idea is whether we can build a

multi-agent system to improve the reasoning here and one key concept here is that instead of getting large Range model to generate answer directly we can actually get a coder agent to write a piece of code that can do this transformation and benefit of that is that then we can get a program verifier

agent to run this code against example input output pairs to say if the program actually deliver result that we want if so use that program to round the result if not give feedback back coder to actually iterate code so this kind of the concept I'm pretty curious to see whether it works so for that method I'm

going to use Auto to set a multi-agent system so I install auto package and then set up a multi-agent system so I'll create some temporary folder to stall the program that generate by coder and I first create agent called patent identifier whose role is specifically to identify the pattern and explain what

the requirements that the program should meet and next one is I want to create a coder who will actually generate code in this code I wanted to take two inputs one is input grade and output grade where output grade would be an optional param and this program should run the code and then return whether the program

running correctly 100% match or program is incorrect and in the end I will write a program verifier who will play the role as QA and run the code against all the examples input output pair any of those input output example pair return incorrect then give feedback to the coder to iterate code and if the result

is actually correct then run the test input and return final result terminated this agent should be able to execute code as well so I will put a code execution config and in the end I will put a user proxy agent and create a group chat as well as Define a group chat manager so that's pretty much it I

will do the same thing to run this code and in this case you can see that it will pass on to the pattern identifier which in this case successfully identify a requirement for the code which is it should map the value eight to a new consistent number and remove all the other value that not eight and then the

coder start generating a code that can meet this criteria if output grade is non know and the result is 100% match that it will return program running correctly otherwise it will return program Incorrect and then the program verifier start wronging this code multiple times against examples that's

that it seems that the output has successfully returned the results in the end even though the program verifier Arrow out for some reason the answer is correct this time and if you look deep into the program it written you realize that this program probably is not correct cuz it is always mapping 8 to7 a

specific number which is probably not true so let me just try to run again okay in the second attempt it seems still not very good I just keep failing generating the whole program for some reason but I can clearly see that this mess three in teral reasoning steps seem to be more reliable than the other two

methods and later I did read an article from Ry who achieved 50% score on the public test data set and the method he was using is actually very interesting so in this sh the method he was using is also getting the large L model to generate code to actually answer the question but instead it is a lot more

sophisticated with a lot of optimization so it will give the large language model which is GPD 40 both the image representation of input and outputs as well as text representation and first it alls the L model to reason and plan what kind of code should be written but next step is instead of it right once or use

a kind of agent to iterate multiple times based on one piece of code it get agent to run 3,000 to 5,000 different attempts to get large L model generated code so this is a crazy amount of the exploration and generation and from those 3,000 to 5,000 examples it pick up 12 best programs and then run against

example input and output to verify and if there's any error it will iterate so the high idea is actually similar but the crazy part is it generates huge amount of codes and also looks like multimodal can lead to better reasoning in this example and I took a look at his GitHub it actually few short prompt

examples to teach large L model how to explain the image and text representation of the challenge as well as the python code example to and this method of exploring a huge amount of possibility is something we normally call discrete program search it Bas this process of getting the model to search

and explore massive amount of different options then do the check to verify which option actually leads to right pass like running the code to verify the output and in the end to select the ones that actually worked it's a similar concept that ARA go adopt where it explore a huge amount of different PA

and possibilities so this seem to be a really effective method except this is going to burn a huge amount of cash to run such program and frenches also post a tweet to talk about this he said the main issue with program synthesis which is basically this program search is combinatory explosion which means the

space of all programs grow combinator with number of available operators and the best solution to fight this explosion of all the possible passes is leverage intuition over the structure of program space which means you can probably find a specific spefic model to sample program and suggest the right

branching Deion so instead of exploring all the possible different passes you can use certain model to help deciding which path is more worth exploring versus others and even though that Intuition or judgment might not be correct it will still guided to a more possible pass with much more efficient

structure and he actually has a Google slides that explain a few different concepts in details I put a link in the description below where you can click on that to check more details and on the other hand I also noticed something that called active inference that seem to deliver really good results with r model

and the concept here is basically using synthetic Arc AGI like data to find your L model during the evaluation stage and here's a quick clips where Fishers talk about this specific method the trick to making this LM based solution work so the thing is if you take a state-ofthe-art LM and you additionally

pre-train it on millions of CTIC generated AR like tasks that still doesn't work very well at all it's maybe on the order of 10% so not very good in fact much worse than relatively basic discrete problems of solutions and the trick to actually making this approach work well is active inference which is

this idea that when you're presented with one of the test tasks that you're supposed to solve so you're presented with a small number of input output demonstration examples and the idea is going to be to fine tune the llm on these examples and of course because you only have a couple of them that's not

really enough to uh get stastical and this to work uh you're going to want to expand them artificially uh using using a DSL that's going to just the pl Transformations uh to them uh so trying to make them more more more diverse to have basically enough data points to fit a curve uh but still trying to make them

match original task and this trick of doing active inference tuning is actually what unlocks the performance of this approach and I don't think this is something that I've seen with with LMS before actually I don't think anyone else is is doing that and the fact that it has this outsized impact on the

solution I think it's really interesting and it feels intuitive that llms are not on their own the solution like llms near things like gini orp and so on because they're basically Frozen at inference time they're not actually learning anything when you show them a new task but that's not how humans operate

obviously when you look at a task you're forced to adapt to it you're not just fetching something from your memory that matches this task if it's a task you've already seen before then sure maybe that's what you're doing uh but the idea is that you can be exposed to these stars that you've never seen before and

you need to make sense of them and so you need to basically learn from them right you need this active inference step which vanilla on doing and I think that's really one of the Big Blocks on their performance especially on Arc so those are few example implementation of how you can attempt to solve the arc

challenges and the key thing here is that the real breakthrough hasn't even show up yet so there's loads of method that you can try so I definitely recommend you to go ahead play you can go to k go Arc price 2024 to just join and submit your solution if you want to find some example you can go to code

there are some examples already like this llama 3ab example that you can use as a reference to see how to approach the solution you did I'm really Keen to see what kind of interesting solutions that people are start exploring this is definitely a project I'm going to continue monitoring I'm quite

interesting to try the methods of fine-tuning with synthetic data as well to see how well the method can work if you do want to keep update please comment below about interesting method that you heard or tried I'm really Keen to discuss more on this and if you want to keep update please And subscribe

thank you and I see you next time
