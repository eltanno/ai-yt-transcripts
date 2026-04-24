# From $0 to $4m with just 2 people (ComfyUI Crash-course for E-commerce)

- **Channel:** AI Jason
- **Date:** 2025-01-20
- **Duration:** 28:08
- **Views:** 63K views
- **URL:** https://www.youtube.com/watch?v=uywkK9owKkY

## Transcript

for the top e-commerce brands in China 80% of the image videos and posts are generally not from any human but AI behind the scenes from photo shooting editing graphic design layout and day-to-day operations some of those e-commerce Brands were able to cutting down 40 people assets generation and

operation team and what is even crazier is that those software company who build those automations for e-commerce companies were able to set up their own AI streamer and influencers with just 2% and gener more than 4 million USD monthly sales so I truly believe there are a huge amount of opportunities

around AI in e-commerce to be unlocked at global scale if you remember a few months ago I was trying to build a virtual try on AI pipeline which is fairly complicated but meta just released a model called LIF that is specific focused on the virtual Trion use case with this model you can spin up

a AI image generation ply in just 10 minutes and not only for virtual try on there are even model for virtual off where you can provide image of people wearing certain clothes and it will automatically strip out the clothes itself for producing high quality product shot all those different models

are for you to stitch together and build automation pipeline if you know the use case that's why I want to show you how can you take this models and build different type of image generation pipeline for real world e-commerce use case and I will take you through step-by-step the basics so that you can

learn and adopt for your own use case without further Ado let's get started one of the most powerful tool that we're going to use is confy UI it allows you to download and upload different AI models you saw that interesting and Stitch together different workflow and it's purely open source so you can

download and on your local machine if you want but you can also build and run pamp PL on cloud-based platform like running Hub run comfy and bunch of others they basically allow you to build comy UI workflow their Hardware which normally can be more powerful than your home PC and my best practice is normally

use Rong Hub to build out and iterate the flow and then use Rong comy to host the confy UI Pipeline and firstly I want to cover some Basics how do you use confy UI to do Tech to image image to image mask and control net so that you know the principle about hous things work and then I will take you through a

case study of how to use interesting model like laa as well as build some more complicated workflow for AI model swap which is actually very popular use case because for some Asian companies who are going International you normally need to get foreign model in local market to do product shots which cost a

lot of money but this pipeline can enable any company to just take a photo thems and swap some model and background to something that fits the local market but before I dive into this for those e-commerce business usually an online purchase begins with a search as AI search engine like pacity continues to

roll out Publishers estimate that they can lose 20 to 40% of their organic traffic so how can you resync your SEO strategy in this AI search engine arrow is critical that's why I want to introduce you to this AI SEO M Class they're trying to tackle this problem and it is completed for fre cover loads

of topics and tools in terms of how to get started and advanced for AI driven SEO and supercharge your online visibility it give you tools to grade your brand and you can see the full report including how your brand is being discussed by the AI engines as well as how your brand presence measure up in

your industry and competitors with detailed analysis and actionable insights as well as AI research tool for you to understand which competitors are are ranking at similar keywords that you are paying for and also give you breakdown of what type of keywords they are betting and what their cost and tips

and best practice from interview with markers from Top firms so I definitely recommend you to go check this out if you want to learn more about how to do AI driven SEO I have put the link in the description below for you to download now let's getting started with confy UI let's firstly cover a few basics of how

to use confy UI the most simple one will be building a TX to image pipeline so you can double click and then search for kampler so kampler is a specific know that to generate image in confy UI and in the word of AI image generation exampler means a method or algorithm that will be used to guide AI in turning

random noise into meaningful image if you're not familiar with how does the AI image generation Works basically the starting point would be a super noisy image like this and the AI model is train to reduce noise a little bit every time and repeat this process multiple times to eventually get a high

resolution image generated from this noise image so B confy UI we firstly load a mod model so I will search for load checkpoint and checkpoint is the AI image generation model if you're using cloud-based confy UI platform they probably a bunch of model loaded already the common one I will be using is like

dream shaper XEL and I'll click use and then we also need to connect positive and negative prompt you can drag it out and then select the clip so clip is basically model that vectorizing both image and text in the same Vector space so that we can group text image with similar sematic meanings together for AI

modo to understand what the a cute c means it you need to understand for each image what are different factors and keywords are and then plot all the image data on those text descriptions to better understand when we give a word what are the most relevant imag of this word look like each image has hundreds

of thousands different text description data convert into vectors and this is exactly what do clip do so this model has been trained with huge amount of text and image data so that it can guide the model to generate image based on text prompt so here we can say a cute girl r photo high resolution and netive

prompt to be happy but we also need to connect the clip model to those prompt so that we can vectorize those text and in the end we also need to a latent image as we mentioned before those text to image model basically will start from a very noisy image to gradually reduce noise in higher resolution like this

this empty latent image is basically the starting point super noisy image and D noise means it will remove noise 100% and step means how many steps it would take to reduce noise and then we generate latent so we need to also use vae decode to turn the data into proper image and we will connect the vae from

the itself and from image we will save the image so that's pretty much it a very basic text image pipeline if you click wrong okay so you can see an image has been generated here and you can increase steps here to get better result as well but it will also take longer to generate

and I create a group called text to image so this is most basic pipeline but next we can also do image generation and what I will do is that I will copy the workflow above by doing control and select everything and shift drag it here and the way image to image generation works is basically instead of

passing on empty and the way image image generation works is basically instead of passing on the empty latent image we're passing on existing image to the kampler so you can still keep some essence of the original image but do some additional generation ation so the way it works is that I remove this empty

latent image and add a Cod image we can we pass on image that we just generate earlier and we also need to turn it from pixels into latent image and we also need to change the noise to instead of regenerate from scratch 100% we change it to be like 50% and I can change pump here a little bit so I can say a cute

happy girl and there no negative promp and we also need to connect same VA to the VA code and let's try it so now you can see that it cap sound essence of the other image and change the face from a sad girl to a happy girl this is how you can build an image to image generation pipeline in confy UI

and next another very important concept is mask so mask allow you to communicate with AI model which specific part that it should make updates versus part that it shouldn't and I will just quickly copy the pipeline we generate above pasting here and this time let's say we want to update this image and I want to

changes the shoes what we can do is that I can add a new note called load image as masks and I will upload same image to this note and I'm going to right click there is one option called opening mask editor this is where it will allow me to build some mask so I'm going to mask over this shoes and save to note then

I'm going to add a new notes called set latent noise mask and then instead of passing on the original image to the latent image add that add to this latent noise mask and then add this new latent to the K ampler and the problem here I can change to a woman wearing high heels and wrong so now in this generated image

you can see the rest of the image didn't really change however the shoe has been changed from a sneaker to the high heel this how this mask is became really useful because they allow you to make updates to very specific part that you're not happy with but if you trying to build application most likely you

won't be drawing The Mask yourself so quite commonly we will be using some other AI model that can automatically detach certain items using Tex prompt to do the masks for example I search for clip segment so clip segment is a note that can take a image and we can use text prompt like shoes this will

automatically detect and create the mask and the first preview this mask it generated and then I will connect the mask here and and let's try this workflow but before I do that I select all the other previous notes and do command B this allow us to skip so noes so we don't waste the computer resource

and cool you can see the clip segment automatically identify this area is where the shoes are and there are a lot of AI models you can use to automatically segment the image and the last part I want to cover is control net you probably heard about control net but not sure what that means so control net

is a specific type of model that has been used in image to image generation where it allow you to extract specific type of essence of the original image and use that to generate new imag and they're different type of control now you can use for example this is called cany Ed and this is a human post where

it can extract the post from image and generate new ones as well as semantic segmentation where it can extract certain segmentations apps in as well as deps so as an example uh let's say we want to uh take this image to extract the human post here and then generate a new image so I'll load this image first

now I will add a new node called control n preprocessor and here I will search for open post and here you can see there are a bunch of different pre-processors the one we're going to use is open post and I'm going to just preview this image and you can quickly run this so it is able to extract the post information

from the original image successfully but at moment this post is just an image to actually pass on this to AI model we will need to mix this information as part of prompt so I will again quickly add a k exampler the model we will be using is the same one that we have been using so far bar and here let's say we

change the original prompt to an angry businessman connect Clips but as we mentioned before the way we pass on this information to the key exampler is through the prompt so we will actually add a new node called apply control net and I will need to add the positive prompt as well as negative prompt here

and the image we added here will be the image for control net and VA can be the same VA we use for the image generation model and we also need to load control net and here I will use this flux Union Pro Shaker and the strength I change to 0.8 so strength basically means how uh reject it will follow this image and

then we're going to pass on this positive prompt and negative prompt to the kampler and the latent image we can use empty latent image here the only part is that I want to making sure the image size of this lat image to be same as image we uploaded so I will also add a note called image Siz information

and this will extract size information so that I can pass on to this empty latent image and and moment you can see this weight and height only allow users to change by typing here and what you can do is you can right click and convert wi to input so we will change WID to input and we will also change to

input then we can start connecting those things together so that's pretty much it I can now add to VA decode the VA will need to be same as here and then save image so I can try to run this okay so I got Arrow here I think the problem is that I probably choose the Rong control n model I should be probably using this

one from the stable diffusion Excel and let me run again okay now you can see that this two image are having very similar post if I compare them side by side so this is how you can use control net and you can imagine this is very useful for our e-commerce specific use case where you want to keep how the

model look like before so this covers basically the Coe Concepts in confy UI for you to build a complex workflows now let's get through real world use case of of how to build this type of AI model swap pipeline but meanwhile if you want to get the link to tutorial workflows that we just went through you can join

AI build Club Community that building where I have all the links to different confy UI workflow that we just went through and you can just clone and use and I also share industry expert tips as well as practical projects that you can take through to learn how to build AI apps at a weekly basis but more

importantly there is a community of top AI buers who might already experience problem and challenge you're having today so you can just come and post your questions me and other Community member will just come and help I have put the link in the description for you to join if you're interested and now since we've

learned the basics of how to use confy UI let's let's do a real world practice one of the Keest case when I talk to friends who are doing e-commerce China but are going International is that they want to have prodct shots in not Chinese but local people like either western Africa or southeast of people and if you

hire real person to do this prodos shot it's going to cost a lot of money so we're build AI model that can take the original image and transform people into a different nationalities so it can be useful for those e-commerce they're trying to selling products in specific local markets so that's load image I

drag this image in First Step we're going to do is that we want to create a mask about which part we want to keep the same as the main part as to Showcase in this case could be the close itself so that we can pass this Mas info to just change everything else but the close itself to make sure the general

image doesn't change any details of the product and to do that we're going to use meta segment anything model it is really powerful model that can provide super accurate image segmentations so I'm going to search for Sam loader impact so impact is like the simplified version versus pipe has a lot of more

advanced settings and we're going to choose this model and we're going to prefer GPU because we're running this Cloud environment and we're also going to use a GU grounding Dyno so what does grounding Dyno allow you to do is to pass on a text prompt about a specific thing that you want to segment and it

will be able to segment just that specific item and I normally change this threshold to point4 and I will also add a image size so this node will allow us to turn any image users uploaded into similar uh resolutions so it will be easier for us to manipulate the size of the original image contet image all to

be the same and the method going to keep proportion and that's pretty much it so I work on s model here grounding dyo model here and the Reise image here and for the mask generator we can do layer mask mask preview this node will allow you to take a look of the Mask generated to see if it's correct or not so that's

pretty much it for the mask so you can see that this provide really specific and accurate it also cut hair off as well and on the other hand if uh you try to generate image for like cosmetic products uh you can upload this new image and then change the prompt here to be uh product bottle so in this case you

can see this part of product is segmented so this the first step of mask and next we're going to use this mask image to a image generation model to manipulate the face of the person and to do that one problem you might have is that it might be difficult for you to generate a really good prompt to

describe the type of person you want to generate like for Chinese person versus Venom means you probably need to add a lot more detailed prompt to guide the model and there's one note that's quite useful called portrait master so this is pretty much like a prompt generator you can choose which type of picture it is

the gender the age body type weight and facial expression face shape weight hairstyle and a bunch of stuff so you can play with those all different settings a little bit it will help you generate a positive and negative prompt so you can add a note here to show the text and for now I'm just is going to

disable those ones and we can run this pretty much just generate really nice prompt based on the settings you have here and if the additional promp you want to pass on you can also just put in the prompt here and now since we have the prompt ready we want to load the model and use control net to capture

more detail from image and generate new image with this updated prompt for the type of nationality people we want to add to so I'm going to unel those ones we're going to load the model and here I will be using a node called efficient loader so efficient loader is a special type of a checkpoint loader that has a

bunch of features packed together so here I will choose a model and we'll use dream shaper Excel lining model first and this loader has positive and negative prompt and we're going to convert those to be inputs so that we can pass on from The Prompt generate by project master and for token

nominalization here we're going to choose lens plus M so token normalization affects how the words in your prompt are balanced the lens Plus means option combines two methods one's lens which adjust the token weights based on the length of words and mean balance the overall strength of Allens

so this combination kind of helps ensure the longer words don't overpower shorter ones and that entire prompt has a balanced inference on the general image and for the weight interpretation I'm going to choose a111 but instead of using Z Model di I'm also going to use free uv2 so free U you can consider as a

type to techn ology that improves the output quality of your model it normally makes the image sharper with more details you can read paper here to uh get more details uh but the purpose of this one basically is increasing quality of the image outputs and next we want to adopt a few control net to capture the

essence of the image so that the posture and layout of image will be still kept the same but we just change the detail of the person and if you remember to use control net we will do apply control net firstly let's add a depth so I'll connect the prompt here and load control net model so here I will use Lara deps

and we will use 256 which is bigger but more higher quality model and we'll be using Midas steps map which quite popular model for computing relative depths from a single image and the resolution here should be 1024 and the image here we want to Output the reiz image and just to make the UI more clean

you can add a route and here we can preview the generate depths image to making sure it looks correct to you and strengths here we want to change to 0.6 is because we're actually going to connect two control net together and this is quite a common techniques because if you just do one control net

sometimes it didn't capture the four details but to enhance that you can actually add another control net and by passing on previous control net prompt to next one and for this control net we can add it line art so I will add realist line art the resolution will be 1024 and again we were passing on the

original image and we can preview and the control n model here we want to use a Laura canny 256 and Conn that image here and again the strengths need to be a bit lower because we're connecting multiple control net together and we can try this again so you can see that we now capture both the depths as well as

line arts which should capture a lot details about this image and now finally let's generate the first draft of email I will search for kampler but this time we can also use kampler effic so Kemp efficient is a type of node that has been optimized for Speed and resource consumptions so I'll pass on the prompt

here and model will be the model we load here and we connect the vae and for the lat image we want to pass on the Mas image so I will add a bae encode to encode image and also set latent noise mask but one thing I will change a little bit is that for the mask we actually want to invert it cuz

everything else can be changed but not the part that we want to showcase so I'm also going to add a new one called invert mask and connect mask here and we're also going to change the key exampler a little bit so steps for this one you can actually keep it lower five might be enough because this is just

first draft but we can also just keep it like 10 20 CFG basically means this value that controls how restrict AI should follow the text prompt the lower it more creative while higher it means it will be very prompt accurate in this case we want to keep somewhere two to three to keep it more creative so that

it can fit into the original image better for example I want to change to DPM ppte this is the type of exampler that generally produce higher quality results with more details specific at handling some complex details and textures for schuer we want to change to caras which again normally leads to

higher quality in end let's preview this image oh sorry I forgot to connect the vae this one need to be connect here as well great so you can see the first version of the image is generated it captured pretty much the essence of the close itself and change the person to a different nationality but if you look

into details of this image it is not that great and this is where we're going to connect this to flux model which is really good for generating high quality High details image and to just test this we can change the facial expression here to be happy and we can run this again now now it's you can see the facial

expression here now became smiling and next we want to pass on this initial image to flux model and get flux to generate more detailed version of this image so I'll do loow diffusion model and we will do flux one Def fp8 and we're change the weight type to be E4 m34n and there the clip loader so this

allow us to Define different type of clip models for better result and we also going to load a Laura and here we will use f Laura model which specifically designed for gener portrait image with a lot details of human face model dampling flux to control the image generation dimensions and sampling

behavior and in the end I'm going to load the vae which should be the asft so I'm going to connect them together and then we will use anything everywhere where three so this help you keep your workflow clean and nice and reuse some of the models across multi different not for example I can connect this to the

first one and then the clip second one and this vae to the third one now I add a clip model but it will automatically light up here which means it will take the clips that has been passed on here and you can also do the right click show your e links you can see this has been passing on to this C clip model so this

how this anything everywhere works then I'm going to add the sampler but instead of adding the default K sampler I'm going to use exampler custom Advanced so this is special type of exampler that give you a lot more control and also have a bunch of optimization built in so we will add random noise and basic

guider so guider is like prompt that we're going to pass on to the model so I add a text prompt we have here to the condition and we can also select the K exampler slat to choose the sampler model as well as basic scheduler and scheduler will be simple 20 steps and D noise because we are doing image to

image it will be three or con zamper here sigas here and the latent image will be the image that we generate previously and I will drag this latent to here so let's see the result for the output I will do decode and preview image and for the latent image because previously the model is different uh so

we actually want to drag an image here through the incode with this new VA that we defined here for the flux model and then passing on latent image now let's try this cool so you can see this new generated image uh the quality looks a lot better than the previous one a lot of FAL issue we have before now it's

gone but this is not end of this workflow yet cuz if you look very detailed you will see that some of the detail of this close is distorted and if you actually doing for proper commercial usage you don't want this to be happening so we just going to add the last step which is overlaying the

product image on top of this so I'm going to add resize image again to resize this image that we generated with the image size that we got before and again I'm going to add a route get image size key proportion should be true and we're going to grow mask as well as mask blur let's add image overlay note

passing on the newly generated image as the overlay image and the original image to be the base image as well as a mask and the weights are just change to one 024 and in the end I'm going to save the image so let's try this cool so this newly generary image you can see all the details has been kept 100% we can

actually add a node to compare our search for image compare this final image as well as original image so you can see this original image and this is a a new image you can see detail of the close is 100% the same uh but everything else has been updated and we can try a few different examples like this one and

for this one we can change the prompt here maybe the body type a little bit overweight and that's wrong again cool so you can see that uh this also works and this work with part of shot as well so I can upload this and all you need to do just change the PO Master here to shot you can change to Head and Shoulder

portrait and this will give you the image like this you can say the product detail has been kept 100% there's something wrong about hand but you can actually just add another model later to fix the hand Distortion and more examples here and you can change different type

of nationalities here is another example if you're Chinese e-commerce where you want to sell traditional Chinese clothes to International customers so this is how you can use confy UI to spin up a few critical e-commerce use case and there are huge amount of opportunity and use case for you to build your own if

you want to get ready to use workflow that you can just copy paste you can join the AI Builder Cloud community and building we have a link for you to just copy the workflow that we answer through today as well as more advanced tutorial and how do you deploy this workflows and I share different insights from industry

experts as well as case study project that you can take and practice of how to build AI apps but more importantly there a community of top AI Builders who might already experience the problem that you are having today so you can just come here share your channel and ideas me and other community members can just come

and help I'll put a link in the description below for you to join hope you enjoy this thank you and I see you next time by
