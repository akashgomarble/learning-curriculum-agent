# Curriculum: Learn Kubernetes deeply and pass the CKA exam, including hands-on cluster setup

**Budget:** 45 min · **Planned:** 43 min · **Videos:** 6 · **Candidates assessed:** 36

**How I read the goal:** In 45 minutes of viewing, the learner gets a solid conceptual foundation in Kubernetes architecture, core objects, kubectl, and kubeadm cluster setup, framed around the CKA exam, along with a clear picture of the exam's scope and what to study next.

**Assumptions:** 'Nothing from before 2023' means videos must be published in 2023 or later, and since titles are the only signal available, titles that mention older years or outdated exam versions are excluded.; The learner will use the remaining CKA preparation (practice labs, mock exams) outside this 45-minute video plan.; The learner has no prior Kubernetes exposure, so the plan starts at architecture and does not assume cloud-managed clusters.; The current CKA curriculum covers cluster architecture/installation/configuration, workloads and scheduling, services and networking, storage, and troubleshooting.

> **Not fully achievable in this budget.** Deep Kubernetes mastery and passing the CKA cannot be achieved in 45 minutes of video. Realistic in this budget: understand the CKA scope and format, learn Kubernetes architecture, pods/deployments/services, core kubectl usage, and see a kubeadm cluster setup walkthrough, which gives a foundation for later hands-on practice and mock exams.
> ⚠️ Feasibility: deep Kubernetes mastery and passing the CKA cannot be achieved in 45 minutes of video. This plan is a foundation only; the CKA is a hands-on exam, so you need lab practice and mock exams afterwards.
> ⚠️ No verified quotes were available for any candidate, and every transcript is poor or metadata-only. Every pick is therefore judged from titles and summaries and carries moderate confidence; evidence_quote_ids are empty throughout.
> ⚠️ The kubectl pick uses an assumed 0-9 minute range of a 31-minute lecture, because the card has no segment map. Check that the range makes sense and keep watching if it is useful.
> ⚠️ Services coverage is thin: the pick covers NodePort and the endpoints/selector workflow, but ClusterIP, LoadBalancer and basic cluster networking concepts get little time.
> ⚠️ Pods get light direct coverage, because the pick focuses on Deployments and ReplicaSets.
> ⚠️ Coverage of CKA domains is partial. Storage, scheduling details, RBAC, etcd backup and troubleshooting are not covered and need separate study.
> ⚠️ The kubeadm video's segment map covers only part of its 9.1 minutes. The whole video is counted toward the budget.
> ⚠️ Planned viewing is 42.7 of 45 minutes (about 95%). The 2.3 unused minutes are left because no fitting, unflagged, post-2023 video was available to add.
> ⚠️ All picks come from 2023 or later, using upload dates as the check. Titles that mention future years were not trusted over the metadata.

## Plan

- **CKA exam format, domains and study strategy** (`cka_overview`): The learner needs exam-prep orientation: what the current CKA covers, the weighting of domains, and the time-pressured, hands-on format.
- **Kubernetes architecture: control plane and worker node components** (`k8s_architecture`): Coming from single-server Docker, the learner must understand how API server, etcd, scheduler, controller manager, kubelet and kube-proxy fit together to orchestrate containers across nodes.
- **Pods, ReplicaSets and Deployments** (`pods_deployments`): These are the core workload objects replacing 'docker run'; the learner knows containers but not how Kubernetes schedules, scales and updates them declaratively with YAML.
- **Services and basic cluster networking** (`services_networking`): Single-server Docker port mapping differs from Kubernetes Services (ClusterIP, NodePort, LoadBalancer) and DNS, which are heavily tested in the CKA.
- **kubectl essentials and exam-speed imperative commands** (`kubectl_essentials`): The CKA is a command-line practical exam; the learner needs fast kubectl usage, imperative commands, dry-run YAML generation, and kubectl explain/docs navigation.
- **Cluster setup with kubeadm** (`kubeadm_setup`): Hands-on cluster installation (init, join, CNI, node prep) is a core CKA domain and the learner has never built a multi-node cluster.

## Watch in this order

### 1. [CKA Exam Prep: How I Became a Kubestronaut](https://www.youtube.com/watch?v=SuKkL8YjXMg)
Cloud DevOps with Ana · 4 min · counts 4 min · beginner, concept_explainer · covers cka_overview · **confidence 0.50**

Gives a CKA-specific roadmap of exam format and key topics, and it is the only post-2023 exam-overview video that fits the 4-minute slot. This sets the scope before any Kubernetes content.


_Confidence note: The transcript is unavailable, so the content is judged from the title and summary only. Confidence would rise if the video shows the current exam domains and weightings._

### 2. [Kubernetes Architecture Explained: Control Plane, Nodes & Pod Lifecycle | CKA Ch 1.1](https://www.youtube.com/watch?v=5NHMNVeutT8)
DevopsJourney · 10 min · counts 10 min · beginner, concept_explainer · covers k8s_architecture · **confidence 0.70**

A CKA-chapter video that covers control plane components (kube-apiserver, etcd, scheduler, controller-manager) and node components (kubelet, runtime, kube-proxy, CNI). It also walks the Deployment-to-Running-Pod lifecycle and shows how to match failure symptoms to components, which is useful for troubleshooting questions.


_Confidence note: The summary matches the slot well and is exam-oriented. There is no transcript or verified quote, and the segment map looks incomplete._

### 3. [EP05 - Kubernetes Deployments & ReplicaSets](https://www.youtube.com/watch?v=yeUBojfuhiI)
Devops Basics with Dali · 6 min · counts 6 min · beginner, project_build · covers pods_deployments · **confidence 0.60**

Explains Deployments and ReplicaSets (self-healing, scaling, rolling updates), then creates a Deployment from a YAML manifest with kubectl. This gives a Docker user the jump from single containers to managed replicas.


_Confidence note: Short and hands-on, but it is not CKA-framed and has no transcript. Pods on their own are covered only lightly._

### 4. [Stop Losing Easy Points on the CKA: Complete NodePort Workflow (CKA Trap)](https://www.youtube.com/watch?v=yL_DurdVxak)
Uptime Unicorn · 4 min · counts 4 min · intermediate, concept_explainer · covers services_networking · **confidence 0.55**

A CKA-oriented NodePort workflow that exposes a Deployment. It covers common exam traps: missing container ports, invalid kubectl flags, and selector mismatches that leave a Service with no Endpoints.


_Confidence note: Strong on exam practice but narrow, since it covers NodePort only. ClusterIP and LoadBalancer concepts are not clearly covered, and it has no transcript._

### 5. [Day 13: Imperative commands for Deployments, Services and Troubleshooting | CKA Course 2025](https://www.youtube.com/watch?v=ZDFqVFbX0Ic)
Cloud With VarJosh · 31 min · watch 00:00–09:00 · counts 9 min · beginner, lecture · covers kubectl_essentials · **confidence 0.45**

Part of a CKA 2025 course on imperative commands for Deployments, Services and troubleshooting, which is the exam-speed kubectl skill needed. Only the opening segment is used to fit the budget.


_Confidence note: The card has no internal segment map, so the 0-9 minute range is an assumption. Confidence would rise if the opening minutes are confirmed to cover core imperative commands._

### 6. [How to Install Kubernetes with Kubeadm (2025 Update) | Full Cluster Setup Walkthrough](https://www.youtube.com/watch?v=j3a2Sr2n8eQ)
KubeSkills · 9 min · counts 9 min · beginner, project_build · covers kubeadm_setup · **confidence 0.60**

A step-by-step kubeadm cluster install on Ubuntu 22.04 with containerd and Calico CNI. It has no red flags and was updated for 2025, so the learner sees the init and join flow that the CKA tests.


_Confidence note: This is the only unflagged, recent, short kubeadm walkthrough. The segment map covers only 4:30 of a 9.1-minute video, and there is no transcript._

## Considered and dropped

- [Kubernetes Architecture Explained: Exploring etcd, Schedulers, Managers, and Node Components](https://www.youtube.com/watch?v=klxZke9qbvg): A solid 9-minute architecture explainer, but flagged pure_theory and not exam-framed. 5NHMNVeutT8 covers the same components plus the pod lifecycle and failure mapping.
- [Setup Kubernetes Cluster Using Kubeadm [Multi-node]](https://www.youtube.com/watch?v=xX52dc3u2HU): A 2023 multi-node kubeadm walkthrough, but at 16.4 minutes it would push the plan over budget. It is also a different creator and setup from the chosen kubeadm video.
- [How to Setup a Kubernetes Cluster using Kubeadm on Ubuntu | K8S Cluster Setup| LinuxGKTech](https://www.youtube.com/watch?v=VTWQt8rOCHM): A 2026 kubeadm setup, but at 21.6 minutes it is too long for the slot. Much of it is port and prerequisite discussion.
- [Kubernetes Services explained | ClusterIp NodePort & LB| Part - 2 ..... #Kubernetes #CKA @AlokKumar](https://www.youtube.com/watch?v=bhGufLt75X4): A 2023 CKA-tagged Services video, but flagged pure_theory and 28 minutes long with no segment map to excerpt from. It is far over the services slot.
- [How to Pass the CKA Exam in 2026 | Certified Kubernetes Administrator](https://www.youtube.com/watch?v=YNPap3UH1IA): The title says 2026, but the upload date is 2022, which breaks the learner's 2023 floor. It is also flagged surface_intro with no transcript.
- [Kubernetes Crash Course for Absolute Beginners [NEW]](https://www.youtube.com/watch?v=s_o8dwzRlu4): A 2021 upload, which breaks the 2023 floor, and 72 minutes long with no transcript.
- [Upgrade Kubernetes Cluster with Kubeadm in 2024: Step-by-Step Guide | CKA | CKS | TechWiseRahul](https://www.youtube.com/watch?v=Uj0XaNUesXs): Covers kubeadm cluster upgrades, not initial setup. It is an intermediate topic the learner is not ready for in this budget.
- [Kubernetes Cluster Setup 2026 | Kubeadm Multi-Node Installation](https://www.youtube.com/watch?v=RTMXEIGbeHM): Its title says 2026 but the upload date is 2023, an inconsistency. It is 18.8 minutes long, and the card's segment map gives little evidence of setup depth.
- [How Kubernetes Heals Itself: ReplicaSets Explained](https://www.youtube.com/watch?v=rNFiI9QVOMw): Covers ReplicaSets only. yeUBojfuhiI covers Deployments and ReplicaSets with a hands-on part in less time.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.219 · 67 s_
