This script will generate a Koch Snowflake.

I put this together as a mean to help wrap my mind around recursion.

It pretty much does what I expect it to, but I'm still not sure I really grok recursion, beyond simple examples.

Nevertheless, I think this is pretty cool.

You can move the drawing turtle around by modifying the paramters for jonney.goto(x, y):

Ex: jonney.goto(-200,0)

You can also specify the complexity of the snowflake by modifying the paramters of draw_snowflake(length, depth): 

Ex: draw_snowflake(10, 4)

Caution: Using a recursion depth of more than 5 takes a really long time to draw, even after modifying the drawing speed.
Warning: Recursion depths of 8 or greater, crash my computer.

