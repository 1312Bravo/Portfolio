# Portfolio Workflow

## Purpose
Use this file for active collaboration rules while developing portfolio content across all projects.

The portfolio writing guide defines the voice, structure, and content style. This file defines how we work together during drafting and editing.

## Step-By-Step Drafting
- Do not apply new blog text, page structure, or major wording changes immediately unless the user explicitly asks for direct editing.
- Draft proposed `.qmd`, Markdown, or card text in the chat first.
- When drafting one substantial base part of a target `.qmd` file in chat, also save that proposed chunk under `notes/<target-qmd-file-name>/` so the discussion copy is not lost. Use small, clearly named files such as `part-01-opening.qmd`.
- Treat files under `notes/` as base snapshots. Do not update them for every small rephrase or local wording change unless the user explicitly asks; continue those edits in chat first.
- Work in small chunks so the user can decide what to keep, change, or skip.
- Treat proposed wording as discussion material, not final copy.
- After the user approves a chunk or asks for a specific edit, apply only that agreed change.

## Project Posts
- Use project landing pages to frame the project family and link to child posts.
- Keep detailed methods, diagnostics, formulas, and conclusions in child posts.
- When one post supports another, make the supporting post stand on its own and let related posts link back to it instead of repeating the full explanation.
- Separate exploratory explanation from final model or result interpretation when shaping analysis-heavy posts.

## Short Version Blocks
- For long or analysis-heavy posts, add a visible `Short version` block after the opening idea/question and before the detailed data or methodology sections.
- Use the reusable Quarto block pattern:

```markdown
::: {.post-summary}
#### Short version

<div class="summary-label">Mini section title</div>

...
:::
```

- Treat the short version as a compact mini-post, not as an abstract, conclusion repeat, or notebook dump.
- Before writing it, review the full post and identify the actual story arc: question, data scope, key transformation or method, main descriptive result, model or analysis result, limitation if important, and final meaning.
- Write it in connected prose, usually as a sequence of compact mini sections. Use bullets only if the post itself is primarily a list or guide.
- For longer blocks, use `<div class="summary-label">...</div>` labels inside the summary box, such as `<div class="summary-label">Normalized race time</div>` or `<div class="summary-label">Final model</div>`, followed by one or two short paragraphs.
- Choose mini titles that match the post's analytical steps, but make them reader-facing and simple. Prefer names of ideas, metrics, models, or results over generic labels like `Method` or `Analysis`.
- Keep the technical spine: preserve core metrics, formulas, model definitions, feature groups, and final signals when they are central to the post.
- Cut filler and repeated explanation. The short version should not explain every step twice; each sentence should either define the setup, name the method, report the result, or connect the result to the takeaway.
- The summary should compress what the full post really focuses on. Do not introduce results, claims, or caveats that the full post does not explain later.
- For existing posts that are missing this block, add it only after rereading the full post and making sure each summary sentence points to a section that expands it.

## Working Rhythm
- Prefer "draft here first, edit later" for writing-heavy work.
- Make assumptions explicit before proposing copy.
- Offer alternatives when structure or wording could go in multiple good directions.
- Keep changes reversible and easy to review.
