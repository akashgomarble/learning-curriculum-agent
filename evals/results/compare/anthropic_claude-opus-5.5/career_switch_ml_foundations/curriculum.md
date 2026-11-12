# Curriculum: Go from zero ML knowledge to training and evaluating a small image classifier in PyTorch

**Budget:** 1200 min · **Planned:** 1190 min · **Videos:** 5 · **Candidates assessed:** 36

**How I read the goal:** The learner can explain how neural networks learn (loss, gradient descent, backprop), and can write, train and evaluate a small CNN image classifier in PyTorch from scratch, understanding overfitting and metrics.

**Assumptions:** The 1200 minutes is pure viewing time, so long code-along courses are acceptable and no time is reserved for separate practice.; A small image classifier means something like MNIST/Fashion-MNIST/CIFAR-10 trained with a CNN.; Because the learner knows calculus and linear algebra, math explanations can be intuitive but not simplified to avoid derivatives or matrices.; No constraints rule out particular video titles, so title exclusions are empty.
> ⚠️ About 1190 of 1200 minutes are used: 43.7 minutes of 3Blue1Brown plus about 1146 minutes of the freeCodeCamp course. The course's 17:13:32-23:45:00 stretch (custom Dataset class, baseline model) is skipped to fit the budget. Watch it if you get extra time.
> ⚠️ The start of the last window (23:45:00) is estimated. Check the video's chapter markers and shift the window to begin at the 'loss curves' or 'overfitting' chapter, keeping roughly the same length.
> ⚠️ 3Blue1Brown Deep Learning Chapter 1 (what a neural network is) was not in the pool. Consider watching it (about 19 minutes) before Chapter 2, though that would slightly exceed the budget.
> ⚠️ None of the candidates had transcripts, so every assessment rests on chapter lists and descriptions. Autograd depth in particular is unverified.
> ⚠️ Regularization techniques beyond overfitting and data augmentation (for example dropout and weight decay) may be covered only lightly.

## Plan

- **Machine learning fundamentals: supervised learning, loss functions, train/test split** (`ml_basics`): Learner has zero ML background; needs the vocabulary and framing before touching neural networks, though numpy and linear algebra let them move quickly.
- **Gradient descent, neural networks and backpropagation with math intuition** (`gd_backprop`): Learner knows calculus, so the chain rule view of backprop will click fast; this gives the intuition they want for why training works.
- **PyTorch tensors and autograd** (`pytorch_tensors_autograd`): Learner knows numpy, so PyTorch tensors map onto familiar ideas; autograd connects directly to the backprop they just learned.
- **Building models and training loops in PyTorch (nn.Module, optimizers, DataLoader)** (`training_loop`): Needed to turn the math into working code, including batching, loss, optimizer steps and GPU/CPU handling.
- **Convolutional neural networks for images** (`cnn`): Image classification needs convolutions, pooling and feature maps; the learner's linear algebra background helps with understanding the operations.
- **Model evaluation, overfitting, and regularization** (`evaluation_overfitting`): The learner must measure accuracy on held-out data, read loss curves, and use techniques like augmentation, dropout and weight decay to reduce overfitting.
- **Build, train and evaluate an image classifier end-to-end in PyTorch** (`image_classifier_project`): A code-along project ties everything together on a dataset like CIFAR-10 or Fashion-MNIST and matches the stated goal.

## Watch in this order

### 1. [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w)
3Blue1Brown · 21 min · counts 21 min · beginner, concept_explainer · covers ml_basics, gd_backprop · **confidence 0.75**

A visual walkthrough of how a network uses training data and a cost function, then minimises that cost with gradient descent on the MNIST digit example. It gives you the math intuition (gradient vectors, cost landscape) before any code, at a level that suits your calculus background.

> [00:00] “Cost functions and training for neural networks.” _(from chapters/description; no transcript)_

_Confidence note: The chapter list clearly matches cost functions and gradient descent, but there is no transcript. It is Chapter 2 of a series, and Chapter 1 (network structure) is not in the pool._

### 2. [Backpropagation, intuitively | Deep Learning Chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
3Blue1Brown · 13 min · counts 13 min · beginner, concept_explainer · covers gd_backprop · **confidence 0.75**

An intuitive walkthrough of what backpropagation actually does to the weights, plus stochastic gradient descent. It continues the same MNIST example, so you keep one mental model.

> [00:00] “What's actually happening to a neural network as it learns?” _(from chapters/description; no transcript)_
> [00:00] “The main goal with the follow-on video is to show the connection between the visual walkthrough here” _(from chapters/description; no transcript)_

_Confidence note: The chapters clearly cover backprop and SGD. The rating is held back only because the assessment comes from metadata, not a transcript._

### 3. [Backpropagation calculus | Deep Learning Chapter 4](https://www.youtube.com/watch?v=tIeHLnjs5U8)
3Blue1Brown · 10 min · counts 10 min · intermediate, concept_explainer · covers gd_backprop · **confidence 0.80**

A deliberately symbol-heavy follow-up that derives backprop with the chain rule, including derivatives with respect to weights and biases and multi-neuron layers. This fits your calculus background and your wish to understand the math behind autograd.

> [00:00] “This one is a bit more symbol-heavy, and that's actually the point.” _(from chapters/description; no transcript)_
> [00:00] “The goal here is to represent in somewhat more formal terms the intuition for how backpropagation works in part 3 of the series” _(from chapters/description; no transcript)_

_Confidence note: This is the right level for someone who knows calculus. The rating would be higher with a transcript._

### 4. [PyTorch for Deep Learning & Machine Learning – Full Course](https://www.youtube.com/watch?v=V_xro1bcAuA)
freeCodeCamp.org · 1537 min · watch 00:00–17:13:32 · counts 1034 min · beginner, full_course · covers ml_basics, pytorch_tensors_autograd, training_loop, cnn, image_classifier_project · **confidence 0.70**

This code-along course takes you from PyTorch tensors through a full train/test workflow on linear regression and neural-network classification. It then moves into computer vision with datasets, DataLoaders and a first CNN, which is your main hands-on path from zero to a working image model.

> [00:00] “Learn PyTorch for deep learning in this comprehensive course for beginners. PyTorch is a machine learning framework written in Python.” _(from chapters/description; no transcript)_
> [4:37:12] “Creating training and test sets (the most important concept in ML)” _(from chapters/description; no transcript)_
> [14:22:46] “What is a convolutional neural network?” _(from chapters/description; no transcript)_

_Confidence note: The chapter list matches the plan closely, but there is no transcript, so how deeply autograd itself is explained is unverified. Being beginner-level suits a learner with zero ML knowledge._

### 5. [PyTorch for Deep Learning & Machine Learning – Full Course](https://www.youtube.com/watch?v=V_xro1bcAuA)
freeCodeCamp.org · 1537 min · watch 23:45:00–25:37:26 · counts 112 min · beginner, full_course · covers evaluation_overfitting, image_classifier_project, cnn · **confidence 0.45**

The final part of the same course covers the food-image CNN project: loss curves, overfitting versus underfitting and how to address them, and predicting on new images. This completes your evaluation and end-to-end project goals in the same codebase you already know.

> [21:42:29] “Writing a custom dataset class from scratch” _(from chapters/description; no transcript)_

_Confidence note: The segment map only says loss curves and overfitting sit somewhere in 17:13:32-25:37:26. The start point of 23:45:00 is my estimate, so if the overfitting discussion starts earlier, shift this window back._

## Considered and dropped

- [AI Engineering Full Course (PyTorch) 2026 UPDATED | Beginner to Advanced | One Shot | Sagar Chouksey](https://www.youtube.com/watch?v=UqA7bxp7VBk): It covers similar tensors, training-loop and CNN material in 290 minutes but has no evaluation or overfitting section. It would only repeat the freeCodeCamp course with a new codebase.
- [Deep Learning with PyTorch Full Course | Master PyTorch, Tensors, and Neural Networks](https://www.youtube.com/watch?v=IFsVsXAqPto): It is a broad survey that also spends time on RNNs and multi-input models, with no evident hands-on project. Its evaluation content overlaps with the freeCodeCamp course.
- [PyTorch Tutorial 14 - Convolutional Neural Network (CNN)](https://www.youtube.com/watch?v=pDdP0TFzsoQ): It is a solid CIFAR-10 CNN build, but CNNs and image classification are already covered in the freeCodeCamp course. Adding it means switching creators to repeat a topic, and the budget is full.
- [Image Classification CNN in PyTorch](https://www.youtube.com/watch?v=CtzfbUwrYGI): This CIFAR-10 CNN project is redundant with the freeCodeCamp CNN sections and has no transcript evidence of explanation depth.
- [Gradient Descent From Scratch | End to End Gradient Descent | Gradient Descent Animation](https://www.youtube.com/watch?v=ORyfPJypKuU): It is a two-hour from-scratch gradient descent lecture whose spoken language is unverified. 3Blue1Brown covers the intuition and math more efficiently.
- [PyTorch in 1 Hour](https://www.youtube.com/watch?v=r1bquDz5GGA): Its tensor, autograd and nn.Module material overlaps the freeCodeCamp course, and it ends on a transformer block rather than images.
- [Deep Learning with CIFAR-10 Dataset - CNN Classifier | Neural Network  | Pytorch | Hindi | Bababoss](https://www.youtube.com/watch?v=U1Z39cFzenQ): The video is in Hindi.
- [Image classification using CNN (CIFAR10 dataset) | Deep Learning Tutorial 24 (Tensorflow & Python)](https://www.youtube.com/watch?v=7HPwo4wnJeA): It uses TensorFlow rather than PyTorch and is flagged for wrong language.
- [Part 2 - Supervised Learning | Complete Machine Learning Course for Beginners | Sheryians AI School](https://www.youtube.com/watch?v=Lb0JzFtTmBs): It teaches scikit-learn linear regression, which is off-topic for building PyTorch neural networks.
- [Gradient Descent From Scratch in Python - Visual Explanation](https://www.youtube.com/watch?v=gsfbWn4Gy5Q): Plain-Python gradient descent is useful, but it is redundant once 3Blue1Brown plus PyTorch's built-in gradient descent are covered, and the budget is full.

<details><summary>Filtered before assessment (29)</summary>

- Train a CONVOLUTIONAL NEURAL NETWORK on the CIFAR-100 dataset using PyTorch (prefilter): too short (92s)
- Building a CNN from Scratch for MNIST Digit Recognition | Step-by-Step Explanation (prefilter): pool cap reached
- Lec-37: Supervised, Unsupervised and Reinforcement Learning in Artificial Intelligence in Hindi (prefilter): pool cap reached
- Understanding BackPropagation Using Multi-variate Calculus [Machine Learning Tutorial] (prefilter): pool cap reached
- Gradient Descent For Neural Network | Deep Learning Tutorial 12 (Tensorflow2.0, Keras & Python) (prefilter): pool cap reached
- PyTorch crash course: from tensors to training a handwritten digit classifier (prefilter): pool cap reached
- ODSC East 2016 | Alex Wiltschko - "Building Neural Networks at Twitter with Autograd" (prefilter): pool cap reached
- CIFAR-10 Image Classification with CNN | Deep Learning Project 2 (prefilter): pool cap reached
- Learn PyTorch for deep learning in a day. Literally. (prefilter): pool cap reached
- Complete Machine Learning In 6 Hours| Krish Naik (prefilter): pool cap reached
- Understanding Backpropagation In Neural Networks with Basic Calculus (prefilter): pool cap reached
- Machine Learning Tutorial Python - 4: Gradient Descent and Cost Function (prefilter): pool cap reached
- Dataset & DataLoader Class in PyTorch | Video 6 | CampusX (prefilter): pool cap reached
- Exploring the Deep Learning Framework PyTorch - Stephanie Kim (prefilter): pool cap reached
- How to Build a CNN Image Classifier in PyTorch (CIFAR-10) — Beginner Guide (2026) (prefilter): pool cap reached
- Image Classification Using CNN (prefilter): pool cap reached
- Supervised Machine Learning Tutorial for Beginners [Part 10] | Logloss Function & its Interpretation (prefilter): pool cap reached
- Backpropagation Calculus Explained Simply | Chain Rule in Neural Networks | Deep Learning Chapter 4 (prefilter): pool cap reached
- Gradient descent from scratch in python (prefilter): pool cap reached
- Learn PyTorch FAST - Full Course for Beginners (2026) Part 1 Basics  (prefilter): pool cap reached
- JAX in 100 Seconds (prefilter): pool cap reached
- Introduction to Gradient Descent | How Models Minimize Loss (language): transcript is 'hi', learner needs 'en'
- CNN for CIFAR 10 (prefilter): pool cap reached
- Build Your Own Butterfly Image Classifier with Python AI (prefilter): pool cap reached
- Loss Functions in Deep Learning | Deep Learning | CampusX (prefilter): pool cap reached
- Chain Rule To find Derivative In Back Propagation (prefilter): pool cap reached
- Deep Learning With PyTorch - Full Course (prefilter): pool cap reached
- Pytorch - Minimizing every function using Pytorch - 01 (prefilter): pool cap reached
- CNN Image Classification with PyTorch | CIFAR-10 Tutorial | PyTorch vs TensorFlow  | Part 2 (prefilter): pool cap reached

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-opus-5.5 · cost $0.206 · 61 s_
