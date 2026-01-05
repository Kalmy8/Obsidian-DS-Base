---
type: note
status: done
tags: [tech/ml/recsys]
sources:
-
authors:
-
- "[[Recommender Systems Course]]"
---
## A/B Testing for Recommender Systems

In recommender systems, offline metrics (like NDCG, Precision@K, MAP) are essential for iterating on models quickly. However, they don't always correlate with real user behavior and business goals. An A/B test is the gold standard for measuring the true impact of a new model or feature in a live production environment.

The core idea is to randomly split users into two or more groups:
-   **Group A (Control):** Sees the existing, old version of the recommender system.
-   **Group B (Treatment):** Sees the new model or feature you want to test.

By comparing the key business metrics between these groups, you can determine with statistical confidence whether your change had a positive, negative, or no effect.

### The A/B Testing Process: A Practical Workflow

This is a typical full-cycle workflow you would follow in the role described.

1.  **Formulate a Hypothesis:** Start with a clear, measurable statement.
    *   *Bad:* "The new model is better."
    *   *Good:* "The new diversity-aware recommendation model (Treatment) will increase the average listening time per user (ATS) by at least 2% compared to the current model (Control)."

2.  **Choose Key Metrics:** Based on your job description, these are paramount.
    *   **Primary Metrics (Goals):** These determine the success or failure of the test.
        *   **ATS (Average Time Spent):** For audio content, this is a proxy for user engagement and satisfaction. How long do users listen in a session or per day? A higher ATS for the treatment group is a strong positive signal.
        *   **User Retention:** The ultimate metric. Does the new model make users come back more often? Measured as Day-1, Day-7, Day-30 retention. (e.g., "What percentage of users in Group B returned to the app 7 days after their first session, compared to Group A?").
    *   **Secondary/Guardrail Metrics (Checks):** Things you don't want to harm.
        *   **CTR (Click-Through Rate):** Are users clicking on the recommendations?
        *   **Infrastructure Cost:** Does the new model cost significantly more to run?
        *   **Latency:** Does the new model slow down the user experience?

3.  **Calculate Sample Size (Deeper Dive):** Before starting, you must determine how many users you need per group. Running a test with too few users means you won't be able to detect real effects (an "underpowered" test). This is a statistical calculation that requires four inputs:
    *   **Baseline Conversion Rate (BCR) or Mean:** The current, pre-test value of your primary metric. For example, your current Day-7 Retention is 12%. You need this to estimate the variance of the metric.
    *   **Minimum Detectable Effect (MDE):** The smallest change you actually care about detecting. This is a business decision, not a statistical one. A PM might say, "We only want to ship this if it improves ATS by at least 1%." A smaller MDE requires a much larger sample size.
    *   **Statistical Power (1 - β):** The probability of detecting an effect *if it is real*. This is typically set to 80%. It means you have an 80% chance of correctly concluding there is a difference if the true lift is equal to your MDE.
    *   **Significance Level (α):** The probability of detecting an effect *that is not real* (a false positive). This is usually set at 5% (corresponding to a p-value of 0.05).
    
    You would use these four values in an online sample size calculator to determine the required `N` for each group.

4.  **Run the Experiment:** Randomly assign users to a group and expose them to the corresponding experience for a fixed period (e.g., 2 weeks). It's crucial that the assignment is random and consistent for each user.

5.  **Analyze Results:** After the test concludes, compare the metrics between the groups.
    *   Calculate the difference in means or proportions.
    *   Perform a statistical test (e.g., a t-test for means, chi-squared test for proportions) to get a **p-value**.
    *   **Interpreting the p-value:** If the p-value is below a certain threshold (usually 0.05), you can reject the "null hypothesis" (that there is no difference) and conclude that your change had a statistically significant effect.

6.  **Make a Business Decision:**
    *   **Positive Significant Result:** Roll out the new model to 100% of users.
    *   **Negative Significant Result:** Discard the new model and analyze what went wrong.
    *   **No Significant Result:** Keep the old model (or roll out the new one if it has other benefits, like lower cost).

### Common Interview Questions & How to Answer Them

**Q1: You've built a new recommendation model that improved offline NDCG by 10%. What are your next steps?**
**A:** "That's a great offline signal, but it doesn't guarantee a better user experience. My next step would be to design an online A/B test to validate the model's real-world impact. I would formulate a hypothesis, for example, that the new model will improve user retention. The new model would be the 'treatment' and the current production model the 'control'. I'd focus on primary metrics like ATS and D-7 retention, while also monitoring guardrail metrics like latency and CTR. Based on the statistically significant results of the test, we would then make a data-driven decision on whether to roll it out."

**Q2: In our A/B test for a new music recommender, we saw a 5% lift in CTR, but a 3% drop in Average Time Spent (ATS). What's your interpretation?**
**A:** "This is a classic trade-off scenario that requires deeper investigation. A higher CTR could mean the new model is better at generating 'clickbait'—tracks with appealing titles or artists that users click but then quickly abandon. The drop in ATS, which is likely a better proxy for true engagement, suggests that users are less satisfied with the content *after* the click. My hypothesis would be that the old model was better at recommending tracks that lead to longer, more engaging listening sessions. I would analyze the properties of the recommended tracks in both versions (e.g., popularity, diversity, novelty) and conduct follow-up tests to try and build a model that combines the high CTR of the new model with the high ATS of the old one."

**Q3: What is a p-value, and how would you explain it to a non-technical product manager?**
**A:** "A p-value helps us decide if the results of our experiment are real or just due to random chance. Imagine we see that the new model (Group B) has a 1% higher retention rate. The p-value answers the question: 'If our new model actually had *no effect at all*, what's the probability we'd see a difference of 1% or more just by pure luck?' If that probability (the p-value) is very low—say, under 5%—we can be confident that our new model really did cause the change and the result isn't just a random fluke."

**Q4: What are some potential pitfalls or biases you need to be aware of when running A/B tests?**
**A:** "Several things can invalidate a test. A big one is the **novelty effect**, where users initially engage more with a new feature simply because it's new, not because it's better; the effect fades over time. Another is **seasonality**, where an external event (like a holiday) affects user behavior and can be mistaken for an effect of your change. It's also critical to avoid **peeking** at the results before the test has run its course, as this can lead to false conclusions. Finally, ensuring your user split is truly random and that you run the test long enough to get a sufficient sample size is crucial for reliable results."

**Q5: How do you handle multiple experiments running at the same time on the same page? What is "salting"?**
**A:** "Running multiple tests concurrently can cause interference. For example, a user in the treatment group for a new UI *and* the treatment group for a new algorithm might behave differently than expected. The best practice is to ensure experiments are **orthogonal**. This is often achieved by **salting**. Before hashing a `user_id` to assign it to a group, you concatenate the ID with an experiment-specific string or 'salt' (e.g., `hash(user_id + "new_recs_algorithm_exp_2024_q4")`). This ensures that a user's assignment in one experiment is completely independent of their assignment in another. It's like having multiple separate layers of experiments; a user's journey through one layer doesn't predict their path through another."

**Q6: We need to test three different recommendation algorithms this quarter. What is the problem with running three separate A/B tests and checking for a p-value < 0.05 each time?**
**A:** "This introduces the **multiple comparisons problem**. If your significance level (alpha) is 5%, you accept a 5% risk of a false positive for any single test. If you run three independent tests, the probability of getting *at least one* false positive balloons to about 14% (`1 - 0.95^3`). You're more likely to be misled by randomness. To solve this, you need to control the 'family-wise error rate'. The simplest method is the **Bonferroni correction**, where you divide your alpha by the number of tests. So, for three tests, a result is only significant if its p-value is less than `0.05 / 3 = 0.0167`. This makes your significance criteria stricter to account for the multiple chances you're giving yourself to find a fluke."

**Q7: Your test results for a new model are flat—the p-value is 0.4. But the product manager insists they've heard good anecdotal feedback and wants to launch it. How do you handle this?**
**A:** "This is a common situation where data needs to be balanced with qualitative insights. My first step would be to present the results clearly: 'The experiment shows no statistically significant lift in our primary metrics, meaning we can't be confident that this new model is better than the old one.' However, a flat result doesn't mean it's worse. I would then dig deeper. I'd perform a **segmented analysis** to see if the model had a strong positive impact on a specific user group that was washed out in the average (e.g., new users, users in a specific country, fans of a niche genre). If a key segment shows strong improvement and no other segment is harmed, we could consider a partial or targeted rollout. If the analysis shows nothing, the final decision is about business risk. If the new model is cheaper to run or easier to maintain, launching it might be acceptable. If not, the data-driven decision is to stick with the current model and iterate on a new hypothesis."

