## Pytorch is the basis

Random initilisation of the datasat for neural network learning. 

Theory:

From a database, x will be the input into the NN, from which y is the output;

What would an example be?

x could be size, equal to 7 pixels within an image

y will be a vector of 10 probabilities, 10 possibilites for the arrangement of the pixels.

10 possibilities, which are determined by the classes within the database. Weights are applied during the calculations to affect the outcome; if randomised (random initilisation), weights will of course be suboptimal at best.

Forward pass: Feed a neural network information, computations, output.

To improve, you have to implement a backward pass to retrain the NN, to re adjust the weights.

Error is a function of the weights which exist within the NN; considering that error will deviate depending on the quality of the output, which quality is dependent on the weights, this is self-evident.

