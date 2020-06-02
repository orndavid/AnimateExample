# Animation Exploration
We wanted to figure out how to create a animation using the matplotlib FuncAnimation funciton call and then save the output as a .mp4 output.

The package dependecies are
- Numpy      V 1.18.1
- matplotlib V 3.1.3
- Scipy      V 1.4.1

Scipy is used to compute the distance between points here.

## Lesson learned
Approach the project as a a continuous step process, where you either increment the step or take as an input the step number (frame number). 

When drawing get the objects that you were drawing (typically the lines) and change those, you create apriori designs of type and then draw them sequentially.
