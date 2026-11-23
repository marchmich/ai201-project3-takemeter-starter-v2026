# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

I have chosen the reddit community r/AIsafety. My classifier sorts posts into carreer advice, discussions/hot takes, questions, and projects.

---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `Career Advice`

**Definition:** This refers to any post in which users are asking for carreer guidance or advice to other users. It can also include questions about the field, or similar fields such as AI governance, evaluation, or software engineering.

**Example 1:**
>  Are there AI Safety professional options beyond AGI? Hi, everyone! I'm not sure this is the right place to ask about this; if it's not, I apologise in advance and I'm happy to receive directions! I have been working in Tech and Research for more than 8 years now. I studied (an applied) the statistical foundations and data requirements of AI models before the AI hype. I don't like AI and I'm really worried about its impact. This is an informed opinion and I'm not coming to this thread looking to discuss it. Because of this worry of mine, I've been looking at alternative professional paths related to AI Safety and Security for the past few months. However, almost every program I find (paid or not) focuses on AGI, misalignment and existential risks, or at leasts assumes that's the worst that AI can do to our society and something we should really care about.
I don't. I care about the current problems of AI: biases, data centers, human cognition deterioration, IP theft, impact on moderator/labeller mental health, invasion of privacy, frontier labs that do NOT put the required security measures for their tests (if a tiger goes free into a city the responsibility is the zoo's, not the tiger's).
Is there any AI Safety space where I could belong? If there isn't, does anyone know which term I should search for to find the professional spaces I'm looking for?
Thank you in advance to all of you that took the time to read this far 

**Example 2:**
> I'm a computer science student and I want to build a career in AI Safety. I made a roadmap to follow while still going to school (obv😅). But I find it hard to be consistent and grind as much as I planned to, I also wonder if there's someone else doing the same thing as me (studying computer science or a similar course in uni) and planning to enter the AI safety field. I wonder what their action plan is like. It'll be nice if I can join or create a community with people like this. I want to be an AI/ML engineer or mech interp

### `Discussions`

**Definition:** This refers to post in which users exchange or debate ideas, developments, milestones, or issues. 

**Example 1:**
> The answer to all these cyber attacks is simple - rebuild everything from scratch
Everyone's saying that AI should be banned because of these malicious AI bots (most likely commanded by malicious humans) and how they're finding vulnerabilities in legacy systems.
Well isn't the answer obvious? The legacy systems have to completely go. You need completely new paradigms (probably new programming languages altogether) which are built to be completely watertight from the ground up.
The older languages (straw houses) were built to shield yourself against bad humans (the wind). The newer languages should be built to shield yourself against bots (the big bad wolf). Make them out of "bricks".
In fact if you ask me, I think you should have a AI assistant continously scanning it as you build it just to point out vulnerabilities (if they do exist at all).

**Example 2:**
>    Why human oversight remains important with  increased capabilities of AI systems. AI systems are becoming increasingly useful but one issue that needs more consideration is knowing when not to trust them.
Advanced models will often give a confident answer that contains incorrect information, or will misunderstand what they have been asked, and fail to consider important context. This is an issue when using AI in areas such as healthcare, finance, education, or decision making.
I believe that AI safety should look at how we can make models more capable but also increase their limitations. Having human oversight along with clear evaluation and ongoing monitoring of models is key to responsible implementation.
What do you feel is the biggest challenge in making increasingly capable AI systems reliable and safe?

### `Questions`

**Definition:** This refers to posts in which the users are asking a question for clarification, request an explanation, or a different point of view. It is meant to make an idea or concept clearer for the user.

**Example 1:**
> How do we know when an AI system is safe enough to deploy?  \
AI systems are becoming more capable and are being integrated into more everyday tools and workflows. But I find it interesting that there's still no simple way to determine when a system is actually safe enough for real-world use.
Benchmarks can measure performance, and safety testing can identify known risks, but what happens when a system behaves unexpectedly outside controlled testing environments?
I'm curious how people working in AI safety approach this. Should deployment decisions depend more on independent evaluations, continuous monitoring, human oversight, or some combination of all three?

**Example 2:**

> How are you building an inventory of the AI tools people are actually using? \
People at work are using AI assistants, coding agents, browser extensions, MCP servers, you name it, and we don’t have a clear view of what’s in use or what data is going into any of it. How are you finding unapproved AI tools and agents, on endpoints and in SaaS? Did you lean on what you already had, like EDR, DLP, identity logs, proxy or CASB, or add something dedicated? We already run Netskope, and axonius is one of the options we’re comparing for the inventory side, since it would match the AI apps people sign into with SSO against our IdP. It won’t show what data goes into them though, that part stays with Netskope. Then there’s all the little scripts and internal tools people knock together with AI in an afternoon. Security usually hears about those after they’re already in use. Blocking it all isn’t really an option and nobody wants that anyway. Mostly after visibility and a few sensible guardrails. What’s worked for you, and where are you still blind?

### `Projects`

**Definition:** This refers to posts in which users are requesting help, collaboration, or any input regarding any projects they are working on.

**Example 1:**
> Looking for a study buddy to transition into AI Governance together, complete beginner, starting from scratch \
Hey everyone,
I'm looking for someone who is also trying to break into the AI Governance field and wants to go through the journey together as study partners.
I'm very new to this space so I'll be starting from the absolute basics. No prior background in AI policy or governance needed, just genuine curiosity and commitment to show up consistently.
The idea is pretty open and flexible. We figure it out together as we go, deciding what to read week by week, whether that's books, research papers, case studies, or policy documents. We could work on small projects together, discuss what we're learning, hold each other accountable, and slowly build up our understanding of the field side by side.
Ideally I'd love someone who can commit to daily or near-daily study sessions even if it's just 30 minutes of reading and a quick sync. Consistency matters more to me than speed.
If you're someone who is also pivoting into AI governance, policy, safety, or anything adjacent and you want a structured but flexible learning partner for the long haul, drop a comment or send me a DM. Would love to connect.


**Example 2:**
> I built a website to track AI threats and incidents around the globe with live tracker of recent events. Check it out!

### The hardest boundary

**Which two labels:** Projects and questions can be confused because they both discuss an idea, and ask a question. In the case for projects, the person is asking for collaboration. 

**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's analysis, even
     if the tone is heated." -->

If the post invites to collaborate, or connect then it is 'Project', even if it also contains a question.


---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:** Reddit, r/AIsafety

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

I labeled 20 posts as cold and the rest I used AI to labelled them. I then double-checked that the labels were right and corrected the ones that were not..


**Counts per label:**

| Label | Count | Share |
|---|---|---|
| discussion | 217 | 63.08% |
| career advice | 63 | 18.31% |
| projects | 58  | 16.86% |
| questions | 6 |  1.74%|
| **Total** | 344 | 100% |


**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:*
> How Ransomware Operators Put AI Agents to Work? 
> *Could have been:*
> Discussion
> *I chose, because:*
> I chose Questions because the user was asking other users for clarification, but it was confusing because the user provided some ideas. 

**2.**
> *The post:*
> "Running (or starting) an AI safety group at your university? Pathfinder Fellowship applications are open until November 24! The Pathfinder Fellowship supports students organizing AI safety and AI policy groups at universities anywhere in the world. Fellows get 1-on-1 mentorship from experienced organizers, funding for their group, and a community of organizers at 80+ universities. New groups launching next semester are welcome, and we support organizers at every experience level.

We're also looking for mentors who have organized a university group before.

The program runs from early December 2026 through the spring semester. Applications close November 24, 2026 (11:59 PM AoE).

* [More info](https://pathfinder.kairos-project.org/?utm_source=reddit-aisafety&utm_medium=forum&utm_campaign=pathfinder-s27)
* [Apply as a fellow](https://forms.kairos-project.org/pathfinder/fellow?utm_source=reddit-aisafety&utm_medium=forum&utm_campaign=pathfinder-s27)
* [Apply as a mentor](https://forms.kairos-project.org/pathfinder/mentor?utm_source=reddit-aisafety&utm_medium=forum&utm_campaign=pathfinder-s27)

Happy to answer questions in the comments!"
> *Could have been:*
> Another category, miscellany.
> *I chose, because:*
> I kept it under the career guidance label, because it can be related, but falls outside the description label I gave.

**3.**
> *The post:*
> If AI alignment is so important, why do you need to get hired to help solve it? 
> *Could have been:*
> Discussion
> *I chose, because:*
I chose question, but could have been discussion as well. I decided that the user was mostly looking for answers, rather than introducing a new idea.
---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**
I am using distilbert-base-uncased

**Settings:** <!-- epochs, learning rate, batch size, seed -->
seed 42, 3 epochs, lr 2e-05, batch 16

**Anything I changed from the defaults, and why:**
I did not changed anything from the defaults. I will be testing how accuracy increases in the fine-tuned scenario.

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->

train 240  ·  val 52  ·  test 52
               train  val  test
label                          
questions         45    9     9
career advice      4    1     1
projects          40    9     9
discussions      151   33    33

---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:* To label the reddit entries, using the following labels: question, career advice, discussions, projects label.
- *What came back:* A list of all 344 entries labelled by my criteria.
- *What I changed:* I changed the notes from pre-label to 'cold' in the 20 entries I had done earlier. I also changed the entries mislabeled by AI.

**Pre-labelling disclosure:** I used Claude for pre-labelling but I double-checked every entry and edited those that were mislabeled by AI.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->
| Measure | Baseline |
|---|---|
| Overall accuracy | 0.269 |
| Macro F1 | 0.296 |
| F1 — `career advice` | 0.000 |
| F1 — `discussions` | 0.162 |
| F1 — `projects` | 0.429 |
| F1 — `questions` | 0.593 |


**What I predicted before I looked:**
I predict my model will have higher accuracy overall, but particularly will have higher accuracy for discussions because I have a large dataset.

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.269 | 0.635 | +0.365 |
| Macro F1 | 0.296 | 0.194 | -0.102 |
| F1 — `career advice` | 0.000 | 0.000 | +0.000 |
| F1 — `discussions` | 0.162 | 0.776 | +0.614 |
| F1 — `projects` | 0.429 | 0.000 | -0.429 |
| F1 — `questions` | 0.593 | 0.000 | -0.593 |

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->

There is an increase of 0.365 in the overall accuracy, which means that the fine-tuning enhanced the system. The f1 score for projects and question dicreased which could signify that the label is confusing and maybe too similar or that the data set was too small.

---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  | Overall accuracy | >60% | 0.635 | 0.635 | 0.635 | PASSED |
| 2.  | Every label F1 | >60% | 0.194 | 0.194 | 0.194 | MISSED |
| 3.  | Precision on career guidance | >40% | 0.0 | 0.0 | 0.0 | MISSED |
| 4.  | Recall on questions | >60% | 0.0 | 0.0 | 0.0 | MISSED |
| 5.  | Beats the baseline on accuracy |  yes | yes | yes | MET |

| Measure | Seed 42 | Seed 7 | Seed 2024 | Spread |
|---|---|---|---|---|
| Overall accuracy | 0.635 | 0.635 | 0.635 | 0.000 |
| Macro F1 | 0.194 | 0.194 | 0.194 | 0.000 |
| F1 — `questions` | 0.000 | 0.000 | 0.000 | 0.000 |
| F1 — `career advice` | 0.000 | 0.000 | 0.000 | 0.000 |
| F1 — `projects` | 0.000 | 0.000 | 0.000 | 0.000 |
| F1 — `discussions` | 0.776 | 0.776 | 0.776 | 0.000 |

Accuracy moved 0.000 across seeds. Stable enough to trust.

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted | questions | career advice | projects | discussions |
|---|---|---|---|---|
| **questions** | 0 | 0 | 0 | 9 |
| **career advice** | 0 | 0 | 0 | 1 |
| **projects** | 0 | 0 | 0 | 9 |
| **discussions** | 0 | 0 | 0 | 33 |



**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->

The biggest off-diagonal number is 9 and appears twice. That is because all 9 "project" were labelled "discussions", so 0 correct, and because all 9 "questions", were labelled "discussions", so 0 correct.

This means that the model is leaning towards 'discussions' and it is lopsided. As I noted before, the labels discussions and questions tend to overlap, so it might be a good idea to merge them.

career advice (1 true): the 1 example was labelled "discussions", so 0 correct
discussions (33 true): all 33 were labelled "discussions", so all correct
---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1.  | Overall accuracy | >60% | PASSED | The accuracy was greater than 60% for all seeds. |
| 2.  | Every label F1 | >60% | 0.194 | 0.194 | 0.194 | MISSED | The f1 scores are very low for all labels |
| 3.  | Precision on career guidance | >40% | 0.0 | 0.0 | 0.0 | MISSED | results indicate low precision for career guidance because of the small data set. |
| 4.  | Recall on questions | >60% | 0.0 | 0.0 | 0.0 | results indicate recall for question. |
| 5.  | Beats the baseline on accuracy |  yes | yes | yes | MET | 

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->

Criterion 2: — Every label F1 >60%: MISSED

This is mainly a data imbalance problem. The training set contains only 6 career-advice examples, while discussions has 217. 

Criterion 3: Career-advice precision >40%: MISSED

This is also because of the same too-few-examples problem. I do not consider this to be a labeling problem. Career advice appears only 6 times in 344 rows, and none of the held-out career-advice examples received a career-advice prediction. The agreement report does not contain career-advice examples, so it provides no direct evidence of a career-advice boundary inconsistency.

Criterion 4 — Questions recall >60%: MISSED

All 9 held-out questions were predicted as discussions, so the model learned discussions more strongly than the questions/discussions boundary. The agreement report’s 70% agreement and some repeated reaction/analysis and hot-take/analysis disagreements show that one of the project taxonomies has inconsistent boundaries, but it does not directly measure the questions/discussions boundary. The confusion matrix is therefore stronger evidence that this miss comes from model and data limitations rather than an established labeling error.



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** 21 / 30 = 70%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

| Post | Staff said | I said | My call, and why |
|---|---|---|---|
| The club championship scoring changed in 2019 from top-6 to top-10. S… | analysis | reaction | I said reaction because the post responds to a concrete rule change and supports its reaction with data. I would change it to analysis because the post uses that evidence to explain a broader interpretation: the scoring system, not athlete depth, is what changed the outcome. |
| Carbon plates aren't the whole story. My times dropped 2% in the shoe… | analysis | reaction | I said reaction because it its mostly talking from personal experience, it reports what just happened to the writer and how it felt. But since he is introducing the data, and most likely willing to discuss it, it can be analysis
 |
| Three of us ran the same session on the same day, different shoes, wi… | analysis | reaction |  I said reaction because reports what just happened to the writer and how it felt. |
| Heart rate zones are astrology for runners. | hot_take | analysis | I  labelled it as analysis because makes the post is trying to make an argument backed by a specific, named comparisonm as described in the taxonomy. |
| Track sessions are wasted on anyone running slower than 8 minute mile… | hot_take | analysis | I labelled it as analysis, thinking the idea could be expanded, but it is not. Therefore, it is a hot take. |
| First run back after eight weeks out. Two miles, slower than my warm-… | reaction | hot_take | I called it as a hot take, but it is definetely a reaction because it reports what just happened to the writer and
how it felt. |
| Blew up at 20 with the pace band still in my hand like it was going t… | reaction | analysis | I called it as a analysis, but it is definetely a reaction because it reports what just happened to the writer and
how it felt. It is a bit amiguous because it is hard to understand what the writer is trying to convey. |
| Someone handed my kid an orange slice at mile 22 and I have been cryi… | reaction | analysis | I made a mistake in this label, this should have definitely been labeled as a reaction. |
| Just realised the shoes I set every PB in this year are the ones I bo… | reaction | analysis |  I thought that if expanded, the argument could be that the wrong size shoes were helping him set PB more frequently. However, the idea is not further expanded, therefore is not substatial enough to be an analysis. Therefore, I do agree that reaction is a much better fit. |

**1.**
> *The post:*
> The club championship scoring changed in 2019 from top-6 to top-10. Since then our B team has finished above the A team twice. That's not depth improving, it's the scoring rewarding turnout.
> *Staff said / I said:*
> analysis | reaction
> *My call, and why:*
> I said reaction because the post responds to a concrete rule change and supports its reaction with data. I would change it to analysis because the post uses that evidence to explain a broader interpretation: the scoring system, not athlete depth, is what changed the outcome.
> *Which pile:* a

**2.**
> *The post:*
> Carbon plates aren't the whole story. My times dropped 2% in the shoes and another 2% the following year in the same pair, when the only thing that changed was going from 35 to 50 miles a week.
> *Staff said / I said:*
> analysis | reaction
> *My call, and why:*
> I said reaction because it its mostly talking from personal experience, it reports what just happened to the writer and how it felt. But since he is introducing the data, and most likely willing to discuss it, it can be analysis
> *Which pile:* b

**3.**
> *The post:*
> Three of us ran the same session on the same day, different shoes, within 10 seconds of each other over 5 miles. I'm not saying shoes do nothing, but whatever they do was smaller than the noise between three people.
> *Staff said / I said:*
> analysis | reaction
> *My call, and why:*
>  I said reaction because reports what just happened to the writer and how it felt.
> *Which pile:* c

**4.**
> *The post:*
> Heart rate zones are astrology for runners.
> *Staff said / I said:*
> hot_take | analysis
> *My call, and why:*
> I  labelled it as analysis because makes the post is trying to make an argument backed by a specific, named comparisonm as described in the taxonomy.
> *Which pile:* c

**5.**
> *The post:*
> Track sessions are wasted on anyone running slower than 8 minute miles. You'd get more out of just running more.
> *Staff said / I said:*
> hot_take | analysis
> *My call, and why:*
> I labelled it as analysis, thinking the idea could be expanded, but it is not. Therefore, it is a hot take.
> *Which pile:* a

**6.**
> *The post:*
> First run back after eight weeks out. Two miles, slower than my warm-up used to be, and I don't care even slightly.
> *Staff said / I said:*
> reaction | hot_take
> *My call, and why:*
> I called it as a hot take, but it is definetely a reaction because it reports what just happened to the writer and
how it felt.
> *Which pile:* a

**7.**
> *The post:*
> Blew up at 20 with the pace band still in my hand like it was going to help. Rough one.
> *Staff said / I said:*
> reaction | analysis
> *My call, and why:*
> I called it as a analysis, but it is definetely a reaction because it reports what just happened to the writer and
how it felt. It is a bit amiguous because it is hard to understand what the writer is trying to convey.
> *Which pile:* b

**8.**
> *The post:*
> Someone handed my kid an orange slice at mile 22 and I have been crying on and off since.
> *Staff said / I said:*
> reaction | analysis
> *My call, and why:*
> I made a mistake in this label, this should have definitely been labeled as a reaction.
> *Which pile:* a

**9.**
> *The post:*
> Just realised the shoes I set every PB in this year are the ones I bought by accident in the wrong size.
> *Staff said / I said:*
> reaction | analysis
> *My call, and why:*
> I thought that if expanded, the argument could be that the wrong size shoes were helping him set PB more frequently. However, the idea is not further expanded, therefore is not substatial enough to be an analysis. Therefore, I do agree that reaction is a much better fit.
> *Which pile:* a



**What the pattern in my disagreements tells me:**

That for some, I did have a consistency problem applying the rules to loosely. However, some of the posts were just ambiguous, therefore hard to label them consistenly.

---

## The Improvement

**What I changed:** I first increased the epochs and the batches thinking this would increase the f1 scores for the labels but there was little to no change. Therefore I decided to increase the dataset instead. I added more entries for career advice.


**Which diagnosis pointed at it:**

The f1 scores. However, the most obvious diagnosis is that the label definition for analysis and question is too similar. I do not have a dataset wide enough to provide more clear examples of each for training, so I thought to merge them, but to keep the testing consistent across units I will be keeping them for now.

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  | Overall accuracy | >60% |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |


| 1.  | Overall accuracy | >60% | PASSED | The accuracy was greater than 60% for all seeds. |
| 2.  | Every label F1 | >60% | 0.194 | 0.194 | 0.194 | MISSED | The f1 scores are very low for all labels |
| 3.  | Precision on career guidance | >40% | 0.0 | 0.0 | 0.0 | MISSED | results indicate low precision for career guidance because of the small data set. |
| 4.  | Recall on questions | >60% | 0.0 | 0.0 | 0.0 | results indicate recall for question. |
| 5.  | Beats the baseline on accuracy |  yes | yes | yes | MET | 

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
