# Curriculum: Go from zero ML knowledge to training and evaluating a small image classifier in PyTorch

**Budget:** 1200 min · **Planned:** 324 min · **Videos:** 16 · **Candidates assessed:** 36

**How I read the goal:** The learner can explain core ML and backpropagation intuition, then write and run a PyTorch training loop for a small CNN image classifier and evaluate it for overfitting and accuracy.

**Assumptions:** The 1200 minutes is pure viewing time, so it covers about 20 hours of videos with no time reserved for practice.; Because the learner likes code-along videos, the plan favors tutorials where the presenter writes code live.; 'Small image classifier' means a CNN trained on MNIST, Fashion-MNIST or CIFAR-10, not a large pretrained model pipeline.; Each video or course part should fit within a 90-minute sitting, so long courses are picked in chunks of 90 minutes or less.; Calculus and linear algebra are already known, so math-focused videos should build intuition for ML and not reteach prerequisites.
> ⚠️ Under-filled: only about 324 of 1200 minutes are used (~27%), roughly 876 unused. The pool has no long courses and few substantial PyTorch tutorials, and I did not pad with weak or redundant videos.
> ⚠️ None of the cards has verified quotes, so evidence_quote_ids is empty for every pick. Reasons rest on the card summaries and metadata, and confidence is moderated for that.
> ⚠️ Thin coverage of PyTorch tensors and autograd: the only usable pick is the StatQuest intro, which is flagged surface_intro. Consider supplementing with the official PyTorch tutorials or a longer PyTorch course.
> ⚠️ Evaluation coverage is mostly conceptual (bias/variance, regularization). No video clearly shows a train/validation/test split or tracking accuracy in code, so do this yourself in the project.
> ⚠️ Sittings: all picks fit within 90 minutes. The 78-minute CS229 lecture should be its own sitting; group the shorter videos into sessions of at most 90 minutes.
> ⚠️ Several picks (codebasics CNN explainer, TensorFlow-based) use different tooling for concepts; transfer to PyTorch is assumed. Upload dates of 2026 on a few cards look odd but there is no date floor, so I ignored them.
> ⚠️ Practice time is not included in the budget; consider coding along with the videos and reproducing the CIFAR-10 project yourself.

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
64TechBits · 12 min · counts 12 min · beginner, concept_explainer · covers ml_basics · **confidence 0.60**

Starts from zero with supervised learning: model representation, loss functions and optimization, taught with the math. That suits a learner with a strong math background and no ML. It is flagged pure_theory, but that is what this learner asked for.


_Confidence note: Based on the summary only; the card has no verified quotes. Confidence would rise with transcript evidence of depth._

### 2. [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA)
StatQuest with Josh Starmer · 7 min · counts 7 min · beginner, concept_explainer · covers ml_basics, evaluation_overfitting · **confidence 0.65**

Explains bias and variance intuitively. This is the conceptual basis for underfitting, overfitting and train/test behavior, so it sets up the later evaluation material.


_Confidence note: Short, well-matched concept video; the flags (pure_theory, surface_intro) are acceptable because the learner wants intuition._

### 3. [Stanford CS229: Machine Learning - Linear Regression and Gradient Descent |  Lecture 2 (Autumn 2018)](https://www.youtube.com/watch?v=4b4MUYve_U8)
Stanford Online · 78 min · counts 78 min · beginner, lecture · covers ml_basics, gradient_descent_backprop · **confidence 0.60**

A full university lecture on supervised learning, linear regression and gradient descent with the derivations. It uses the calculus and linear algebra the learner already has to give a rigorous ML foundation. At 78 minutes it fits one 90-minute sitting.


_Confidence note: Lecture format rather than code-along; the card gives only a summary and the 'likely includes derivations' judgement is unverified._

### 4. [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w)
3Blue1Brown · 21 min · counts 21 min · beginner, concept_explainer · covers gradient_descent_backprop · **confidence 0.80**

Gives the visual and mathematical intuition for cost functions, gradient descent and how neural networks learn their weights. This is the math-intuition backbone the learner wants before touching PyTorch.


_Confidence note: Clear content match for the sub-topic; there are no verified quotes._

### 5. [Machine Learning Tutorial Python - 4: Gradient Descent and Cost Function](https://www.youtube.com/watch?v=vsWrXfO3wWw)
codebasics · 28 min · counts 28 min · beginner, concept_explainer · covers gradient_descent_backprop, ml_basics · **confidence 0.65**

A code-along that implements gradient descent for linear regression in plain Python, covering cost function, MSE and learning rate. It turns the math intuition into numpy-style code the learner can follow.


_Confidence note: The segment map lists only the first 15 minutes of a 28-minute video, so the second half is unverified._

### 6. [Backpropagation, intuitively | Deep Learning Chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
3Blue1Brown · 13 min · counts 13 min · beginner, concept_explainer · covers gradient_descent_backprop · **confidence 0.80**

Builds intuition for backpropagation, showing how each weight's influence on the cost drives its update. It is the most relevant video in the pool for the backprop concept itself.


_Confidence note: Strongest backprop-intuition match; no quotes to verify._

### 7. [Backpropagation calculus | Deep Learning Chapter 4](https://www.youtube.com/watch?v=tIeHLnjs5U8)
3Blue1Brown · 10 min · counts 10 min · intermediate, concept_explainer · covers gradient_descent_backprop · **confidence 0.75**

Gives the chain-rule calculus behind backpropagation, which this learner can follow given their calculus background. It shows how gradients flow backward and prepares them for what autograd automates.


_Confidence note: pure_theory flag is desirable here since the learner wants the math._

### 8. [Backpropagation Explained By Hand: Two-Layer Neural Network, Chain Rule and Gradient Descent](https://www.youtube.com/watch?v=fZtjO2cs3VQ)
CodeFlow Daily · 8 min · counts 8 min · intermediate, concept_explainer · covers gradient_descent_backprop · **confidence 0.70**

Works through a two-layer network by hand with numerical values and checks the analytic gradients against finite differences. A numerical worked example like this fits an engineer, and it previews what autograd will compute.


_Confidence note: Content is specific and matches the need; it is a single short video with no quotes._

### 9. [The StatQuest Introduction to PyTorch](https://www.youtube.com/watch?v=FHdlXe1bSe4)
StatQuest with Josh Starmer · 23 min · counts 23 min · beginner, concept_explainer · covers pytorch_tensors_autograd, nn_training_loop · **confidence 0.50**

A step-by-step PyTorch walkthrough that builds a small network, makes predictions and optimizes parameters with backpropagation. It is the best available coverage of tensors and autograd, though it is flagged surface_intro, and no unflagged candidate covers this sub-topic.


_Confidence note: Thin coverage of tensor operations; a dedicated PyTorch tensors/autograd video would be better but none is in the pool. Transcript is poor._

### 10. [Create a Basic Neural Network Model - Deep Learning with PyTorch 5](https://www.youtube.com/watch?v=JHWqWIoac2I)
John Elder · 16 min · counts 16 min · beginner, project_build · covers nn_training_loop · **confidence 0.55**

Code-along showing how to define a PyTorch nn.Module with layers and a forward function. This is the model-building half of the training loop for the learner's first network.


_Confidence note: Covers model definition only, not the training step; the training loop is covered later by the CNN code-alongs._

### 11. [Simple explanation of convolutional neural network | Deep Learning Tutorial 23 (Tensorflow & Python)](https://www.youtube.com/watch?v=zfiSAzpy9NM)
codebasics · 24 min · counts 24 min · beginner, concept_explainer · covers cnn_fundamentals · **confidence 0.60**

A beginner-friendly explanation of how convolutions, filters and CNN architectures work. The learner has no prior CNN knowledge, so the concept is wanted here even though the examples use TensorFlow.


_Confidence note: Explains the concept in TensorFlow context, not PyTorch; the concept transfers._

### 12. [Convolutional Neural Networks from Scratch | In Depth](https://www.youtube.com/watch?v=jDe5BAsT2-Y)
Erai · 13 min · counts 13 min · intermediate, concept_explainer · covers cnn_fundamentals · **confidence 0.55**

A math-oriented look at convolution and pooling layers in a PyTorch-trained MNIST model. It adds the deeper intuition this learner wants beyond the basic explainer.


_Confidence note: Poor transcript and pure_theory flag; the level is intermediate but suits a math-comfortable learner._

### 13. [Pytorch CNN example (Convolutional Neural Network)](https://www.youtube.com/watch?v=wnK3uWv_WkU)
Aladdin Persson · 10 min · counts 10 min · beginner, project_build · covers cnn_fundamentals, nn_training_loop · **confidence 0.60**

A short code-along that builds a CNN in PyTorch on MNIST, turning the CNN concepts into code. It is a gentle step before the longer CIFAR-10 project.


_Confidence note: Brief video; the card shows relevance to CNN and the loop but no quotes._

### 14. [Regularization | L1 & L2 | Dropout | Data Augmentation | Early Stopping |  Deep Learning Part 4](https://www.youtube.com/watch?v=hpFzuMSYg9k)
ByteQuest · 14 min · counts 14 min · beginner, concept_explainer · covers evaluation_overfitting · **confidence 0.60**

Covers overfitting remedies: L1/L2 regularization, dropout, data augmentation and early stopping. It gives the learner the main regularization options to try on the classifier.


_Confidence note: The segment map covers only part of the video; the transcript is poor._

### 15. [13 PyTorch tutorial - Popular techniques to prevent the overfitting in a Neural Networks](https://www.youtube.com/watch?v=fRqQwCXSeqo)
datahacker. rs · 16 min · counts 16 min · intermediate, concept_explainer · covers evaluation_overfitting · **confidence 0.55**

A PyTorch-specific tutorial on techniques to prevent overfitting in neural networks, linking the concepts to the framework the learner is using.


_Confidence note: Poor transcript; unclear how much is coded live._

### 16. [Image Classification CNN in PyTorch](https://www.youtube.com/watch?v=CtzfbUwrYGI)
NeuralNine · 30 min · counts 30 min · beginner, project_build · covers image_classifier_project, nn_training_loop, cnn_fundamentals · **confidence 0.70**

An end-to-end PyTorch walkthrough that trains a CNN on CIFAR-10 and covers the training process. It is the capstone code-along for the learner's goal.


_Confidence note: Strongest project match in the pool; evaluation or overfitting checks within it are unverified because the transcript is poor._

## Considered and dropped

- [PyTorch Sinhala Tutorial #2 - Auto Grad and Tensor Functions - PyTorch in Sinhala](https://www.youtube.com/watch?v=lSDhp0kr1ZE): Taught in Sinhala (wrong_language), so it cannot serve this learner despite covering autograd.
- [Fixing loss.backward() Gradient Issues in PyTorch S3FD PGD Attack](https://www.youtube.com/watch?v=DK1GBJ-yWgw): Narrow adversarial-attack (PGD) debugging fix, too advanced and off-topic for a first autograd lesson.
- [Image classification using CNN (CIFAR10 dataset) | Deep Learning Tutorial 24 (Tensorflow & Python)](https://www.youtube.com/watch?v=7HPwo4wnJeA): CIFAR-10 CNN comparison in TensorFlow, not PyTorch; a PyTorch alternative covers the same project.
- [Tensorflow Fashion MNIST Tutorial. | Tensorflow Image Classification | Neural Networks Deep learning](https://www.youtube.com/watch?v=Ynhr-F5WwOA): TensorFlow Fashion-MNIST tutorial with wrong-language and poor-transcript flags; not PyTorch.
- [PyTorch a framework for research of dynamic deep learning models - Adam Paszke](https://www.youtube.com/watch?v=BZyKufPCKdI): 2017 conference talk on PyTorch design, not a hands-on tutorial, and flagged as outdated tooling.
- [Exploring the Deep Learning Framework PyTorch - Stephanie Kim](https://www.youtube.com/watch?v=kUkGR5Lu3DU): Overview talk on PyTorch 1.0 design philosophy with no hands-on code, which doesn't fit a code-along learner.
- [PyTorch Tutorial 14 - Convolutional Neural Network (CNN)](https://www.youtube.com/watch?v=pDdP0TFzsoQ): Good CIFAR-10 CNN in PyTorch, but largely redundant with the picked CIFAR-10 project video; the MNIST code-along already covers the CNN code step. A viable swap if the learner prefers it.
- [Regularization in a Neural Network | Dealing with overfitting](https://www.youtube.com/watch?v=EehRcPo1M-Q): Conceptual regularization explainer that overlaps the two picked overfitting videos and adds no new gap.
- [Building a CNN using PyTorch | Video 11 | CampusX](https://www.youtube.com/watch?v=hkiBZLRFvO4): PyTorch CNN build with unverifiable content from a poor transcript, and it duplicates the picked CNN code-alongs.
- [Cat Vs Dog Image Classification Project | Deep Learning Project | CNN Project](https://www.youtube.com/watch?v=0K4J_PTgysc): Cat vs dog project with an unclear framework and only a brief verified segment; it is less certain than the CIFAR-10 PyTorch project.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.258 · 66 s_
