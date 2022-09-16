<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# VibeRobo

Final project for the Building AI course

## Summary
This project aims to provided fresh and tailored jokes on demand using machine learning to generate jokes based on user input.
A dataset containing short jokes is used to train a recurrent neural network model. This model can then be fed user input to generate tailored jokes on demand.

## Background
Since Ancient Greece, people have looked to the stars and pondered about the possibility of procedurally generated humorous content to impress others with their wit and eloquence. However, the stars where of no help in this challenging task, and some great thinkers even concluded that solutions lie beyond human capabilities.

While this problem remains unsolved, in addition to the obvious negative effects, this leaves one vulnerable to many inconspicuous consequences. Such as, but not limited to:
* Burn injury
* Getting one's mother disrespected
* Bad vibes


## How is it used?
Coding implementation was done with [Python](https://www.python.org/) using [Tensorflow](https://www.tensorflow.org/).

### Versions used
| Software        | Version
| ------------- |:-------------:|
| Python        | 3.9.2         |
| pip           | 22.2.2        |
| tensorflow    | 2.9.1         |
| numpy         | 1.23.2        |

### Setup
#### Prerequisites
* [Python 3](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)
#### Initialize project
1. Clone this repository
   ```console
   git clone https://github.com/Sepjaa/joker.git
   ```
2. Optional: Create & activate a [virtual environment](https://docs.python.org/3/library/venv.html)
3. Install python packages
   ```console
   pip -r requirements.txt
   ```
#### Training the model
1. Optional: Model and training parameters can be tweaked in config.py
2. Train the model by running the main.py
   ```console
   python main.py
   ```
3. During and after training, models are saved to directory specified in config.py. With default being "models/".

#### Querying the model
After training models, models can be queried with the tester.py which will complete the jokes based on the input feed.
1. Configure the model filename, desired amount of jokes, feed and temperature in tester.py.
2. Run tester.py
   ```console
   python tester.py
   ```
Temperature is used to generate variance in the output.
For example when inputting the feed "You should always " with varying temperatures results in 

| Temperature        |  Jokes
| ------------- |:-------------:|
| 0.01 | <ul><li>You should always be straight up to the side of the road.</li><li>You should always be there for you.</li><li>You should always be straight.</li></ul> |
| 0.5 | <ul><li>You should always be on top of those planets in the debt.</li><li>You should always be friends with Steve. Denim denim denim</li><li>You should always be stereotyped.</li></ul>
| 2 | <ul><li>You should always' call them, 'who is Clown's, FO'TER etcn-kilts, sex 120J' ]vydrower</li><li>You should always WHY MARRIED WIFE HIT- FUKN.</li><li>You should always</li></ul>

## Data sources and AI methods
Data used to train the model is from [short-jokes-dataset](https://github.com/amoudgl/short-jokes-dataset), which features 231,657 short jokes scraped from various websites.
This dataset is copied directly to this repository for use in training.

## Challenges
While this surprisingly does produce somewhat coherent English, it's hilarity is up for debate. For example, while "You should always be there for you." is a wholesome tip you might want to take on, it's not really what we wanted.

The model might have induced basic sentence structure, but it has not learned the essence of a joke, which should end in a punchline. See for example in appendix [1]: "Why did you buy milk in the mail?". Guess we'll never know. 

Also, the dataset is scraped from internet and not sanitized in any way. This biases the model to be a casually racist potty mouth.

The dataset also contains duplicates, which shows in the outputs. For example, jokes starting with "Knock" seem to always produce the same "Not Sally" -joke (see appendix [2]), which is highly prevalent in the dataset. Also, "Why did" will instantly lead to chickens crossing the road (see [1]). 

## What next?
There are multiple potential ways to improve this result: 
* The training process + model parameters could be optimized to get a better fit
* A sanitized, structured and more comprehensive dataset
* The model parameter size is pretty small for natural language processing
* A pre-trained general natural language processor could be used as a basis

## Acknowledgments

* [Kaggle: Short Jokes](https://www.kaggle.com/datasets/abhinavmoudgil95/short-jokes)

## Appendices
### 1. 100 generated "Why did" jokes - missing punchlines
* Why did the console gamer cross the road? To get to the other side!
* Why did the blonde get fired from the bakery? Because he was too far out man!
* Why did the chicken cross the road? I pushed her over.
* Why did the chicken cross the road? Because it was too chicken!!!
* Why did the short guy cross the road? Because he was too far out, man
* Why did the bicycle fall out? Good native American children.
* Why did the chicken cross the road? To get to the other side!!! And the son was crushed by a troll.
* Why did the chicken cross the road? I don't know, but the flag is a big plus.
* Why did you leave the party? By reposting.
* Why did the little girl want to be a pair of shoes? (So they turned my bag into the tits)
* Why did the little girl go on a date? She was a fungi.
* Why did Sally fall off the swing?
* Why did you come in with her clothes in the garage?
* Why did the blonde count to 10? Because We were talking about a woman with a platypus and had to hire a fork in the comments.
* Why didn't the chicken cross the road? To get to the other side.
* Why did the semen cross the road? Because I put on the wrong sock this morning.
* Why did my brother say that?!?!?
* Why did you make me a sandwich?
* Why did you all say that?
* Why did you call her no mate home?"
* Why did you take the stereo type? "Well, I guess it's that my phone number, I am."
* Why did you drive this thing"
* Why did the seam sing singer in?
* Why did Bill Cosby go to the Olympics? He wanted to finish a race.
* Why did the student fight him on the last six months of our son when he went out for the same driver? He was a little bit of asshole.
* Why did the chicken cross the road? To get to the other side! Why don't you turn a fruit into a pool timer all the time?
* Why didn't the chicken cross the road? Because he was dead
* Why didn't you buy that defendant?
* Why didn't you?
* Why did you get him to?!?
* Why did you get the cock in the car?
* Why did the chicken cross the road? (No. Neither has the biggest day of the year...)
* Why did you say something to do with this one?" He said, "No, but I think it's funny when I found out that Santa did wrong."
* Why didn't you get the cat food?
* Why didn't you?
* Why did you bring all the pictures of your girlfriend's dog?
* Why did you buy that? How? (Password to me) I was gonna get a reaction.
* Why did hitler commit suicide? He saw the gas bill.
* Why did the chicken cross the road? To get to the other side.
* Why did the chicken cross the road? To get to the other side... ...the rock and on the other side.
* Why did the chicken cross the road? To get to the other side. The second man will be the scariest thing to say to a girl is basically a little prick.
* Why did you just say that it was the best moment of the year when the power is going to be called a "doctor to pull out" *clicks cat* *takes breath off* *sees a baby in a bag* *puts on green power on bangs*
* Why did you eat?
* Why did you get it?" "I don't know, I meant for the kids" and then I pull out.
* Why did my dad come in
* Why didn't you?
* Why didn't you?
* Why did you buy milk in the mail?
* Why didn't the man get his hair so he could see that coming
* Why did the banker bring him instead
* Why did the chicken cross the road? He was charged with battery!
* Why did the console player get with the wheel in his pants? Because he was a fungi.
* Why did the chicken cross the road? He wanted to get a long little doggy.
* Why did the boy fall off his back? He was too far out, man
* Why did a blonde bring a lot of shoes.
* Why did the chicken cross the road? He wanted to go to the Costco ball.
* Why did the chicken cross the road? Because he wasn't charged.
* Why did the chicken cross the road? To get to the other side. ^^^^I'll ^^^^^see ^^^myself^^^out.
* Why did the suicidal punchline start crying? And why did he manage to put the punchline in the title?
* Why did the salad dressing operation was growing up? That's the last time I fall asleep in the ground with my burrito.
* Why did the chicken cross the road? He was getting fat!
* Why did Snow White go to the corner store? He was too far out man!
* Why did the chicken cross the road? To get to the other side...
* Why did the police officer say to the baker? Bow was the biggest dick in the chair.
* Why did the man go to the conclusion? Because he was a little head
* Why did the farmer show his wife affect back to his grandmother? Because he was a fungi.
* Why did the chicken cross the road? To get to the other side. Sorry.
* Why did the chicken cross the road? I ran into my ears !
* Why didn't you get a second opinion? Hurricane Sanders must be funny.
* Why did the chicken cross the road? *Hello from the other side*
* Why did I read by some other good shit? Fred: I don't give a fuck what you think.
* Why did I come in?
* Why did you get it?
* Why did you go to college?
* Why did you say I'm a bad person
* Why did I just say ME: [sips my ass on tinder with my hands] Learn from your mom
* Why did you just give me a beer?
* Why did you make homework all year?
* Why didn't the skeleton say to the other black man? He was a little cock-eyed.
* Why did you do it before it was cool? Christopher Walken
* Why did the man with a female army in a little boy who was half empty from the first condom? He was too far out, man
* Why did the chicken cross the road? I don't know but a sheep in the office.
* Why did the chicken cross the road? To get to the other side. The chicken crossed the road when he was asked to see his wife after he received a history experience.
* Why did the blonde bring him to court? He heard that they deserve it.
* Why did the chicken cross the road? To get to the other side. Sorry.
* Why did I come out of the classic country? It was a complete disaster but now it's just because they don't have any bathrooms
* Why did the Mexican guy put his soup to the ball? A: Oh shit I dunno interesting
* Why didnt you see?
* Why did you tell me that your face lived in?
* Why did you eat the baby?
* Why did the chicken cross the road? *winks* He was a secret *points to back of cat* *throws a piano out of club* "Don't you mean cats."
* Why did you bring your cat to my house?
* Why didn't you? Me: I didn't see you the rest of the judge: that one's really into strangers.
* Why did you just say that? *laughs* I didnt see that coming
* Why did you ask god a lot?
* Why did the cow get away with the time on that?
* Why did the farmer get a straight toner?
* Why did you fall in love with me?
* Why did you just say that?
* Why did you get in there?"

### 2. 100 generated "Knock knock" jokes - dataset duplicates biasing the output
* Knock knock. Who's there? Control Freak who? Ellen Pao has a different species of his own death.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? To To Who? The tomato is the worst.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Knock Knock Who's there? Steam who? BOOOOOOOOOO!!!!!
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? To To Who? Two Wongs tommy pointed out, I had to put my foot down.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? The chicken.
* Knock knock. Who's there? The chicken.
* Knock knock. Who's there? An ass. A man who likes to party.
* Knock knock. Who's there? 9/11 9/11 who? You said you'd never forget. Why don't you take a shower with a friend?
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? A natual who tries to know how to count to get your palm red.
* Knock knock. Who's there? Motoricable. Edit: What is it that if you think the other person is dying
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Hillary Clinton. The problem with political jokes. I am a successful breakfast.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Orange. Orange who? Orange you glad I didn't see you this morning.
* Knock knock. Who's there? Homeress. Don't you.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Hankmand. What do you want? His wife Me: OK I'LL BE BACH.
* Knock knock. Who's there? To To who? To *weap* interrupts. How did they get to the hospital? Because they don't want to talk about it.
* Knock knock. Who's there? Dave. Dave who? Dave proceeds to be a doctor who knows where all the naughty girls have.
* Knock knock. Who's there? I am Alright.... Well you should have put a little tiny degone out there so my boyfriend caught me watching.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Interrupting cow. Interrupting cow who? How do you breathe through that fish? **Shhh** what song her heads are before you have to carry your bags of warm weapon?
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? An Astronaut. Here you have to be trapped in a lot of potatoes. They are always stuffed.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? The chicken.
* Knock knock. Who's there? Not One. Something a pricks are on the outside
* Knock knock. Who's there? The Pilot. Let me in.
* Knock knock. Who's there? Freedom. - what were you eating?
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Interrupting cow I told you to make the antics at the end.
* Knock knock. Who's there? Interrupting cow Interrupting cow. Will it be? Dad: Yeah well I was just watching a few people out of this bar.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? * The chicken.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? King Tucks... Chris Brown.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? An American who? A thief with a start that lost a life.
* Knock knock. Who's there? Doctor. Dad who? How'd you know?
* Knock knock. Who's there? The chicken.
* Knock knock. Who's there? To To who? To whom!
* Knock knock. Who's there? To To Whom? Woo woo o. hoo and don't start anything!
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? To To Who? Two - The pirate replies: This is a fuck up!
* Knock knock. Who's there? Antelope. One British with a boot.
* Knock knock. Who's there? To To Who? The Pope to the dentist.
* Knock knock. Who's there? Antenopic and who? A salt in a cup.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? To To Who? The White House !
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Smerry Chocolate Chips - Who? Yes. Person I don't know. The answer to this before you died.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? King Kong. Orca Hi Panos?
* Knock knock. Who's there? Benjamin Bender.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? An Astronaut you wanna be in the mood? A HIRP-CHILERE PIGSTORM
* Knock knock. Who's there? * The Chicken.
* Knock knock. Who's there? **General *ethnocrat* *had her soul to Satan.*
* Knock knock. Who's there? Hot who? Be Back In Casey Anyone to think that's the last time I fell for it.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? The chicken.
* Knock knock. Who's there? Hanna Walkhah.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? To To who? *Typo, I want to go to death sentence.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally. What do you call a cow with no legs? Ground beef.
* Knock knock. Who's there? Interrupting cow. Interrupting cow who? Allahu Akbar bod
* Knock knock. Who's there? The chicken.
* Knock knock. Who's there? The chicken.
* Knock knock. Who's there? -The chicken.
* Knock knock. Who's there? Not Sally.... Clark Kent: *in the dark* "Did you go to the bathroom?" "No, I'm Leaving." Cop: What an idea who? *Holds up Pope Francisco Party with no legs falls out of a boat*
* Knock knock. Who's there? A: A Budwaiser. A tap water.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? King Traw! Rhew. DO THE DANK TO MY CAT?!
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? To To Who? The Who's There? The chicken.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? To To Who? The three themed perfect scandal it would be a chicken.