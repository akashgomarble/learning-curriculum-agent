# Curriculum: Go from zero ML knowledge to training and evaluating a small image classifier in PyTorch

**Budget:** 1200 min · **Planned:** 291 min · **Videos:** 13 · **Candidates assessed:** 36

**How I read the goal:** By the end, the learner understands supervised learning, gradient descent and backprop (with math), PyTorch tensors/autograd/training loops, how CNNs work, and can train and evaluate a CIFAR-10-style CNN while diagnosing overfitting. All of this is spread over four sittings of 90 minutes or less.

**Assumptions:** Learner is fine with the CS229 lecture as a math-heavy start because they have calculus and linear algebra and asked for the math intuition.; Tensors and autograd are learned inside the StatQuest and CNN code-alongs. The pool has no standalone tensor-operations video in English.; The learner can do the Colab or local setup themselves.
> ⚠️ Only about 5.2 hours (about 313 min) of the 1200-minute budget is used. The candidate pool has no more good, non-duplicate English material, and I chose not to pad it.
> ⚠️ Suggested sittings, each 90 minutes or less: (1) CS229 lecture; (2) codebasics GD, 3Blue1Brown ch.2–4, bias/variance; (3) StatQuest PyTorch, John Elder NN, codebasics CNN, Erai CNN; (4) NeuralNine CIFAR-10, AssemblyAI, datahacker.
> ⚠️ No video covers PyTorch tensor operations or Dataset/DataLoader as a standalone topic. Learn them from the code-alongs and the official PyTorch docs.
> ⚠️ No confusion-matrix or precision/recall coverage was found; evaluation here is accuracy and train-versus-validation comparison.
> ⚠️ I kept NeuralNine over Patrick Loeber's CIFAR-10 CNN video because it spends more time on data loading, transforms and the test evaluation loop. I also dropped Aladdin Persson's MNIST CNN video as a near-duplicate that, by its own description, skips how convolutions work.
> ⚠️ The codebasics CNN explainer uses TensorFlow for its other videos. I used only its conceptual explanation here.

## Plan

- **ML basics: supervised learning, loss, linear regression** (`ml_basics`): Foundation for everything else; the learner has no ML background.
- **Gradient descent and backpropagation (code and math intuition)** (`gd_backprop`): Core training mechanism; the learner knows calculus, so the chain rule can be applied directly.
- **PyTorch tensors, autograd, nn.Module and the training loop** (`pytorch_core`): Turns the theory into code with loss.backward() and optimizer.step().
- **Convolutional neural networks** (`cnn`): The architecture used for image classification.
- **Train and evaluate a CNN image classifier in PyTorch** (`project`): The end-to-end goal: data loading, training, test accuracy.
- **Evaluation, overfitting and regularization** (`overfit`): Learn to detect overfitting with validation data and fix it with dropout and weight decay.

## Watch in this order

### 1. [Stanford CS229: Machine Learning - Linear Regression and Gradient Descent |  Lecture 2 (Autumn 2018)](https://www.youtube.com/watch?v=4b4MUYve_U8)
Stanford Online · 78 min · counts 78 min · beginner, lecture · covers ml_basics, gd_backprop · **confidence 0.80**

A rigorous lecture on supervised learning, the squared-error cost and the derivation of the gradient descent update. It suits an engineer with calculus and linear algebra who wants the math. Sitting 1 (78 min).

> [25:00] “minimize the square difference between what the hypothesis outputs, H sub-script theta of X, minus Y, squared, right”
> [30:27] “gradient descent, we are going to start with some value of theta, um, and it could be, you know, theta equals the vector of all zeros”
> [02:13] “supervised learning and regression, so, I think the simplest, maybe the simplest possible learning algorithm”

_Confidence note: Pure theory with no code, but the learner explicitly wants the math._

### 2. [Machine Learning Tutorial Python - 4: Gradient Descent and Cost Function](https://www.youtube.com/watch?v=vsWrXfO3wWw)
codebasics · 28 min · counts 28 min · beginner, concept_explainer · covers gd_backprop · **confidence 0.80**

A code-along that implements gradient descent with MSE and partial derivatives in Python, applying last session's math. Sitting 2 starts here.

> [07:30] “gradient descent is that algorithm that finds best fit line for given training data set in very less number of iteration”
> [25:30] “partial derivatives gives you a slope and then once you have direction, now you need to take a step, so for the step, you use something called a learning rate”

_Confidence note: The numpy-style implementation matches the learner's background._

### 3. [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w)
3Blue1Brown · 21 min · counts 21 min · beginner, concept_explainer · covers gd_backprop · **confidence 0.85**

Gives the geometric intuition for the cost function over thousands of weights and for the negative gradient as the steepest-descent direction.

> [07:30] “the cost function is a layer of complexity on top of that. It takes as its input those 13,000 or so weights and biases”
> [13:59] “the negative gradient of the cost function is just a vector. It's some direction inside this insanely huge input space that tells you which nudges to all of those numbers is going to cause the most rapid decrease to the cost function”

_Confidence note: Standard visual explainer._

### 4. [Backpropagation, intuitively | Deep Learning Chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
3Blue1Brown · 13 min · counts 13 min · beginner, concept_explainer · covers gd_backprop · **confidence 0.85**

Explains intuitively how backpropagation computes the gradient, and introduces mini-batches and stochastic gradient descent, which the PyTorch training loops use.

> [02:23] “Back propagation, the topic of this video, is an algorithm for computing that crazy complicated gradient.”
> [03:24] “The magnitude of each component here is telling you how sensitive the cost function is to each weight and bias.”
> [17:11] “This technique is referred to as stochastic gradient descent.”

_Confidence note: Direct fit._

### 5. [Backpropagation calculus | Deep Learning Chapter 4](https://www.youtube.com/watch?v=tIeHLnjs5U8)
3Blue1Brown · 10 min · counts 10 min · intermediate, concept_explainer · covers gd_backprop · **confidence 0.85**

Applies the chain rule to the cost function, which formalizes backprop and shows what autograd automates. It fits a learner who knows calculus.

> [05:46] “the chain rule, where multiplying together these three ratios gives us the sensitivity of C to small changes in WL”
> [06:43] “the derivative of C with respect to AL works out to be two times AL minus Y”
> [10:27] “you can just keep iterating this same chain rule idea backwards to see how sensitive the cost function is to previous weights and previous biases”

_Confidence note: Right level for calculus-literate learner._

### 6. [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA)
StatQuest with Josh Starmer · 7 min · counts 7 min · beginner, concept_explainer · covers overfit, ml_basics · **confidence 0.80**

A short intro to the train/test split, bias, variance and overfitting. It prepares the learner to read train-versus-test accuracy later. Ends sitting 2 (about 79 min total).

> [01:49] “The first thing we do is split the data into two sets, one for training the machine learning algorithms and one for testing them”
> [03:21] “The inability for a machine learning method like linear regression to capture the true relationship is called Bias”
> [06:42] “the difference in fits between data sets is called Variance”

_Confidence note: Brief but covers the concept._

### 7. [The StatQuest Introduction to PyTorch](https://www.youtube.com/watch?v=FHdlXe1bSe4)
StatQuest with Josh Starmer · 23 min · counts 23 min · beginner, concept_explainer · covers pytorch_core · **confidence 0.80**

Builds a network in PyTorch with Parameters, then uses loss.backward() and optimizer.step() in a training loop. It links the backprop theory to autograd. Sitting 3 begins here.

> [06:59] “So we create a new variable called w00, and make it a neural network Parameter.”
> [28:21] “Next we use loss.backward() to calculate the derivative of the loss function with respect to the parameter”
> [33:43] “optimizer.step() also has access to the derivatives stored in model and can use them to step in the correct direction”

_Confidence note: Flagged surface_intro and assumes NN basics, which sitting 2 provides._

### 8. [Create a Basic Neural Network Model - Deep Learning with PyTorch 5](https://www.youtube.com/watch?v=JHWqWIoac2I)
John Elder · 16 min · counts 16 min · beginner, project_build · covers pytorch_core · **confidence 0.70**

Code-along showing how to write an nn.Module class with fully connected layers and a forward pass, the pattern every later model reuses.

> [02:24] “You have an input layer here, an output layer here, and then inside of here, we have hidden layers of neurons.”
> [17:04] “fully connected one and fully connected two, because they are fully connected.”

_Confidence note: Useful but covers only the model definition, not training._

### 9. [Simple explanation of convolutional neural network | Deep Learning Tutorial 23 (Tensorflow & Python)](https://www.youtube.com/watch?v=zfiSAzpy9NM)
codebasics · 24 min · counts 24 min · beginner, concept_explainer · covers cnn · **confidence 0.75**

Visual intuition for CNNs: convolution filters, feature maps, ReLU and pooling stacked into a classifier. The learner has no CNN background.

> [10:04] “The way convolution operation works is you take 3x3 grid from your original image and multiply individual numbers with this filter.”
> [13:24] “When you apply this filter or a convolution operation, you are generating a feature map that has that particular feature detected.”
> [28:24] “You will have typically a convolution and ReLU layer, then you will have pooling, then there will be another convolution ReLU, pooling.”

_Confidence note: Flagged surface_intro, but it supplies the fundamentals the learner lacks. The code is TensorFlow, but this part is conceptual._

### 10. [Convolutional Neural Networks from Scratch | In Depth](https://www.youtube.com/watch?v=jDe5BAsT2-Y)
Erai · 13 min · counts 13 min · intermediate, concept_explainer · covers cnn · **confidence 0.75**

Walks through the matrix math of a CNN forward pass (convolution, max pooling, flatten, fully connected layer). It adds the math side that the learner wants. Ends sitting 3 (about 76 min).

> [00:50] “First off, we will perform a convolution with two filters that have a filter size of 5x5x1 and use an activation function called ReLU.”
> [17:30] “A fully connected layer consists of input nodes and output nodes that are connected with weights and biases.”
> [20:04] “The output matrix Z is defined as the matrix multiplication of the input nodes times the weights plus the bias terms.”

_Confidence note: Concept only, with no PyTorch code._

### 11. [Image Classification CNN in PyTorch](https://www.youtube.com/watch?v=CtzfbUwrYGI)
NeuralNine · 30 min · counts 30 min · intermediate, project_build · covers project, cnn, pytorch_core · **confidence 0.85**

Full code-along that loads CIFAR-10 with transforms, defines a Conv2d CNN, writes the training loop with zero_grad, and evaluates test accuracy. This is the capstone for the goal. Sitting 4 begins here.

> [00:24] “we're going to load the data, we're going to have training and testing data, we're going to train the model, and we're going to evaluate the model”
> [13:30] “we have a 5 * 5 pixel kernel that moves across the image, calculates a dot product and creates feature maps”
> [29:06] “optimizer.zero_grad, so we reset the gradients, we set all of the gradients to none, and then what we do is we say the outputs”

_Confidence note: Covers data, training and evaluation end to end._

### 12. [Regularization in a Neural Network | Dealing with overfitting](https://www.youtube.com/watch?v=EehRcPo1M-Q)
AssemblyAI · 12 min · counts 12 min · beginner, concept_explainer · covers overfit · **confidence 0.70**

Explains why overfitting happens and covers L1/L2 regularization, dropout, early stopping and data augmentation.

> [00:44] “Overfitting is when your model really closely fits the training data, so much so that it is not able to generalize really well to the real world.”
> [03:59] “Regularization is a way to limit this flexibility that the model has in hopes to avoid overfitting.”
> [08:22] “The idea behind L1 and L2 regularization is to adding the weights into the loss calculation or the cost function to punish the network for having higher weights.”

_Confidence note: Concept only, but it pairs with the code-based video that follows._

### 13. [13 PyTorch tutorial - Popular techniques to prevent the overfitting in a Neural Networks](https://www.youtube.com/watch?v=fRqQwCXSeqo)
datahacker. rs · 16 min · counts 16 min · intermediate, concept_explainer · covers overfit · **confidence 0.75**

Shows how to detect overfitting with a validation set and how to apply nn.Dropout and weight_decay in PyTorch, so the learner can fix an overfitting classifier. Sitting 4 totals about 80 min.

> [02:27] “The best way to tell if your model is overfitted is to use the validation data set during training”
> [10:25] “The most common regularization method is to add a penalty to the loss function in in proportion to the size of the weights in the model”

_Confidence note: Practical PyTorch coverage of the regularization methods._

_Models: agent_loop=anthropic/claude-sonnet-5.5 · cost $0.317 · 85 s_
