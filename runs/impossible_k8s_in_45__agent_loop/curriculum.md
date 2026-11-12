# Curriculum: Learn Kubernetes deeply and pass the CKA exam, including hands-on cluster setup

**Budget:** 45 min · **Planned:** 44 min · **Videos:** 4 · **Candidates assessed:** 36

**How I read the goal:** With 45 minutes, the learner gets a recent, exam-oriented starting path: the architecture mental model, a hands-on kubeadm cluster build, the kubectl imperative workflow the CKA rewards, and an exam strategy. This is the start of CKA prep, not the whole of it.

**Assumptions:** The 2023+ constraint is judged from titles and content (2025/2026 labels). I couldn't check upload dates for the KodeKloud architecture video, which is conceptual and slow to go out of date.; The learner will practice alongside the videos on their own VMs or a lab.; Deep coverage of the whole CKA curriculum needs a full course (50+ hours). 45 minutes can only set the foundation.

> **Not fully achievable in this budget.** Learning Kubernetes deeply and passing the CKA can't be done in 45 minutes. What fits is the foundation: architecture, a kubeadm cluster build, imperative kubectl for deployments and services, and an exam strategy. Storage, RBAC, etcd backup and restore, cluster upgrades, scheduling, and troubleshooting need a full CKA course plus practice labs such as Killer.sh.
> ⚠️ Total is about 44.5 of 45 minutes.
> ⚠️ Big gaps remain: storage, RBAC, etcd backup/restore, cluster upgrades, scheduling, NetworkPolicy, and troubleshooting. Follow with a full CKA course and Killer.sh practice.
> ⚠️ I chose the KubeSkills kubeadm video (9 min, labeled 2025) over the DevopsCube multi-node video (16 min). The DevopsCube video has no date I could check, and it would not fit the budget alongside the other picks.
> ⚠️ The Nana and KodeKloud crash courses (72 and 130 min) are too long for the budget and not exam-focused.
> ⚠️ The ByteByteGo architecture video overlaps with the KodeKloud one, so I kept only the KodeKloud lecture. It covers each component in more depth and ties to the CKA curriculum.

## Plan

- **Kubernetes architecture (control plane and node components)** (`arch`): Everything in the CKA builds on knowing what the API server, etcd, scheduler, controllers, kubelet and kube-proxy do.
- **Hands-on cluster setup with kubeadm** (`kubeadm`): Cluster installation is a core CKA topic, and the learner has only run single-server Docker.
- **kubectl imperative workflow: pods, deployments, services** (`kubectl`): The exam is timed and hands-on, so fast imperative commands and YAML generation with dry-run matter.
- **CKA exam strategy and study plan** (`strategy`): Covers exam rules, time management, docs bookmarking, and mock exams.

## Watch in this order

### 1. [Kubernetes Architecture Explained: Exploring etcd, Schedulers, Managers, and Node Components](https://www.youtube.com/watch?v=klxZke9qbvg)
KodeKloud · 9 min · counts 9 min · beginner, concept_explainer · covers arch · **confidence 0.70**

The KodeKloud lecture is tied to the CKA course. It walks through etcd, the scheduler, controllers, the API server, kubelet and kube-proxy, which the learner doesn't know yet.

> [03:13] “The master node is responsible for managing the Kubernetes cluster, storing information regarding the different nodes”
> [08:19] “The kube API server is the primary management component of Kubernetes. The kube API server is responsible for orchestrating all operations within the cluster”
> [11:39] “A kubelet is an agent that runs on each node in a cluster. It listens for instructions from the kube API server and deploys or destroys containers”

_Confidence note: It is pure theory, which suits this knowledge gap. I couldn't confirm its upload date._

### 2. [How to Install Kubernetes with Kubeadm (2025 Update) | Full Cluster Setup Walkthrough](https://www.youtube.com/watch?v=j3a2Sr2n8eQ)
KubeSkills · 9 min · counts 9 min · beginner, project_build · covers kubeadm · **confidence 0.80**

A 2025 walkthrough that builds a control plane and worker with containerd, kubeadm init, kubeadm join and a Calico CNI. This is the setup flow the learner needs.

> [00:00] “we're going to be installing the container D runtime, the Kube ADM, Kublet, and Kubectl to install our Kubernetes cluster”
> [10:27] “Kube ADM join, and then that contains the token that's going to join the worker node to the cluster”
> [11:42] “we're going to use the Calico CNI. We can run the command Kubectl apply. Just as we would any other YAML file”
> [13:21] “we've successfully bootstrapped a Kubernetes cluster, so congratulations on that. Now we can continue to run our pods”

_Confidence note: It is short and recent, and it covers the full bootstrap._

### 3. [Day 13: Imperative commands for Deployments, Services and Troubleshooting | CKA Course 2025](https://www.youtube.com/watch?v=ZDFqVFbX0Ic)
Cloud With VarJosh · 31 min · watch 00:00–13:20 · counts 13 min · intermediate, project_build · covers kubectl · **confidence 0.75**

A CKA 2025 course lesson that uses imperative commands to generate deployment YAML skeletons (dry-run), create deployments, and expose them as services. The first ~13 minutes teach the exam-speed workflow.

> [00:00] “imperative commands are super handy for quick testing, troubleshooting, and even during the CKA exam”
> [03:46] “imperative commands can do those things quickly. So we can use imperative commands to create a skeleton deployment YAML”
> [07:21] “In deployment, when you specify a port, you are specifying the container port. This is just for documentation purposes”

_Confidence note: Only the opening part fits the budget. The later connectivity and DNS testing section is cut._

### 4. [How to Pass the CKA Exam in 2026 | Certified Kubernetes Administrator](https://www.youtube.com/watch?v=YNPap3UH1IA)
Cloud Guru · 13 min · counts 13 min · beginner, concept_explainer · covers strategy · **confidence 0.60**

It covers the exam rules (one docs tab), time management, repetition-based practice and mock exam resources. That is the exam orientation the learner asked for.

> [00:29] “during the test, you're allowed to have one additional tab open with your Kubernetes documentation”
> [01:50] “this exam is, it's about two things. One, knowing how to do the material, but two, also knowing how to manage your time”
> [10:40] “the key to passing this CKA exam is all, you know, repetition, right? So learning how to do the same thing over and over”

_Confidence note: It is a surface-level strategy talk. That is acceptable here because the learner wants exam prep, and no other 2025+ video covered it._

_Models: agent_loop=anthropic/claude-sonnet-5.5 · cost $0.108 · 30 s_
