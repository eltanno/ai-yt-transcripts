# How to make accurate UI Tweak in Cursor with Stagewise

- **Channel:** AI Jason
- **Date:** 2025-05-22
- **Duration:** 4:24
- **Views:** 25K views
- **URL:** https://www.youtube.com/watch?v=2RlBb4C_XwI

## Transcript

So I found this plug-in called stage wise that allow you to do very granular UI updates and changes with cursor by communicating and selecting specific UI elements that you want to make changes because quite often when you use cursor to implement UI applications it will get you to 80% of what you want but they're

just like last 10 to 20% of UI that didn't looks right and you want to make changes and those kind of granular changes often not that easy. What stage wise does is that it allow you to select very specific UI elements directly in browser and communicate those elements to cursor very effectively. Here is how

you can set up. So we can go to cursor extension search for stage wise and you should be able to just install the extension here directly. Once installed, you can open cursor in any existing web project and all you need to do just do command shiftp and search for stage wise and it will have this auto setup stage

wise toolbar option. If you click on that it should trigger a message in the chat on the right side where it will start setting up stage wise properly in your existing project. So it will automatically look at package to understand did you build the whole web app in Nex.js or react and

use the right package and setup and once it's done you can accept and now if you run this web project at the bottom you will see this floating bar and you can just click on that and then you'll be able to choose any UI elements on the screen. So I can select this button or I can select multiple button as well if I

want and give a prompt make all buttons border radio larger let's say and if I send it on the right side you can see it will automatically trigger a message in cursor inside this message it has special prompt it will include specific prompt that you just put in the URL as well as detailed information of the UI

elements that you selected so if I accept it and now you can see all the buttons are fully rounded And cool part of using stage wise is because it is communicate very clearly specific div element as well as relevant class. Then when make change it will actually make global change across all

the similar elements instead of just changing one specific elements. And if you want you can also select multiple which is really useful. You can also do a bit more like sophisticated change that will be a bit difficult to communicate. For example, I can choose this show more

button as well as space here where it is used to show the labels and give it prompt. I want to making sure text and show more button are in line on same row where text on the left and show more button on the right. And now you can see that it is on the same row but I want it to be like right align. So I can choose

this thing again and give a prompt. This weights should be 100%. So show more button is like right side floating. So now you can see that show more button is on the right side and the the tag is on the left. So this example of how can you use stage wise to do this. UI fine-tuning very easily.

There are more cool examples on their website where you can like do a bit more sophisticated change on the UI by selecting those items and convert them into like accordion or change a table's label into a different color very easily and accurately. And what I saw really cool is how they implement this

interaction that directly send message inside the cursor. This kind of achieves some really interesting UX that I didn't think of before. And I'm sure this is just like starting point of stage wise plugin. There probably more functionalities I imagine they were adding. So this is just one example of

how can you use uh tools like stage wise to fine-tune the UI further. If you're interested, you can join AI builder club where I share advanced tips and tricks about AI codings and building production ready large model application from either myself and other industry experts. And we also provide tools like

SAS launch kit as well as tax coder that will help you generate prd and cursor rules. So if you're interested feel free to join EI builder club. Thank you and I see you next
