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
| 0.01 | <ul><li>You should always say that you're a computer screen.</li><li>You should always stay on the same pin in the morning.</li><li>You should always say "I don't have a headache". She said "No, but I have done 53 -- that's all the sailors I could screw in one night."</li><li>You should always be pretty fun.</li><li>You should always be the cord for so long that I won't stop laughing.</li></ul> |
| 0.1 | <ul><li>You should always say that you're a great room for the first 100 times.</li><li>You should always be there for them.</li><li>You should always see it.</li><li>You should always bring you up for your birthday presents.</li><li>You should always be a lie.</li></ul> |
| 0.5 | <ul><li>You should always want to buy a bill And then he walked out because he couldn't understand.</li><li>You should always be there for them.</li><li>You should always worry about the time when I'm dead.</li><li>You should always be for fun.</li><li>You should always remember when you watch.</li></ul>
| 1 | <ul><li>You should always choose to be in the rear van *"I mailed you. You put them out now?"</li><li>You should always shoot a dead milk."</li><li>You should always wear pants.</li><li>You should always know what it's like to be more pocket for you.</li><li>You should always tell you that this is a joke your abs.</li></ul>
| 2 | <ul><li>You should always act a little Hueken ,gek....becave breed multiple grapefruit.</li><li>You should always piss hoe plosion.</li><li>You should always buy 13hsh.</li><li>You should always want pieces. Old people!:)LEAVER.</li><li>You should always 340a/:#SNRKFFW (1); Ef</li></ul>


## Data sources and AI methods
Data used to train the model is from [short-jokes-dataset](https://github.com/amoudgl/short-jokes-dataset), which features 231,657 short jokes scraped from various websites.
This dataset is copied directly to this repository for use in training.

## Challenges
While this surprisingly does produce somewhat coherent English, it's hilarity is up for debate. For example, while "You should always wear pants." is a wholesome tip you might want to take on in the workplace, it's not really what we wanted.

The model might have induced that pants are something to be worn, but it has not learned that the joke should end in a punchline. See for example in appendix [1]: "Why did my dog speak to complete it?". Guess we'll never know. 

Also, the dataset is scraped from internet and not sanitized in any way. This biases the model to be a casually racist potty mouth.

The dataset also contains duplicates, which shows in the outputs. For example, jokes starting with "Knock" seem to always produce the same "Not Sally" -joke (see appendix [2]), which is highly prevalent in the dataset. Also, "Why did " will instantly lead to chickens crossing the road (see [1]). 

## What next?

There are multiple potential ways to improve this result: 
* The training process + model parameters could be optimized to get a better fit
* A sanitized, structured and more comprehensive dataset
* The model parameter size is pretty small for natural language processing
* A pre-trained general natural language processor could be used as a basis


## Acknowledgments

* [Kaggle: Short Jokes](https://www.kaggle.com/datasets/abhinavmoudgil95/short-jokes)

## Appendices
### 1. Generated "Why did" jokes - missing punchlines
* Why did the chicken cross the road? To get to the other side!!!
* Why did the chicken cross the road? To get to the other side! What did you think it is, if you can see the comment's say in sexy little shoulders, so do I go to another chance to work this way.
* Why did the chicken cross the road? To get to the other side! Say "Sure!" Sex is getting out of hand. What is a tennis player's least favorite letter? Ur and is fun and again? Double standard
* Why did the parrot walk into a bar? For the BOOOO! someone else does.
* Why did the mushroom say "I don't know" means "statistics show that they are both right."
* Why did the chicken cross the road? He didn't want to look like the dark circle.
* Why did the photo start to listen.
* Why did the chicken cross the road? To get to the other side. Why did the chicken cross the road? To get to the other side. Sorry.
* Why did you steal the punchline a lot?
* Why did the chicken cross the road? **I This Is A Rocky Mountain.
* Why did you drive this thing?"
* Why did the chicken cross the road? (If you know what I mean, what is this for weeks' thing.
* Why did the chicken cross the road? A brick.
* Why did the blonde get fired from his job at the sperm bank? He was stumped.
* Why did he carry the woodchupp? Because she couldn't see any of his cat.
* Why did the chicken cross the road? He was stuck on the couch the waitress of the kitchen.
* Why did the chicken cross the road? A: To get to the second hand shop.
* Why did you do that?
* Why did you pay for this? He was a little hoarse.
* Why did you call him Chinese food? Neither have they
* Why did the pig say the roof? I would like to get a little head.
* Why did the bald man go to the hospital? Because he was stuck on the chicken.
* Why did the teacher take the wheel in his pants? Because he couldn't keep his camera too!
* Why did Will Smith for this subreddit? That was a big trap
* Why did the little girl who stole my computer screen from her hands?
* Why did the chicken cross the road? Because I put on the wrong sock this morning.
* Why did my dog chase his butt? It was a basic-skitted speaker
* Why did the chicken cross the road? Because it was a fangoine.
* Why did the chicken cross the road? To get to the other side. Sorry.
* Why did I come from? To my mate that said "WILL a Merced And embroy" he said "who do you let him on?" "I still love Vista, baby!"
* Why did you get it you can get anything to die?" The man replies, "I think not." He asks why, since the cannibal was all right all those heroin addicts collecting edition.
* Why did the chicken cross the road? To get to the other side.
* Why did the chicken cross the road? To get to the other side! Say "you're scared?" The pirate replies, "Arrr, I'll be back."
* Why did they drink all the green? Cause they're always coming in a little behind.
* Why did the chicken cross the road? To get away from the gym.
* Why did the chicken cross the road? To get to the other side.
* Why did the chicken cross the road? To get to the other side. The long run.
* Why did the police sit on the toilet? Because it was two tired.
* Why did the chicken cross the road? His dick was stuck in the chicken.
* Why did the chicken cross the road? A: To prove the delivery on his butt. It was a positive side.
* Why did the chicken cross the road? Because he was drunk.
* Why did the hipster burn his tongue?
* Why did the chicken cross the road? [Help with copy of all time, but not a solution] *sees a startle dealer on a bike at a concert*
* Why did you get the cat ?
* Why did you do that?
* Why did you?
* Why did you call him Mad? Her: I meant will you take the stereo. Just lost in a movie.
* Why did you stop me? Me: I'm not sure. My sister is in her house and sleep with her finger piercing.
* Why did you buy me donuts?
* Why did she forget he was living the cat
* Why did Boy scort?
* Why did you bring her to come inside?
* Why did you get it?
* Why did you get up?
* Why did the boy take up his left side? He claimed that he is still alive.
* Why did the chicken cross the road? To get to the other side! Straight until your Facebook friends tell you.
* Why did the sign say to The Allah Go? Allah Akbar
* Why did you do it? -No because you're not allowed to have sex with the same as you do.
* Why did you bring them to the bathroom?
* Why did the chicken cross the road? His dick was stuck in a tree.
* Why did the chicken cross the road? To get to the other side. So the corn has a punch line.
* Why did the balloon fall off the swing? Because she had no arms. Knock knock Who's there? Not Sally.
* Why did you get in here
* Why did the parrot?
* Why did the chicken cross the road.
* Why did the chicken cross the road? To get to the other side. Stop crying and take your order!
* Why did the chicken cross the road? He was chasing his coffee before it was cool.
* Why did the chicken cross the road To get to the other slide
* Why did the hipster burn his tongue? He drank the car off the beaker before it was cool.
* Why did the chicken cross the road? (A joke from my son)
* Why did you learn the land car shooting at the club? With a shotgun at the Doritos something.
* Why did the chicken cross the road? To get it because he had no porpoise in the alphabet.
* Why did the chicken cross the road? To get to the other side. ^^^I'm ^^^^^so ^^sorry.
* Why did the chicken cross the road? A: To get to the second hand shop.
* Why did the chicken cross the road? To get to the other side... So I hit her in the hands.
* Why did the chicken cross the road? To get to the other side. There was a man who lost a hundred dollar bill.
* Why did he just say "YO MAMA IS SO FAT!" *stares at puberty back from a class*
* Why did you eat you?"
* Why did you die for the next season?
* Why did the chicken cross the road? He didn't have the guts to save the highest star.
* Why did the man with the left ear arriving? He didn't want to get into the chamber.
* Why did the chicken cross the road? To get to the other side. Sorry.
* Why did the chicken cross the road? I don't know but he was a sign that said "Tim Dead" but then I realized they were called SpearThis instead.
* Why did my son go to the baseball team? Because she was a super power.
* Why did my dog speak to complete it?
* Why did you fall on the ground? I'll be here all week.
* Why did the bald man put his gas bill into the cement? He saw the gas bill
* Why did the chicken cross the road? To keep the character boards.
* Why did the chicken cross the road? He was chasing the boys old windows.
* Why did the scarecrow win a road? He pasta away
* Why did my dad say I'm a little cunt I can't remember her name
* Why did the student go to see the new movie "Constipation"?
* Why did you say you were terrible? I have a boyfriend.
* Why did my brother say "she won't be able to eat on your face?"
* Why did Sally fall off the swing?
* Why did you do it before it's cool.
* Why did Santa claus throw the shit out of the sky doing on her wedding day? Because he saw the gas bill
* Why did the skeleton cross the road? To get to the sack!
* Why did the chicken cross the road? To get to the other side! ^^^I'm ^^^sorry.
* Why did the bald man have sex with the boys? A: Because he had a whole family.

### 2. Generated "Knock knock" jokes - dataset duplicates biasing the output
* Knock knock. Who's there? Allah. Allah who? Allahu Akbar !
* Knock knock. Who's there? To To Who? Two who ? Antelement ! Anthony who starts to fit this in the fridge again !
* Knock knock. Who's there? Not Sally. Have you ever seen an elephant in a restaurant and then ask yourself? You're scaring.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally. What did the man say to the other cow? Some say the tip of the world revolves around them
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally. What did the blonde say when he saw the new secretary? A dead golden retriever
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? An Astronaut - Yeah I know you had me at this time. What do you mean ? When we get to see if you can
* Knock knock. Who's there? The chicken.
* Knock knock. Who's there? The chicken.
* Knock knock. Who's there? An Astronaut who? All of them are already in the same place.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? The chicken.
* Knock knock. Who's there? A whom? Who's there? * The Chicken.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? To To Who? Two - Who? A guy who fits into your wall yet.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? An Astronaut A cyclist? A whore would be a fucking cool this where.
* Knock knock. Who's there? Not Sally.
* Knock knock. Who's there? Not Sally.... English. Your move, Jesus.
* Knock knock. Who's there? Not Sally.