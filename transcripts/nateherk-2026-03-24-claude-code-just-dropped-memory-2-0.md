# Claude Code Just Dropped Memory 2.0

- **Channel:** Nate Herk | AI Automation
- **Date:** 2026-03-24
- **Duration:** 8:30
- **Views:** 58K views
- **URL:** https://www.youtube.com/watch?v=LrgfmZkl3nc

## Transcript

So, Enthropic just silently released this feature called AutoDream. And based on people's discussions, it basically runs a sub agent periodically that consolidates Claude's memory files for better long-term storage. And I saw this tweet from Anthony here that said, "It's pretty crazy because that's basically

how humans actually store long-term memories is by sleeping." So, you can see right here in this project, I was playing around with the autodream. And so, because this is still being rolled out and it's like an experimental feature, I tried running this right here in my project and it is working. As you

can see, it's dreaming because right here in my status line, you can see that it says dreaming. And then I basically go down and I enter it to view the tasks. And you can see what it's doing. It starts off by saying, "Let me search for more user feedback, preferences, and new project relevant information across

recent sessions. And it's basically looked through all of our messages and all of our different things that we've asked it to do." And then it gets to phase three where it's consolidating stuff. So here are all of the key findings that it needs to update the memory files with since the last time it

ran. And you can see that this is a pretty comprehensive task. It's running for almost 10 minutes now. It's reviewed 13 sessions and it's touching different memory files. And basically the whole point of this is to be an automatic background cleanup and organization system for your cloud memories so that

each time you start up a new session, it feels sharp instead of kind of fuzzy or cluttered. Now cloud code does already have automemory which lets it remember things about your project in a memory.mmd file. And that usually gets injected at the beginning of your sessions and your conversations. And

that's what allows Cloud Code currently to feel like it understands a little bit more contextually about what's going on. But the Autodream is a little bit different because rather than just kind of like flooding in some information, it's consistently compacting and pruning and making that file better and better.

It's keeping everything feeling a lot more fresh because it basically takes all of this different information that goes into your memory MD file. When it does its Audream, it merges them, it prunes them, it refreshes them, and it compacts things. And then all of the different memory files are a lot

cleaner. So, if I switch back into this project, you can see that it improved five memories. That took about 10 minutes. It improved all of these different MD files, which the project will now be able to use, and they're a lot more clean and up-to-date. And so, the way that you get here is you go to

/memory. You can see right here we have edit clawed memory files. And when you open that up, you'll notice right here we see Autream on. This was last ran 11 minutes ago, as you guys just saw. And we can use /dream to run it. Now, when you open this up, this will be off. All you have to do is hover over it, hit

enter, and it will change to being on. And by default, your auto memory for your claude will probably already be on as well. And what you'll notice about the memory is that it's turned on globally across all of your different projects, but each autodream has its own files that it plays with. So in this

other session, you can see that autodream is on. It last ran 11 minutes ago. And now if I go over to my Herk 2 project, which I've never turned on the Autodream feature, and I go ahead and do memory, the Autodream feature is already turned on, but you can see that it says that it has never been ran yet. And of

course, the memory files are different because in here I've got all these different files. And then back in this other project, which was kind of more of a demo, you can see that we only have these main three, which are project, user, and the automemory folder. So now, if I'm in my Herk 2 project, and I know

that my autodream has been turned on, it says that I can use /dream to run. So if I come in here and I do /dream, what's going to happen? It basically just says unknown skill and we don't see anything going on. So right now you can kind of invoke this using natural language even though claude code itself might be a

little confused about what you're trying to do. So I'm just going to say run your autodream and we'll see what it does with that information. So right now it says I don't have the autodutream skill and it's kind of confused but right here you can see in the status line we do see that it's dreaming. And if I go down

here and I enter the tasks we can see that it's running this stream consolidation. It's going to orient itself with the environment and then we're going to see the list of I'm grabbing this file. I'm looking at these sessions and right now because this is a bigger project for me. You can see that

it's reviewing 285 sessions. So this will probably take longer than 8 to 10 minutes. So while we're letting this run, let's talk a little bit more about why this matters. So obviously this just came out and I haven't had time to really really test it and see if it's worth it or not. But based on what I'm

seeing, I definitely think it is. And let's talk about why that is. So the first big point is that you have less repetition. Even with auto memory, I still feel like sometimes I'm reexplaining things or I'm trying to, you know, carry over context from one session to another. And less repetition

is obviously a good thing. Another thing that we have that kind of floats behind the scenes is less bloat because part of the system is that it's compacting and pruning stuff. Pruning basically just meaning like eliminating things that are unnecessary, trimming the fat. And when we're getting rid of all of that excess

fat and excess tokens, it obviously helps us with our bloat and helps us with our context management. We also have better recall because it's getting rid of things that we don't actually need. It's easier to find things. So, just picture an example of like, you know, you've got a 100 different balls

in a ball pit and you're looking for one pink one out of all the blue. Well, what if we take away half of the blue? It's going to be easier to find that pink. And then what I think is really cool is it's basically just like sleep. So, whatever cadence that this runs on, which we'll talk about a little bit

later, when it hits that point, it basically just resets. So, it's like a checkpoint. Every time you get to a new checkpoint, you're basically saving yourself. So, before it would have all of these different files, right? you'd have these huge bloated context files, MD files, but now Autodream takes all of

that and just keeps the important information that you need, which may only be, you know, a couple different bullet points rather than having hundreds of lines. So, the way that it actually works is step one, once it's activated, it will gather session info. After that, it will read the current

existing memory files and then it will load it into a sub agent which does the actual dream prompt. So, I don't know for certain, but I'm imagining that the dream prompt is something like this. You are performing a dream, a reflective pass over your memory files. Synthesize what you've learned recently into

durable, wellorganized memories so future sessions can orient quickly. Keep memory MD under a line limit. It's an index, not a dump. Link to memory files with oneline descriptions. Do not copy full memory into it. After it's ran that prompt, it goes through the consolidation and pruning, which like I

said is just cleaning things up. And then it goes ahead and it stores all of the results. And then whenever it wakes up the next time to do a dream, it basically just repeats that process every time. So once you have automemory turned on and autodream turned on, how does the autodreaming actually take

place besides you invoking it with /dream or telling it to? Well, basically two different types of triggers or both. It could be based on hours, which means like, hey, every 12 hours I'm just going to do my autodream. Or it could be based off of sessions. So maybe once you hit 300 sessions, it automatically does uh a

dream. Now this isn't confirmed with official documentation. This is just basically what it seems like after some X discussions and some Reddit discussions, but just keep that in mind. That is likely how this works, but I don't know for certain. Now, once that's running, you'll basically be able to see

a couple different statuses. You can either see that it's running, you can see that it's never ran before, you can see when it was last ran, or you can see basically just nothing and it will be idle. And what's important to know here is that it's only going to touch memory files. As you guys saw in that first

example, it said I updated five files, those were all context files. So all of these right here that said I improved five memories all of these are MDs none of these are code or scripts or anything like that. So how do we think about the different layers between these different types of you know systems within cloud

code. So for normal sessions we basically just have the ability to code to debug to refactor to you know talk to cloud code. Then in the middle we have that automemory which records decisions patterns important things about the actual project or about you. But there's not a great method for cleaning that up

consistently unless you Frankenstein your own solution to do that. So basically what Autodream does is in the background without you having to manually go in there and prompt it to looks through everything, cleans everything up and fixes a lot of stuff. And so that's why having these three

layers work together, it creates a really powerful system that likely is going to help you scale better and keep all of your sessions feeling cleaner and way more like a human who can remember things about you rather than, you know, a chatbot. So this has been running now for over 6 minutes. I'll just check in

with you guys when this is done and we can see what memory files it went ahead and updated. So, this one actually only took 8 minutes, which was interesting, even though it had to look through way more sessions, 285 compared to about 13, but it was able to update these three different memory files. And you can now

see that there are no background tasks currently running. And if you want a little bit more visibility, you can see what it actually did explicitly. So, it added these couple entries and it removed these sections. And now, if I wanted to restore those or add some more insights, I could. And I could also go

view the file, of course, if I wanted to make sure that it was all accurate. And the cool thing about this is as you use the AutoDream more and more, it's going to get better and better at understanding what type of context is important to you and what is not. But anyways, that is going to do it for

today. So, if you guys enjoyed the video or learned something new, please give a like. Helps me out a ton. And as always, I appreciate you guys making it to the end of the video. I'll see you on the next one. Thanks everyone.
