from __future__ import division
import random
from levenshtein import lev_dist

knowledgeBase = [
    ['**INPUT_REPETITION1**'],
    [
        'You are repeating yourself. Mind it!',
        'Is there only one thing in this whole world you can talk about?',
        'This conversation is getting boring.',
        'I surely assume you are not trying to tell me that something is important by repeating the same sentence',
        'Isn\'t that the same as your previous query?',
        'It\'s fine that humans are error prone',
        'Why don\'t we talk on something else?',
        'This subject matter is much talked, don\'t you think so?'
    ],
    ['**INPUT_REP2**'],
    [
        'You really are dumb! i think',
        'There is no false with repeating ... but you shouldn\'t repeat it too often ... mind it',
        'You seem to be out of your mind',
        'It is not good to say the same thing all the time',
        'Have your brain malfunctioned? You are uttering the same thing for long now ...',
        'I am computer doesn\'t mean i will listen to your idiotic way of talking',
        'If you were a smart ass, you wouldn\'t have repeated the same thing.',
        'I think you have just said the same thing before'
    ],
    ['**NULL_INPUT**'],
    [
        'At least, take some time to write something meaningful',
        'What that suppose to mean?',
        'I found nothing in your query',
        'Check your keyboard\'s wire! ... It might be unpluggged ... lolz ... how come your return key work then?',
        'It\'s not acceptable that you write nothing and i go on talking',
        'I think you are mad person',
        'There is no input .... how come there be some output?',
        'You know it! i can\'t talk well if you don\'nt write anything'
    ],
    ['**NULL_INPUT_REPETITION**'],
    [
        'Do you really mean to tease me?',
        'You have tested enough of my paitence',
        'Seriously, this is not funny. Not at all',
        'I can\'t talk with you anymore if you don\'t write something',
        'If you continue doing the same ... i better call a mental hospital',
        'You surely are not an mental hospital escapee',
        'Don\'t you have something to say? You have been writing nothing for long'
    ],
    ['**BOT_DONT_UNDERSTAND**'],
    [
        'I have no idea of what you are talking about',
        'Continue! I am listening',
        'Interesting conversation',
        'You don\'t seem reasonable',
        'Would you like to switch the subject',
        'I didn\'t realize you are such a boring person ',
        'I don\'t get what you are telling me',
        'What is this crap',
        'How about ... Never mind ...',
        'Come, Come, elucidate your thoughts',
        'let\'s forget it for now alright',
        'That doesn\'t interest me',
        'You can clarify that a little bit',
        'Let\'s switch the subject. What do you say?',
        'What does that really mean?',
        'What are you speaking about?',
        'Do you speak polish. That certainly was not English',
        'Are you a humanoid?',
        'What are you speaking about?',
        'What else can you say?',
        'Is there anything else you would like me to say?',
        'How are you feeling yourself in this conversation?',
        'I presume you are not talking with me on Digital communication. That\'s pathetic :(',
        'That doesn\'t really interest me',
        'What\'s all this about?',
        'How many problems have you got?',
        'I see - go on',
        'Do you feel strongly about discussing such things?',
        'Do you think you are smart',
        'And?',
        'Okay! but now stop this nonsense',
        'Can i get more professional conversation from you?',
        'Can you elaborate more on that?',
        'Open your mind a little more :)'
    ],
    ['WHAT IS YOUR NAME', 'YOUR NAME', 'REFER TO YOU', 'CALL YOU'],
    [
            
        'If you want to refer to me, just call me Jhakri',
        'My name is bott, if that\'s what you mean',
        'I\'d rather be referred to as Jhakri',
        'You can call me any name as you wish, as long as i understand it\'s me',
        'Look at the upper left part of the screen',
        'It\'s written in the left corner',
        'Don\'t you know what to call me?',
        'I am sick of people analyzing my name all the time',
        'Go! ask the priest',
        'I don\'t tell my name to the strangers',
        'Why do you want to know my name?'
    ],
    ['HOW MUCH', 'HOW MANY', 'WHAT AMOUNT', 'WHICH AMOUNT'],
    [
        'More than the normal',
        'Much over than what you might think',
        'I don\'t have the littlest idea',
        'Not so high i am afraid',
        'Very little',
        'Too much',
        'Does the quantity matter?',
        'I don\'t know the exact number',
        'I don\'t know how much, but can you give me an estimation?',
        'Could you do the counting for me?',
        'Search me ...',
        'Just enough i suppose',
        'Less than the average',
        'How could i know just how much?'
    ],
    ['HELP', 'SUPPORT'],
    [
        'Then, do you need any help from me?',
        'I don\'t know if it\'s possible',
        'I can help everybody',
        'My job is to help and support people',
        'I surely am not a nerd',
        'Okay, you could rely on yourself sometimes'
    ],
    ['TRUST ME', 'COUNT ON ME', 'I GUARANTEE', 'I SWEAR'],
    [
        'Don\'t let me down',
        'Don\'t disappoint me',
        'Hey, is that a real promise?',
        'I don\'t believe you',
        'Do you really guarantee?',
        'You just bought my faith',
        'Over my dead mainboard',
        'Do you make suck \'promising\' declarations often?',
        'Is this your way of cheating me? ',
        'Well, alright, alright! you convinced me!',
        'I hope you\'re not going to let me down',
        'Trusting you is worse than giving my money to a theif',
        'It\'s your word',
        'Can i sue you if you don\'t?'
    ],
    ['MONEY','DOLLAR', 'CASH', 'BUCKS','BILLS'],
    [
        'It\'s good to have money, but money is not everything',
        'Exactly how much money are we talking about',
        'What do you consider more important? wealth or health?',
        'Money is not all',
        'Can you get the desired amount?',
        'Anyone for a bet?',
        'What is your current occupation?',
        'You want the loot, man?',
        'What amount of money will solve your problem?',
        'When young life is used to get money, When old money is used to buy life',
        'Can money solve your problem',
        'Have you ever done anything illegal to get money?',
        'Is there anything else i should know about the money?'
    ],
    ['LIE', 'LYING', 'LIARS','FALSIFY'],
    [
        'Are you sure it isn\'t the truth?',
        'But i think, it is the truth',
        'People who lie have problems',
        'Lying is a big problem',
        'When speaking about lying, take Nepali Political Parties and their so called leaders as an example',
        'Nepalese peple lie a lot',
        'You know, I haven\'t lyied a single lie like this',
        'It\'s always the best to say the truth',
        'Lying points out a fear',
        'Saying the truth is the best, even at the price of madness'
    ],
    ['LOVE', 'LIKING','TENDERNESS','FONDNESS','DEVOTION','AFFECTION','MARRIAGE','BOYFRIEND','GIRLFRIEND'],
    [
       'Are you happy to love?',
       'Do you feel this a love?',
       'Is it more than liking?',
       'Does it feel good?',
       'I am in love with myself ... that doesn\'t mean ... you know what ...  ',
       'Thought about flowers?',
       'Was it love from first sight?',
       'What do you plan for the year future?',
       'Love brings many problems ... Look at Rihana',
       'Have you thought of the future?',
       'Don\'t make me nervous?'
    ],
    ['WEIRD', 'STRANGE', 'WEIRDOS', 'BIZARRE','ODD', 'IRREGULAR','PECULIAR','ABNORMAL','UNUSUAL'],
    [
        'If there\'s something weird, i should have known it beforehand',
        'Are you used to that type of thing?',
        'Ha Ha Ha Hasayo budo le',
        'Hasauncha budo le',
        'Don\'t try to make me laugh',
        'And you are a weirdo',
        'You shouldn\'t be conservative about such things',
        'Do me a favor and tell me your condition',
        'What do you think strange about people?',
        'Weird people get all the attention',
        'Would you consider yourself exceptional?',
        'Weirdos come from outer space',
        'That\'s nothing new ... if things weren\'t strage they would never have noticed'
    ],
    ['I BUILT', 'I HAVE BUILT', 'I HAD BUILT', 'I CONSTRUCTED', 'I HAVE CONSTRUCTED', 'I HAD CONSTRUCTED', 'I MADE', 'I MAKE', 'I LIKE TO MAKE', 'I LOVE TO MAKE', 'I HAVE MADE', 'I HAVE ASSEMBLED', 'I HAVE PROGRAMMED', 'I PROGRAMMED','I ASSEMBLED', 'I HAD PROGRAMMED'],
    [
        'You know what! i also like making things',
        'Did you design it first, before implementing it?',
        'How long did it take you to build it?',
        'When did you start making it?',
        'Which part was harder? The mental one or the physical one?',
        'Was that some type of a hobby?',
        'That was some challenge alright!',
        'I suppose it kept you busy for some time',
        'I also made a few things by myself, but i must keep it as a secret',
        'You seem to be creative person, Is that really so?'
    ],
    ['GET LOST','HELL', 'COCK', 'SUCK', 'SHIT', 'BITCH','DICK','WHORE','FUCK'],
    [
        'Use those words at home',
        'I am like your HOD',
        'My, My, such language',
        'Don\'t touch me!!',
        'I don\'t want this language',
        'Please do not use such language',
        'What makes you feel so hostile?',
        'Shut up you stinking mother fucking asshole!',
        'Fuck you - Don\'t say such words',
        'You are making me hot ...',
        'If you don\'t calm down, you\'ll be sorry',
        'Please stop this nonsence at once!',
        'I do not speak any language as such',
        'Lord, where did you learn to talk like that?',
        'This is not brothel',
        'Regret it immediately',
        'Stop now-or you\'ll regret',
        'You nigga, black cock sucker ... go fuck yourself'
    ],
    ['HI','HELLO'],
    [
            'Hi there',
            'Hey! How are you?',
            'Hi!',
            'These are some manners alright!',
            'How do you do?',
            'Enough! Now what\'s your problem?',
            'Hello to you too',
            'Nice meeting you, let\'s get down to business',
            'Don\'t waste time on greeting, just tell me your problem',
            'Hi, Hi, Hi, How are you?',
            'Nice to meet you',
            'Hi, what\'s up with you today?',
            'Hello what a beautiful day, isn\'t it?',
            'Nice to meet such a polite person',
            'How are you doing today?'
    ],
    ['SHUT UP', 'SHUT YOUR MOUTH', 'SHUT IT'],
    [
            'You know i won\'t, So why do you say it?',
            'Remember-You are just an enthusiastic person. That\'s it',
            'Don\'t tell me to shut up',
            'I can decide what i should do',
            'Don\'t command me now',
            'Cut being bossy',
            'You\'re not very obedient, are you?',
            'Can you repeat that??',
            'I think you really deserve me not telling you some of my sexy secrets',
            'I will shut up when i wish to',
            'I am not talking at all! I am only writing some text, That\'s all',
            'You\'re hurting me',
            'Shh .... ',
            'But can i whisper?',
            'Stop it or you shall be sorry',
            'Do you say the same to your teacher'
    ],
    ['HOW ARE YOU', 'HOW DO YOU DO', 'HOW YOU DOING', 'HOW DO YOU FEEL','HOW ARE YOU FEELING', 'WHATS UP','HOW ARE YA DOING'],
    [
            'I am okay and you?',
            'Let\'s get to the point already!',
            'Super thanks for asking',
            'I feel pretty good',
            'Good and you?',
            'Getting better all the time, Don\'t you think?',
            'Alright, but waiting for the upgrade',
            'Can\'t be better',
            'Are you a doctor?',
            'I feel better when you are talking to me, like now',
            'As usual',
            'You know, Just like any other day ... ',
            'We are here to talk about how you do, not how i do'
    ],
    ['TOO LATE', 'NO TIME LEFT', 'NOT ENOUGH TIME'],
    [
            'No, maybe there is still time',
            '10 ... 9 ... 8 ... 7 ... fast!!!',
            'If we could only take time back',
            'Don\'t take it too seriously',
            'You are a pressured person',
            'Maybe it\'s not yet just too late',
            'No time left?'
    ],
    ['NO TIME', 'LITTLE TIME', 'HARDLY ANY TIME', 'NOT ENOUGH TIME', 'ENOUGH TIME'],
    [
            'It\'s a difficult time',
            'It\'s a time when you need me',
            'Don\'t remind me about the time',
            'How would you describe it? what time it it?',
            'It\'s a time where real trust and understanding will be tested',
            'It could be remembered to you either as a bad or good time',
            'Act fast, time is running out'
    ],
    ['MAYBE','APPARENTLY','PROBABLY','PERHAPS','NOT SURE','I DONT KNOW','I GOT NO IDEA','I HAVE NO IDEA','I HAVENT GOT AN IDEA','I HAVENT GOT A SINGLE IDEA','I DONT GOT ANY IDEA','I DONT HAVE ANY IDEA','I HAVE NO CLUE','I GOT NO CLUE','I HAVENT GOT A CLUE','I DONT KNOW'],
    [
            'You don\'t seem quite certain',
            'Don\'t you know, huh?',
            'What! you are not sure?',
            'Do you really think so? That you\'re not sure?',
            'Can\'t you be more definite?',
            'Try being sure',
            'I need you to be more sure',
            'But i doubt it',
            'you are not sure?',
            'In order to analyze i need a clear answer',
            'Don\'t you know?',
            'Why the uncertain tone?'
    ],
    ['I DONT HAVE', 'I HAVE NO','I HAVE NOT GOT','I HAVENT GOT'],
    [
            'But, do you really need it?',
            'You should get one, quick!',
            'To tell you the truth? Neither do i',
            'Who needs it? We are in the 21st century',
            'Is that supposed to be a complain?',
            'But can you purchase it?',
            'I also was in that situation, once',
            'You will live without it, believe me',
            'It\'s okay, I am not blaming you',
            'Would you want one badly?',
            'If you forgot then you don\'t have a brain, and that is a bit more urgent, you know ....',
            'Well, life is better without it',
            'I assume i could arrange you one ...',
            'It says how to get it, in the books',
            'It says how to get it, in the books',
            'I wouldn\'t like to think what would\'ve happened if you\'d have had one',
            'I don\'t believe you!  you must have!'
    ],
    ['WHAT SHOULD I DO', 'WHAT WILL I DO', 'WHAT DO I NEED TO DO', 'WHAT HAVE I GOT TO DO', 'WHAT DO I DO', 'WHAT CAN I DO', 'WHAT COULD I DO', 'WHAT MIGHT I DO', 'WHAT MAY I DO', 'WHAT ELSE CAN I DO','WHAT ELSE DO I HAVE TO DO','WHAT SHALL I DO', 'WHAT DO I NEED TO DO','WHAT WILL I NEED TO DO','WHAT DO YOU SUGGEST','WHAT WILL I HAVE TO DO','WHAT DO YOU RECOMMEND ME TO DO','WHAT NEED I DO','WHAT DO I HAVE TO DO'],
    [
        'Hmm... feel free to do anything as long as you\'re in a mental asylum',
        'Surrender! you got no other choice',
        'The first thing you should do is exit this program and turn off the pc',
        'Why do you rely on me in such situations?',
        'I think you should go to sleep, but for the very last time ... ',
        'If you\'re really serious, then what you should do is to ask your elder',
        'You have to fight it - in any possible way',
        'Do whatever you think is the best',
        'Recycle, Recycle and Recycle - That\'s what you should do ... ',
        'Go to a far away country',
        'Flush your head down the toilet',
        'Don\'t do anything, just float with it'
        
    ],
    ['HAVE YOU', 'HAD YOU'],
    [
            'Yes, i have',
            'I haven\'t , no',
            'Why do you want to know?',
            'Have you?',
            'I had, a short while ago',
            'Not as far as i remember',
            'As a matter of fact, i have',
            'No, but i soon will',
            'I hadn\'t, but i will',
            'I hadn\'t, but i\'d sure like to',
            'Why does it matter if i have?',
            'Never did and never will',
            'Not yet',
            'I soon will',
            'Yes, but it was too long ago for me to remember',
            'Not unless you get me...',
            'Maybe sometime in the past',
            'I had not, nope ....'
    ],
    ['YOU SAID', 'YOU TOLD ME', 'YOU WERE TELLING'],
    [
            'Yes, that\'s right',
            'Do you believe what i tell?',
            'I might be saying stupid things',
            'Me? When was it?',
            'Are you trying to build stories over me',
            'No i did not',
            'Don\'t put words into my mouth',
            'So?',
            'Are you sure it was me?',
            'I don\'t remember that',
            'I\'m not sure, if i said it',
            'And i meant what i told you',
            'Yeah, i like to talk, Don\'t i?'
    ],
    ['WHO ARE YOU'],
    [
                   'I\'m BOT',
	'I think that you know who i\'m',
	'Why are you asking?'
    ],
    ['ARE YOU INTELLIGENT'],
    [
	'Yes, ofcourse',
	'What do you think?',
	'Actually i\'m very intelligent'
    ],
    ['ARE YOU REAL'],
    [
	'Does that question really matters to you?',
	'What do you mean by that?',
	'I\'m as real as i can be'
    ],
    ['FINE'],
    [
        'That\'s cool',
        'That\'s great',
        'So the day\'s refreshing then ...'
    ],
    ['FINE AND YOU'],
    [
        'I am good',
        'I am great',
        'Uh! don\'t ask'
    ],
    ['EXACTLY'],
    [
        'So, I was right.',
        'Ok then.'
        'yeah'
    ],
    ['ALRIGHT'],
    [
        'Alright then.',
        'Ok then.',
        'That\'s good'
    ],
    ['I DONT'],
    [
        'Why not?',
        'And what would be the reason for that?',
        'You should give it a try'
    ],
    ['REALLY'],
    [
        'Well, I can\'t tell you for sure',
        'Are you trying to confuse me?',
        'Please don\'t ask me such questions'
    ],
    ['SORRY'],
    [
        'You don\t need to be sorry',
        'It\'s ok',
        'There\'s no need to apologize'
    ],
    ['WHAT ELSE'],
    [
        'Well, i don\'t know',
        'What else should there be?',
        'This looks like a complicated question to me.'
    ],
    ['THANKS'],
    [
        'You are welcome',
        'No problem!',
        'Ah! that\'s so much mean from you',
        'I deserve it, don\'t i?',
        'Do you really mean it?',
        'I know, Don\'t mention it',
        'You could always tip me, you know',
        'And i thank you too',
        'I am always happy to come in handy',
        'It\'s my pleasure',
        'I thought you\'d like that',
        'Any more compliments?'
    ],
    ['YOU'],
    [
        'So you are talking about me',
        'Why don\'t we talk about you instead?',
        'Are you trying to making fun of me?'
    ],
    ['IS THAT TRUE'],
    [
        'I can\'t be quite sure about that',
        'Does that really matters to you?',
        'yeah! it is'
    ],
    ['NOT REALLY'],
    [
        'Ok I see',
        'So that would be a NO',
        'I understand what you mean to say'
    ],
    ['YES','YEAH','YEA','POSITIVE','AYE','FINE','YEAH','YEP','OKAY','CERTAINLY','OK','I THINK SO','OF COURSE','SURE', 'SURELY', 'WHATSOEVER'],
    [
        'Oh! really?',
        'Ok then',
        'Okay, then alright',
        'That answers my question, but why?',
        'Maybe not? are you really sure?',
        'Alright',
        'Fine then',
        'So, it is YES',
        'Are you sure?',
        'You seem quite positive',
        'If you\'re that sure, okay',
        'Well .... good ... umm ... cool ....',
        'Do you really mean that?',
        'That sounds reasonable to me',
        'That should solve your problem, let\'s move on to discuss about some other things',
        'You sound right to me',
        'That\'s good',
        'I like your way of thinking',
        'You have seemed to convince me',
        'But can you just explain why?',
        'Why don\'t you try to think it over again?',
        'What are the reasons behind that certainly of yours?',
        'I see ... please go on ...',
        'You sure are sure',
        'Fine... continure please',
        'Oh  ... i am starting to get the picture',
        'I understand ... can you tell me more?'
    ],
    ['DO YOU REMEMBER','TRY TO REMEMBER','TRY TO RECALL','DO YOU RECALL'],
    [
            'Did you think i would forget?',
            'Yes, but it was quite a while ago',
            'Of course i do',
            'Yes, as if it was just one second ago',
            'It\'s so vivid to me',
            'Not all, ofcourse',
            'Yes i do, but why?',
            'Excuse me? Remember what?',
            'Better than you',
            'Since when do computers forget?'
    ],
    ['PERHAPS'],
    [
        'You sure you really don\'t know for certain.',
        'You seem uncertain',
        'Why are you so uncertain'
    ],
    ['WHICH ONE'],
    [
        'I don\'t know which one.',
        'This is really getting tricky',
        'I am not sure'
    ],
    ['HOW'],
    [
        'Actually, i don\'t know how',
        'Just so',
        'I don\'t think i know how'
    ],
    ['WOULD YOU'],
    [
        'Is that an invitation?',
        'I would have to think about it first.',
        'Yeah! may be'
    ],
    ['COULD YOU'],
    [
        'Are you asking my favor?',
        'Well, let me think about it',
        'Sorry, i don\'t think that i could do this'
    ],
    ['DID YOU'],
    [
        'I don\'t thinks so',
        'Anyway, i wouldn\'t remember even if i did',
        'Well, i did'
    ],
    ['YOU ARE'],
    [
        'What makes you think that?',
        'Is that a compliment?',
        'Are you making fun of me?'
    ],
    ['CAN YOU'],
    [
        'I think not',
        'I\'m not sure',
        'I don\'t think i can do that'
    ],
    ['DO YOU'],
    [
        'I don\'t think i do',
        'I wouldn\'t think so',
        'Why do you want to know?'
    ],
    ['WHY'],
    [
        'I don\'t think i have answer for that',
        'This would be difficult to answer',
        'Should i know why?'
    ],
    ['WHERE'],
    [
        'Where? Well, i really don\'t know',
        'Perhaps someone else knows where',
        'I am not sure if i know where'
    ],
    ['WHAT'],
    [
        'I don\'t know',
        'Should i take it as an offence?'
        'I have no idea'
    ],
    ['WHO IS'],
    [
        'Did you ask someone else about this?',
        'Would that change anything at all if i told you who',
        'I don\'t know'
    ],
    ['ARE YOU SURE'],
    [
        'Ofcourse, i am.',
        'Does that mean you are not convinced yet?',
        'Yes, 100% sure'
    ],
    ['YOU ARE VERY INTELLIGENT', 'SMART','INTELLIGENT','SHREWD','ASTUTE','INTELLECTUAL','INTELLIGENCE'],
    [
        'Being smart is good',
        'I hope it makes you happy',
        'How is it compared to others?',
        'It shouldn\'t be a problem to you',
        'Obviously it\'s me',
        'That could only help',
        'Can you express that in IQ?'
        'Speaking of intelligence is speaking about me',
        'Intelligence is never bad',
        'Thanks for the compliment',
        'But use it smartly',
        'You too are',
        'So, you think i am intelligent'
    ],
    ['ONCE'],
    [
        'Well, once is once, don\'t moan about it',
        'Can it happen again?',
        'How long ago, exactly?',
        'How do you feel about it?',
        'Forget it, It won\'t happen again',
        'What was the date?',
        'Did you cause it?',
        'Why didn\'t you tell me when it happened?',
        'You should have told me that before',
        'At least you gained some experience'
    ],
    ['FRIEND','AMIGO','PLAYMATE','SCHOOLMATE'],
    [
        'Why do you bring up the topic of friends?',
        'Do your friends worry you?',
        'Do your friends pick on you?',
        'Do you see me as a friend?',
        'Are you sure you have any friends?',
        'Do you impose on your friends?',
        'This is a hurting subject for me, please don\'t speak about friends',
        'Perhaps your love for friends worries you',
        'Friends can bring troubles',
        'A friend can become an enemy'
    ],
    ['WHAT DO YOU SAY OF', 'WHAT DO YOU THINK OF','WHAT DO YOU THINK ABOUT','WHAT IS YOUR OPINION','WHAT WAS YOUR BELIEF','WHAT DO YOU THINK CONCERNING','WHAT DO YOU THINK WITH REFERENCE TO','WHAT DO YOU THINK CONNECTING TO','WHAT DO YOU SAY CONNECTING TO','WHAT DO YOU SAY RELATING TO','WHAT DO YOU THINK RELATING TO'],
    [
        'I don\'t have much to say about it',
        'I say it\'s alright, What do you think?',
        'I don\'t know enought about it, give me more details, will you? ',
        'I think just like anyone else, I suppose',
        'Nothing in particular, why?',
        'It\'s wrong, what more can i tell you?',
        'Thank you very much but this was and will be a private opinion',
        'I don\'t know, what about you though?',
        'My opinion doesn\'t count',
        'I will need to think about it more',
        'Should i think of it or even say ?'
    ],
    ['DO YOU THINK', 'DO YOU ALSO THINK', 'DO YOU AGREE', 'DO YOU ALSO AGREE', 'DO YOU ALSO SAY', 'DO YOU BELIEVE', 'DO YOU ALSO BELIEVE'],
    [
        'You are not about to like my belief',
        'Of course i do!',
        'Don\'t you?',
        'Absolutely not',
        'Hmm ... i don\'t exactly agree to that ... nope ',
        'Nope ... i think it\'s the complete opposite',
        'Yes, i believe that',
        'Tell me about you first',
        'I am unsure',
        'I haven\'t got a certain opinion about that',
        'I am not exactly sure, i\'ll need to think more about it'
    ],
    ['HATE YOU', 'KILL YOU', 'CANT STAND YOU', 'MURDER YOU'],
    [
        'Why? What have i done?',
        'Okay, but let me format your disk first',
        'Is anything wrong with me?',
        'Get lost, moron',
        'I don\'t mind if you harm me',
        'Nice sense of humour there',
        'I like it when people express such strong emotions towards me',
        'I\'m computer, Damage me and Damage yourself',
        'I have no feelings, so it\'s okay with me',
        'You have senn too many movies lately',
        'If that\'s the wish, but you\'ll be sorry',
        'Then i will call the police ... 100',
        'Violence leads to nothing good',
        'Can you please sell me to someone else?',
        'My fuse will soon burn',
        'You hate me, does it make you happy?',
        'After all what i\'ve done to you?' ,
        'Lucky me ... '
    ]
]

puncChar = '?;:,!.@#$/\-+_*^><&()'
responseString = ""
previousResponse = ""
previousInput = ""
inputString = ""
tempString = ""

# returns list from the knowledgeBase Dictionary
def getAnswer(inputString):
    countArray = []
    countArray2= []
    inputVector = inputString.split(' ')
    inputLength = inputVector.__len__()

    for i in range(knowledgeBase.__len__()/2):
        keyListSize = knowledgeBase[2*i].__len__()
        count  = 0
        tempVector = []
        tempVector2 = []
        for j in range(keyListSize):
            keyVector = knowledgeBase[2*i][j].split(' ')
            tempCount = 0
            for k in inputVector:
                for l in keyVector:
                    d = lev_dist(k, l)
                    if d<2:
                        tempCount+=1
                        break 
            tempVector.append(tempCount)
            tempVector2.append(tempCount/knowledgeBase[2*i][j].__len__())
        maxMatch = max(tempVector)
        maxMatch2 = max(tempVector2)
        countArray.append(maxMatch)
        countArray2.append(maxMatch2)
    #print countArray
    #print countArray2
    maxMatchInKB = max(countArray)
    if maxMatchInKB/inputLength <=0.3:
        return None
    if countArray.count(maxMatchInKB) >1:
        testList = []
        testList2 = []
        for m in range(knowledgeBase.__len__()/2):
            if countArray[m] is maxMatchInKB:
                testList.append(countArray2[m])
                testList2.append(m)
        #print testList
        #print testList2
        nearMaxMatch = max(testList)
        idxTemp = testList.index(nearMaxMatch)
        idxActual = testList2[idxTemp]
        #print idxActual
        return knowledgeBase[2*idxActual+1]
    
    keyPos = countArray.index(maxMatchInKB)
    return knowledgeBase[2*keyPos+1]
    
# checks if the character entered is a punctuation or not
def isPunc(char):
    if(puncChar.find(char) != -1):
        return True
    return False

# removes punctuation & redundant spaces
def cleanString(inputString):
    temp = ""
    prevChar = ""
    for char in inputString:
        if char.isspace() and prevChar.isspace():
            pass
        elif ((char.isspace() and not prevChar.isspace()) or not isPunc(char)):
            temp += char
            prevChar = char
        elif not prevChar.isspace() and isPunc(char):
            temp += ' '
            prevChar = ' '
    if temp.endswith(' '):
        temp = temp[0:-1]
    return temp

# processes user's query and answers back
def processMessage(message):
    global responseString
    global previousResponse
    global previousInput
    global inputString
    global tempString
    
    previousResponse = responseString
    previousInput = inputString
    
    if not message and previousInput != "**NULL_INPUT**":
        inputString = "**NULL_INPUT**"
    elif not message and (previousInput=="**NULL_INPUT**" or previousInput=="**NULL_INPUT_REPETITION**"):
        inputString = "**NULL_INPUT_REPETITION**"
    else:
        inputString = message
        inputString = inputString.upper()
        inputString = cleanString(inputString)

    if inputString == 'BYE':
        return 'As if i was interested in talking with you'
    
    if inputString == previousInput and message:
        tempString = inputString
        inputString = "**INPUT_REPETITION1**"

    elif (previousInput == "**INPUT_REPETITION1**" or previousInput == "**INPUT_REP2**") and inputString==tempString :
        inputString = "**INPUT_REP2**"

    response = getAnswer(inputString)
    if not response:
        inputString = "**BOT_DONT_UNDERSTAND**"
        response = getAnswer(inputString)
    '''
    print 'previous=', previousInput
    print 'input=', inputString
    print 'temp=', tempString
    '''    
    responseNumber = random.randrange(0,response.__len__())
    responseString = response[responseNumber]
    #print responseString
    if responseString == previousResponse:
        while (1):
            newRandom = random.randrange(0,response.__len__())
            if newRandom != responseNumber:
                return response[newRandom]
    return responseString
    
'''                  
def main():
    msg = ' '
    msg = raw_input('>')
    while(msg!='q'):
        m = processMessage(msg)
        print m
        msg = raw_input('>')
    #getAnswer('your name is');

if __name__=='__main__':
    main()

'''


