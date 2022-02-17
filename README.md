# monolopy #
Stats are hard.  Brute forcing accurately is harder.

### But Why ###
Saw something on Reddit.  People ripped the poster apart, of course.

### How ###
BRUTE FORCE.  Basically, I sent a player around the board MAAAANY times, and recorded how many times each tile was landed on.

### Is it accurate? ###
I haven't taken much in the way of stats.  I've read that randomized approaches like this only become statistically significant at a large enough sample size.  I've also read people who say that's not true, so who even know's what's true anymore.

### Is it fast? ###
There are 39 tiles, and I have to loop through an array of them, twice, each move on the board.  It was in linear time outside of those I believe

### Results? ###
Well, here's what I got from 500,000 loops around the board.

![Results](https://i.imgur.com/kZxgfms.png)
