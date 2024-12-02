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

With backpard pass, or back propagation, the purpose is to find the direction of improvement; to compute the gradient in which error will be minimal, which as a function of weight, will help elucidate the best fitting NN model.

Response to "purpose of this forwards backwards process"?:

Say we have an input dimension of 1000, a hidden size of 100 and an output dimension of 10, the error of this NN model could be shown as:

l for linear model

$l1: R^1000 => R^100$ 

Where:

$x => xA^T + b$

And:

Where xA, $x = R100*R1000$

Where $b = R100$