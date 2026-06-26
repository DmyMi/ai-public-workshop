---
layout: section
---

# Build & measure

Train the model. Then check whether you trust it.

---

## Build the model step by step

<v-clicks>

- Pick an approach that fits the problem (classification for churn)
- Fit on the prepared features; we'll stop and explain what each step does
- Log what you tried: versions, parameters, results

</v-clicks>

<v-click>

The point is to understand what the model learns and what comes out the other end, not just run cells until something prints.

</v-click>

---

## How good is it?

<v-clicks>

- Accuracy isn't enough for churn; precision, recall, and ranking all matter
- Translate the metrics into business terms: who are we catching, who are we missing?
- If it's weak, you have options: more data, better features, a different model, or a clearer definition of success

</v-clicks>

<v-click>

If you can't evaluate it, you probably shouldn't ship it.

</v-click>
