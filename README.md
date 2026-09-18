# OpenWorkout-Engine
> This project is founded on the core belief that **everyone has the right to train properly.**

The system takes user-specific information and needs as input to automatically generate a fully personalized workout program.

---

## Core Logic & Rules

Before building the actual routine, the generation engine adheres to a strict set of physiological and structural rules:

* **Muscle Regions:** For advanced lifters, different regions of the same muscle are treated as distinct targets by the algorithm, meaning they are always trained within the same workout (with the exception of the `Full Body A/B` split).
* **Recovery Window:** Each muscle cannot be trained twice within a **48-hour** window.
* **Exercise Selection:** Exactly **one exercise** is picked for each muscle or muscle region.
* **Frequency:** Each exercise must be repeated at least **2 times per week** (unless the user works out only once a week or follows the `Full Body A/B` routine).
* **Glutes & Adductors Handling:** 
  * If glutes or adductors are in the top 3 priority muscles, **both** receive an isolation movement.
  * Otherwise, both are trained through a squat or hinge pattern, and the compound movement is placed where the lowest-priority muscle between the two ranks.
* **Volume Baseline:** The baseline number of sets for each exercise starts at **one**.

---

## How the Algorithm Works

The core algorithm follows a straightforward iterative process based on the rules defined above:

1. **Priority Filling:** For each muscle (in order of priority), the algorithm fills the highest available slot across the workouts, aiming to maximize frequency.
2. **Cycle Iteration:** This cycle repeats until the entire muscle list is processed. When multiple slots allow the same frequency, preference is given to the higher slot.
3. **Duration Adjustment (Too Long):** If the generated workouts exceed the user's requested time limit, the algorithm starts from the bottom of each workout and removes one instance of an exercise performed 3 times a week.
4. **Duration Adjustment (Too Short):** If the workouts are too short to meet the time requirement, additional sets are added sequentially from top to bottom until the duration requirement is satisfied.

---

## Special Case: Full Body A/B

The `Full Body A/B` template is a special structure. Even if a user trains 3 times a week, there are only **two distinct workouts** that alternate in a rolling cycle:
* **Week 1:** `A -> B -> A`
* **Week 2:** `B -> A -> B`

---

## User Inputs Required

To generate a personalized program, the system requires the following inputs from the user:
* **Experience Level:** Beginner or Advanced.
* **Training Days:** Days available per week.
* **Workout Duration:** Desired length of each session.
* **Available Equipment:** List of tools and machinery at hand.
* **Muscle Priorities:** A ranked list of priority muscles vs. non-priority muscles.
