# Curriculum: Go from zero ML knowledge to training and evaluating a small image classifier in PyTorch

**Budget:** 1200 min · **Planned:** 1155 min · **Videos:** 7 · **Candidates assessed:** 36

**How I read the goal:** The learner can explain how neural networks learn (loss, gradient descent, backprop), and can write, train and evaluate a small CNN image classifier in PyTorch from scratch, understanding overfitting and metrics.

**Assumptions:** The 1200 minutes is pure viewing time, so long code-along courses are acceptable and no time is reserved for separate practice.; A small image classifier means something like MNIST/Fashion-MNIST/CIFAR-10 trained with a CNN.; Because the learner knows calculus and linear algebra, math explanations can be intuitive but not simplified to avoid derivatives or matrices.; No constraints rule out particular video titles, so title exclusions are empty.
> ⚠️ Every candidate was assessed from chapter lists and descriptions only, with no transcripts, so all confidence values are modest. Check the first few minutes of each range to confirm it matches the segment map.
> ⚠️ The plan reserved more time for gradient descent and backprop (240 min) than 3Blue1Brown's three videos provide (about 44 min). The rest of that sub-topic is covered only through the PyTorch course's workflow and training chapters.
> ⚠️ Total viewing time is about 1155 of 1200 minutes. I skipped the course's neural network classification chapters (8:32:00–14:00:48, about 328 min) and the last ~1.6 hours (24:00:00–25:37:26) to stay within the budget. Activations and multiclass loss are therefore covered only by the 3Blue1Brown videos and whatever the CNN part reviews.
> ⚠️ The freeCodeCamp timestamps are derived from per-chapter titles, and the course's tensors section is long. Skip anything you already know from numpy.
> ⚠️ Explicit regularization (dropout, weight decay, augmentation) is not confirmed in the chosen ranges. Overfitting is confirmed only through loss curves.
> ⚠️ I assumed the learner wants PyTorch only, so the TensorFlow/Keras CNN videos were not considered.

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
3Blue1Brown · 21 min · counts 21 min · beginner, concept_explainer · covers ml_basics, gd_backprop · **confidence 0.60**

The chapters cover training data, cost functions and gradient descent on an MNIST-style network. That gives a mechanical engineer the loss and gradient intuition before any code. It is visual, and the learner already knows the calculus.

> [00:00] “Cost functions and training for neural networks.” _(from chapters/description; no transcript)_

_Confidence note: Based on the chapter list only, with no transcript. Confidence rests on the well-known structure of this series._

### 2. [Backpropagation, intuitively | Deep Learning Chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
3Blue1Brown · 13 min · counts 13 min · beginner, concept_explainer · covers gd_backprop · **confidence 0.60**

A visual walkthrough of how backpropagation nudges weights, followed by stochastic gradient descent. It builds the intuition for the later autograd material.

> [00:00] “What's actually happening to a neural network as it learns?” _(from chapters/description; no transcript)_
> [00:00] “The main goal with the follow-on video is to show the connection between the visual walkthrough here” _(from chapters/description; no transcript)_

_Confidence note: Chapters and description only. The content is probably right, but it could not be verified._

### 3. [Backpropagation calculus | Deep Learning Chapter 4](https://www.youtube.com/watch?v=tIeHLnjs5U8)
3Blue1Brown · 10 min · counts 10 min · intermediate, concept_explainer · covers gd_backprop · **confidence 0.60**

Gives the formal chain-rule treatment of backpropagation with derivatives for weights and biases. It suits a learner who wants the math, and it explains what loss.backward() computes.

> [00:00] “This one is a bit more symbol-heavy, and that's actually the point.” _(from chapters/description; no transcript)_
> [00:00] “The goal here is to represent in somewhat more formal terms the intuition for how backpropagation works in part 3 of the series” _(from chapters/description; no transcript)_

_Confidence note: No transcript. The level is borderline-intermediate but should be fine given the learner's calculus._

### 4. [PyTorch for Deep Learning & Machine Learning – Full Course](https://www.youtube.com/watch?v=V_xro1bcAuA)
freeCodeCamp.org · 1537 min · watch 00:00–4:17:27 · counts 257 min · beginner, full_course · covers pytorch_tensors_autograd · **confidence 0.50**

The first part of this course is a code-along on PyTorch fundamentals and tensors, the first hands-on step after the backprop concepts. Continuing with one creator keeps a single codebase and teaching style for the rest of the plan.

> [00:00] “Learn PyTorch for deep learning in this comprehensive course for beginners. PyTorch is a machine learning framework written in Python.” _(from chapters/description; no transcript)_

_Confidence note: Chapter titles only. This segment is long and may spend time on basics the learner already knows (numpy-like operations). It is unclear how much autograd it covers._

### 5. [PyTorch for Deep Learning & Machine Learning – Full Course](https://www.youtube.com/watch?v=V_xro1bcAuA)
freeCodeCamp.org · 1537 min · watch 4:17:27–8:32:00 · counts 255 min · beginner, full_course · covers ml_basics, training_loop, evaluation_overfitting · **confidence 0.55**

Covers the PyTorch workflow on linear regression, including creating training and test sets, the loss function, the optimizer and the train/test loops. This fills the ML-basics and training-loop gap in code.

> [4:37:12] “Creating training and test sets (the most important concept in ML)” _(from chapters/description; no transcript)_

_Confidence note: Based on the chapter list. The workflow and train/test split are clearly named, but the depth of the explanations is unverified._

### 6. [PyTorch for Deep Learning & Machine Learning – Full Course](https://www.youtube.com/watch?v=V_xro1bcAuA)
freeCodeCamp.org · 1537 min · watch 14:00:48–17:13:32 · counts 193 min · beginner, full_course · covers cnn, training_loop · **confidence 0.50**

Computer vision basics, datasets and DataLoaders, then the CNN introduction, both in PyTorch. This part skips the tabular classification chapters and goes straight to images.

> [14:22:46] “What is a convolutional neural network?” _(from chapters/description; no transcript)_

_Confidence note: Chapter titles only. Whether the CNN math is explained well is unverified._

### 7. [PyTorch for Deep Learning & Machine Learning – Full Course](https://www.youtube.com/watch?v=V_xro1bcAuA)
freeCodeCamp.org · 1537 min · watch 17:13:32–24:00:00 · counts 406 min · beginner, full_course · covers cnn, evaluation_overfitting, image_classifier_project · **confidence 0.50**

Builds CNNs, a baseline model, a custom image dataset class and loss curves to diagnose overfitting. This is the end-to-end image classifier project with evaluation. The range stops before the final chapters to stay within the budget.

> [14:22:46] “What is a convolutional neural network?” _(from chapters/description; no transcript)_
> [21:42:29] “Writing a custom dataset class from scratch” _(from chapters/description; no transcript)_

_Confidence note: Chapter list only. Regularization techniques and the exact content of the trimmed end are unverified._

## Considered and dropped

- [AI Engineering Full Course (PyTorch) 2026 UPDATED | Beginner to Advanced | One Shot | Sagar Chouksey](https://www.youtube.com/watch?v=UqA7bxp7VBk): A 290-minute alternative that covers tensors through CNNs, but it has no evaluation or overfitting coverage. Using it would mean a second creator and codebase on top of the freeCodeCamp course, which covers the project and overfitting.
- [Deep Learning with PyTorch Full Course | Master PyTorch, Tensors, and Neural Networks](https://www.youtube.com/watch?v=IFsVsXAqPto): A 116-minute survey whose chapters are mostly titles. It is too shallow for a long-course learner and has no end-to-end project.
- [Gradient Descent From Scratch | End to End Gradient Descent | Gradient Descent Animation](https://www.youtube.com/watch?v=ORyfPJypKuU): A good-looking two-hour gradient descent from scratch, but it is a lecture with no PyTorch. 3Blue1Brown plus the course's workflow part already cover gradient descent more efficiently.
- [PyTorch Tutorial 14 - Convolutional Neural Network (CNN)](https://www.youtube.com/watch?v=pDdP0TFzsoQ): A good PyTorch CIFAR-10 CNN code-along (22 min). It was left out to avoid a new creator and codebase, since the course covers CNNs and the project and the budget is nearly used.
- [PyTorch in 1 Hour](https://www.youtube.com/watch?v=r1bquDz5GGA): A one-hour PyTorch crash course on tensors, autograd and nn.Module. It would repeat the tensor and training-loop material from the freeCodeCamp course.
- [Image Classification CNN in PyTorch](https://www.youtube.com/watch?v=CtzfbUwrYGI): A short CIFAR-10 CNN project with unverified depth. The course already covers this sub-topic in more depth.
- [Part 2 - Supervised Learning | Complete Machine Learning Course for Beginners | Sheryians AI School](https://www.youtube.com/watch?v=Lb0JzFtTmBs): A 161-minute regression lecture built on scikit-learn rather than PyTorch, with no neural network or image content.
- [Mastering PyTorch Fundamentals | Tensors, Autograd & Neural Networks (in 30 Minutes)](https://www.youtube.com/watch?v=44zW9dWxxXc): A 30-minute video on tensors and autograd with an Iris classifier. It uses tabular data, has no CNN, and duplicates the course.
- [Tutorial 6-Chain Rule of Differentiation with BackPropagation](https://www.youtube.com/watch?v=CRB266Eyjkg): A short chain-rule video. 3Blue1Brown's backprop chapters cover the same ground, and the learner already knows the chain rule.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-sonnet-5.5 · cost $0.114 · 42 s_
