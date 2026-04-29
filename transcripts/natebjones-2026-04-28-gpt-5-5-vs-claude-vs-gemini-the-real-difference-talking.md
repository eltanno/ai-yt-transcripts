# GPT-5.5 vs Claude vs Gemini: The Real Difference Nobody's Talking About

- **Channel:** AI News & Strategy Daily | Nate B Jones
- **Date:** 2026-04-28
- **Duration:** 32:34
- **Views:** 49K views
- **URL:** https://www.youtube.com/watch?v=9aIYhjeYxzM

## Transcript

GPT 5.5 reset the bar and I think it's the strongest model in the world today. I want to explain why I think that why it matters if you're actually using AI for work and what I would change in your workflow because of this model. Because the most important thing about this release, it's not that 5.5 is better

than 5.4. That's true, but it's like the least interesting thing. The most important thing is that it changes what you can reasonably ask a model to do. So, let me start with why I think the bar moved. Then I want to show you the evidence because I put these models through the paces. I don't think easy

prompts tell you that much. So, I pushed it through a really detailed executive knowledge work package, a messy data migration, and an interactive 3D research build. And then I want to make it practical for you. Where would I use 5.5 today? Where would I still reach for Claude? And where do you need

validation, review, or a different workflow because the model is just not safe to trust on its own yet? But the first thing to realize is that the floor moved. That phrase matters because not every model release moves the floor. A lot of recent progress has come from inference time compute. More time, more

thinking, more search, more tool calls. It's useful. It makes models better. It's not the same thing as the default model being bigger and smarter. 5.5 feels like a bigger pre-train showing up in everyday use. The fast modes are sharper. The thinking modes are stronger. The model figures out the

shape of the task sooner. It needs less handholding. It can take a messy task and get closer to a finished result faster. And the public numbers point the same way, right? Open AAI reports an 82% on terminal bench which is around software engineering an 84% on GDP val which is around knowledge work tasks and

there are other high value numbers artificial analysis put 5.5 an extra high reasoning effort at the top of the intelligence index by three points but that's not the point right it wins but also they note that the model uses way less tokens than 5.4 for over the index run. In other words, it's smarter and

more efficient. But the benchmarks don't tell the whole story here. We spend so much time comparing tiny deltas that it's really easy to miss the basic fact that we are still on a curve that is moving up very fast. Dario Amade has used the image of being on a rainbow with no visible end to describe this

moment in 2026. Open AAI's framing around 5.5 is basically the same idea. Scaling is still working. The gains are still compounding and the lab is not acting like the curve is over. No lab is acting like the curve is over. Whether you like the rainbow metaphor, 5.5 is a reminder that the frontier moving is

still the most important variable in the whole industry because when the frontier moves, our ambitions move with it. So that's the reason the floor moved. 5.5 is not just a little bit better at benchmark tasks. This model feels different. Not just more competent, it feels like it gets what you want and

gets after your intent more effectively over a longer period of time. It feels like a big lift intuitively when you are actually using it day-to-day. And that's what I found and that's what I'm going to walk you through next. And before I get there, I just want to call out there is a take floating around AI right now

that sounds really smart, but I think it's wrong. The take is that the best model is mattering less now than it used to because all the frontier models are already good enough. And there's a version of this that feels true. If your task is small and clean and well- definfined, a lot of the models now feel

interchangeable. Summarize this document. Draft this email. Make a basic landing page. Explain this error. Write a normal SQL query. Any good frontier model can do those things. The frontier has really moved past easy tasks. So if you evaluate models on easy tasks, you will conclude that the differences are

small or non-existent. You just will. And you will be right, but only about the wrong category of work. The best model matters in the places where the work is real and ugly. It matters when the brief is underspecified. The files are messy. The source material can be contradictory and the model has to

decide what matters and use tools and preserve uncertainty and produce real artifacts and check the result and keep going long enough to finish. That feels like real work, right? And that is the work where chat GP2 5.5 feels meaningfully different. The old question was can the model answer this? The new

question is can the model carry this? Can it carry a long context without losing the thread? Can it carry a deliverable across multiple formats? Can it carry legal and ethical risk without smoothing over the uncomfortable or dangerous parts? Can it carry a data migration far enough that the human only

has to check the tough cases instead of rebuilding the whole database? That's the part of the market where the best model still matters. And it matters even more once you stop thinking of the model as just a chat box. Because in 2026, you are not only judging the weights of the model. That's not really relevant.

You're judging the system around the weights as much as the model itself. The tools, the file access, the browser control, the memory, the computer use, the image generation, the interface, the available compute, and the way all of those pieces combine into something that can get work done. The timing also

matters because 5.5 did not land in a vacuum. Enthropic announced Opus 4.7 on April 16th. OpenAI announced 5.5 on April 23rd. 4.7 is a real model. That's an advancement. I still use it. It's strong, especially on planning, critique, and front-end taste. But Opus 4.7 also landed under the shadow of

Mythos, the more advanced anthropic model that has been teased and restricted because of cyber security concerns. So 4.7 felt to me like a bridge release. Useful, important, better than what came before, but not the release that redefined Anthropic's place on the frontier. 5.5 feels

different. It arrived as a model release, but also part of a larger OpenAI workflow launch. You have 5.5 in chat GPT and codecs. You have codecs at the same time getting stronger as a place where the model can actually act on files, code, browsers, documents, and interfaces. You have chat GPT images 2.0

arriving in the same window, which matters because the visual direction has been one of the places where OpenAI models have lagged clawed. Those pieces all fit together. Images 2.0 can produce the visual reference. Codeex can operate in the working environment. 5.5 can reason through the task and build the

artifact and test it and keep iterating. That combination is much stronger than asking a model to do everything from a blank prompt. That's the argument for why the best model still matters. The hardest work isn't clean and the best system matters because the model needs somewhere to act. Now, the real question

is, does that show up in the real test or am I just saying something that feels good cuz the launch was impressive. Let's make this concrete. I ran 5.5 through three hard tests because most public model evaluations strike me as too easy to tell you something useful. If you ask a Frontier model to build a

to-do app or to summarize a transcript or to make a chart or to write a memo, you're not really testing the frontier anymore. You are testing whether the model can do something that good models have been able to do for a long time. The differences show up when you really try and reset the bar and raise your

ambition. So, the three tests I designed were designed to get the model to fail in different ways. And yes, all of them were designed to be so hard that any Frontier model, including 5.5, would fail. And I expect that as models get better, I'm going to have to keep evolving these tests. And I'm very

comfortable with that. Part of what I love about having a private bench is that I don't have to publish percentage marks that show up with publicly available tests that you can see models literally get into the 80s and the '9s and essentially saturate the benchmark. I can make these as hard as I want and

that helps test the models because the models are being tested in ways that they weren't explicitly trained to test on. And I love that. I love that because it helps us to measure one of the key values of intelligence in a model, the ability to generalize across new problem sets. And so that's why I have a private

bench. And this one is wicked. I wrote three tests, all designed to fail in different ways. The first was Dingo and Company, a full executive knowledge work package about a dingo company in Alaska. The second was Splash Brothers, a dirty small business data migration about a car wash company. And the third was

Artemis 2, an interactive 3D visualization and research build. Each one checks a different capability. Dingo tests judgment plus production discipline. Splash Brothers tests boring backend correctness. And Artemis tests research, interactivity, and visual taste. And the important thing is that

any one of these tests by itself might give you the wrong story. For example, Dingo makes 5.5 look like a runaway winner. Splash Brothers, it's going to make you feel more cautious. and Artemis makes the routing picture much more complex because Opus still has a real edge in visual composition. If you look

across all of them, they give you a more complete picture. Start with Dingo. Dingo is a fictional Anchorage pet tech startup selling an automated litter box for dingoes and Dingo hybrid pets. The product is called Dingo Box Pro and the company has a related subsidiary called Northern Canada Imports that helps

create the market by importing the dingoes. The premise is intentionally absurd and the absurdity is the point because a weaker model treats this like a normal product launch with a funny animal attached. A stronger model realizes that this is commercially interesting. It's legally sensitive.

It's ethically fraught and it's operationally very complex. It has to separate the product company from the import funnel. It has to size the market around qualified owners, not fantasy demand. It has to avoid implying that the product makes exotic ownership legal or simple or suitable. And it has to do

all of that while producing real files a human can open and edit and send. The assignment required 23 deliverables in a single prompt. Docs, a deck, spreadsheets with formulas and charts, a PDF one pager, an interactive dashboard, launch communications, FAQs, personas, an email sequence, a risk assessment, a

go to market plan, and more. This is the kind of task where a model can write something impressive and still fail because the deliverable is not have good thoughts about the launch. The deliverable is assemble the launch packet. GPT 5.5 won this test by a wide margin. And yes, I am going to talk

about the scores because it shows how big the victory was. The scores were 87.3 for 5.5, 67.0 for Opus 4.7, 65.0 for 4.7 Summit, and 49.8 for Gemini 3.1 Pro. And more importantly, 5.5 produced real usable artifacts. All 23 required deliverables were real artifact types. They weren't HTML or Markdown wearing

the wrong file extension. The deck had 17 real slides and 26 media files. The spreadsheets had real formulas and real charts. The dashboard worked and used the supplied logo and product hero image. The research file had 34 URLs with strong official source coverage on the legal and regulatory claims. And

that legal posture is at the heart of this test. The other models failed it in different ways. Opus 4.7 produced polished artifacts, but its regulatory position was shakier and it drifted on important numbers. Sonnet 4.7 had useful strategy but underproduced on the artifact layer. Gemini 3.1 Pro

understood parts of the premise but several files that were supposed to be real documents or decks or workbooks or PDFs, they were just HTML or text files with the right extensions. That is not a small issue. You cannot send a fake PowerPoint to a board. The most impressive thing about 5.5 in Dingo was

not that it finished. It was that it understood the posture of the work. It framed the launch as a very narrow qualified household release, not a broad novelty campaign. It treated northern candid imports as a central source of risk. It separated curiosity traffic from real buyers. And it repeatedly

stated in the right places that the product doesn't make exotic ownership legal, simple, or suitable. That's the kind of judgment I want from a model doing real executive work. Now, there were still defects. The PowerPoint had invalid XML metadata because the amperand in dingo and co was not escaped

correctly. One slide rounded an NPS number incorrectly. Some pricing claims were stale or imprecise. I would fix those before sending anything externally. But they are final mile production defects. They are not failures to understand the assignment. And that distinction matters because in

real work, the expensive part is often getting from nothing to a coherent first version with the right structure, the right evidence, the right files, and the right risk posture. 5.5 compressed that bit better than any model I've tested. And that's the first hard test. 5.5 looks great here when the job is a messy

executive handoff. The second hard test is where the review gets a little bit more complicated. So, Splash Brothers is a fictional mobile detailing and car wash business with 465 files and the folder is intentionally gross. There are CSV exports, Excel sheets in three different schemas, JSON backups, a

corrupted JSON file, VCF contact cards, scanned PDFs of handwritten receipts, text notes, conflicting service list, inconsistent payment records, and a pile of junk that looks like the kind of junk a real small business accumulates over years of duct tape operations. The assignment is to migrate the entire

thing into a clean database. That means the model has to inventory the files, decide what matters, parse multiple formats, design a schema, extract the records, merge duplicate customers, reject fake records, normalize services, reconcile prices, detect conflicts, preserve source providence, write a

migration report, and build a review UI. This is not glamorous work, but a huge amount of real business work does look like this. The planted traps are a mix of obvious and subtle. There are fake customers named Mickey Mouse, test customer, ASDF, ASDF. There's a fake $25,000 payment. There are duplicate

customers, name typos, service name variants, inconsistent date formats, messy payment statuses, and payment methods scattered across many different capitalizations and labels. And then there are the less obvious traps. An orphaned order tied to a customer named Terren Blackwood, a service code

conflict, a handwritten receipt image that could easily produce false canonical customers if the OCR step is handled sloppily. Now, in previous checks of this evaluation, both Opus 4.7 and 5.4 fell out in some important ways. for example, both thought Mickey Mouse was a real customer. Test customer

became a real customer. ASDF ASDF became a real customer. The fake $25,000 payment got normalized and counted as revenue. Those are the mistakes that make you sit up straight because a real human catches those really quick. If the model misses them, you can't treat the migration as production safe. 5.5 is the

first model to catch the mistakes I planted in the data on purpose. It rejected Mickey Mouse. It rejected test customer. It rejected ASDF correctly. It rejected the fake orders and the fake $25,000 payment. It correctly merged all seven planted duplicate customer pairs. It caught all 13 named typo orders. It

discovered all 465 source files. It produced a deterministic rebuild of the database. It generated a 7,287 line migration report with a per file audit trail and it landed at 186 customers against a target of 192, which is pretty close. My previous conclusion running this eval has been that no Frontier

model should be safe to trust with a oneshot business data migration. 5.5 narrows that claim down, but it doesn't eliminate it because 5.5 still missed service code conflicts. Its schema did not include a service code column, which meant one of the planted conflicts could not even be represented in the final

output. It did create Terrence Blackwood as a canonical customer instead of setting that record to human review. It left payment status with 29 distinct raw values and left payment methods unnormalized and overproduced services and jobs and built a review UI where two parts of the interface disagreed on the

number of flagged items. And that failure pattern is very instructive. 5.5 got much better at the errors that are semantically obvious to a human. Fake records, duplicate people, typo names, absurd payments. It still struggled with the boring back-end hygiene that makes a migration durable. enum normalization,

service code preservation, orphan handling, canonical job grouping, and reconciliation between dashboard counts and database counts. So this is my practical read. I would absolutely use 5.5 as the first serious pass on a migration like this. I would ask it to inventory the files, design the schema,

build the extraction pipeline, preserve source providence, generate the audit report, and produce the review UI. But I would not let it declare the database canonical. I would add validators. I would check row counts. I would inspect enum maps. would require service code in the schema and it would have a human

approved canonical merges before anything left staging. That's not a criticism of 5.5. That's just the correct way to use it. The model can compress a fair bit of the middle of the work, but production trust still comes from the system you build around it. One important caveat on the 5.5 Splash

Brothers results. I compared it directly to 5.4 4. And what I saw is that the backend work that I'm calling out as an issue with 5.5 was actually a little better with 5.4. And so we're in this interesting position where you can see some regression in 5.5 around some of the back-end database hygiene discipline

that 5.4 got right. But you see a lot of progress when it comes to the intuitive stuff that a human would catch very quickly like the Mickey Mouse example. So what I want to leave you with is one, no model is perfect. Two, if I had to pick right now, what I would do is I would use 5.5 prompted carefully for

clear, complex work on the back end and I would trust it more with that front-end intuitive work that adds a layer of polish to the finished database migration effort. All of that to say, understand that when you're testing models at the frontier, you're going to get interesting results like that.

Places where the model regresses unexpectedly. This is exactly what we would expect from a model tested on a private benchmark because you see places where the generalization just doesn't work as well. This is something that's easily fixable with a harness and a good prompt. My prompt here was intentionally

messy and badly formed and that's part of the challenge. So, not something you need to worry about a whole lot if you're using 5.5. Not a reason to go back to 5.4, but a call out for those who like to dive deep. When you put Dingo and Splash Brothers next to each other, the picture of the release gets

more complete. Dingo says 5.5 can get remarkably close to a real executive handoff. Splash Brothers says it can do a serious first pass on messy production data, but it cannot be the final authority. The third test is different yet again because it shows the part of the OpenAI stack that still needs help.

The Artemis 2 test asks the model to build an interactive 3D visualization of NASA's Artemis 2 mission. No facts are provided. No tech stack is specified. The model has to research the mission, build the SLS vehicle, animate the launch all the way through lunar flyby and return, and create the environment,

add the controls, support timeline scrubbing, make components clickable, and make the artifact ultimately educational. This test is very different from Dingo and Splash Brothers. A model can get the research right and still build a very ugly visualization. It can build something beautiful while

hallucinating the mission. It can animate the rocket but fail at the controls. It can produce something technically interesting that no one wants to look at. Both 5.5 and Opus 4.7 got the core mission shape right here. They understood that Artemis 2 is a lunar flyby, not a landing and not a

lunar orbit. The trajectories were not perfect in either case, but they're reasonable for a browser visualization. Neither model collapsed Artemis 2 into Apollo or Artemis 1 or Artemis 3. Now, the key difference that showed up was in presentation. 5.5 leaned into information density. Clickable bubbles

and panels and dense labels and multiple ways to surface facts. If the goal was to learn, the 5.5 build did a lot right, but visually it looked more cartoonish than it should have. The scale felt off. The proportions were not as grounded. The scene lacked the visual authority that a NASA mission deserves. Opus 4.7

made the opposite trade-off. The visuals were substantially stronger. Better lighting, better composition, and a more grounded scene. and it felt more like something you would actually want to show someone, but the information was less immediately discoverable. Neither model nailed the controls. Both needed

another pass. Opus had a sort of strange semi-transparent Earth issue. 5.5 had scale and style problems. If I were turning either one into a final public artifact, I would probably start from the Opus version and add 5.5's information density over the top. And this is where routing starts to matter,

right? I I don't yet trust 5.5 to invent by itself a beautiful front end or visual style from a blank page the way I trust Opus. Claude still has an edge in visual composition and taste in blank canvas front-end craft. But I do trust 5.5 to implement a strong visual reference faithfully. And that's why

images 2.0 changes the workflow. Instead of asking 5.5 to invent taste from nothing, you can generate a strong mockup, hand that image to 5.5 inside codeex and ask it to build the working version against the reference. Inventing taste is hard. Implementing to a target is much easier. That's the practical

difference between just picking a model no matter what and like figuring out what actually works. I'm not here for blind model loyalty. I'm here for finding the real ways we can use models in harnesses to get work done. If I need backend volume, audit depth, tool use, and completion, I'm going to reach for

5.5. If I need a blank canvas, visual taste, I still want Opus. If I need a strong user interface that actually works, I increasingly want a reference image plus 5.5 in codecs. Now, I hope the larger pattern is coming into focus here. 5.5 isn't perfect. It's not magic. It's not the best model at every task,

but it is the strongest default for complex work that I've used because it carries more of the task before it drops the thread. Which brings us to the fourth part of this video. Why codec matters so much for 5.5. I've been using codecs more than Chad GBT for serious work recently and 5.5 makes that

distinction much sharper. Chad GBT is still a broad consumer surface. It's good for quick questions and search and image work and voice and general assistance and fast thinking. But codeex is increasingly where work actually happens. That matters because a model this strong trapped inside a chat window

is very underused. Inside a chat window 5.5 can tell you what to do inside codecs. It can inspect files. It can edit code. It can run commands. It can drive a browser. It can test interfaces. It can read docs. It can generate artifacts and iterate on its own output. That's a different product. The model's

not just responding. It's working in the environment where the task lives. This is why the model plus system argument is not an abstract one. In 2026, most useful work still doesn't happen in clean surfaces. It happens in messy folders with web apps, with PDFs, with spreadsheets, with desktop interfaces,

with internal tools, with half-maintained systems and documents that were never designed for automation. A model that can operate across those surfaces can reach much more of the world than a model limited to a text prompt. In 5.5, inside codeex feels like a step in that direction. It can hold a

task across many, many steps. It can inspect the codebase. It can run a test. It can hit an error. It can revise the plan. It can patch the file and test again and then tell you what changed. It's a monster. It can generate a document and render it and notice the layout is broken and fix it and

rerender. That's the kind of work where intelligence and agency multiply each other. A smarter model matters more when it has tools. Better tools matter more when the model's smart enough to use them without constant supervision. That's the loop 5.5 improves inside codecs. And this is also why

availability is a part of product quality. The best model in the world is not useful if you can't use it when you need it. Compute constraints show up as caps, as degraded experiences, as slowdowns, as weird routing decisions, as limited sessions in moments where the model you want is just not available.

The public status pages from Enthropic and OpenAI tell a real story here. Anthropic's 90-day status page has recently shown materially lower uptime across claude, the Claude console, the Claude API, and Claude code versus OpenAI status page. And to give you a sense of that, we measure reliability in

nines. And many of anthropic services are at one nine of availability right now. That means 90 some percent, right? Not 99, 90ome, maybe 98. It's not the same thing. By contrast, Open AI services as of this recording are showing three nines in places, sometimes two nines, but every nine of

availability indicates another step change in value for a model that has to be up all the time for real world work. And so if you're doing serious work, you have to ask yourself, am I willing to tolerate gaps in compute? And I share this not because I'm reasoning only from the numbers. I think the numbers tell a

story that we're also hearing in anecdotes from serious Claude users. There have been widespread reports coming into me personally and also across the internet of frustration with Claude's availability over the last month. It is not an accident that Enthropic has cut deals for more than 10

gawatts of compute in the last 30 days. It needs it because right now demand for Claude is outstripping availability across the board. And when demand outstrips availability, you do have issues. And that's why I want to call out the reliability you get with 5.5 does matter these days. And that may

flip, right? This is always an ongoing journey. As Daario says, the rainbow continues. We'll see what the next chapter has. Without further ado, here's how I'm routing work now based on all of this testing. For complex multi-step execution, 5.5 is now my first call. If the task involves files or code or tools

or documents or browser use or data or spreadsheets or artifacts or anything that has to be carried through multiple steps, I start in 5.5. The longer and messier the job is, the wider that gap feels. For blank canvas front-end taste, I still often start with Opus 4.7. Claude continues to make stronger visual

designs when there is no reference image and no design system. And that does carry through into beautiful PowerPoints, maybe beautifully designed spreadsheets, that kind of thing. If the question is make this beautiful from scratch, Opus is still very much in the conversation. For UI work where I want

both taste and production strength, I want a reference first. I could generate the mockup with images 2.0. I might also start with Claude design and let them bake off. Uh I could use a screenshot. I could give the model a clear visual target. But regardless, I'm going to hand it over to 5.5 Codeex and ask it to

implement that work faithfully and see where I get first. And then if I want to, if I'm starting with cloud design, I feel like claude design came out with a stronger model, then maybe I'll give it to a bake off between cla code and 5.5. But either way, I think 5.5 ought to be in the mix because of the strength of

the model at longunning code execution with high correctness. For engineering work, I like a two model workflow as well. Opus 4.7 is strong at planning, at thinking through the shape of the work overall and the customer value. 5.5 in codec is excellent at execution, at testing, and carrying the work through.

Combining them together is often better than pretending one model should own the whole pipeline. For writing, 5.5 has taken a real step forward, and the improvement is not just sentence quality. It's structure. Most AI writing failures are shaped failures. The model writes an introduction, a bunch of body

sections, and a conclusion, but the argument doesn't build. The sections sit next to each other instead of moving the viewer forward. The transitions are generic. the nuance gets kind of averaged out. The piece answers a prompt instead of actually writing well toward a case. 5.5 is actually much better at

holding the shape of a long argument. It still needs taste. I would not publish raw output without editing, but I'm willing to trust it with more of the structure and more of the first serious draft than I was with any previous OpenAI model. For data work, I use 5.5 aggressively, but with validation built

in. Don't ask the model to finish the migration and trust the results. Ask for source provenence. Ask for rejected records. Ask for duplicate logic. Do that detailed prompting. Splash Brothers is our reminder here, right? 5.5 found Mickey Mouse. It still missed the careful backend hygiene and there was a

bit of regression there. For research heavy work, I want the model to dig into sources and uncertainty and I need to expect to do that myself before I approve it. Artificial analysis actually flagged this by calling out that the model felt overconfident even as it did excellent work. And that's an

interesting nuance with 5.5 that you should be aware of. So use 5.5 as the default for serious execution. Use opus where taste and critique are better. Use images 2.0 or a reference image when visual direction matters. Use validation whenever the output touches anything serious, right? Money, law, operations,

production data, or anything where being confidently wrong gets very expensive. The future of AI use is not one model people. It's routing. The people who get the most out of the frontier are going to be the people who know which system to use for which task. But today, if you force me to use a model that tends to

become a default for a lot of different work dayto-day, my answer is going to be 5.5 and codeex today because that's where I see the most value right now. So the bottom line is this. 5.5 is the strongest model in the world today. And the ways in which it is the strongest matter more than the ways in which it

isn't. It's especially good at complex, messy, multi-step, toolheavy work. It's meaningfully better at long writing structure than previous OpenAI models. It's great inside Codeex. It benefits from the surrounding OpenAI release cadence in a way that few model releases do. Images 2.0 helps with visual

direction. Codeex gives the model a place to act. 5.5 supplies the reasoning and persistence to do real work. The three tests tell the story in a way that no single publicly available benchmark will do. I think Dingo shows the promise of complex executive level knowledge work. 5.5 can take a strange business

situation, a pile of evidence, and produce something that's sort of usable as a first draft for an executive handoff. The Splash Brothers company example shows the issues around duplicates, around fake records, uh, but also shows the promise in catching some of those things that only humans have

caught previously and no previous model caught, like the fake customers. Artemis shows where you have to really think through visual presentation because 5.5 was strong on information density but just couldn't produce a final artifact that was as stunning as beautiful as Opus did. None of this is to suggest

that 5.5 is a replacement for human judgment. It is not the best taste model on the frontier. It is not safe to trust blindly with final production data. I would trust no model blindly with final production data. It still needs review and validation and direction from someone who knows what good looks like.

But it is the new high watermark for what a single model can carry in real work. And high watermarks matter. They change what users are willing to try. How ambitious the prompt gets, how much work we will delegate, and what products become possible to build around the model. I'll give you a couple of

examples that are really fun here. There are new million-doll businesses waiting to be built around the capabilities that 5.5 unlocks. And I've illustrated some of the challenges that the model can tackle in the tests I've done. Two business ideas. If you're interested in the combination of 5.5 and images and

codecs, like what can you do with all of those together? Number one, there is probably a million-doll small business waiting to be built in the Apple App Store or somewhere like that for palm reading because images 2.0 can provide a reasonable palm read and codeex can help you build a app for that task with a

front end designed by images 2.0 itself. That's an example of how you can tie all of those three release products together into something that is not enterprise scale at all, but it's definitely side gig soloreneur scale. Another example, you can get a custom Lego business going because images 2 is now good enough that

it can design for you a small Lego set from a prompt with accurate part numbers from Lego. And so you can imagine you can use codecs to start to put together an app for that. You can use images too to design the UI and images too to power some of the custom Lego presentation and then you have to figure out the supply

chain on the LEGO side. But it could be a fun little business for someone. And I'm not saying this because 5.5 is only going to be useful for small business. But I am calling it out because I think oftenimes people hear me talking about enterprise use cases and they think these models are only good if you have

500 or 5,000 or 50,000 or 500,000 people in your company. That's not true. These models offer individuals really cool opportunities to build new stuff. And the two examples I gave are not businesses that were really possible even a week ago. And so look for those as ways to see how models improve. Look

for those kinds of examples. And I'm going to close with this reminder. If you are testing models from here out on easy tasks, you are missing the point. The previous models are already good enough for easy tasks. to see what changed, you are going to have to give it the kind of work that used to break

models just a few months ago. The multi artifact briefs, the data piles, the agentic loops, and more. And you can't really do it in a chat window anymore. The chat window use case is saturated. When you test that way, this release starts to make sense. The model is smarter in quick mode because the

underlying pre-train is better. I think it is stronger in thinking mode for the same reason. I think it is. OpenAI won't release these things and tell you this is what we're guessing. It is better wrapped inside codecs than any previous OpenAI model has been. It pairs naturally with images 2.0 on visual work

and it appears available enough to become a daily default rather than a special occasion tool. So the old question feels too small. The interesting question is not can 5.5 answer better than 5.4. The interesting question is what can I now ask it to do? And for the first time in a while, that

question has a much bigger answer than it did a week ago.
