---
title: "Bayesian Probability, Statistics, And Project Ideas"
subtitle: "A conceptual note for a future Training Log predictor"
author: "Urh"
date: "July 2026"
output:
  html_document:
    toc: true
    toc_depth: 3
    number_sections: false
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(
  echo = TRUE,
  message = FALSE,
  warning = FALSE
)
```

### Idea

The goal of this note is to build a reusable foundation for a future Bayesian project.
The immediate motivation is the Training Log project: can a model use past training to say something useful about future readiness, future training, or race probability?

But the deeper question is more general:

> How should I update what I believe when new evidence arrives?

That is the heart of Bayes.

Most statistical models produce an estimate. Bayesian models produce a belief distribution. This difference matters. In endurance training, racing, health, finance, polling, forecasting, and many other real situations, the useful answer is rarely just one number. The useful answer is often a range, a probability, or a decision under uncertainty.

For example, instead of asking:

> What will my race time be?

we can ask:

> What is the probability that my race time is below a target, given what I currently know?

Instead of asking:

> Am I ready?

we can ask:

> How much evidence do I have that my current training state is above the level usually associated with being ready?

This small change is powerful. It moves the analysis from prediction as certainty to prediction as calibrated uncertainty.

### The point of Bayesian thinking

Bayesian statistics starts from a simple idea: uncertainty is part of the model, not an embarrassing leftover after the model is finished.

If a quantity is unknown, we describe our uncertainty about it with a probability distribution. The unknown quantity may be a race-day readiness score, a future weekly training volume, the probability of completing a hard workout, the average effect of more elevation training, or the hidden fatigue accumulated during a training block.

In classical statistics, probability is often interpreted as long-run frequency. If we repeat an experiment many times, the probability of an event is its limiting proportion. That view is useful, especially for randomized experiments and repeated sampling.

In Bayesian statistics, probability can also represent degree of belief under uncertainty. This does not mean "random opinion." It means a coherent mathematical description of what is known before and after seeing data.

The Bayesian workflow has three main pieces:

1. A **prior** distribution, which represents what we believe before seeing the current data.
2. A **likelihood**, which describes how plausible the observed data are under different parameter values.
3. A **posterior** distribution, which represents updated belief after combining prior information and data.

In symbols:

$$
p(\theta \mid y) =
\frac{p(y \mid \theta)p(\theta)}{p(y)}
$$

where:

- $\theta$ is an unknown parameter or hidden state.
- $y$ is the observed data.
- $p(\theta)$ is the prior.
- $p(y \mid \theta)$ is the likelihood.
- $p(\theta \mid y)$ is the posterior.
- $p(y)$ is the evidence, also called the marginal likelihood.

The same formula can be written in its most useful conceptual form:

$$
\text{posterior} \propto \text{likelihood} \times \text{prior}
$$

This is the whole machine. We begin with a belief, observe data, and update the belief.

### A simple example: probability of completing a planned workout

Suppose I want to estimate the probability $\theta$ that I complete a planned quality workout as intended. Each workout is either completed or not completed.

Let:

$$
y_i =
\begin{cases}
1, & \text{if workout } i \text{ was completed as planned} \\
0, & \text{otherwise}
\end{cases}
$$

Assume:

$$
y_i \sim \text{Bernoulli}(\theta)
$$

If there are $n$ planned workouts and $s$ successful completions, then:

$$
s \sim \text{Binomial}(n, \theta)
$$

Before seeing the data, we place a prior on $\theta$:

$$
\theta \sim \text{Beta}(\alpha, \beta)
$$

The Beta distribution is useful here because it lives between 0 and 1, so it is natural for probabilities. It is also conjugate to the Binomial likelihood, which means the posterior has a simple closed form:

$$
\theta \mid s,n \sim \text{Beta}(\alpha + s, \beta + n - s)
$$

If we use a weak prior, such as:

$$
\theta \sim \text{Beta}(2, 2)
$$

and then observe $s = 8$ successful workouts out of $n = 10$, the posterior is:

$$
\theta \mid y \sim \text{Beta}(10, 4)
$$

The key point is not only that the average completion probability is high. The key point is that we get a full distribution over plausible values of $\theta$.

That lets us ask questions like:

$$
P(\theta > 0.75 \mid y)
$$

In words:

> Given the observed workouts, what is the probability that my true workout completion probability is above 75%?

This is the Bayesian style of question. It is direct, practical, and decision-oriented.

### Prior, likelihood, posterior

The prior is often misunderstood. A prior is not a trick for forcing the model to say what we want. A good prior is a disciplined way to state what values are plausible before looking at the current data.

For a Training Log project, a prior might express knowledge like:

- Weekly running distance cannot realistically jump from 40 km to 180 km without being unusual.
- A high-intensity session after several hard days is less likely to go well.
- Race readiness changes gradually, not randomly from one extreme to another overnight.
- Two weeks of training should not completely overwrite years of background fitness.

The likelihood is the data-generating story. It answers:

> If the hidden quantity had this value, how likely would the observed data be?

For example:

- If readiness is high, strong workouts are more plausible.
- If fatigue is high, failed or modified workouts are more plausible.
- If the typical weekly load is 70 km, then a 72 km week is more plausible than a 140 km week.

The posterior combines these pieces. It is the model's updated uncertainty after observing the data.

This is why Bayesian modeling is so useful in personal analytics. Personal data is usually messy, small, biased, and uneven. A Bayesian model can still be honest because it does not need to pretend that the data knows more than it knows.

### Posterior prediction

Estimating parameters is useful, but prediction is usually the part we care about.

In Bayesian statistics, prediction uses the posterior predictive distribution:

$$
p(\tilde{y} \mid y) =
\int p(\tilde{y} \mid \theta) p(\theta \mid y) d\theta
$$

where:

- $y$ is the observed data.
- $\tilde{y}$ is a future or unobserved outcome.
- $\theta$ is the uncertain parameter.

This equation says:

> To predict the future, average over all plausible parameter values, weighted by how plausible they are after seeing the data.

This is important. A non-Bayesian model may estimate one best parameter value and then predict from that. A Bayesian model carries parameter uncertainty into the prediction.

For training, this could mean:

$$
p(\text{next week's distance} \mid \text{training history})
$$

or:

$$
p(\text{race time} < T \mid \text{current training state})
$$

or:

$$
p(\text{complete next hard workout} = 1 \mid \text{recent load, fatigue, workout type})
$$

This is one of the main reasons Bayes is attractive for a dashboard. The dashboard does not need to say "the answer is 83." It can say:

> The most likely value is around 83, but values between 76 and 89 are still plausible.

That is more honest and more useful.

### Credible intervals and probability statements

Bayesian intervals are called credible intervals. A 90% credible interval for $\theta$ means:

> Given the model and the observed data, there is a 90% posterior probability that $\theta$ lies inside this interval.

That interpretation is direct. It is usually what people wish a confidence interval meant.

For example, a dashboard could say:

> Estimated readiness: 71, with a 90% credible interval from 63 to 78.

or:

> Probability of being above the target readiness threshold: 82%.

These outputs are decision-friendly. They translate uncertainty into the kind of language that can guide planning:

- Should I increase training load?
- Should I maintain?
- Should I recover?
- Is a race goal realistic yet?
- How much uncertainty is still left?

### Why Bayes fits training data

Training data is not clean experimental data. It has all the usual personal-data problems:

- The sample size is limited.
- The data-generating process changes over time.
- Some variables are measured precisely, like distance and duration.
- Some variables are rough proxies, like effort category or perceived fatigue.
- Important variables are missing, like sleep quality, life stress, heat, nutrition, and motivation.
- Observations are not independent, because yesterday's workout affects today's workout.

Bayesian modeling does not magically solve these problems. But it gives us a framework for being explicit about them.

For example, if readiness changes gradually, we can encode that:

$$
R_t \sim \text{Normal}(R_{t-1} + \delta_t, \sigma_R)
$$

where:

- $R_t$ is hidden readiness at time $t$.
- $\delta_t$ is the expected change from training stimulus and recovery.
- $\sigma_R$ controls how much unexplained variation is allowed.

Then observed workouts give noisy evidence about readiness:

$$
y_t \sim \text{Normal}(\mu_t, \sigma_y)
$$

with:

$$
\mu_t = \alpha + \beta R_t
$$

This is a state-space idea. The model separates the hidden state from the noisy observations. That is exactly how training often feels: the real thing we care about is not directly observed, but every workout gives partial evidence.

### The difference between prediction and decision

A prediction tells us what might happen. A decision rule tells us what to do.

Bayesian analysis becomes especially useful when we define events that matter. For example:

$$
P(R_t > R_{\text{goal}} \mid y_{1:t})
$$

This means:

> The probability that current readiness is above the goal threshold, given training data observed so far.

Or:

$$
P(\tilde{T}_{race} < T_{\text{target}} \mid y_{1:t})
$$

This means:

> The probability that future race time is below the target time, given current evidence.

This is more useful than a point estimate because it connects directly to decisions. If the probability is 15%, the conclusion is different from 85%, even if the expected value is similar.

### Partial pooling and hierarchical models

One of the most important Bayesian ideas for portfolio work is hierarchical modeling.

Suppose we want to estimate workout success probability by workout type:

- Easy run
- Long run
- Tempo
- Intervals
- Hill session
- Race

If we estimate each workout type separately, some groups may have very little data. A workout type with only two examples can produce an unstable estimate.

Hierarchical Bayes solves this through partial pooling.

Let:

$$
y_{ij} \sim \text{Bernoulli}(\theta_j)
$$

where:

- $y_{ij}$ is outcome $i$ in workout type $j$.
- $\theta_j$ is the success probability for workout type $j$.

Instead of giving each $\theta_j$ a completely independent prior, we assume:

$$
\text{logit}(\theta_j) \sim \text{Normal}(\mu, \tau)
$$

and:

$$
\mu \sim \text{Normal}(0, 2)
$$

$$
\tau \sim \text{HalfNormal}(1)
$$

The workout types now learn from each other. A group with lots of data mostly follows its own evidence. A group with little data is pulled toward the overall pattern.

This is partial pooling.

For the Training Log project, this could be useful for:

- Estimating different workout types.
- Comparing training blocks.
- Comparing weeks with different fatigue levels.
- Estimating race readiness across distances.
- Learning from sparse race outcomes without overreacting to one result.

Partial pooling is often one of the cleanest ways to show why Bayesian modeling is not only philosophical. It solves a real modeling problem: how to estimate group-level effects without pretending that every group has equally strong evidence.

### Model checking

A Bayesian model should not only produce elegant posterior distributions. It should be checked.

The most important check is posterior predictive checking. We simulate data from the fitted model and compare simulated data with the real data:

$$
\tilde{y}^{(s)} \sim p(\tilde{y} \mid \theta^{(s)})
$$

where $\theta^{(s)}$ is one posterior draw.

Then we ask:

> Does the model generate fake data that looks like the real data in the ways that matter?

For training data, this could mean checking whether the model reproduces:

- Typical weekly distance.
- Variation in weekly load.
- Frequency of rest days.
- Number of hard sessions per week.
- Distribution of long-run distances.
- Load spikes.
- Seasonal training blocks.

If the simulated data is too smooth, the model is missing volatility. If it predicts too many extreme weeks, the model is too noisy. If it cannot reproduce recovery weeks, it is missing structure.

The point is not to make the model perfect. The point is to make its limitations visible.

### Bayesian project ideas

The following ideas all use the same Bayesian foundation, but they ask different practical questions.

### Option 1: Bayesian Training Readiness Dashboard

This is probably the strongest idea for the Training Log project.

The goal would be to estimate a hidden readiness state over time. Readiness is not directly observed, but training gives evidence about it.

Possible observed inputs:

- Weekly distance
- Weekly duration
- Elevation gain
- Long-run duration
- Number of hard sessions
- Easy/hard training balance
- Training consistency
- Recent load ramp
- Recovery days

Possible observed outcomes:

- Workout completion
- Pace or speed for comparable workouts
- Race results
- Subjective fatigue, if available
- Training interruptions

A simple latent model could be:

$$
R_t \sim \text{Normal}(R_{t-1} + \beta^\top x_t, \sigma_R)
$$

where:

- $R_t$ is readiness in week $t$.
- $x_t$ contains training features.
- $\beta$ measures how each feature changes readiness.
- $\sigma_R$ captures unexplained week-to-week movement.

An observed performance signal could be:

$$
y_t \sim \text{Normal}(\alpha + R_t, \sigma_y)
$$

The dashboard could show:

- Posterior readiness over time.
- 50%, 80%, and 95% credible bands.
- Probability that readiness is above a chosen target.
- Weeks where the model is uncertain.
- Training variables that most changed the readiness estimate.

The story would be:

> My training log is not only a diary. It is evidence that updates a belief about current readiness.

This project would fit naturally with the existing Training Log work because it turns descriptive training metrics into an uncertainty-aware model.

### Option 2: Bayesian Race Goal Probability

This idea asks:

> Given current training, what is the probability of achieving a specific race goal?

The target could be:

- Finish a race.
- Finish under a certain time.
- Be ready for a certain distance.
- Reach a target performance index.

Let $G$ be the event that the goal is achieved:

$$
G =
\begin{cases}
1, & \text{goal achieved} \\
0, & \text{goal not achieved}
\end{cases}
$$

A simple model could be:

$$
G_i \sim \text{Bernoulli}(p_i)
$$

with:

$$
\text{logit}(p_i) = \alpha + \beta^\top x_i
$$

where $x_i$ contains features from the training block before race $i$.

The output is:

$$
P(G_{\text{future}} = 1 \mid \text{current training})
$$

The project could become a race-readiness page:

- Define a race goal.
- Summarize recent training.
- Estimate probability of success.
- Show which features increase or decrease the probability.
- Simulate future training scenarios.

This is very appealing because the result is easy to understand. The model does not say "you will succeed" or "you will fail." It says how much evidence currently supports the goal.

### Option 3: Bayesian Future Training Load Forecast

This idea predicts future training itself.

The target could be:

- Next week's distance.
- Next week's duration.
- Next month's total load.
- Number of hard sessions in the next block.
- Probability of a recovery week.

For weekly distance $D_t$:

$$
D_t \sim \text{Normal}(\mu_t, \sigma)
$$

with:

$$
\mu_t = \alpha + \phi D_{t-1} + \beta^\top x_t
$$

This is an autoregressive Bayesian regression. It says the next week depends partly on the previous week and partly on other features.

The posterior predictive distribution gives:

$$
p(D_{t+1} \mid D_{1:t}, x_{1:t})
$$

The dashboard could show:

- Expected next-week training load.
- Predictive interval.
- Probability of exceeding a safe ramp threshold.
- Comparison between planned and likely training.

This idea is useful, but it needs careful framing. Since training is partly chosen, the model is not predicting nature in the same way weather forecasting does. It is predicting the continuation of observed behavior.

The stronger framing is:

> If current patterns continue, what range of training load should I expect, and when does that pattern drift away from the intended plan?

### Option 4: Bayesian Overload Or Risk Signal

This idea estimates the probability that a week is an overload week.

The model could define overload not as injury, but as a measurable training state:

$$
O_t =
\begin{cases}
1, & \text{week } t \text{ exceeds a load or intensity threshold} \\
0, & \text{otherwise}
\end{cases}
$$

Then:

$$
O_t \sim \text{Bernoulli}(p_t)
$$

with:

$$
\text{logit}(p_t) =
\alpha +
\beta_1 \text{Ramp}_t +
\beta_2 \text{IntensityShare}_t +
\beta_3 \text{LongRunShare}_t +
\beta_4 \text{RecoveryDeficit}_t
$$

The model would produce:

$$
P(O_{t+1}=1 \mid \text{recent training})
$$

This could be shown as:

- Low, medium, or high overload probability.
- Main contributors to current risk.
- Comparison with historical training blocks.
- Simulation of alternative next weeks.

Important limitation: without true injury, illness, soreness, or fatigue labels, this should not be called an injury prediction model. It is better to call it an overload signal or training stress probability.

That honesty actually makes the project stronger.

### Option 5: Bayesian Workout Completion Predictor

This project asks:

> What is the probability that a planned workout will be completed as intended?

This needs planned-versus-actual data. If that exists, it can be modeled directly. If not, one could construct a weaker proxy, but the story is cleaner with explicit planning data.

Possible model:

$$
y_i \sim \text{Bernoulli}(p_i)
$$

where $y_i = 1$ means workout $i$ was completed as planned.

Then:

$$
\text{logit}(p_i) =
\alpha +
\beta_1 \text{WorkoutDifficulty}_i +
\beta_2 \text{RecentLoad}_i +
\beta_3 \text{DaysSinceRest}_i +
\beta_4 \text{WorkoutType}_i
$$

This could become a very practical dashboard:

- Select a planned workout.
- Estimate completion probability.
- Show how the probability changes after adding rest.
- Compare workout types.
- Detect when the plan is becoming unrealistic.

This project would be especially interesting if combined with decision-making:

> If completion probability is low, should the workout be modified, moved, or replaced?

### Option 6: Bayesian Personal Calibration Lab

This is a more unusual project.

The idea is to make personal probability forecasts and evaluate them over time.

Examples:

- I think there is a 70% probability I run more than 70 km next week.
- I think there is a 60% probability I complete two hard workouts.
- I think there is an 80% probability I sleep at least 7 hours on average.
- I think there is a 50% probability I race within a target pace range.

Then, after outcomes are observed, we evaluate calibration.

If all events assigned 70% probability happen roughly 70% of the time, the forecasts are calibrated.

A Bayesian version can model the forecaster's calibration curve:

$$
y_i \sim \text{Bernoulli}(p_i^*)
$$

where $p_i$ is the stated probability and $p_i^*$ is the true empirical probability implied by calibration.

This project is less directly about training performance, but it is very original. It turns Bayes into a personal learning system:

> Am I good at knowing how uncertain I am?

That is a beautiful question.

### Option 7: Bayesian Ranking Or Rating System

This idea is broader and can be applied to races, routes, workouts, shoes, books, movies, restaurants, or anything with ratings.

The problem with simple averages is that they ignore uncertainty. A route rated 5.0 after two runs should not automatically outrank a route rated 4.7 after fifty runs.

Bayesian ratings solve this by shrinking small-sample ratings toward the overall average.

For item $j$:

$$
y_{ij} \sim \text{Normal}(\theta_j, \sigma)
$$

and:

$$
\theta_j \sim \text{Normal}(\mu, \tau)
$$

The posterior for $\theta_j$ balances:

- The item's own data.
- The overall population average.
- The amount of evidence for that item.

Applied to training, this could rank:

- Routes by enjoyment or performance.
- Workout types by success probability.
- Shoes by perceived quality or injury-free distance.
- Training blocks by race-readiness outcome.

This is a useful option if the Training Log data includes subjective ratings.

### Recommended project direction

The best next project is probably:

> Bayesian Training Readiness Dashboard

The reason is that it naturally combines personal data, endurance sport, mathematical modeling, and uncertainty. It also continues the existing Training Log story instead of starting from zero.

The initial version should be simple:

1. Aggregate training by week.
2. Define a small number of features:
   - total distance
   - total duration
   - elevation gain
   - long-run distance
   - hard-session count
   - easy/hard balance
   - recent ramp
3. Define an observable outcome or proxy:
   - weekly performance score
   - workout completion
   - race readiness label
   - target-distance readiness
4. Fit a Bayesian model.
5. Plot posterior readiness over time.
6. Add a probability statement:

$$
P(R_t > R_{\text{target}} \mid y_{1:t})
$$

This gives the project a clear statistical spine.

### Possible dashboard sections

A dashboard could have the following sections.

**Current state**

- Posterior readiness estimate.
- Credible interval.
- Probability of being above target.

**Training evidence**

- Weekly distance and duration.
- Elevation gain.
- Long-run exposure.
- Hard/easy balance.
- Recent ramp.

**Goal probability**

- Select a race distance or target.
- Show probability of readiness.
- Show uncertainty interval.

**Scenario simulator**

- What if next week is a recovery week?
- What if the next four weeks increase volume gradually?
- What if hard-session count increases?
- What if long-run exposure improves?

**Model checks**

- Posterior predictive checks.
- Historical predictions versus observed outcomes.
- Calibration of probability statements.

### Minimal mathematical model for a first version

For a first version, we can avoid making the model too ambitious.

Let $t$ index weeks. Let $x_t$ be a vector of standardized training features:

$$
x_t =
\begin{bmatrix}
\text{distance}_t \\
\text{duration}_t \\
\text{elevation}_t \\
\text{long run}_t \\
\text{hard sessions}_t \\
\text{consistency}_t \\
\text{ramp}_t
\end{bmatrix}
$$

Define latent readiness:

$$
R_t \sim \text{Normal}(\alpha + \beta^\top x_t, \sigma_R)
$$

If there is an observed readiness proxy $z_t$, such as a performance score:

$$
z_t \sim \text{Normal}(R_t, \sigma_z)
$$

If the outcome is binary, such as whether a target was achieved:

$$
y_t \sim \text{Bernoulli}(p_t)
$$

with:

$$
\text{logit}(p_t) = R_t
$$

Then:

$$
P(y_t = 1 \mid x_t)
$$

is the estimated probability of being ready, successful, or above threshold.

This first model is not perfect, but it is understandable. It gives a base that can later be extended into:

- A time-dependent state-space model.
- A hierarchical model by workout type.
- A model with explicit fatigue and fitness states.
- A race-specific model with course and weather inputs.

### More advanced model: fitness and fatigue

A more realistic endurance model can separate fitness from fatigue.

Let:

- $F_t$ be latent fitness.
- $A_t$ be latent fatigue.
- $R_t$ be readiness.

Then:

$$
F_t = \rho_F F_{t-1} + \beta_F \text{Load}_t + \epsilon^F_t
$$

$$
A_t = \rho_A A_{t-1} + \beta_A \text{Load}_t + \epsilon^A_t
$$

and:

$$
R_t = F_t - A_t
$$

The idea is simple. Training increases fitness, but it also creates fatigue. Fitness usually decays slowly. Fatigue usually changes faster. Race readiness is not just high fitness. It is high fitness with manageable fatigue.

This is a very natural Bayesian model because $F_t$ and $A_t$ are hidden. We never observe them directly. We infer them from training and performance signals.

Observed performance could be:

$$
z_t \sim \text{Normal}(\alpha + R_t, \sigma_z)
$$

This would make a strong second version of the dashboard.

### What makes this Bayesian project portfolio-worthy

This project would be strong because the Bayesian method is not decorative. It is needed.

Training decisions are uncertain. Race outcomes are uncertain. Readiness is hidden. Historical data is limited. Personal data is noisy. The model should not hide that. It should show it.

A good final project post could say:

> I did not build this model to know the future. I built it to measure how uncertain the future is, and to update that uncertainty as training changes.

That sentence is basically the project.

### Possible final titles

- "Bayesian Training Readiness"
- "A Bayesian Dashboard For Race Readiness"
- "Updating Belief From A Training Log"
- "What My Training Log Believes About My Race Readiness"
- "From Training History To Race Probability"
- "A Probabilistic View Of Endurance Readiness"

### Suggested next step

The next concrete step is to inspect the existing Training Log data and decide what the first model can actually observe.

The key question is:

> What is the outcome variable?

Possible outcomes:

- A race result.
- A workout-completion label.
- A performance score.
- A weekly readiness proxy.
- A goal-readiness threshold.

Once the outcome is defined, the Bayesian model becomes much easier to design. Without an outcome, the project can still estimate latent training state, but validation becomes harder.

The best first implementation would probably be:

> Weekly Bayesian readiness score using training features, followed by a target-readiness probability.

That is small enough to build, but rich enough to become a serious portfolio post.

