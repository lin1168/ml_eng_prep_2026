# Automatic Differentiation (Autograd)

Sentence 1: requires_grad gives you ability to label which is the variables in the function to ultimately do backpropogation 
Sentence 2: backward() does backpropogation?
Sentence 3: .grad stores something the gradient of im not sure if its the loss or the function itself
Sentence 4: Why use it? i think a package for optmizing a neural network through backpropogation to get the lowest loss?
Sentence 5: How it connects to training? im not really sure what you mean but i suppoesed you are talking about using training data to do the above like through backpropogation to get the optimized neural network then supposed we should get a better result during testing 

done lets goOrchestrated Week 2 curriculum overview and readiness assessmentOrchestrated Week 2 curriculum overview and readiness assessmentWeek 2 Plan (Jul 13–19) — Two Pointers & Sliding Window · First Neural Net End-to-End
You're moving from hash maps to two-pointer patterns (classic interview material) and building your first end-to-end neural net on FashionMNIST.

Week 2 At a Glance
DayDSAMain BlockArtifactMon 07/13Valid Palindrome (125)Datasets & DataLoaders + Transforms (FashionMNIST load + visualize 9 samples)notebooks/02-fashionmnist.ipynb startedTue 07/14Two Sum II (167)Build the Neural Network (MLP: Flatten → Linear/ReLU stack as nn.Module)MLP class defined + model printoutWed 07/153Sum (15) [Medium] or Remove Duplicates (26) [Easy]Optimizing Model Parameters (train + test loops, 5 epochs FashionMNIST)Training loop running, ~half-understanding OKThu 07/16Best Time to Buy and Sell Stock (121)Add accuracy metrics, save model (torch.save), reload, predict on 5 imagesEnd-to-end notebook committedFri 07/17Longest Substring Without Repeating Characters (3)Review + redo list2 SQL: Employees Earning More (181), Rising Temperature (197)Sat 07/20Longest Repeating Character Replacement (424) [Hard Medium]Clean FashionMNIST notebook (markdown header explaining every block)Flagship artifact committedSun 07/21Permutation in String (567) or redo-listSkim learnpytorch.io 02. Classification (map to what you already did)Weekly review + log

Key Shifts This Week

DSA: Two-pointer problems are more algorithmic than hash maps — you'll see left/right pointers moving. Different muscle.
PyTorch: You're not copying tutorials anymore. You're writing the model class from scratch, then training it. Expect ~50% understanding on first pass — that's normal and the handbook says so explicitly.
Project artifact: By Sunday, you'll have one clean notebook that explains FashionMNIST training end-to-end. This becomes your interview portfolio piece.


Before Monday 07/13
This weekend (07/13–07/14):

Rest. You crushed Week 1.
Optionally: skim the FashionMNIST dataset structure on torchvision docs (not a requirement, just context).
Make sure your ml_eng_prep conda env is activated and PyTorch imports clean.


Monday 07/13 Opening
When you sit down Monday:

Valid Palindrome (125) — 25 min timed attempt (two pointers converging from edges)
Main block: Load FashionMNIST via torchvision, visualize 9 random samples with labels in a grid
Log it

Questions before Monday? Or you good to go?no the project part we havent startReconciled timeline confusion between learning exercises and actual portfolio projectReconciled timeline confusion between learning exercises and actual portfolio projectPerry is right — we haven't started Project 1 yet. Looking at the handbook timeline:

Week 1-6: Phase 1 (Foundations)
Week 7-13: Phase 2 (Ship Something) — THIS is when Project 1 starts
Week 9 specifically: Project 1: EDA + baselines

So Project 1 doesn't start until Week 9 (Aug 31 – Sep 6). We're currently in Week 2 (Jul 13-19).
What Perry is referring to when he says "the project part" is probably the FashionMNIST notebook work in Week 2 — which is not actually a "project" in the sense of a deliverable portfolio piece. It's pure learning/practice.
The "project" learning modules are:

Week 2-4: Building PyTorch skills on FashionMNIST + transfer learning (learning artifacts)
Week 7-13: Project 1 (actual repo, real dataset, baselines, FastAPI, Docker, etc.)

So I need to clarify:

Weeks 2-4 are learning projects (building ML skills, not portfolio pieces)
Week 9 onwards: Project 1 (the real portfolio capstone that goes on GitHub)

I should confirm this with Perry so he's not confused about the timeline.
Perry is right to clarify. Let me check the handbook timeline:
Looking at Phase Overview (Section 4):

Phase 1: W1–W6 (Jul 6 – Aug 16) — Foundations
Phase 2: W7–W13 (Aug 17 – Oct 4) — Ship Something: Docker, FastAPI, Project 1

And in Phase 2 details, Week 9 is when Project 1 actually starts:

W9 (Aug 31 – Sep 6): Project 1: EDA + baselines

The real portfolio piece doesn't begin until Week 9. Right now in Week 2-4, Perry's working through learning exercises with FashionMNIST and transfer learning — foundational skills, not the actual deliverable. Week 7 covers Docker, Week 8 covers FastAPI, then Week 9 is when the actual Project 1 kicks off with exploratory data analysis and baseline models. I should clarify this sequence with Perry so there's no confusion about what counts as the portfolio project versus the learning phase.Show moreDoneRight catch. Let me clarify the timeline:
Weeks 2–4 (where you are now): These are learning exercises, not your portfolio project yet.

Week 2–3: PyTorch fundamentals on FashionMNIST (practice building models)
Week 4: Transfer learning (practice fine-tuning ResNet)
Artifact: Clean notebooks explaining how you trained them

Week 7–13 (Phase 2: "Ship Something"): This is when Project 1 actually starts.

Week 7: Learn Docker
Week 8: Learn FastAPI
Week 9 onward: Project 1 — real dataset (SECOM semiconductor or Kaggle predictive maintenance), baseline models, FastAPI service, Dockerfile, GitHub repo, README
Artifact: Public GitHub repo with model + API + Docker

So right now in Week 2:

FashionMNIST notebook is practice to build PyTorch skills
You're not building a production service yet
Just learning how to: load data → build a model class → train → evaluate

Week 9 is when you start the real project that goes on your resume.
Does that clear it up? Ready to hit Week 2 Monday as planned, or do you want the full Week 9 project breakdown now?no i mean for today besides dsa and sqlIdentified review tasks and logging requirements for todayIdentified review tasks and logging requirements for todayToday (Fri 07/10) after DSA + SQL:

Autograd review block (10 min):

Talk out loud for 2 min explaining requires_grad, backward(), and .grad without looking at your notes
Then check your notes/autograd.md — did you miss anything or explain it better now?


Update redo list in your tracking sheet:

Group Anagrams (49) — redo 07/12
Top K Frequent Elements (347) — redo 07/13


Log the day in Excel:

Energy level (1–5)
One thing you couldn't do before (example: "dict.items() unpacking + lambda syntax")


Quick Summary (your autograd note):
requires_grad=True  → tells PyTorch "track operations on this tensor"
.backward()         → compute gradients for all tracked tensors
.grad               → attribute holding the computed gradient value

e.g.
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2
y.backward()          # computes gradient of y w.r.t. x
print(x.grad)         # prints 4.0 (dy/dx when x=2)
