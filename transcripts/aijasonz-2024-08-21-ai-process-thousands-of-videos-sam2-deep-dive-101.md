# AI process thousands of videos?! - SAM2 deep dive 101

- **Channel:** AI Jason
- **Date:** 2024-08-21
- **Duration:** 12:57
- **Views:** 21K views
- **URL:** https://www.youtube.com/watch?v=IW7jFq3vQbw

## Transcript

how can you use Mata Sam 2 model to build new types of AI application that wasn't possible before like automated tracking for sports analytics or video editor AI that can automatically blur out passengers face in Street interview in this video I'm going to show you how does meta Sam 2 model exactly works as

well as step-by-step tutorial of how can you build such AI application by itself So Meta relase segment anything model 2 a couple weeks ago which is model that can do extremely accurate object tracking and segmentation in videos even in some very complex things where the object is covered by mle different

things and this model is very interesting because some of the use case that was very expensive or difficult to build regarding computer vision now became really accessible to build like building automated system to detect shoplifting or monitor retail and Cafe stores cuz with model like Sam 2 it is

multiple magnitude cheaper to prepare training data for specific type of computer vision task and even some kind of interesting use case where you can just allow people to search across the video to find specific objects and meta is referring to this model as a real time probable object segmentation so

what exactly does this real time promp object segmentation means well that means Sam 2 model is able to predict the masket of every single frame in the video or image a masket is a spatial temporal mask that represent spatial relationship of the object that it is tracking as well as a temporal aspect of

how the object exists in previous frames and the user is also able to prompt the model to get more accurate segmentation result so they can do positive prompt to track certain object in the video or image as well as negative prompt to remove certain objects from the tracking so to get this mosto result it will

break down the video into different frames of image for each frame it refers to use image encoder to turn a image into a embedding which is a way that the machine can understand what the image is and this process will be repeated for every single frame in the video but at this point each image embedding is kind

of independent from each other so there's no real temporal relationship between them and that part will be handled by other components like memory encoder and memory bank which we'll talk about later and next user can add different prompts on each frames those prompt are not our common text prompt it

is more like a visual prompt including Point clicks Bing box or masks on top of the image and those prompt edit will be going through a prompt encoder which will generate a prompt token that capture the sematic meaning of what the user prompt is so for each frame we have the image embedding created from image

encoder as well as prompt token converted from prompt encoder and both of those token will be FedEd to the mask decoder which will be used to predict the mask L and what you see here is basically a Sam one model that is able to S object within a image and of course four difference between Sam 2 and Sam

one model is a Sam 2 introduce concept of memory bank and memory attention they will basically take each musket generated for every single frame into a memory bank which will be used to insert memory attention for the next frame so there's continuity and temporal relationship between frames and this is

how Sam 2 is able to track object in the video Even though for some complex things where the object is covered by other things in the video and this is a Nal of how the Sam 1 and Sam 2 model is able to track object within image as well as a video it is extremely powerful model that totally change the game of

image segmentation but your question might be this looks cool what exactly can you do about it and to understand that it's probably useful for us to understand how is original segment anything model one was used for the past few months so there are two type of main use case I observe people doing one is

that a lot of people are using Sam one model to prepare and lay image data for training visual model for specialized tasks so image annotation is quite a tedious job and normally require a huge amount of human cost to be able to annotate and Track image data they can be used for training specialized model

to identify like defects in the production line or medical data and previously there are visual model that try to do this type of segmentation job but with the same one model it is able to identify and segment specific object in just one goal and this reduce the cost of image annotation by multiple

magnitude so that people can create a huge amount of image annotation data to train specific model for certain tasks so I would imagine this use case will still remain a very big way of how people use Sam 2 model to generate High quity video annotation data for training specific models but on the other side it

also open doors for people to use Sam 2 zero short prompt ability plus other models to build interesting applications like building video ater AI is able to created visual effects will be otherwise very expensive to build and there are also people already integrated Sam 2 model with drone and CCTV data to be

able to do certain tasks like track and compare the health of each Farm segments as well as building some sorts of sports Antics applications all those use case that could be quite expensive to build before now is actually very accessible for all developers and things became even more interesting when you start

extending sigment anything model's ability with other models for example you might notice that the prompt segment aning model can't accept are meaning the visual prompt like clicks bounding box and mask it can't really do any text prompt so if you want to build some kind of interesting application where user

can just ask a model to find specific object in the video and apply special visual effects to it you can't really do it now but if you combine with other model that is capable to identify object based on text prompt but not as good as generating the specific mask then you can start having some quite interesting

application for example I build an AI application where we combine Florence two which is one of the best lightwe Vision language model that is capable of many Vision language task like take a text prompt to identify object within image it can create positive based on text prompt like human face to find all

the faces on screen and use negative prompt to identify who are the main speakers then use Sam 2 model to segment all those passengers face so that you can can apply special visual effects to either blur out their face or swap with something else and this is just one example of what kind of interesting a

application you can start building once you comb by different models together and I'm going to show you how can you create this step by step so you can start expanding the use case but before I dive into this I know many of you just getting started with your AI engineer Journey or are trying to figure out what

does a road map look like for learning AI That's why I want to share with you this free ebook as introduction to python cuz python is a main language you need to learn and master as AI engineer since most of popular library and framework are available in Python and this ebook is introduced by hopspot who

is sponsoring this video in this guide it will cover all the fundamentals about python how to getting started and set up and basic syntax method and functions that you will need to build AI applications as well as how to use some of important thirdparty libraries for both data analysis and building a

applications such as Panda metap plet and numpy it also show you example of good code and bad code with with coding Snips that you can just copy paste plugin and play so if you're just getting started with your AI engineer journey I definitely highly recommend you to go and take a look at this free

ebook you can click on the link in the description below to download it for free now let's get back how can we build an AI application using Matas Sam 2 model so I'm going to run the code in Google clap so I can access a better GPU and making sure you use at least the T4 GPU and you can run this code to check

if you're running a n media GPU and first thing we want to download both the Florance model as well as segment an model and also clone segment anything 2 to install everything and then we're load the model and processor for Florance 2 import a few different libraries and firstly I will create a

function called find all faces so I will give prompt OD which represent for object detection and when you use object detection and task type at default it didn't allow you to give more specific prompt to detest specific type of object and this will basically return every single object it was able to identify

with taex labels and then we want to filter our only Tex label that is related to human face and then return all the bounding box that has label human face if I run this function on this test image you will see that it return three different human faces bounding box and each bounding box has a

specific coordinates and next function is that I want to use Floren to find who is the main speaker in the image and this time I'm going to use the caption to phrase grounding so this is where you can give specific text X prompt and then Florence will try to identify this specific object in the image and return

us the bounding box so rest code is pretty similar so we're going to run Florence model to find the specific human face with mean speaker and then return the list and if I come up and then try to run this function here you will see that first image will return three different human faces but the

second function will return only the main speaker who are speaking and then we can write some function to detect if two bonding box are overlapped if so so we can filter out those overlab bonding box and this is useful because we're going to compare the bounding box from the two function and then try to filter

out what are the negative prompt which is this two versus the positive prompt which is this one and in the end we're going to combine everything together to create a function called find all pass and B this will basically return the filtered box so if I move up again and then just run this function so this time

you can see it only return two bonding box that is represent all the pass and by faces apart from the speaker then we can use this to as a visual promp to Sam 2 mode to segment specific PN by faces and I'm going to create a one function called pixel region so this function will basically add pixel visual effects

on the image based on the MK it was given and you can set up some pixel size in the end I will create one function called pixel8 off face where we will try to get the bonding box of all the passer by and if the result is not zero then we try to pass that on to Sam 2 model to get specific masks and R the function to

pixelate those mask area so now let's try to run this function on one single image to see if it works okay so you can see the Florence model to successfully find the passenger face and then pass on to Sam 2 model which successfully Mas area for this two passengers and in the end we're going to use the function to

pixelate this two passenger face so this looks like it's working pretty well the next is we want to start feeding the video data to make this apply to video I'm going to extract every single frame from the video and then going through this processing for every single frame and now you might ask why don't I use

the actual native Sam 2 uh video processing ability instead of extracting frame by frame the main reason is because for the video like straight interview normally there are are new people coming all the time and so far I haven't really figured out way to get Sam 2 model to just base on one single

prompt and finding all the random objects that's why I'm kind of doing this way if you know how to do it please comment below let me know so our firstly run a few function that's going to take a source video and extract every single frame into a folder so if I go to the segment anything to it should create a

new folder that is same name as a video name and at default you probably don't have the pixela folder yet before you process those image and then I will create this function to go through all the image with the pixel all faces function that I created before and in the end combine all the frames back into

a video and user can set frame rate as well that's pretty much it you can see that the model goes through every single frame to identify main speakers and passent B and successfully identify all those passent B and pixelated their faces and this is the final effect you can see every single frame people's

faces has been blurred out apart from the mean speaker and as I mentioned before this is just the beginning of many different use case that you can potentially create it I'm really ke to hear what kind of interesting use case you guys were start building and on the other side if you want to have a bit

deeper dive into specific project or have questions you want to ask you can join my newly Crea a community for AI Builders where I will share stepbystep detailed code breakdown for each interesting AI project I'm doing including this one and I were also doing interview with some top AI expert and on

the other hand you will also get a chance to connect with other AI Builders who are at a similar stage and I already went through some of hurdles that you are experiencing now there's a link in the description below where you can click and join the community I hope you enjoy this video thank you and I see you

next time
