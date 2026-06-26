---
layout: section
---

# From data to insight

No model until you know what you're looking at.

---

## Explore the dataset

<v-clicks>

- Load customer records in Python with the usual data libraries
- Check shape, types, missing values, distributions
- Ask business questions: *What do churned customers look like?*

</v-clicks>

<v-click>

The output should be charts and summaries a stakeholder can read, not just numbers in a notebook.

</v-click>

---

## Raw data → model-ready data

<v-clicks>

- Clean gaps, outliers, and inconsistent values
- Encode categories, scale numbers, add features that might matter
- Hold back a test set so you're not grading the model on the same rows it learned from

</v-clicks>

<v-click>

Most of the real work is here. A decent pipeline on messy data usually beats a clever algorithm on raw input.

</v-click>
