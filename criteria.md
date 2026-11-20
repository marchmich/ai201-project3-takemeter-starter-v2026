# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---
## 1.

Every label except *project* has an F1 score of at least 0.65 on a held-out test set that contains at least 30 examples of each of those labels.

**Why this target:**

At 0.65, roughly 3 in 10 predictions for a label are wrong or missed. That is the most error I can tolerate before fixing mistakes by hand takes as long as labeling from scratch. Requiring 30 test examples per label keeps one lucky or unlucky batch from swinging the score. If a label misses 0.70, I will add training examples for it and check which labels it is confused with.

---

## 2.

The *project* label (posts asking to collaborate) must reach an F1 of at least 0.50 on the held-out set, and no more than 0.20 below the average F1 of the other three labels.

**Why this target:**

There are far fewer collaboration posts than other kinds, so this label will be harder to learn and its score will be noisy. I accept a lower floor, but not no floor: a model that never predicts *project* would defeat the purpose of having the label. If it falls below 0.50, I will collect more *project* examples before trusting the model.

---

## 3.

Predictions with a confidence of 90% or higher must be correct at least 90% of the time, and at least 50% of all predictions must reach that confidence level. Predictions below 60% confidence are sent to a person for review.

**Why this target:**

A confidence score is only useful if it can be trusted: if "90% sure" predictions are right only 75% of the time, I can't use confidence to decide what to accept automatically. The 50% coverage requirement stops the rule from being met in a useless way (for example, if only 5% of predictions ever reach 90%). Sending low-confidence predictions to a person catches the cases the model is least sure about. If calibration fails, I will recalibrate the scores or raise the review threshold.

---

## 4.

When a second person independently labels a random sample of 100 posts, we must agree on at least 80% of them, with a Cohen's kappa of at least 0.65.

**Why this target:**

If two people can't agree on the labels, the model has no consistent answer to learn, and no accuracy number can be trusted. With four labels, some agreement happens by luck, so kappa corrects for that. The sample must be random so it includes the harder *project* posts. If agreement falls below the target, I will rewrite the label definitions and relabel the disagreements before training. This also sets a ceiling: the model shouldn't be expected to beat human agreement.

---

## 5.

In the training data, the most common label may be no more than 3 times as frequent as the rarest label, and every label must have at least [50] training examples.

**Why this target:**

When one label dominates, the model learns to favor it, and overall accuracy looks good even if the rare labels are handled poorly (a model that always guessed the most common label would still score well). The minimum count matters most for *project*, the rarest label. If the ratio goes above 3x, I will collect more examples of the rare labels or resample before training.
---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
