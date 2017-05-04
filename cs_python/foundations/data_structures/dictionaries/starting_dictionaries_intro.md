Title: Restarting Dictionary  
Author: Joe Seiler  
Date: 2017-05-04  
category: Python Lessons  

## All you can do with Dictionaries.

***  

### The focus will somewhat be on removing/replacing values.

- This recent focus in May 2017 is due to testing out a
sort of *"hypothesis"* pertaining to the Alexa skill, JoeDaddy.  

### Hypothesis(or abstract):  

Since the SSML/card portion of the skill
is contained in what looks like a dictionary (or is it JSON?!), perhaps
there is a way to set up a callable function loop to replace the card's
content to match the 'fact' called by the user.

*Background*: Currently, there are a few problems with the displayed card for the skill.
As of now, the home card for the skill is displayed, no matter what function is called.
This can be useful; however, JoeDaddy is not passing publication due to this occurrence.
If the card's content is changed to "output" (the quotes here are for emphasis in this doc;
they are omitted in the current lambda function), the SSML tags, <speak></speak> are shown; which
is another cause for failing publication.
