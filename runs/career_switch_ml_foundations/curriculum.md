# Curriculum: Go from zero ML knowledge to training and evaluating a small image classifier in PyTorch

**Budget:** 1200 min · **Planned:** 359 min · **Videos:** 17 · **Candidates assessed:** 36

**How I read the goal:** The learner can explain core ML and backpropagation intuition, then write and run a PyTorch training loop for a small CNN image classifier and evaluate it for overfitting and accuracy.

**Assumptions:** The 1200 minutes is pure viewing time, so it covers about 20 hours of videos with no time reserved for practice.; Because the learner likes code-along videos, the plan favors tutorials where the presenter writes code live.; 'Small image classifier' means a CNN trained on MNIST, Fashion-MNIST or CIFAR-10, not a large pretrained model pipeline.; Each video or course part should fit within a 90-minute sitting, so long courses are picked in chunks of 90 minutes or less.; Calculus and linear algebra are already known, so math-focused videos should build intuition for ML and not reteach prerequisites.
> ⚠️ Picks total about 359 minutes of the 1200-minute budget (about 30%). About 841 minutes are unused because the pool has no more good, non-redundant PyTorch material, and I did not pad with weak or redundant videos.
> ⚠️ Every pick is under 90 minutes, so the 90-minute sitting limit is met without splitting. The longest is the Stanford lecture at 78 minutes.
> ⚠️ Duration is taken from the 'minutes' field, but several transcripts' segment maps run longer than that. Real lengths may differ, so check the total against your sittings.
> ⚠️ Tensor and autograd coverage is thin: only the StatQuest video teaches them in code, and the other candidates are flagged lectures or overviews. Practice tensor operations and requires_grad yourself in the PyTorch docs.
> ⚠️ The two foundations videos and the later 3Blue1Brown/backprop videos are theory-heavy, and the curriculum has no dedicated tensor-basics tutorial or batch/DataLoader walkthrough beyond what the CNN code-alongs show.
> ⚠️ The CampusX video is taught in Hinglish with English technical terms.
> ⚠️ Some candidate upload dates (2026) look implausible. I assumed they are valid and that you set no date floor.

## Plan

- **Machine learning fundamentals: models, loss, features, train/test split** (`ml_basics`): The learner has no ML background, so they need the vocabulary and framing (supervised learning, loss functions, generalization) before touching neural networks.
- **Gradient descent and backpropagation intuition and math** (`gradient_descent_backprop`): The learner knows calculus, so they can learn the chain rule applied to computation graphs and see how weights are updated, which gives the math intuition they want.
- **PyTorch tensors and autograd** (`pytorch_tensors_autograd`): The learner knows numpy, so tensors map to familiar ideas. They need to learn the PyTorch API, GPU/device handling, and how autograd computes gradients.
- **Building neural networks and training loops in PyTorch** (`nn_training_loop`): They need to write nn.Module models, pick loss functions and optimizers, use DataLoaders and run the train/eval loop end to end.
- **Convolutional neural networks: convolutions, pooling, architectures** (`cnn_fundamentals`): Image classification needs CNNs. A linear algebra background helps with understanding convolution as a sliding dot product and with feature maps and shapes.
- **Model evaluation, overfitting, and regularization** (`evaluation_overfitting`): The learner must measure accuracy and tell whether the model generalizes, using validation splits, loss curves, confusion matrices, data augmentation, dropout and weight decay.
- **Build and train an image classifier end to end in PyTorch** (`image_classifier_project`): A code-along project ties everything together: load an image dataset, build a CNN, train it, evaluate it, and iterate to improve results.

## Watch in this order

### 1. [[ML1] Machine Learning Fundamentals: Supervised Learning & Linear Regression](https://www.youtube.com/watch?v=TH8cvKLSXGg)
64TechBits · 12 min · counts 12 min · beginner, concept_explainer · covers ml_basics · **confidence 0.80**

Gives the supervised-learning framing: prediction equation, loss (MSE), feature vectors, gradient descent and the train/validation/test split. It is pitched at someone with linear algebra who needs the ML vocabulary first.

> [00:43] “We want to learn them from the available data. That's the fundamental idea behind supervised machine learning.”
> [08:47] “A loss function measures the discrepancy between the model's prediction and the actual target.”
> [13:42] “The model might perform extremely well on the training set but poorly on the test set. This is commonly associated with overfitting.”

_Confidence note: Content matches the slot and level. The upload date (2026) looks odd and the segment map runs past the stated length._

### 2. [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA)
StatQuest with Josh Starmer · 7 min · counts 7 min · beginner, concept_explainer · covers ml_basics, evaluation_overfitting · **confidence 0.80**

Short, intuitive treatment of train/test split, bias, variance and overfitting. It sets up the later evaluation material.

> [01:49] “The first thing we do is split the data into two sets, one for training the machine learning algorithms and one for testing them”
> [03:21] “The inability for a machine learning method like linear regression to capture the true relationship is called Bias”
> [06:42] “the difference in fits between data sets is called Variance”

_Confidence note: Clear on the concepts, but it is theory only._

### 3. [Stanford CS229: Machine Learning - Linear Regression and Gradient Descent |  Lecture 2 (Autumn 2018)](https://www.youtube.com/watch?v=4b4MUYve_U8)
Stanford Online · 78 min · counts 78 min · beginner, lecture · covers ml_basics, gradient_descent_backprop · **confidence 0.60**

A full lecture that derives the squared-error cost and the gradient descent update rule, including batch vs stochastic. It suits a learner who wants the math behind training and already has calculus and linear algebra.

> [25:00] “minimize the square difference between what the hypothesis outputs, H sub-script theta of X, minus Y, squared, right”
> [30:27] “gradient descent, we are going to start with some value of theta, um, and it could be, you know, theta equals the vector of all zeros”

_Confidence note: The segment map is inconsistent with the 78-minute length. The normal-equation part is less needed. It fits in one 90-minute sitting._

### 4. [Machine Learning Tutorial Python - 4: Gradient Descent and Cost Function](https://www.youtube.com/watch?v=vsWrXfO3wWw)
codebasics · 28 min · counts 28 min · beginner, concept_explainer · covers gradient_descent_backprop · **confidence 0.75**

Code-along that implements gradient descent in plain Python on a linear regression cost function. It shows partial derivatives, learning rate and the update loop in code the learner can already read.

> [07:30] “gradient descent is that algorithm that finds best fit line for given training data set in very less number of iteration”
> [25:30] “partial derivatives gives you a slope and then once you have direction, now you need to take a step, so for the step, you use something called a learning rate”

_Confidence note: Linear regression only, not a neural network. It is a good bridge to the PyTorch loop._

### 5. [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w)
3Blue1Brown · 21 min · counts 21 min · beginner, concept_explainer · covers gradient_descent_backprop · **confidence 0.85**

Visual explanation of cost functions, the negative gradient as steepest descent, and how this trains a digit-recognizing network. It builds the intuition the learner asked for.

> [00:04] “the first is to introduce the idea of gradient descent, which underlies not only how neural networks learn, but how a lot of other machine learning works as well”
> [13:59] “the negative gradient of the cost function is just a vector. It's some direction inside this insanely huge input space that tells you which nudges to all of those numbers is going to cause the most rapid decrease to the cost function”

_Confidence note: Pure theory, but that is what this learner wants for this slot._

### 6. [Backpropagation, intuitively | Deep Learning Chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
3Blue1Brown · 13 min · counts 13 min · beginner, concept_explainer · covers gradient_descent_backprop · **confidence 0.85**

Explains backpropagation intuitively: how each weight's effect on the cost is computed, and mini-batch stochastic gradient descent. It prepares the learner for what loss.backward() does.

> [02:23] “Back propagation, the topic of this video, is an algorithm for computing that crazy complicated gradient.”
> [03:24] “The magnitude of each component here is telling you how sensitive the cost function is to each weight and bias.”
> [17:11] “This technique is referred to as stochastic gradient descent.”

_Confidence note: The segment timestamps are messy, but the quotes confirm the content._

### 7. [Backpropagation calculus | Deep Learning Chapter 4](https://www.youtube.com/watch?v=tIeHLnjs5U8)
3Blue1Brown · 10 min · counts 10 min · intermediate, concept_explainer · covers gradient_descent_backprop · **confidence 0.85**

Formal chain-rule derivation of the gradients of cost with respect to weights and biases. It gives the math side of backprop and fits a learner with a calculus background.

> [05:46] “the chain rule, where multiplying together these three ratios gives us the sensitivity of C to small changes in WL”
> [10:27] “you can just keep iterating this same chain rule idea backwards to see how sensitive the cost function is to previous weights and previous biases”

_Confidence note: The level is right for someone who knows calculus._

### 8. [Backpropagation Explained By Hand: Two-Layer Neural Network, Chain Rule and Gradient Descent](https://www.youtube.com/watch?v=fZtjO2cs3VQ)
CodeFlow Daily · 8 min · counts 8 min · intermediate, concept_explainer · covers gradient_descent_backprop · **confidence 0.70**

Works backprop through a two-layer network with real numbers, checks the gradients numerically, and ends with weight updates. It makes the earlier intuition concrete just before autograd.

> [00:23] “First, a forward pass where numbers flow from the inputs to a loss. Second, a backward pass where the error flows back through the network layer by layer using the chain rule.”
> [10:12] “Each step moves every parameter against its gradient with learning rate equal to 0.5. The loss falls at every step.”

_Confidence note: Pure theory but short and concrete. The upload date looks odd._

### 9. [The StatQuest Introduction to PyTorch](https://www.youtube.com/watch?v=FHdlXe1bSe4)
StatQuest with Josh Starmer · 23 min · counts 23 min · beginner, concept_explainer · covers pytorch_tensors_autograd, nn_training_loop · **confidence 0.70**

Code-along that builds a small network from tensors and nn.Parameter, then runs a training loop with loss.backward() and optimizer.step(). It is the best coded link between backprop and PyTorch autograd in the pool. It is flagged surface_intro, but no unflagged candidate covers tensors and autograd in code.

> [06:59] “So we create a new variable called w00, and make it a neural network Parameter.”
> [28:21] “Next we use loss.backward() to calculate the derivative of the loss function with respect to the parameter”
> [33:43] “optimizer.step() also has access to the derivatives stored in model and can use them to step in the correct direction”

_Confidence note: It assumes you know neural network basics, which the earlier picks supply. It uses a toy dataset, not images._

### 10. [Create a Basic Neural Network Model - Deep Learning with PyTorch 5](https://www.youtube.com/watch?v=JHWqWIoac2I)
John Elder · 16 min · counts 16 min · beginner, project_build · covers nn_training_loop · **confidence 0.70**

Builds an nn.Module with fully connected layers and a forward pass with ReLU, with live debugging. It shows how a PyTorch model class is structured before moving to CNNs.

> [02:24] “You have an input layer here, an output layer here, and then inside of here, we have hidden layers of neurons.”
> [17:04] “fully connected one and fully connected two, because they are fully connected.”

_Confidence note: Covers model definition but not the training loop. The loop comes from the StatQuest and CNN code-alongs._

### 11. [Simple explanation of convolutional neural network | Deep Learning Tutorial 23 (Tensorflow & Python)](https://www.youtube.com/watch?v=zfiSAzpy9NM)
codebasics · 24 min · counts 24 min · beginner, concept_explainer · covers cnn_fundamentals · **confidence 0.75**

Visual intuition for convolution filters, feature maps, ReLU, pooling and the full conv-pool-dense architecture. It is flagged surface_intro and pure_theory, but the learner wants concept intuition. It uses TensorFlow only for naming.

> [10:04] “The way convolution operation works is you take 3x3 grid from your original image and multiply individual numbers with this filter.”
> [13:24] “When you apply this filter or a convolution operation, you are generating a feature map that has that particular feature detected.”
> [28:24] “You will have typically a convolution and ReLU layer, then you will have pooling, then there will be another convolution ReLU, pooling.”

_Confidence note: Conceptual and framework-agnostic. The segment map has gaps._

### 12. [Convolutional Neural Networks from Scratch | In Depth](https://www.youtube.com/watch?v=jDe5BAsT2-Y)
Erai · 13 min · counts 13 min · intermediate, concept_explainer · covers cnn_fundamentals · **confidence 0.75**

Walks through the actual arithmetic of convolution, max pooling, flattening and the fully connected output in a trained MNIST CNN. It supplies the math view of CNNs for a learner who wants more than the diagram.

> [00:50] “First off, we will perform a convolution with two filters that have a filter size of 5x5x1 and use an activation function called ReLU.”
> [17:30] “A fully connected layer consists of input nodes and output nodes that are connected with weights and biases.”
> [20:04] “The output matrix Z is defined as the matrix multiplication of the input nodes times the weights plus the bias terms.”

_Confidence note: Forward pass only, with no training code._

### 13. [PyTorch Tutorial 14 - Convolutional Neural Network (CNN)](https://www.youtube.com/watch?v=pDdP0TFzsoQ)
Patrick Loeber · 22 min · counts 22 min · intermediate, project_build · covers cnn_fundamentals, nn_training_loop · **confidence 0.80**

Code-along that implements a CIFAR-10 CNN in PyTorch with Conv2d, pooling, flattening, a training loop and accuracy evaluation. It is the first end-to-end PyTorch CNN, straight after the CNN concepts.

> [27:09] “now after these convolutional layers, when we put them into our classification layers, we want to flatten the 3D tensor to a 1D tensor”

_Confidence note: Content is clearly on target, but only one quote is available on the card._

### 14. [13 PyTorch tutorial - Popular techniques to prevent the overfitting in a Neural Networks](https://www.youtube.com/watch?v=fRqQwCXSeqo)
datahacker. rs · 16 min · counts 16 min · intermediate, concept_explainer · covers evaluation_overfitting · **confidence 0.80**

Explains how to detect overfitting with validation data and covers early stopping, augmentation, L1/L2 and dropout. It shows nn.Dropout and weight_decay in PyTorch.

> [02:27] “The best way to tell if your model is overfitted is to use the validation data set during training”
> [10:25] “The most common regularization method is to add a penalty to the loss function in in proportion to the size of the weights in the model”

_Confidence note: Good mix of concept and PyTorch code._

### 15. [Curing Overfitting with Regularization | Season 1 | Part 29](https://www.youtube.com/watch?v=8rqSbzap8oo)
Soance Learning Hub · 5 min · counts 5 min · intermediate, project_build · covers evaluation_overfitting · **confidence 0.70**

Demonstrates an overfitting gap between training and validation loss on a Fashion-MNIST CNN in PyTorch. It then reduces the gap with batch norm, spatial dropout and augmentation.

> [03:39] “This diverging space is the overfitting gap, confirming the network stops learning universal properties and starts memorizing specific training noise.”
> [05:31] “By artificially expanding the structural variety of the training data, we provide the network with a much wider empirical foundation.”

_Confidence note: Very short, so it works as a demonstration after the datahacker video rather than as a standalone lesson._

### 16. [Building a CNN using PyTorch | Video 11 | CampusX](https://www.youtube.com/watch?v=hkiBZLRFvO4)
CampusX · 32 min · counts 32 min · intermediate, project_build · covers image_classifier_project, cnn_fundamentals · **confidence 0.75**

Builds a Fashion-MNIST CNN in PyTorch, reaching 92% test accuracy while noticing about 99.9% training accuracy (overfitting). This ties the project back to the evaluation lessons.

> [13:21] “CNN ki sabse badi khaasiyat ye hai ki agar aap usko grid based data doge toh woh uske andar ke jo spatial patterns hain toh unko bahut acche se woh identify kar pata hai”
> [17:06] “Convolution layer mein aap kya karte ho ki aapke paas chhote-chhote filters hote hain, let's say 3x3 ke aur aap in filters ko uthate ho aur aap apne image ke upar un filters ko apply karte ho”

_Confidence note: Taught in Hinglish with English technical terms, which may affect comprehension. The content fit is strong._

### 17. [Image Classification CNN in PyTorch](https://www.youtube.com/watch?v=CtzfbUwrYGI)
NeuralNine · 30 min · counts 30 min · intermediate, project_build · covers image_classifier_project · **confidence 0.75**

Complete CIFAR-10 pipeline in PyTorch: transforms, a Conv2d/pool/linear CNN, a training loop with zero_grad, and test accuracy. It is a second full project to consolidate everything.

> [00:24] “we're going to load the data, we're going to have training and testing data, we're going to train the model, and we're going to evaluate the model”
> [29:06] “optimizer.zero_grad, so we reset the gradients, we set all of the gradients to none, and then what we do is we say the outputs”

_Confidence note: It overlaps with the Loeber video on CIFAR-10. It is kept as the capstone because it covers the full train/evaluate/inference workflow._

## Similar videos: why only one made the cut

- kept `fRqQwCXSeqo` over `hpFzuMSYg9k` (both cover evaluation_overfitting): Shows validation-based overfitting detection and implements dropout and weight_decay in PyTorch, which suits a code-along learner.
- kept `pDdP0TFzsoQ` over `r6yRAxDpamQ` (both cover cnn_fundamentals, nn_training_loop): Includes the training loop and evaluation as well as the CNN class, whereas the other stops after defining the model and optimizer.

## Considered and dropped

- [Image classification using CNN (CIFAR10 dataset) | Deep Learning Tutorial 24 (Tensorflow & Python)](https://www.youtube.com/watch?v=7HPwo4wnJeA): Strong CNN/CIFAR-10 content, but it is TensorFlow/Keras and flagged wrong_language for a PyTorch goal.
- [Regularization | L1 & L2 | Dropout | Data Augmentation | Early Stopping |  Deep Learning Part 4](https://www.youtube.com/watch?v=hpFzuMSYg9k): Good regularization math, but it duplicates the datahacker video's topics and has no PyTorch code.
- [Regularization in a Neural Network | Dealing with overfitting](https://www.youtube.com/watch?v=EehRcPo1M-Q): Conceptual regularization overview that adds little beyond the datahacker and ByteQuest-style content, with no code.
- [Convolutional Neural Network Model - Deep Learning with PyTorch 16](https://www.youtube.com/watch?v=r6yRAxDpamQ): Only defines the CNN class and optimizer with no training or evaluation, and the CNN model-building is already covered by Loeber and CampusX.
- [PyTorch a framework for research of dynamic deep learning models - Adam Paszke](https://www.youtube.com/watch?v=BZyKufPCKdI): Lecture on PyTorch's design (define-by-run) rather than a code-along. It is flagged pure_theory/surface_intro, and the StatQuest video covers autograd in code.
- [Exploring the Deep Learning Framework PyTorch - Stephanie Kim](https://www.youtube.com/watch?v=kUkGR5Lu3DU): Overview talk heavy on deployment (TorchScript, ONNX) with little hands-on tensor or autograd teaching.
- [Pytorch CNN example (Convolutional Neural Network)](https://www.youtube.com/watch?v=wnK3uWv_WkU): Short MNIST CNN code-along, but it explicitly skips how convolutions work and is flagged surface_intro. Other candidates cover CNNs more fully.
- [Tutorial 6-Chain Rule of Differentiation with BackPropagation](https://www.youtube.com/watch?v=CRB266Eyjkg): Chain-rule backprop explanation that duplicates the 3Blue1Brown chapters, which are clearer for this learner.
- [PyTorch Sinhala Tutorial #2 - Auto Grad and Tensor Functions - PyTorch in Sinhala](https://www.youtube.com/watch?v=lSDhp0kr1ZE): Covers tensors and autograd but is flagged wrong_language (Sinhala).
- [Fixing loss.backward() Gradient Issues in PyTorch S3FD PGD Attack](https://www.youtube.com/watch?v=DK1GBJ-yWgw): Flagged too_advanced_for_learner and off_topic (adversarial PGD attack debugging).

<details><summary>Filtered before assessment (31)</summary>

- Regularization - Early stopping (prefilter): too short (23s)
- Visualization of cnn  #ai #machinelearning #deeplearning (prefilter): too short (59s)
- MLP using Fashion-MNIST dataset (prefilter): too short (74s)
- Episode 2: PyTorch Dropout, Batch size and interactive debugging (prefilter): pool cap reached
- PyTorch Lightning Tutorial - Image Classification Using Multilayer Perceptron (MLP) (prefilter): pool cap reached
- Part 2 - Supervised Learning | Complete Machine Learning Course for Beginners | Sheryians AI School (prefilter): pool cap reached
- Gradient Descent in 3 minutes (prefilter): pool cap reached
- PyTorch Python Tutorial | PyTorch Machine Learning Tutorial | Deep Learning Using PyTorch (prefilter): pool cap reached
- Neural Networks with PyTorch (Python Tutorial) (prefilter): pool cap reached
- Convolutional Neural Nets Explained and Implemented in Python (PyTorch) (prefilter): pool cap reached
- Lec-37: Supervised, Unsupervised and Reinforcement Learning in Artificial Intelligence in Hindi (prefilter): pool cap reached
- Chain Rule To find Derivative In Back Propagation (prefilter): pool cap reached
- JAX in 100 Seconds (prefilter): pool cap reached
- PyTorch Crash Course - Getting Started with Deep Learning (prefilter): pool cap reached
- What are Convolutional Neural Networks (CNNs)? (prefilter): pool cap reached
- Module 4- Part 2- Deep Neural Networks  Regularization techniques (prefilter): pool cap reached
- #3 Deep Learning Project using Convolutional Neural Network | Fashion MNIST Classification in Hindi (prefilter): pool cap reached
- All Machine Learning algorithms explained in 17 min (prefilter): pool cap reached
- Backpropagation is Just the Chain Rule (prefilter): pool cap reached
- Pytorch - Minimizing every function using Pytorch - 01 (prefilter): pool cap reached
- Pytorch tutorial for beginners | Pytorch neural network tutorial | Pytorch course (prefilter): pool cap reached
- What is Convolution in CNN | Artificial vs Convolutional Neural Network (prefilter): pool cap reached
- 2019 05 23 PyTorch  Regularization in L1 and L2 (prefilter): pool cap reached
- Introduction to Gradient Descent | How Models Minimize Loss (language): transcript is 'hi', learner needs 'en'
- PyTorch for Deep Learning & Machine Learning – Full Course (prefilter): pool cap reached
- PyTorch in 1 Hour (prefilter): pool cap reached
- Own CNN Architecture for CIFAR 10 Dataset (prefilter): pool cap reached
- Complete Machine Learning In 6 Hours| Krish Naik (prefilter): pool cap reached
- Deep Learning With PyTorch - Full Course (prefilter): pool cap reached
- CSCI 3151 - M37 -  Overfitting, capacity, and deep network generalization (prefilter): pool cap reached
- Learn PyTorch for deep learning in a day. Literally. (prefilter): pool cap reached

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.167 · 70 s_
