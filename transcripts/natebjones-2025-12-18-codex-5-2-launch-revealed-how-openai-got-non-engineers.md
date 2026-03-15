# Codex 5.2 Launch Revealed: How OpenAI Got Non-Engineers Shipping Real Code

- **Channel:** AI News & Strategy Daily | Nate B Jones
- **Date:** 2025-12-18
- **Duration:** 69:17
- **Views:** 9K views
- **URL:** https://www.youtube.com/watch?v=tuLWIK1AVEM

## Transcript

So, a couple of days ago, I had the privilege of sitting down with two members of Codeex's engineering team. I got to talk with uh Tibo, who's pretty well known as an engineering lead at Codeex, and also with Ed, a design engineer. Our focus really isn't the code. So, if you're like not a

developer, this is still going to be super interesting for you. Instead, what we focused on is how does codeex change how OpenAI works? And in particular, when you're talking to someone from a non-technical background like Ed and a technical background like Tibo, how do our workflows shift? How does what we

build change when you have codecs as effectively a teammate? What does that look like in practice? I think we often talk about AI native organizations, but I wanted to take this chance to sit down with a truly AI native organization with OpenAI and actually learn how they use codeex day-to-day and how it's changing

everybody's workflows, not just the technical team. So, jump in. This is going to be a fun one. Well, maybe first like I'd love to hear a little bit from you guys about who you are, how you came to open AI. Uh I know that everyone has their own story here and I'd love to hear a little bit about yours.

Yeah, nice story, Ed. >> Yeah, I'm a designer on Codeex. Um, been in Open AI just over a year. I've been on Codex for about six months. Before that, worked worked in the research team. And yeah, I've always worked at the intersection of design, design, engineering, and research. Worked on

robotics before at Google and a few other things before that. >> Yeah, I uh worked at Google as well uh finally like I didn't know we shared that piece of history. Always figuring things out. So at Google very briefly, moved into uh Deep Mind, worked there for many many years.

>> Mh. >> And then uh decided to like do the big jump and like go to the US and come here and work for OpenAI. That was like about a year and a half ago. Uh that was pre-reasoning like a year and a half ago. That was pre >> Yes. And so in typical OpenAI fashion

joined just before uh that happened like was part of like the 01 sprint. I was more like trying to be useful in any way possible and then uh after that like kind of stuck around built some tooling for research became super obsessed late last year around uh hey like maybe models are going to continue to improve

and their capabilities are you know going to continue to uh impress us and maybe actually like we should think more about the products the infrastructure around it to really benefit from those models and then uh started like prototyping you were working on similar things.

>> Yeah. Uh and we we we were not working together initially and then we joined efforts >> earlier this year. >> Yeah. Yeah. >> And that's that was sort of like how Codex got started. >> Yeah.

>> So you guys were there from the beginning with Codeex. >> Yeah. >> Yeah. I mean it's had a long history, right? Um right. Coding agents had openi you know the name Codex is a throwback to a model which was like you know prejudg I believe right. So coding

agents have been around but the yeah codeex as it is now is >> yeah codeex is the the product uh that was like released what in April this year. >> Yeah. >> Amazing. So one of the things I I'll just ask you what I get asked about

codeex because we get to chat and we get to find out. Uh this is like the number one question I get asked is how do engineers at OpenAI use codeex daytoday? again two different patterns. Um it's like one is everyone just doesn't have a choice on like the code is reviewed by codeex uh no no matter like whether

whether you want it you know reviewed or not it's just been like so useful at catching issues and then there's a lot of um casual usage uh by you know even like nontechnical staff and then what we're also seeing is like at the complete end of the spectrum is like really power users of codecs that deploy

a lot of compute a lot more than know we saw even like a couple of months ago and this continues to increase and increase and increase and um with increasingly uh complex workflows some of them multi- aent you know running like for many many hours >> and so it's a highly personal thing uh

still feel like it's very evolving >> that makes a lot of sense yeah go ahead >> yeah so as I say you know I'm a designer on the team so work very closely with engineers But I'm very much in the codebase a lot myself. And you know, I think the cool thing about Codeex and these recent models over the past few

months is they really have been a step change. And what you've seen, I think even since we launched our most recent product suite is basically everyone at Open using it. You know, I like there's one engineer that I know who uses it for for everything for note takingaking for like it's basically

his like primary interface to his computer. Um, as a designer, you know, I'm seeing more and more in our like work in progress channel on Slack, people posting these demos. And, you know, I DM someone, I was like, I didn't I didn't need a code. And he's like, I I couldn't till a few months ago.

>> Um, so you've got kind of, you know, design engineers like myself hopping in more, submitting more PRs and kind of getting closer to the, you know, closer to the details. And then even even new people, nontechnical people, go to market stuff even, you know, people are really like hopping in and it's just

like this kind of force multiplier. Yeah, that that's exactly where I kind of wanted to chat because I think that for a lot of organizations that remains the dream, but maybe it's something about the command line uh in the terminal sort of scariness that comes with that. Uh but for whatever reason

people find themselves sort of hard limiting a lot of these technical tools to engineering teams. Uh sometimes that is literally at the level of the IT policy. have been in organizations where the IT policy only allows engineers to use tools like this and if they catch you doing this as a

non-technical person that's a violation of policy and I think some of these older ways of working and thinking are having to evolve. >> Yeah. I think the lines are what we're seeing is like the lines are blurring like Ed I mean you're sort of like everywhere like ideulating about the

future but then also like very much like using >> codecs every day and then feeling you know does it feel right like pulling up like you know PRs and little fixes >> there's like how you know that's so evolved very quickly right >> totally yeah yeah and I think yeah you

know to your point there's there's there's kind of one half of it which is like how do you how do you bring organizations along and you have you know particular some of these large organizations might have some more like institutional challenges but um but you know once you get access I feel like

it's kind of getting easier as easy as possible um so you know you mentioned that it might feel like a bit of a step up for people to get in the terminal I think the cool thing with some of our products recently is you know we've shipped an ID extension so we're not just in the terminal we have a CLI

product which we've had for a little bit >> but you know we could we meet people where they code so they might be in VS code they might be in cursor these other kind of idees um and we also have a web product. So you know you can uh you know once you kind of connect all the enterprise uh you know uh kind of puzzle

pieces you can just go in a web product type in a prompt and create a fix. So for example, you know, say you're you want to change some UX copy, you're a copywriter, you know, maybe you don't even need to look at the code, you just want to change some strings, you can just do that yourself, right? You can go

in and you can type this prompt if your kind of enterprise is set up. So um yeah, I think like the number of surfaces that people working across and just like yeah, just makes it kind of easy and easier to get involved. >> Yeah, I I think that there's that that ease of access piece you guys have done

a nice job solving for over the last few months. I think the other piece that I heard as you were talking is that there's a little bit of a healthy constraint in something like having codeex review every PR like doesn't matter it's getting reviewed you have to engage with it and I I think that's also

going to be new for a lot of organizations I talk with >> and the thing we're we've been very careful about is also optimizing for like signal to noise ratio and making sure that the hit rate is very good >> so that people don't actually complain and like you want to turn it off.

>> And overall like as an organization we're getting like way more value out of it than you know potentially sometimes the misses >> and then we keep like improving you know the system and the model over time so that it's capable of finding more and more gnarly and like subtle issues over

time. Uh and people are generally impressed. It's like I hear it all the time like it's like oh this thing is super human. It's like it's doing reviews I would never have done because I don't have the time to dig like four layers deep into the stack >> and just having that always on you don't

have to think about it. You have that safety net that's just there. >> Yeah. Super interesting. Like I think particularly something like code of view as a designer I was thinking through the user experience right it's like oh no is everyone's just going to get loads of emails and um you know it turns out that

like it's like one of the most loved features that I think we've shipped and that the one of the things that changed for me was seeing some of our top contributors across OpenAI not just our team you know commenting in in our Slack saying like this is as you say super human um and you know I look forward to

like those notifications now like it really just like it just adds so much value >> like I think there are two things that are emerging right So like this ambient intelligence and code review is like one example of that where it just happens. You don't have to trigger it. You don't

have to think about it. Uh and you just benefit from that intelligence being deployed. Then the other thing is people starting to use it as like a little assistant in their computer. Like it's not really about code. It's like it does like you know CIS admin task you know pulls like context and you know maybe

the latest news for you and >> um it's just like or craft like some new designs and new ideas. Um and then like for that the current way that we're doing it in the CLI and the extension it's like you're instant uh and so like the current interfaces are maybe like holding things back a

little bit. >> Yeah. It's kind it's kind of like it's kind of both ways really like in in some ways you know there's this throwback to the terminal that that people are getting nostalgic about and you know from a design perspective there are these kind of two counts once is is one

is this it's this kind of parlor trick it's this like transitory you know kind of like form factor and actually you know there's this like perhaps there are some like new interaction paradigms that we're like pushing towards but perhaps aren't there yet. On the other hand, I think like the constraint of the promp

box um you know the terminal like it it's kind of perfect as well for a way right it meets you where you are and it's very cool to see the workflows that people have built around that. So you can literally you can just spin up your terminal and you can yeah as you say right you can write notes you can do all

of these different things from just like s such a simple form factor. Yeah, I I think one of the things that has surprised me like I if I go back to that idea of a non-technical use case for codecs, uh I find that codeex is an extraordinarily logical model and when I'm using it for

a non-technical use case, >> I find that there's a sharpness and a conciseness about how it evaluates a particular set of inputs that feels like I I can see where it came from. It feels like of course you would get this from a a model designed for code, but it turns out that there's a there's an

extensibility to that to that emergent property that helps with a lot of other things. And so like I did a business case analysis and it wasn't technical, right? Like you're analyzing business inputs like revenue and you're analyzing uh sales figures, etc. >> But it applies that same rigor and it

turns out that you get a response that's really coherent. It's really clear. It's cogent. It makes sense. It's easy to read. And it's as a result very very useful. And I just I love the idea that these models end up having extensible properties that perhaps spin off of what they were originally designed for and

allow us to do lots of other things. There's that element of hey this model is trained to be like precise uh and and correct about things and diligent and you know double check maybe trip trouble check its work sometimes and not do all the math in its head right or in its context and maybe write

a little Python script to help itself out. I use it for data analysis like all the time. Uh, and it's not about the code anymore, right? It's it's about the result and like trusting the steps and like as you as you put it, >> it's like a very cogent like legible explanation. You can like see step by

step like what, you know, why it's doing things? Uh, and then there's a question of like at what point, you know, for these kinds of tax, do you still need to look at the code? Is the code just a tool that you don't really care about? And then you're using that as a stepping stone. So then then you have like a

coding agent that's maybe evolving into like you know a more general kind of assistant. I guess that's an interesting thing to think about. >> Yeah. Yeah. In terms of the use you know you mentioned about kind of like you know design showing up in different places. Um and I you know I think the

same way about some of the use cases for designers. So like on the one hand there's like fixing the paper cuts of you know cuz we're in these tools all day every day like literally eight hours a day. You know any small any small paper cut that you get you just see and you can fix it. And obviously, you know,

you're submitting a PR, it needs to, you know, you need to look at the code that you're generating and, you know, we can go through the review process. But if I'm in like a very different mindset and I'm in like design, you know, idiating mindset like, yeah, maybe I can just make my terminal really small, don't

worry too much about the code, just have a local host open and basically, you know, just like narrow this gap from like kind of, you know, thought to to product. Um, and really just focus on the interactions. you know, you can move it, you can think about responsiveness and and that kind of stuff becomes more

important and it becomes more like a canvas. So, you know, similar to if you're writing, very different use case, but you know, also like a very different way of designing. >> Yeah. Because for so long design has been effectively disintermediated from engineering and like coming from a

product perspective, so much of the role traditionally was translate design into something that has requirements that engineers can build against. And so there was always this tension between PMs and engineers and designers when I was coming up where it's like everyone has different incentives. Everyone and

really it's all just a function of disintermediation. Like if you take away the gap and you give everyone access to the code, it's a different world. >> Yeah. Like often it's like hey Ed it's like you're just like an engineer on the team right like writing PRs and just fixing things. You don't need to go and

talk to anyone. You just do it. >> Yeah. Yeah. And I think some of these boundaries as well as you say they're kind of slightly artificial. Um you know they've grown up um you know first we had the terminal and then with you know Mac we then were like started to think about the guey and these kind of new new

disciplines emerged and they're kind of just converging and and and diverging over time. Yeah. >> You don't like being an engineer? >> Oh no no I mean I I yeah I don't know what I call myself now. I think that's the cool thing. >> There's an identity crisis where it's

just like what am I? Yeah, I think that we're getting into a world where job titles matter less and skill sets matter more. Um, and it's really it's exciting to see what happens when people can wear those hats lightly and just focus on what problems they can solve.

>> Yeah, it's it's it's really a lot it brings a lot of clarity. It's like it's all about the problems, >> figuring out what problems to solve, figuring out what questions to ask yourself. so much more is possible and it's much more cheaper to ideate and build and then you find yourself like

being like, "Wow, you know, I really need to be crisp about what I want to go and do." >> Yeah. >> Um it's exciting, but it's also nerve-wracking at the same time, right? >> Yeah.

>> Good ideas matter more. >> They do. And correctly aimed ideas matter more, I think. >> Yeah. The speed and velocity, right? like which direction you going in, >> how fast you learn, like you know those most successful like teams are that we see emerge at open air like really small

teams that set themselves up as well to like learn and iterate super fast. Uh and then there's like a general sense of like oh we're building towards this uh but then like also changing things like is cheaper. Yeah, it's I mean there's the phrase right which has gone around in engineering for a long time which is

kind of code wins and you know you can write as many PDs as you like but until you have the product in your hands and I think that's the very the cool thing that I've seen from like product team is broadly defined whether it's you know designers engineer it's like you know if there's a hackathon like at the end of a

hackathon like you'll have like a fully working product like you won't just have like a kind of you know throwaway react demo like you had before which I think is like super exciting and then yeah this you know the hard decision is then what do you build like you know which which you know which company do you do

Gina nar down? >> Yeah. Often times I mean you come up with like a new idea feature like an entire product and I have like to do it like a double take because it's like it's not like a static thing. It's just I'm like this thing is fully functional like it's almost

chippable like how did you cook this? >> Yeah. Yeah, the cool thing I think about um this is I think this is another fun angle which probably hasn't been explored that much a little bit in kind of like design engineering which is like you know the kind of old world is you're a designer you work in or or you know

product manager for that matter you work in a document you work in a a file and it's this like throwaway piece and then you throw it to the engineer and the engineer kind of productionize it right but now like you know some of the demos that that Tibo was mentioning um I'll just create a fork of the repo and it's

like it's not just demo. It's like a fully functioning thing and like obviously to move fast I've you know taken some shortcuts and like there there's going to be a you know it's going to be a little rough around the edges but um but yeah the fidelity that you can get to is is amazing.

>> Yeah, there's one of the pieces you just used as a throwaway line that I want to dig into a little bit. You talked about this idea that you like come up with an idea and then a team forms around the idea to get that idea to fruition. And I feel like that's a little bit the story of Codeex, but I think it's also an a

story of a new way of working. And so I'd be curious for you guys to share a little bit more about what that feels like on the inside. >> It feels like we are co-evolving Codeex and the way of working. And so Codex is evolving as fast as we

have to adapt to, you know, the new possibilities that it creates. And it's it's it's quite a challenge like but fortunately one thing that's become very clear is like humans are still like the very best at adapting quickly to things. >> Uh and isn't it quite insane to think like earlier this year none of this

really existed. Um >> and like now like I it's very rare to find someone who still codes like without like a little agent by their side. So I think you know we're going to continue to see that. It's pretty clear to me small nimble teams tend to like produce incredible results and I think

that's going to continue to be true. >> Yeah. No, I'd agree. I think Yeah. I think that the really interesting observation that I've seen is just I've been so surprised at how fast people get used to used to these new step changes. you know to Z's point I also joined like just before our reasoning models and I

remember at the time we were talking about it's like ah that you know going to ship this reasoning model it's it's obviously you know the kind of sits on top of all of this research and it's been this you know really huge research project um you know for the company but again it was this lowkey research

preview and it just it was such a step change um you know in in so many areas and if you think about where we are now um and you know I just look at how fast the different teams I've worked in over just the past 6 months. And it does just feel that kind of every few weeks or every model release, you know, we kind

of like push this frontier even more and then a week later, you know, you'll be in some agent loop and you'll get a bug and you'll be like ah this model, you know, like getting frustrated and then you're like you forget forget that it's like, you know, this is insane. So it's just it's one of those, you know, it's

just like, you know, you could apply the same to image generation or video, right? you know, we shipped Sora and it's like mind-blowing and then you see this tiny, you know, this tiny fragment and you're kind of like, oh, you know, but you forget, you know, you zoom out and you just become used to these things

so fast. But super point, I think the cool thing is it's just super empowering for small teams. Um and you know even some of the junior engineers that that that that we work with who you know perhaps are only a few years out of university you know the kind of the breadth of work that they can that they

can do and the kind of big swings that they can take you know I think just even within the past few years has really kind of accelerated their work as well. Yeah, we've got Ahmed on the team. He joined as a new grad. >> Didn't know Rust, learned Rust super quickly. I've never really seen one like

pick up like a new language like as fast as that and like, you know, get productive. And then it's the way that he manages to uh like accept the technology and the potential and like discover the true potential of agents is I think faster than most people on the team. Uh and so

there's sort of like that superpower of like how quickly are you willing to try and adopt new ways of working as well. Um I've seen also like veterans like you know 10 years in the industry like you know kind of stick to their um you know more traditional ways of like developing and uh it's tough. I'm not sure which

one you know is more effective but it's pretty clear to me like you know jump like three months six months from now it's like you know it's going to be very clear which one is more effective. >> Yeah. I I think honestly it'll be a surprise to a lot of folks to hear that there are junior engineers at OpenAI

simply because there's been a widespread perception over the last 12 months that these tools can dramatically accelerate people who know enough of the business context and have the experience to utilize them and then juniors coming in like I hear from juniors directly saying I you know can't for the life of me get

a role anywhere uh because I don't have experience and now you also need to have the ability to have that experience and leverage it with AI and it's even harder and higher. >> But you you guys have juniors and they're apparently doing very well. So, what what's that been like?

>> It's been awesome. Uh I think it brings such a joy uh to to work as well and like fresh perspective and then keeps like us grounded. Um >> and I have been delightfully surprised uh about like you know how well that's been working for us. Uh and it's changed my perception as well of like you know

what is important like know this adaptability. Um, and then like a lot of it was as well like Ahmed, I'm just going to take Ahmed as an example, but uh, sorry Ahmed. Um, he he was sort of like he grew up almost with this. Uh so it's like he

it's it's it's not quite true but you know it will be true at some point where it's like life before coding agents you know background ambient intelligence like you know having a little assistant like in your terminal like that was not a thing and so it's just supernatural to them like whereas like for me and others

sometimes I'm just like oh you know it's like I'm going to go back to Vim and like you know just like that and like I don't necessarily like resort to like using it in the right Okay. And I'm like slowing myself down in a way. And then you you look at the way that you know they are using AI today and you get

inspired. And so it's been actually really interesting of like how they've been able to level up the rest of the team uh who is like on paper more senior right >> and a combination that I've seen work very well is where we do spend a lot of time on the general architecture of a

codebase. You know it's like the principle of software engineering still remain uh and then once you have the right scaffolding then you can just go and like and run and be extremely fast and proficient because the agent goals just like respect the general scaffolding and the boundaries that

you've set. Reading between the lines a little bit, >> it sounds like the quality of character that is most important that you guys are seeing on the ground as you work with these models and to your point evolved teamwork with these models. I is it around openness to experience and

learning new things and the ability to adapt quickly and that's something that really whether you're junior, whether you're senior, whether you're technical, whether you're not technical, that's what you got to have in the AI age or is there something else? I

>> It's interesting. I mean, you know, I interview a lot of designers. It's they're definitely qualities that I that I look for um you know, when hiring. But I you know it's we I mean we're just we're we're going through a you know bit of a step change technology wise and I think it's just you know being open to

those new ideas being open to using those new tools is you know is definitely helpful. Um you know if I think back to I'm a child of the the internet you know I kind of grew up pre- internet and post internet. I kind of feel like we're at the same, you know, the same point now for like software

engineers, creatives, designers, kind of, you know, preAI, postAI. And I I'm seeing more and more people who are like, you know, maybe skeptical or like, you know, learning about a little as, you know, as TA says, kind of setting their ways perhaps they have their workflows, you know, dipping their toes

in and just seeing the seeing the crazy benefits and and from there like moving forward. that I think curiosity and willingness to engage is the one most important thing right now. Uh and it's clear that we're only at the very beginning of you know what's going to continue to evolve

like model capabilities are going to continue to increase like we are not seeing really a sign of a slowdown like the 5.2 2 that just came out. Uh, you know, it's a very strong model, but it's also, you know, one of, you know, many more to come. Uh, and like we have like a very clear research road map there

that like a lot of the of the team and the rest of Open is excited about, but it's just to set the reality is like this will continue to revolutionize how we do software engineering. So if you're not if you're not willing to accept that you're it's going to be tough and like

people who are like curious and are focused on solving problems and are out there in the world and are like hey just like how can I help people's lives you know how can I do this thing faster um you know they're the ones that are having a great time right now that's really been true uh the stories

that I know that are positive hopeful exciting tend to be correlated really closely ly to people who have like a nose for interesting problems and who have a curiosity to solve them and just look at AI is this really cool super tool that they can use to solve those problems.

Like I know uh someone who I think he started out as a music major in college and now he's a technical founder >> uh because he felt like being one, right? And so and now you can do that. And he just went and solved problems for customers. And I think that that's one of the things that I find most

interesting about the trajectory that we're on is that those stories become more and more plausible, right? >> Yeah. I I think I think it's it's maybe one of the underrated or underrated parts of it in that I think there are a lot of you know really valid concerns that people have but I think the thing

that people um you know don't focus on as much is it it is an equalizer like you know if I think of you know when I when I got into design to design as a kind of teenager you know I was I was doing a lot of animation I was kind of hand drawing things I was like doing a lot of creative stuff making movies with

my friends in my you know in the garage you had to build a green screen you had to you know buy the camera which was expensive you had to get you now with like kind of $20 charge of DC subscription you can as a creative make like basically anything uh right you get access to codeex you get access

to all these other things so in many ways it's an equalizer but it does require leaping in as you say kind of having that curiosity and yeah and really like throwing yourself in and learning all about it but you know if you're curious then yeah there's so much >> we still have complaints that usage

limits and rate limits are too low but when you think about it like $20 a month for like a prolific software engineer that can help you get stuff done. It's >> crazy. >> Yeah. >> And like this equalizer thing. It's there's like so many problems that were

not that were left unsolved before this and now that will got solved and that's that's what gets me excited. >> Yeah. I guess that brings me to another question I had. like you referenced earlier this idea that it's about choosing what you're going to focus on in this world because the tools are so

powerful and I think that's definitely been something I've observed and then you just mentioned another big piece I've seen which is that there's a whole host of problems that uh for lack of a better term are SE 3 and SE 4 type problems that are now accessible and legible and solvable because we have a

tool that can do them. And so on the one hand you have like more volume you can attack that's perhaps lower urgency and on the other hand you have a lot more value on picking your overall direction correctly. And I'd be curious to hear like in practice for you guys what is that balance like? How do you guys

tackle sort of those two points on the on the scale? I think that two things that matter to us is general conviction that we have based on information you know around like hey our models are going to continue to improve along you know this set of capabilities like let's build ahead of that so that

we continue to scale and like you know bring bring more benefit to our users and then the second part is like what are people asking for uh and there deploying intelligence like hender helps us as well like I was um was on Twitter the other day like just I started a thread like of like hey you know it's

like what should we build like you know what's holding you back like what's not delightful on Codex right now and then got you know somewhere around like 250 >> yeah I saw that thread yeah it was a good thread >> it it's like 600 like unique ideas but Codex helped me sift through it all and

you know bring it back then and and uh based on my own priorities and my own notes uh like actually section it and then I was able to discuss it with the team but so yeah conviction and and feedback are like two good ways that we go about it. Do you have others? >> Yeah. No, I think that's I think that's

that's a good framework. Um, you know, I think just to mention a few other areas where um, you know, where we've been building. So, we we we have this kind of, you know, CLI product, we have this web product and we have the ID extension. We also have some cool integrations. So, you know, you can add

codecs in Slack and you can add codeex in linear. Um uh and with with a lot of these like smaller issues that you that you spoke about, one really cool trend that I've been seeing is um you know there are a lot of small tickets that you know the end of the year or the end of the course you kind of the team might

struggle to get round to or they're like always there and they're kind of coming up at the end of the meetings and now right so like you know after you've triaged a bunch of these things you know maybe there are a bunch of small ones that you could just put into one of these um one of these integrations and

you can just be like you know Codex fix this or you can literally assign it now in in in linear and other products. So I think like some of the small stuff it we are starting to get to these like really kind of endto-end workflows of you know tracking a small problem meaning like literally writing it down in you know

some short descriptive way and then having a PR that you can review and choose choose to merge or not and I think like being able to free up a lot of time uh you know from focusing on a lot of that low-level work like just frees up pure resources and capacity to focus on some of those some of those big

issues. So that's been a cool cool trend as well which you know obviously you always have to prioritize things you always have to you know filter signals through noise noise and and and make some kind of hard decisions but I do think that we've been able to to to to get a lot of that lowle work um kind of

you know almost kind of enter and automated so that the team can like really focus on those big issues. I it also moves bottlenecks around right so like as we're solving almost solving code generation and you can implement any feature you know like faster and faster like suddenly you're left with

deploying and maintaining the services and you know whenever like like your hardware breaks or like networking has an issue or like whatever like million things that can happen uh like now suddenly that you know you get paged a little bit more and like you're building sort of like ahead of the automation

that we're able to uh deploy and the intelligence is not yet capable of like doing all these things like you know we're not able to yet have codeex deploy the service and like be on call um and this is like an area where currently we're feeling sort of like that load from having almost solved code

generation. >> Yeah, I was going to go there so I'm glad you did because to me it's like >> you you've 100x extra code generation or whatever you want to use the multiple for but now you've just shifted all of that down the pipe. Yes.

>> Yeah. I mean it opens up some cool interesting um you know interface possibilities like like if you think about chatbt right you're you're conversing back and forth with a model and you know you're asking for some piece of information and it kind of you know presents something back to you with

a coding agent it's taking some action in the world and it's coming back you know most often in a codebase and the the kind of artifact and result of that is some code that you have to review if you if you want to do something useful with it. So yeah that at the moment I think we're in this kind of like

transition period where the meme is that kind of like you know a lot of like software engineering is reviewing agent code. So I think like as a you know as an interface and as a problem to solve. I think that's a really interesting one to to think through. It's one that we're thinking through and it's one that I

think you know many people in this in the industry are which is like how do you how do you not kind of shift the burden as you say from like um uh you know kind of like writing code to basically reviewing code and how can you make that as smooth as possible and you know I think we're doing some cool stuff

in that space with with the code review um you know agents and other things but I think that's like one emerging uh you know emerging problem that that that we'll have to solve soon. One of the things that's special about code generation is like you can make it safe. Uh so you're going to have all the code

generated in a sandbox. Yeah. >> Uh and you have no side effects and so therefore you know I think also like just because >> all the context is there it's textual like for code like you have you know you have g you have reboard like a lot of the automation already exists a lot of

the tooling already exists. So it was solved first uh I think primarily due to a combination of reasons but that's a big one >> and you can make it safe like a lot of the work that we do is like we view coding agents under the lens of like you know safety and alignment and like

alignment is not a solved problem which means that whenever you know you go into the world of like deployment and being on call and actually having like real world like consequences of an agent taking actions into the world. That is like a whole other game. Uh where you know you cannot make it yet. You know

you cannot guarantee that the agent will not go and like delete your service or just like you know snoop at like you know user logs and there's a whole security aspect um and figuring out you know how to restrict the set of actions through like a safe space uh or you have to solve you know the alignment problem

uh you know whichever will come first. we're sort of like inching towards that and finding more and more creative ways so that our agents can act upon the world safely and that you know you're able to steer and supervise that. I think that's like the next frontier of you know what we're going to unlock like

you know in 2026 it's like good generation considered mostly solved good review we've been investing a lot in and then you know like where are the bottlenecks now? >> Yeah. Yeah. That's kind of where my head goes as I look at the next year as well. I think one of the things that people

tend to get curious about and I think that will come up more and more as a conversation in 2026 is how do engineers stay fluent and able to read code structures in ways that are meaningful in a world where code generation is to your point mostly a solved problem. How do we keep

the fingertippy skills that are relevant so that you can understand what you're deploying? >> Yeah. So there's this part that we didn't discuss on like code understanding and planning as well like how quickly can you figure out like how your system is act functions today

>> uh and then you know maybe use that knowledge in order to plan like your changes >> and then after you have your changes like how do you have them like you know actually deployed and have an effect upon the world like you know be it a product or or something else. Um yeah,

that whole like um it's not just that but like I am more productive, you're more productive, everyone in the team is more productive and it's also keeping up with all of that. It's like you know what the hell is everyone doing? Uh it's like you know there are new features minted every day. It's like the world is

changing so quickly around u just like in teams even small teams keeping up with it all is a challenge >> and you saying that I just want to be clear everyone's going to be like very discouraged to hear you say that. because we're all trying to keep up. We're building towards that, right? So,

you want to have >> you want to have fast ways to like understand >> what's going on in the codebase? Uh like synthesize things. Is text the right way to do that? Do you want like a little report every day? Um you know, how fast should uh should your agent be in order

to understand to help you understand the state of the code? But and to your point about you know kind of staying on top of um you know staying on top I guess kind of programming as well. So not kind of like delegating everything and and still deeply understanding things like um you know I I've seen some cool examples some

people internally like occasionally kind of turn off their internet and they like I forget the term that they use but they're like basically kind of like you know old school coding and they're like there's no tab complete there's no agent you know there's no codecs next to them. Um and you know human curiosity doesn't

go away. Like people still need to learn like you know the engineers on the team still read engineering books. I still read you know engineering books. So I I don't think that like curiosity is going away and I don't think like it'll become this kind of like you know thing that you hand it off to and you and you lose

all the knowledge yourself. Um and as you say you know like models can can help you stay up to date as well. Like if you know if I'm trying to get to to know a code base um I can talk to the model about it. I can you know ask it like you know how does the back end integrate here like oh like where does

this component come from can you just explain the dependencies like the model itself is also like a you know an amazing feature so um I think that's that's a cool angle as well >> when was the last time you were really surprised by an emergent property in a model

this this morning. So, and >> um so yeah, I just saw someone build scaffolding around a model to enable it to work um on a problem that I thought was out of reach of the current capabilities of models uh and solve it, you know, successfully. And I was really

surprised. I thought we would need to train the model specifically to be able to do this. Um but turns out like it generalized fairly well and worked um for like almost 13 hours on this one. Uh yeah, just just by being more creative on the tools and the setup around it. I hadn't seen this done before. So that

was like really surprising to me. Yeah, I was gonna I mean like most days, you know, there's there there's some things that I, you know, probably can't say, but I think there's one one that actually stuck out to me which we, you know, we released it, but if you go in the web product um and you know, you you

ask uh you ask the model a question and it can kind of send you some front end back. It like takes a photo of it and it like sends it back with it. >> And like when I first saw that, I thought that was magical, right? you know, you know, it's it's kind of using a bunch of tools, but there is something

like very interesting about thinking about coding agents, you know, being able to code, but being able to see, being able to generate these assets and like at a conceptual level, I just found that really interesting as like a as a creative that, you know, this this model can like do so much more than I thought.

>> Yeah. I I think that one of the things that's been my one of my biggest takeaways as I reflect on 2025 is that I probably as much as I was excited about tool use for models and I was I don't think I realized the combinatorial power that gets unlocked when you start to give a

model a good set of tools. It's and and there is something there about like what is the a good set of tools and what the approach that we've taken with codeex is you know just give it access to your computer through like you know good old Unix tools right it's like give

it a shell uh and let's see how far it can get by giving it a shell and then in order to do this safely like have it run in a sandbox >> okay >> and then what emerges from there um is to us like surprising because we don't necessarily care about like you know how

the model is going to be able to achieve its task. >> Uh and so we don't necessarily have a specific bias there uh like other than like you know you should probably use the shell like a bunch of times. Uh but other than that it's like it's a very general tool

and that's something that we've done consciously because we believe it's like one of the more scalable ways of doing things as it scales with like the model capabilities and it's super general. >> Yeah, I guess one of the >> go ahead surprising things as well on the creative side as well is like you

know you know I mentioned that there's someone that that you know use it to write documents and things like that and it turns out that you don't need to give it a document writing tool. you can just use reg x and >> you know like through bash commands edit documents you know write kind of do

anything. I think that was uh yeah like perhaps not surprising but but but pretty pretty amazing capability. >> Like the other day I was just like playing with something and then we had like a codeex SDK and then I just told Codex about it and then it was able to just write code and like use the SDK

write a bunch of TypeScript and then invoke basically invoke itself in order to achieve more. um like we don't have native multi- aent in Codex but this is a form of it that is just completely emerging because I just read the documentation I was like oh you know I can probably get this tool to do

something for me um and I just like wrote that code invoked it and it just worked um Codex is very good at like figuring out ways to solve its problems >> so codeex essentially wrote in read the SDK docs instantiated another codeex instance and used that as a tool to get a job done

>> that's Right. A bunch of them actually. >> Yeah. >> Yeah. Effectively it it bootstrap multi- aent. >> Yes. Like without us like you know thinking about it. Yeah. >> And so there's this thing of like throwaway code is interesting to think

about it right is like code as a tool. It's obviously extremely powerful. Um, but maybe you know there's just like this whole category of things where like the agent is just you know writing code as like it's not a piece of code that you should ever review as a human or like you know that you necessarily care

about. It's just a very general tool. >> Yeah. It's it's code as a means, not code as an output. >> Yes. So sort of riffing off the tool piece, I've also seen sort of models with fewer but more powerful tools that are more general in nature doing better overall.

So that doesn't surprise me. Um I'm going to the other side now looking at the memory side of things and how longunning agentic tasks handle memory problems both maybe sort of stateful memory you have outside the system and also in context memory management approaches. How do you guys think about

that for like you know the 20our task or whatever that you're running? Um h how does memory work? So memory is still an open research topic like it's clear like something there will emerge that is better than you know whatever short-term approaches you know we're are taking like right now

as a form of memories you know you can have the model like the model can write to a file and then you know keep track of like a lot of its state like you know through like just markdown files for example >> another thing that you know we're doing is like for very long running

sessions like the model that that goes beyond its context window. And so the model is forced to like summarize like what it's achieved so far and then reboot itself uh through like a process that we call like compaction where at the end it's just like okay like let's just erase like all of the content of

the the context window and then summarize it and then you know you reboot and then you restart and then you can do this many many times and essentially then you're able to have the model you know the agent work forever. Uh you know if the task like required to work forever it would work forever.

In addition to that because it has access to just like grab and is able to like search through things it can also dump additional context that it doesn't really need to have always in its context window just to files and that's like a form of memory. uh with skills as well like you know you might have skills

in a file somewhere and it's like a form of memory that is shared between the user and the agent >> and you're co-evolving some common knowledge there where it allows you to have an agent that you know performs hopefully better over time. There is a problem with staleness there where it's

just like it's sort of like a poor version and a hacky version of memory and it does feel like this will get disrupted at some point but that's mostly how we've seen like you know it tackled and you know it's a very simple way of achieving it. Yeah, that's one of the themes that I

think is emerging as we chat a little bit more is that you are seeing surprisingly simple primitives be surprisingly successful at solving larger generalized problems. Yeah, I think that's a thing that a lot of people in the field have learned a long time ago and I think it's

sort of like being internalized and it's not necessarily like common general knowledge of like hey keeping things simple with models that are evolving in capabilities month after month after month is probably the right thing to do because otherwise you end up with a pile of complexity that you have to continue

to adapt to the ever evolving capabilities. So that's why we decide to think to keep things very simple as well. >> That makes a that makes a ton of sense. Um the other the other big question I want to get to this gets back to the whole idea of like technical and

non-technical folks using codecs. I get asked a lot how do I think about my career? How do I think about career progression in a world where job titles are increasingly sort of optional hats that you can take off and put on? Uh and it's about the problems you solve. What is the career conversation inside OpenAI

and and how does how does co-evolving with the model shape that? >> Yeah. How do you feel about this? >> Yeah, it's a good question. I mean I think like you know I think one kind of emerging trend that I'm seeing um among designers and to an extent some engineers as well which I personally

think is a positive um uh you know positive direction which is kind of what I spoke to earlier with this kind of idea of kind of equalization is there's less of a focus on kind of credentials and going through certain routes right to get to to to kind of you know ascend certain kind of peaks of credentials and

more a kind of focus on kind of what you've done and what you can show and kind of like you know code wins. So particularly in the design community, you know, what I'm seeing is a lot of people are kind of building really exciting things, putting them out there and from a career perspective, you know,

building up profiles and um you know, kind of like work through what they've done and what they show and no one cares where they went to school, you know, and all of those other things perhaps of the past, which sometimes good, you know, sometimes, you know, bad from like a from kind of a credential point of view.

So I do think there is definitely a kind of like learning through doing and kind of you know kind of proving through you know what you've done. Um which I think is is an exciting uh trend and I you know I think also you know a lot of like creator economy and you know the rise of you know podcasts and personal media is

is kind of similar right it's just like anyone can kind of do you know you can just do things is the internal phrase um but you can just kind of you know do things and show you and show your you know show your skills through that direction. So I think like that's personally one trend that I've seen um

you know to broader broader trends you know I don't know if I have as much of a perspective there but >> yeah yeah I think you can just do things very much a mantra uh the second mantra we have is like I am also curious about this. >> Yeah.

>> Uh this is that's sort of like the two things that people uh you know exhibit at OpenAI. I'd say it's less a challenge on um career progression at OpenAI. It's a you know we look at impact and that's sort of like you know how you progress. It's it's been a challenge on you know interviewing and finding the right

people because the traits that you're looking for and you know like how you can succeed has sort of like broadened. Before it was like do you program well? It's like oh let's give you a series of like programming tasks and like you know really hard ones and you know we're going to pick the best talent there. But

now it's not that easy anymore. It's like you you can actually be very successful, you know, if you're like not going to traditionally be like a top performer at like, you know, hard programming like tasks. And so like being able to um find the talent and be more creative here has been a challenge

for us and like we're sort of like evolving our thinking there, but it's been very interesting. Do do you guys have a silver bullet for the persistent issue we see with interviewing where people will have chat GPT up on the side and we'll just be kind of reading responses back in the

interview? >> Yeah, I mean we we bring people uh on site uh for for a lot of the interviews and then it's also just a a reality of like hey you know in the job you know you're going to use AI all the time. So it's more of a the interview itself needs to evolve and maybe not you know

limiting like you know the tools that people can use. >> Yeah. I think it's like one way of thinking is like how are you using AI to get around some constraint and then another is thinking of it in an empowering way and you know you need to hit certain baselines. You need to um

you know you need to to to to have certain skills in place but also kind of are you open to using tools and how can you understand how those those can give you leverage. Yeah, it reminds me a little bit of one of Jeff Bee's um favorite interview questions where he asks people um how do

you solve uh a problem that has sort of two obvious solutions like I want I I want to uh have a higher quality car that goes faster, right? How do you do that? Uh and you have to pick which one to optimize for. And the trick is you're supposed to invent your way to both. Um you're supposed to think outside the

box. You're supposed to think around the constraint. You're supposed to push on both. And that part of it is just measuring the willingness to break the mental box. >> Yeah. And is the point there that you know if you were using AI on the side like you know

you wouldn't get you wouldn't come up with like a creative >> uh I don't know that it's necessarily that. I think sometimes I've seen that. I think >> the the best way I've seen to push people off script let's assume a remote, right? because I think on-sightes are

critical, but we'll we'll take that as red. Um, if it's a remote interview, I think the most effective tool I've seen is really to push off the standard behavioral interview script pretty fast. >> Um, and push people into a really honest conversation that demands some higher level trade-off

thinking and they don't really have time to feed it into a model and get a response in real time. and you see pretty quickly what their thinking tool set is in their head and that gives you a sense of like what they're going to bring as a partner with AI uh when when they start to work.

>> We have this problem now, right? Like not sure if you're reading the questions off the screen on the right. >> I actually am not. I have no questions up. I'm staring at myself and you guys and I'm just kind of >> So are we. Sorry. Delightfully simple. Yeah, I think it's more fun that way.

Like we get to kind of take the conversation where we want to go. Now, I did prep with chat GPT. I absolutely prepped with questions, but then I was like, ah, you know, they're okay and I'm just going to riff it. So, yeah. >> Yeah. >> Interesting. Uh, you know, another

question we have. I know we only have, you know, a few minutes left here. Um, I think one of the things that we haven't dug into yet that I hear a lot is, and maybe this is like half a design question, half an engineering question. So, for the two of you together, like, it's going to be perfect. Um,

I hear a lot of talk, especially when, um, I put out videos talking about new models. I'm going to do that for Chad GBT 5.2 here. People will say, "What's the difference? I see the same chatbot. >> I see the same terminal. I see a different label." Uh, how do I know that this is actually better? And

like we've even had like comments from I think Sam and others that say chat is essentially a saturated use case. And I kind of agree like I think it's mostly saturated out. How do you convey the significant not significance is the wrong word the step change that you get in capabilities over a six month or year

period to someone who is seeing the same UI. >> It's a good question. I mean I think like if it depends on the use case right like you know I think like what you know like as a designer or design engineer I kind of work with you know different models and then for some for some tasks

I like one you know for others I like the other just like you know many other products um or if I'm in chatbt if I'm asking like a super code question right I'll just like leave it on auto or kind of you know some low reasoning model and if I'm really wanted to think maybe I'll use pro or something like that so I

think it's one of these things where you kind of like you know you test it and and it depends on on the situation. Um you know that being said like we also we have a bunch of research evals you know so I think there are certain barometers that you can use but we've kind of talked through this interview about um

you know the different capabilities that different model steps unlock and I think we have consistently seen that right like models today at least for coding are like substantively different from where they are when I joined this team. Um so it I think it's a case of just try them. Try try many different ones like

you know see what you like. Some things are good for different use cases. Um but uh but um but yeah I I I think like maybe one good mental model perhaps that that people don't think about is you know when thinking about these things they think with a snapshot of where we are currently with how you interact with

chriier models. And I think in five years time it's going to be very different right like if you think about what models these new capabilities can unlock different products will have very different experiences. You know you might you know is chat always the best um uh interface like you know you you

might not be interacting with a model at all but it's still doing work for you in the background and in that case right model quality and and the model that you're using is very different. So yeah >> to come back to that where it's like that's code review is again an example of that where it just happens in the

background the model improves and you know we know like the the either it got faster or it's able to spot more things it's like yay you just got an upgrade for free you don't have to think about it uh and you know you just benefit from it like every day and then codeex itself is a different product from chat uh

agents benefit still like from a a lot of improvements on like we definitely see like whenever we improve on reliability like frontier intelligence how long it can it can go but then it feels like we will need another product at some point as well where you're not going to run codeex for like 3 days in

your terminal um yeah maybe people will maybe people will right but it's like at what point do we have agents that just run forever >> uh in that you you interact with it's like that's going to feel like very different. Maybe you text it from time to time. Maybe you were going to call it

and it's just like we yet have to invent like the right product around this. Like the models are not there yet but they will be. Uh >> and then that's going to be like oh wow you know it's just like we're like GPT7 right? And it's like it'll be like obvious. Um and in the meantime it sort

of feels like oh okay it's like it feels incremental at times. Um but then when you look back like six months ago you're like heck like none of this was possible. Exactly. Like I did a video this morning um about this idea that straight line extrapolation is surprisingly hard to experience in real

time. Uh like you're sitting there and like like you said like people get used to the products so fast and people get disappointed and frustrated by the products. I I vividly remember uh how excited I was working with Chad GPT5 thinking and how it felt like a step change and then I immediately within two

days found a bunch of things that I didn't like about it and wanted to fix and like that's just how it goes because that's how humans sort of scale our taste I guess and I think one of the things that I've been thinking about is how do we take our human defaults where we seem to

assume a static world and start to transition to a human default where we assume a dynamic world where we're living on the slopey part of an S-curve and like we have to think about rapid gains and capability as a default base case. All right. Uh for our last couple

minutes, do you have a question for me or the audience? Like I know you guys are always hungry for voice of customers. There's something that's been bugging you that you would want to ask. >> What are what are you? I mean, I'm always curious like how people use coding agents outside of coding. Like,

you know, you mentioned that maybe you use it, you know, you use chatbt to get ready for the interview, but like how do you use it in your in your day-to-day? >> I love that. Um, so I am a relentless omnivore when it comes to AI models and I tend to jump around

really quickly, but I have settled task groups that once I decide where I want them to live, I tend to put them there. And so right now I am using chat GPT. Well, it was 5.1, now it's going to be 5.2 do for uh a lot of the structuring and brainstorming and researching and

thinking that I do as I start to think about pieces that I write um and what the stories are kind of and how it kind of comes together. Um I'll use codecs when I want I I call it like hard thinking mode. I think that it's been marketed like I think Chad GBT 5.2 2 Pro or 5.1 Pro, like people talk about it

and I've tried it out and I like it, but I think it is sometimes uh overexpressive for what I need. And that's why I mentioned conciseness as a value I appreciate in codeex is that CEX comes back and it doesn't give me, you know, a thousand tokens. It just comes back with

a really concise answer. And I I love the legibility of that and I kind of get addicted to it. And so when I need something that is a very clear concise analysis and it can be a financial analysis, it can be a project analysis, it can be an M&A analysis, it can be uh a doc analysis, it can be a response to

something that is really complicated that I need to think through and I want to draft it out. Codeex is great for all of that because it just it it boils really cleanly, right? You get exactly what it boils down to and it's really dependable that way. Um, I get uh a lot of mileage right now out

of the document tool creation or the tools used to create documents from clot. I know they're the other guys, but they are definitely shipping well there. And just OPUS 4.5 really, really, really does well on that. When I want a PowerPoint, when I want an Excel, it does well. Um, I've been both amazed

and also frustrated by uh using Notebook LM and Nano Banana 2 to or really it's is it three or is it no it's two is Gemini 3 anyway using it to ship powerpoints uh because I don't get editability and I hate that but I get all of these lovely graphics from Nano Banana and that's fantastic. Um, and so

I think we're in this place where people are um, we're tool omnivores because we're desperate to get the best thing in the moment for the particular task. And we all tend to have like that list of paper cuts. Like I was like, I don't like the PowerPoint piece. I think Claude Opus 4.5 has good tool use, but

at the same time, the ability to create decorated PowerPoints is not really there. Um, I think you guys have a ways to go in PowerPoint creation right now. Um, but the completeness that I'm seeing, like I'm doing some early work on shadow GPT 5.2 and and like it spits out a very complete document. Like it is

a complete answer that thoroughly answers the question. And so, one of the things I preach a lot is like you must get really fingertippy with your models to actually be able to use them to solve problems in a way that's differentiated from just type something into a chatbot. So, it's a long way of

saying I I have about half a dozen models and I use them all every single day, including like a bunch of open eyes. >> Yeah. And then you have this like mental model of like, you know, what is this model good for? What is this model good for? That's right.

>> And there isn't yet this like, you know, perfect model that like answers all your needs >> and your needs changing. Yeah. >> Because they keep changing. And that's the thing that you've emphasized that I really strongly agree with is that if I were to try and boil this into a table,

it would look incorrect because I have a um an evolving sense map of where these models are good and not good. And it's very it's very fine grain. Like I have learned which models read handwritten tally marks well and which ones don't. Um because >> when you refresh

>> when you refresh that thinking like you know that knowledge like when you when you allow yourself to say like hey let me try this other one >> all the time like I and that's I think one of the things that like people lean into with my channel is that I am extremely open to new models and new

experiences changing my priors because I think that you have to be to be at all helpful to people in evolving this landscape because you have to assume that any given new model release from any major model maker could upend a key part of your workflow because it's just better and you should not sit there and

say well Chad GPT before didn't do this so I'm not going to pay attention to this tool use capability it's like no you you should you should assume that the model is fully capable of surprising you and test it carefully so I think one of the things I've been thinking about is what what we mean when we talk about

useful work and what useful work looks like and we've talked a ton about codecs and obviously with codecs useful work is poll reviews uh PR reviews uh it's it's coding it's it's work that you can define in terms of the uh you know bits and bites that the model outputs it gets a little bit more complicated with other

knowledge work and so I'd be curious how you guys think about that maybe beyond codecs maybe looking at GPT 5.2 too. >> I would say it's like it's similar question in difficulty like even just for coding. Uh there are certain benchmarks like sweet bench they're like super saturated by now like do they

really measure how much use you're getting out of the model like in day-to-day use and also like know we talked about like how we're going beyond just like code generation and then it's like helping you understand things helping you like review like deploy like doing CIS admin tasks and like more and

more things. So you know helping you build like design prototypes. So it's all about like this economical value that you're able to create and you know open like really worked hard to like on GDP val like 5.2 to soda on GDP val I think it's like interesting to go and like from really hyper specific

saturated evals to a more a better understanding of like how is this impacting the real world you know obviously no eval is perfect but I think whenever a model like it you know puts a new soda on something that measures economical values like it's worth taking a look at it

>> yeah it I I appreciate that you call that out because I think it gets at this idea that people get suspicious of benchmarks when they get reported on and you get close to 100%. It's like okay but what's another 2%. Whereas I think there's something around maybe an implicit measure of

generalizability that you get when you get to some of these measures of economic impact. So GDP val I think is a good one. Um isn't there one around vending machines? That's another one that's sort of in that vein as well. >> Yeah, it's a fun one. >> Yeah, it's a good one. Yeah. Is it

vending bench or vendor? Yeah, but with GTP val it's clearly not saturated yet >> and then that's usually the cycle that you see with eval is you know eval gets published it against traction you know gets saturated like it did measure something useful at some point and then

maybe after a couple of months or years like it's not really measuring anything very meaningful anymore because you know every model is performing more or less like the same on it and then you have a new one like GGP is like measuring something more interesting again uh and given it's not Saturday. It's always

interesting to pay attention to it. Vending Bench is also a fun one. >> Yeah, it sort of underlines the story that we've been sort of telling through this whole hour together where we've talked about this idea that progress just keeps happening relentlessly with these models and that there isn't a

wall. And you know, contrary to popular reports, right, there isn't a wall. We've continue to see progress and it's something that allows us to continue to publish new benchmarks because we keep knocking down the old ones. Yeah, an interesting thing there is sort of like what are the benchmarks of the

future? >> Uh, and that would be pointless to have now because every model would just score like zero. >> Uh, like being able to be the CEO of a multi-billion dollar company, for example. Like, you know, that would be a useful benchmark. Like, do we allow

models yet to run like multi-billion dollar corporations? Like, you know, not quite. Uh, but I'm pretty sure at some point, you know, we're going to have these kinds of crazy bench. They seem crazy now, but like they're not going to be crazy, you know, like in a couple years.

>> That's a really interesting sort of brain teasers. What are what are the evals of 2026 and 2027 that we're going to turn to as measures of value? >> Thanks for having us, Nate. >> Yeah, thank you. That was a good one to end on. Uh this has been lots of fun, guys.

>> Thanks so much. Next time.
