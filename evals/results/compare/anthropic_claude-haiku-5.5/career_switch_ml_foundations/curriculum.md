# Curriculum: Go from zero ML knowledge to training and evaluating a small image classifier in PyTorch

**Budget:** 1200 min · **Planned:** 982 min · **Videos:** 17 · **Candidates assessed:** 36

**How I read the goal:** The learner can explain how neural networks learn (loss, gradient descent, backprop), and can write, train and evaluate a small CNN image classifier in PyTorch from scratch, understanding overfitting and metrics.

**Assumptions:** The 1200 minutes is pure viewing time, so long code-along courses are acceptable and no time is reserved for separate practice.; A small image classifier means something like MNIST/Fashion-MNIST/CIFAR-10 trained with a CNN.; Because the learner knows calculus and linear algebra, math explanations can be intuitive but not simplified to avoid derivatives or matrices.; No constraints rule out particular video titles, so title exclusions are empty.
> ⚠️ Every candidate was assessed from chapter lists or descriptions only, because no transcripts were available. All confidences are therefore lower than they would be with verified transcripts, and the learner should check each pick's first few minutes against the reason given.
> ⚠️ Total picked viewing time is about 982 of 1200 minutes (about 82%). The remaining roughly 218 minutes are unused because no further verified candidates covered the thin sub-topics without repeating material or using the wrong language or framework.
> ⚠️ The image classifier project depends on one 504-minute chapter block from the freeCodeCamp course. Its content is unverified, and it is the single biggest risk in this curriculum. If it proves weak, the CNN and project coverage rests on the Patrick Loeber tutorial and the Sagar CNN section alone.
> ⚠️ Gradient descent and backprop coverage is strong on intuition, but the learner will see several overlapping explanations of the chain rule. This is intentional, since the learner wants math intuition, but it may feel repetitive.
> ⚠️ Evaluation and overfitting coverage is thin. The only dedicated pick is a short scikit-learn segment, and the main neural-network evaluation comes from the freeCodeCamp block. The learner should plan to write a simple train/validation split on their own.
> ⚠️ The CIFAR-10 CNN tutorials in Hindi and TensorFlow were excluded for language and framework reasons, so the learner gets fewer CIFAR-10 variants than the pool offers.
> ⚠️ The Coding With Sagar course is used in four separate segments (foundations, tensors, autograd and training, CNNs) to avoid the rest of the course. The learner should follow it in that order, since the segments are not contiguous with the other videos.

## Plan

- **Machine learning fundamentals: supervised learning, loss functions, train/test split** (`ml_basics`): Learner has zero ML background; needs the vocabulary and framing before touching neural networks, though numpy and linear algebra let them move quickly.
- **Gradient descent, neural networks and backpropagation with math intuition** (`gd_backprop`): Learner knows calculus, so the chain rule view of backprop will click fast; this gives the intuition they want for why training works.
- **PyTorch tensors and autograd** (`pytorch_tensors_autograd`): Learner knows numpy, so PyTorch tensors map onto familiar ideas; autograd connects directly to the backprop they just learned.
- **Building models and training loops in PyTorch (nn.Module, optimizers, DataLoader)** (`training_loop`): Needed to turn the math into working code, including batching, loss, optimizer steps and GPU/CPU handling.
- **Convolutional neural networks for images** (`cnn`): Image classification needs convolutions, pooling and feature maps; the learner's linear algebra background helps with understanding the operations.
- **Model evaluation, overfitting, and regularization** (`evaluation_overfitting`): The learner must measure accuracy on held-out data, read loss curves, and use techniques like augmentation, dropout and weight decay to reduce overfitting.
- **Build, train and evaluate an image classifier end-to-end in PyTorch** (`image_classifier_project`): A code-along project ties everything together on a dataset like CIFAR-10 or Fashion-MNIST and matches the stated goal.

## Watch in this order

### 1. [What is a Loss Function? Understanding How AI Models Learn](https://www.youtube.com/watch?v=v_ueBW_5dLg)
IBM Technology · 10 min · counts 10 min · beginner, concept_explainer · covers ml_basics · **confidence 0.45**

Short IBM concept explainer on loss functions covering regression losses, classification losses, and how a loss drives model optimization. It gives the loss vocabulary needed before gradient descent.

> [00:00] “Unlock the power of loss functions to optimize your AI models and drive better results.” _(from chapters/description; no transcript)_

_Confidence note: Only the chapter list was verified, with no transcript. A 10-minute overview may be shallow on the math._

### 2. [Lec-2: Supervised Learning Algorithms | Machine Learning](https://www.youtube.com/watch?v=LKlOH8OLLcw)
Gate Smashers · 9 min · counts 9 min · beginner, lecture · covers ml_basics · **confidence 0.40**

Covers the supervised learning workflow: labeled training data, training, testing, and a survey of algorithms. It fills the train/test split vocabulary the plan requires.

> [00:00] “where models are trained on labeled data to make predictions or classify new inputs.” _(from chapters/description; no transcript)_

_Confidence note: Chapter-level evidence only. The algorithm survey (trees, SVMs) is not needed for the goal and is a light detour._

### 3. [Part 2 - Supervised Learning | Complete Machine Learning Course for Beginners | Sheryians AI School](https://www.youtube.com/watch?v=Lb0JzFtTmBs)
Sheryians AI School · 161 min · watch 06:29–46:30 · counts 40 min · beginner, lecture · covers ml_basics · **confidence 0.45**

Only the regression section of this scikit-learn lecture is needed: linear regression, the cost function, and the start of gradient descent. This gives a concrete first model before neural networks.

> [00:00] “How to use Scikit-learn to implement Linear Regression” _(from chapters/description; no transcript)_

_Confidence note: Lecture style with no PyTorch code-along. Transcript unavailable, so the cut is based on chapter titles._

### 4. [AI Engineering Full Course (PyTorch) 2026 UPDATED | Beginner to Advanced | One Shot | Sagar Chouksey](https://www.youtube.com/watch?v=UqA7bxp7VBk)
Coding With Sagar · 290 min · watch 03:03–48:01 · counts 45 min · beginner, full_course · covers ml_basics · **confidence 0.50**

Opening foundations chapter of the course: ML versus DL and key terms, before the PyTorch code starts. It gives a code-along-friendly start to the vocabulary.

> [00:00] “Learn AI Engineering from scratch using PyTorch in one complete video.” _(from chapters/description; no transcript)_

_Confidence note: Full-course chapter list only. This slice is the foundations chapter, not transcript-verified._

### 5. [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w)
3Blue1Brown · 21 min · counts 21 min · beginner, concept_explainer · covers gd_backprop · **confidence 0.60**

Visual walkthrough of cost functions, gradient descent, and how a network is analysed. It builds the intuition for how weights move downhill, which the learner needs before any code.

> [00:00] “Cost functions and training for neural networks.” _(from chapters/description; no transcript)_

_Confidence note: 3Blue1Brown is well regarded, but only chapter titles were verified and there is no transcript._

### 6. [3.5: Mathematics of Gradient Descent - Intelligence and Learning](https://www.youtube.com/watch?v=jc2IthslyzM)
The Coding Train · 23 min · counts 23 min · beginner, lecture · covers gd_backprop · **confidence 0.50**

Works through the calculus of gradient descent on linear regression: the cost, the derivative, the update rule, and the power and chain rules. This matches the learner's calculus background.

> [00:00] “I explain the mathematics behind Linear Regression with Gradient Descent” _(from chapters/description; no transcript)_

_Confidence note: Lecture-style with no code. The level is beginner, so the learner may skim the basics._

### 7. [Gradient Descent From Scratch in Python - Visual Explanation](https://www.youtube.com/watch?v=gsfbWn4Gy5Q)
NeuralNine · 29 min · counts 29 min · beginner, project_build · covers gd_backprop · **confidence 0.55**

Implements gradient descent from scratch in plain Python, with a derivative, an optimization loop, and learning-rate analysis. It pairs the math with code the learner can follow.

> [00:00] “In this video we implement gradient descent from scratch in Python.” _(from chapters/description; no transcript)_
> [00:00] “Also I try to give you an intuitive and mathematical understanding of what is happening.” _(from chapters/description; no transcript)_

_Confidence note: Chapter list only. It uses plain Python rather than PyTorch, so it does not teach autograd._

### 8. [Backpropagation, intuitively | Deep Learning Chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
3Blue1Brown · 13 min · counts 13 min · beginner, concept_explainer · covers gd_backprop · **confidence 0.55**

Visual intuition for backpropagation and stochastic gradient descent in a neural network. It is the step from gradient descent to learning a multi-layer network.

> [00:00] “What's actually happening to a neural network as it learns?” _(from chapters/description; no transcript)_

_Confidence note: No transcript and a poor-transcript flag, so this rests on the description alone._

### 9. [Backpropagation calculus | Deep Learning Chapter 4](https://www.youtube.com/watch?v=tIeHLnjs5U8)
3Blue1Brown · 10 min · counts 10 min · intermediate, concept_explainer · covers gd_backprop · **confidence 0.50**

Formal chain-rule derivation of backpropagation for a small network, extended to multi-neuron layers. It meets the math-intuition requirement at a level the learner's calculus supports.

> [00:00] “This one is a bit more symbol-heavy, and that's actually the point.” _(from chapters/description; no transcript)_
> [00:00] “The goal here is to represent in somewhat more formal terms the intuition for how backpropagation works in part 3 of the series” _(from chapters/description; no transcript)_

_Confidence note: Symbol-heavy and intermediate. No transcript, so the depth is not confirmed._

### 10. [Backpropagation is Just the Chain Rule](https://www.youtube.com/watch?v=VCGlYxGJZ04)
DataMListic · 4 min · counts 4 min · intermediate, concept_explainer · covers gd_backprop · **confidence 0.50**

Short derivation of how error flows backward through layers via the transposed weight matrix, with the gradient as input activation times output error. It links backprop to the matrix algebra the learner already knows.

> [00:00] “derive how that error flows backward through the layers via the transposed weight matrix” _(from chapters/description; no transcript)_
> [00:00] “every gradient is just an input activation times an output error” _(from chapters/description; no transcript)_

_Confidence note: Only the description was verified. The video is very short, so it works as a supplement, not a standalone._

### 11. [AI Engineering Full Course (PyTorch) 2026 UPDATED | Beginner to Advanced | One Shot | Sagar Chouksey](https://www.youtube.com/watch?v=UqA7bxp7VBk)
Coding With Sagar · 290 min · watch 48:01–1:27:53 · counts 40 min · beginner, full_course · covers pytorch_tensors_autograd · **confidence 0.60**

PyTorch tensor setup, shapes, indexing, NumPy interop and GPU use from the same code-along course. The learner's NumPy knowledge transfers directly to tensors.

> [48:01] “PyTorch Tensors & Setup (Installation, Tensor Basics, Shapes, Indexing, NumPy ↔ PyTorch, GPU Usage)” _(from chapters/description; no transcript)_

_Confidence note: Chapter list only; the code-along content is not transcript-verified._

### 12. [AI Engineering Full Course (PyTorch) 2026 UPDATED | Beginner to Advanced | One Shot | Sagar Chouksey](https://www.youtube.com/watch?v=UqA7bxp7VBk)
Coding With Sagar · 290 min · watch 1:27:53–2:28:06 · counts 60 min · beginner, full_course · covers pytorch_tensors_autograd, training_loop · **confidence 0.60**

Automatic differentiation, loss functions, optimizers and the training loop. This connects the backprop math from earlier to PyTorch's autograd.

> [1:27:53] “Autograd & Training Models (Automatic Differentiation, Loss Functions, Optimizers, Training Loop)” _(from chapters/description; no transcript)_

_Confidence note: Chapter list only. Confidence depends on whether autograd is explained rather than just called._

### 13. [AI Engineering Full Course (PyTorch) 2026 UPDATED | Beginner to Advanced | One Shot | Sagar Chouksey](https://www.youtube.com/watch?v=UqA7bxp7VBk)
Coding With Sagar · 290 min · watch 2:28:06–3:54:30 · counts 86 min · beginner, full_course · covers training_loop · **confidence 0.55**

nn.Module model definition, layers, activations, DataLoaders and an MNIST classifier. This is the structure the learner needs to write training loops.

> [1:27:53] “Autograd & Training Models (Automatic Differentiation, Loss Functions, Optimizers, Training Loop)” _(from chapters/description; no transcript)_

_Confidence note: Chapter list only. The MNIST classifier is a stepping stone rather than the target image task._

### 14. [Part 2 - Supervised Learning | Complete Machine Learning Course for Beginners | Sheryians AI School](https://www.youtube.com/watch?v=Lb0JzFtTmBs)
Sheryians AI School · 161 min · watch 1:46:17–1:57:37 · counts 11 min · beginner, lecture · covers evaluation_overfitting · **confidence 0.40**

Covers overfitting and underfitting and how they show up when testing on held-out data. This is needed before the CNN project.


_Confidence note: Chapter title evidence only. The overfitting material is in scikit-learn regression, not neural networks._

### 15. [AI Engineering Full Course (PyTorch) 2026 UPDATED | Beginner to Advanced | One Shot | Sagar Chouksey](https://www.youtube.com/watch?v=UqA7bxp7VBk)
Coding With Sagar · 290 min · watch 3:54:30–4:49:58 · counts 56 min · beginner, full_course · covers cnn · **confidence 0.55**

Convolutional layers, pooling and transfer learning for image classification in PyTorch. It gives the conceptual CNN picture before the CIFAR-10 code.

> [3:54:30] “CNNs & Computer Vision (Conv Layers, Transfer Learning, Image Classification Projects)” _(from chapters/description; no transcript)_

_Confidence note: Chapter list only. The transfer-learning content goes beyond the goal._

### 16. [PyTorch Tutorial 14 - Convolutional Neural Network (CNN)](https://www.youtube.com/watch?v=pDdP0TFzsoQ)
Patrick Loeber · 22 min · counts 22 min · intermediate, project_build · covers cnn, image_classifier_project · **confidence 0.60**

Implements a first CNN for CIFAR-10 in PyTorch with layer size calculation, forward pass, training and evaluation. It gives concrete hands-on CNN code.

> [00:00] “In this part we will implement our first convolutional neural network (CNN) that can do image classification based on the famous CIFAR-10 dataset.” _(from chapters/description; no transcript)_
> [00:00] “Max Pooling - Determine the correct layer size - Implement the CNN architecture in PyTorch” _(from chapters/description; no transcript)_

_Confidence note: Chapter-level evidence from metadata only. The teacher is a reliable PyTorch tutorial author, but the code is unverified._

### 17. [PyTorch for Deep Learning & Machine Learning – Full Course](https://www.youtube.com/watch?v=V_xro1bcAuA)
freeCodeCamp.org · 1537 min · watch 17:13:32–25:37:26 · counts 504 min · beginner, full_course · covers cnn, evaluation_overfitting, image_classifier_project · **confidence 0.40**

Chapter block covering CNNs, a custom image dataset, a baseline model, loss curves and overfitting. It is the main end-to-end image classifier project in PyTorch and the evaluation coverage the learner needs.

> [21:42:29] “Writing a custom dataset class from scratch” _(from chapters/description; no transcript)_

_Confidence note: A long chapter-based block with no transcript. Code quality and pace are unverified, and the learner should check that its CNN material matches the earlier CNN picks._

## Considered and dropped

- [PyTorch in 1 Hour](https://www.youtube.com/watch?v=r1bquDz5GGA): Good one-hour PyTorch crash course on tensors and autograd, but it duplicates the tensor and autograd coverage of the chosen course, and adding a second creator costs the learner a new setup.
- [Gradient Descent From Scratch | End to End Gradient Descent | Gradient Descent Animation](https://www.youtube.com/watch?v=ORyfPJypKuU): Two-hour gradient descent course with from-scratch code, but its spoken language is unverified and the plan's gradient descent coverage is already met.
- [Deep Learning with CIFAR-10 Dataset - CNN Classifier | Neural Network  | Pytorch | Hindi | Bababoss](https://www.youtube.com/watch?v=U1Z39cFzenQ): CIFAR-10 CNN in PyTorch, but the title and channel indicate Hindi-language narration, which the learner cannot follow reliably.
- [Tutorial 5 - Chain Rule of Derivatives in Backward Propagation - Krish Naik Hindi](https://www.youtube.com/watch?v=k3B8ZoxTpOk): Chain-rule backprop explainer, but the title marks it as Hindi-language, so it is excluded for language.
- [Image classification using CNN (CIFAR10 dataset) | Deep Learning Tutorial 24 (Tensorflow & Python)](https://www.youtube.com/watch?v=7HPwo4wnJeA): CIFAR-10 CNN in TensorFlow, not PyTorch, which the goal requires.
- [Mastering PyTorch Fundamentals | Tensors, Autograd & Neural Networks (in 30 Minutes)](https://www.youtube.com/watch?v=44zW9dWxxXc): Tensors and autograd in PyTorch, but the classifier is on tabular Iris data, not images, and the transcript is unavailable.
- [PyTorch a framework for research of dynamic deep learning models - Adam Paszke](https://www.youtube.com/watch?v=BZyKufPCKdI): Conference talk on PyTorch internals at intermediate level. It is a lecture rather than a code-along, so it does not teach the hands-on path the learner needs.
- [Deep Learning with PyTorch Full Course | Master PyTorch, Tensors, and Neural Networks](https://www.youtube.com/watch?v=IFsVsXAqPto): Broad 2-hour survey touching every topic, but at chapter-title depth only, with no project. It would repeat material already covered in more detail.
- [What is PyTorch | Introduction to PyTorch | PyTorch Tutorial For Beginners | Intellipaat](https://www.youtube.com/watch?v=Idg5uFnpV1M): Four-minute PyTorch introduction flagged as a surface intro, which is disqualifying when better coverage exists.
- [S1P2. Binary classification with augmentation and pre-trained model](https://www.youtube.com/watch?v=_oQgHpw41qM): Binary classification with a pretrained model in PyTorch Lightning. It skips building and training a CNN from scratch, which the goal requires.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-haiku-5.5 · cost $0.025 · 176 s_
