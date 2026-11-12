# Curriculum: Learn Kubernetes deeply and pass the CKA exam, including hands-on cluster setup

**Budget:** 45 min · **Planned:** 44 min · **Videos:** 5 · **Candidates assessed:** 36

**How I read the goal:** In 45 minutes of viewing, the learner gets a solid conceptual foundation in Kubernetes architecture, core objects, kubectl, and kubeadm cluster setup, framed around the CKA exam, along with a clear picture of the exam's scope and what to study next.

**Assumptions:** 'Nothing from before 2023' means videos must be published in 2023 or later, and since titles are the only signal available, titles that mention older years or outdated exam versions are excluded.; The learner will use the remaining CKA preparation (practice labs, mock exams) outside this 45-minute video plan.; The learner has no prior Kubernetes exposure, so the plan starts at architecture and does not assume cloud-managed clusters.; The current CKA curriculum covers cluster architecture/installation/configuration, workloads and scheduling, services and networking, storage, and troubleshooting.

> **Not fully achievable in this budget.** Deep Kubernetes mastery and passing the CKA cannot be achieved in 45 minutes of video. Realistic in this budget: understand the CKA scope and format, learn Kubernetes architecture, pods/deployments/services, core kubectl usage, and see a kubeadm cluster setup walkthrough, which gives a foundation for later hands-on practice and mock exams.
> ⚠️ Infeasible as stated: 45 minutes of video cannot teach Kubernetes deeply or get anyone through the CKA. This plan gives a foundation; real practice labs and mock exams (e.g. killer.sh) are needed afterwards.
> ⚠️ No post-2022 candidate in the pool is a clean CKA exam overview. The only dedicated overview videos were either flagged (vlog) or pre-2023, so cka_overview is covered only partly, through the exam-scenario framing in the NodePort video and the CKA framing in the architecture video.
> ⚠️ Planned viewing time is about 43.6 of 45 minutes (about 97%). The ZDFqVFbX0Ic range (3:46-18:00) stops before its NodePort and DNS/connectivity-testing sections to fit the budget.
> ⚠️ Services and networking is covered thinly: ClusterIP in the course excerpt and NodePort in the short exam video. Ingress, DNS and network policies are not covered.
> ⚠️ Storage, troubleshooting, scheduling and other exam domains are outside this 45-minute plan.
> ⚠️ Some transcript segment maps list timestamps beyond the stated video length, so the architecture, ReplicaSet and kubeadm picks are played in full and the ZDFqVFbX0Ic range relies on its segment map.

## Plan

- **CKA exam format, domains and study strategy** (`cka_overview`): The learner needs exam-prep orientation: what the current CKA covers, the weighting of domains, and the time-pressured, hands-on format.
- **Kubernetes architecture: control plane and worker node components** (`k8s_architecture`): Coming from single-server Docker, the learner must understand how API server, etcd, scheduler, controller manager, kubelet and kube-proxy fit together to orchestrate containers across nodes.
- **Pods, ReplicaSets and Deployments** (`pods_deployments`): These are the core workload objects replacing 'docker run'; the learner knows containers but not how Kubernetes schedules, scales and updates them declaratively with YAML.
- **Services and basic cluster networking** (`services_networking`): Single-server Docker port mapping differs from Kubernetes Services (ClusterIP, NodePort, LoadBalancer) and DNS, which are heavily tested in the CKA.
- **kubectl essentials and exam-speed imperative commands** (`kubectl_essentials`): The CKA is a command-line practical exam; the learner needs fast kubectl usage, imperative commands, dry-run YAML generation, and kubectl explain/docs navigation.
- **Cluster setup with kubeadm** (`kubeadm_setup`): Hands-on cluster installation (init, join, CNI, node prep) is a core CKA domain and the learner has never built a multi-node cluster.

## Watch in this order

### 1. [Kubernetes Architecture Explained: Control Plane, Nodes & Pod Lifecycle | CKA Ch 1.1](https://www.youtube.com/watch?v=5NHMNVeutT8)
DevopsJourney · 10 min · counts 10 min · beginner, concept_explainer · covers k8s_architecture · **confidence 0.85**

Gives a CKA-framed walk through control plane components (API server, etcd, scheduler, controller manager) and worker components (kubelet, runtime, kube-proxy, CNI). It also traces the six steps from kubectl apply to a running pod, which links the architecture to the objects that follow.

> [01:50] “The control plane makes decisions and stores the cluster's state. The worker nodes run your applications.”
> [10:01] “First, Kube control sends the request to the API server, which authenticates it, authorizes it, runs admission, and stores the deployment in ETCD.”
> [12:24] “When a pod is pending, describe it and read the events section. The scheduler explains itself.”

_Confidence note: Unflagged, exam-oriented and recent. The segment map runs past the stated duration, so the content is inferred from the summary and quotes._

### 2. [EP05 - Kubernetes Deployments & ReplicaSets](https://www.youtube.com/watch?v=yeUBojfuhiI)
Devops Basics with Dali · 6 min · counts 6 min · beginner, concept_explainer · covers pods_deployments · **confidence 0.75**

Explains how a Deployment declares the desired state and how the ReplicaSet keeps the pods running. It shows a Deployment manifest being applied and a pod being deleted and recreated, which gives the learner the object model before the imperative commands.

> [00:20] “The deployment defines the desired state, in this case three replicas. Then, the replica set ensures that three pods are always running.”
> [01:44] “The replica set constantly checks if the desired number of pods is running. So, if one pod crashes or disappears, Kubernetes automatically creates a new one to replace it.”
> [05:04] “We only created one deployment manifest, but Kubernetes automatically created three pods based on the replicas value.”

_Confidence note: Short and clear, but it does not cover pod specs in depth and is not exam-specific._

### 3. [Day 13: Imperative commands for Deployments, Services and Troubleshooting | CKA Course 2025](https://www.youtube.com/watch?v=ZDFqVFbX0Ic)
Cloud With VarJosh · 31 min · watch 03:46–18:00 · counts 14 min · intermediate, project_build · covers kubectl_essentials, pods_deployments, services_networking · **confidence 0.80**

A CKA-course lesson on creating deployments imperatively, using --dry-run to generate YAML skeletons, and exposing them as ClusterIP services. It covers the exam-speed kubectl habits the learner needs, and the range stops before the NodePort and DNS-testing sections to fit the budget.

> [00:00] “imperative commands are super handy for quick testing, troubleshooting, and even during the CKA exam”
> [03:46] “imperative commands can do those things quickly. So we can use imperative commands to create a skeleton deployment YAML”
> [07:21] “In deployment, when you specify a port, you are specifying the container port. This is just for documentation purposes”

_Confidence note: Good fit for the content and level. It is slightly above beginner level, and the range was chosen from the segment map._

### 4. [Stop Losing Easy Points on the CKA: Complete NodePort Workflow (CKA Trap)](https://www.youtube.com/watch?v=yL_DurdVxak)
Uptime Unicorn · 4 min · counts 4 min · beginner, project_build · covers services_networking, kubectl_essentials, cka_overview · **confidence 0.70**

A short CKA-style task: expose a deployment with a NodePort service. It covers the trap that kubectl expose cannot set a custom nodePort and the dry-run-then-edit workflow. It also gives a realistic sense of how the exam scores such tasks.

> [00:49] “The trap is that the kubectl expose doesn't let you pass a custom nodeport flag directly.”
> [03:40] “We must use the dry run client to create a YAML file to generate the basic server spec instantly and dump it to the YAML.”
> [00:00] “Exposing deployment with no port service should be a three or three point on the CKA exam. But almost every year candidate lose mark here.”

_Confidence note: Strong on NodePort and exam technique. It is a weak substitute for a real exam-format and domains overview._

### 5. [How to Install Kubernetes with Kubeadm (2025 Update) | Full Cluster Setup Walkthrough](https://www.youtube.com/watch?v=j3a2Sr2n8eQ)
KubeSkills · 9 min · counts 9 min · beginner, project_build · covers kubeadm_setup · **confidence 0.85**

A compact 2025 kubeadm walkthrough: install containerd and kubeadm/kubelet/kubectl, run kubeadm init, join a worker with the join token, and apply the Calico CNI. This is the cluster-setup part of the CKA that this learner has never seen.

> [00:00] “we're going to be installing the container D runtime, the Kube ADM, Kublet, and Kubectl to install our Kubernetes cluster”
> [10:27] “Kube ADM join, and then that contains the token that's going to join the worker node to the cluster”
> [11:42] “we're going to use the Calico CNI. We can run the command Kubectl apply. Just as we would any other YAML file”

_Confidence note: Recent, unflagged and focused on setup. It uses Ubuntu with Calico, which may differ from an exam environment._

## Considered and dropped

- [CKA Exam Prep: How I Became a Kubestronaut](https://www.youtube.com/watch?v=SuKkL8YjXMg): Flagged as a vlog, surface intro and pure theory. It is a personal story with only brief exam-format coverage, and the yL_DurdVxak exam-scenario pick replaces it.
- [How to Pass the CKA Exam in 2026 | Certified Kubernetes Administrator](https://www.youtube.com/watch?v=YNPap3UH1IA): Upload date is 2022, which breaks the learner's no-pre-2023 limit, even though its title says 2026.
- [Setup Kubernetes Cluster Using Kubeadm [Multi-node]](https://www.youtube.com/watch?v=xX52dc3u2HU): A good kubeadm video from 2023, but its Terraform/AWS infrastructure setup makes it longer and heavier than the focused kubeadm walkthrough chosen.
- [Kubernetes Architecture Explained: Control Plane & Worker Node Components](https://www.youtube.com/watch?v=beYyRumKXZE): Unflagged architecture video, but it runs about 28 minutes and would take most of the budget; the chosen video covers architecture plus the pod workflow in 10 minutes.
- [Day-31 | KUBERNETES ARCHITECTURE USING EXAMPLES | Kubernetes is Easy #devops #k8s #devopscourse](https://www.youtube.com/watch?v=gywke3XiNC0): Flagged pure_theory, 25 minutes long, and spends much of its time on Docker background the learner already knows.
- [Kubernetes Architecture Explained: Exploring etcd, Schedulers, Managers, and Node Components](https://www.youtube.com/watch?v=klxZke9qbvg): Flagged pure_theory and covers architecture only, with no link to pod workflow or the CKA.
- [Kubernetes Explained in 6 Minutes | k8s Architecture](https://www.youtube.com/watch?v=TlHvYWVUZyc): Flagged as a surface intro that includes use-case and trade-off discussion; a CKA-framed unflagged architecture video exists.
- [Kubernetes Services explained | ClusterIp NodePort & LB| Part - 2 ..... #Kubernetes #CKA @AlokKumar](https://www.youtube.com/watch?v=bhGufLt75X4): 28 minutes on services in an EKS cluster. This is a managed-cloud setup, and the services material is covered more efficiently elsewhere.
- [Kubernetes Crash Course: Learn the Basics and Build a Microservice Application](https://www.youtube.com/watch?v=XuSQU5Grv1g): A 130-minute crash course assessed from metadata only, so the evidence is weak and it does not fit the 45-minute budget.

<details><summary>Filtered before assessment (29)</summary>

- Kubernetes Beginner To Expert Level In One Video | Ultimate Kubernetes Guide | #kubernetes #k8s (prefilter): 420 min, far beyond the 45-min budget
- CKA 2026 Crash Course: Learn Kubernetes FAST + Hands-On Full Guide (prefilter): 1283 min, far beyond the 45-min budget
- Kubernetes CKS Full Course Theory + Practice + Browser Scenarios (prefilter): 667 min, far beyond the 45-min budget
- Everything you need to know about AWS Cloud Practitioner ☁️ #aws (prefilter): too short (41s)
- Learn Kubernetes in 6 Hours – Full Course with Real-World Project (prefilter): 353 min, far beyond the 45-min budget
- Day 9 – ReplicaSets ExplainedWhen a Pod crashes, gets deleted, or becomes unhealthy (prefilter): too short (23s)
- Kubernetes Zero to Hero: The Complete Beginner’s Guide (2025 Edition) (prefilter): 170 min, far beyond the 45-min budget
- Are Certifications Worth it? The Truth About PMP and Scrum Master (prefilter): too short (44s)
- Kubernetes Tutorial for Beginners [FULL COURSE in 4 Hours] (prefilter): 217 min, far beyond the 45-min budget
- 3 Career Paths for 1 Crore Salary! | Kushal Lodha #shorts (prefilter): too short (59s)
- CKA Skill Builder: Manually Upgrade a Kubernetes Cluster with kubeadm (prefilter): pool cap reached
- What is Kubernetes? | Kubernetes Explained (prefilter): pool cap reached
- Kubernetes Architecture Explained in Hindi | Control Plane & Node Components Simplified | Tutorial#2 (prefilter): pool cap reached
- Kubernetes Deployment Explained 🚀 | Create, Update & Scale Deployments | Kubernetes Tutorial (prefilter): pool cap reached
- Kubernetes Services explained and Labs | ClusterIP vs NodePort vs LoadBalancer vs Headless Service (prefilter): pool cap reached
- Day 6/40 - Kubernetes Multi Node Cluster Setup Step By Step | Kind Tutorial (prefilter): pool cap reached
- Kubernetes Cluster Architecture | Control Plan & Node Component | #Kubernetes #CKA @AlokKumar (prefilter): pool cap reached
- Kubernetes Deployments: Update Your App Without Downtime (prefilter): pool cap reached
- Kubernetes Service Explained | ClusterIP, NodePort & LoadBalancer with Hands-On Lab | CKA (prefilter): pool cap reached
- Setup Kubernetes v1.29 Cluster using Kubeadm and Containerd on AWS (prefilter): pool cap reached
- Kubernetes Crash Course for Beginners | Hands-On Tutorial + First Deployment (prefilter): pool cap reached
- Day 9/40 - Kubernetes Services Explained - ClusterIP vs NodePort vs Loadbalancer vs External (prefilter): pool cap reached
- Day 27/40 - Setup a Multi Node Kubernetes Cluster Using Kubeadm (prefilter): pool cap reached
- Day 12: Kubernetes Services IN-DEPTH | ClusterIP, NodePort, LoadBalancer, ExternalName | CKA 2025 (prefilter): pool cap reached
- kubectl commands cheat sheet 2026: Master Kubernetes CLI [CKA Roadmap] (prefilter): pool cap reached
- DAY-35 | EVERYTHING ABOUT KUBERNETES SERVICES | DISCOVERY | LOAD BALANCING | NETWORKING | #devops (prefilter): pool cap reached
- From Zero to CKA Hero: Master the Exam with Payload Pat's Tips! (prefilter): pool cap reached
- Day 34/40 - Step-By-Step Guide To Upgrade a Multi Node Kubernetes Cluster With Kubeadm (prefilter): pool cap reached
- Kubernetes and EKS for Beginners – Crash Course with Pulumi (prefilter): pool cap reached

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.245 · 91 s_
