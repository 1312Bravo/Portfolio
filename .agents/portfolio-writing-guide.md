# Portfolio Writing Guide

## Purpose
This guide explains how the Portfolio project is structured and how writing should sound across homepage text, project landing pages, and detailed project posts.

Use it when drafting, editing, restructuring, or reviewing portfolio content.

## Project Structure
- `index.qmd`: homepage and high-level personal introduction.
- `about.qmd`: optional about page.
- `projects/<project>.qmd`: project landing page with motivation, context, GitHub link, and post cards.
- `projects/<project>/<post>.qmd`: detailed project article or analysis post.
- `projects/<project>/saved_files/<post-name>/`: figures used inside a specific post, where `<post-name>` matches the `.qmd` file stem.
- `projects/<project>/saved_files/`: shared figures used across multiple posts in the same project.
- `styles.css`: reusable visual components such as cards, link boxes, profile image, embedded sheets, and click-zoom images.
- `other/`: static personal assets such as profile photo and CV.
- `_quarto.yml`: site configuration, navigation, theme, and render options.
- `_site/`: generated website output. Do not edit directly.

## Content Levels
### Homepage
The homepage should answer:

- Who is this person?
- What kind of work appears here?
- What projects are featured?
- Why should a reader care?

Homepage structure:

1. YAML title and subtitle.
2. Optional HTML dependency block if needed.
3. Profile photo.
4. Personal introduction.
5. Explanation of project philosophy.
6. Social/CV icons.
7. Featured project cards.

Keep the homepage broad, warm, and curiosity-driven. Do not put detailed methodology there.

### Project Landing Pages
Project landing pages should explain the project family, not one specific analysis.

They should answer:

- What is this project about?
- Why does it matter personally or analytically?
- What kind of posts live under it?
- Where is the source code?
- Which posts should the reader open next?

Project landing page structure:

1. YAML title.
2. Optional HTML dependency block.
3. 2-5 paragraphs of project context and motivation.
4. GitHub repository link box.
5. Blog cards for child posts.

Keep detailed methods, formulas, and diagnostics in child posts.

### Detailed Posts
Detailed posts should be self-contained. A reader should understand the question, data, method, and conclusion without opening the notebook.

Do not simply copy notebook sections, outputs, or every intermediate result into the post. Use the notebook as the analytical source of truth, then turn the useful parts into a readable story: select the numbers that move the argument forward, explain why they matter, and omit details that are only needed for exploration or debugging.

Typical structure:

1. Title.
2. Optional HTML dependency block.
3. `### Idea` or equivalent.
4. Definition of the problem or question.
5. Data source and preparation.
6. Methodology.
7. Visual evidence.
8. Diagnostics or assumptions.
9. Interpretation.
10. Conclusion.
11. GitHub/code link box.

Small posts can be shorter, but analysis-heavy posts should preserve this flow.

### Short Version Summary Boxes
Long or analysis-heavy posts should include a `Short version` box after the opening idea/question and before the detailed data or methodology sections.

Use this pattern:

```markdown
::: {.post-summary}
#### Short version

<div class="summary-label">Mini section title</div>

...
:::
```

The short version should read like a small version of the post. It should give the reader the main question, the data or evidence used, the key method or transformation, the central result, and the final interpretation. A reader who knows statistics should understand the analytical route without reading the whole post, while a non-technical reader should still understand the main idea and conclusion.

Write the short version in connected prose, not as a checklist. For long posts, structure it as a small article inside the summary box: a short opening paragraph, then compact mini sections introduced with summary labels. Use labels like `<div class="summary-label">Normalized race time</div>`, `<div class="summary-label">Performance group descriptive analysis</div>`, or `<div class="summary-label">Final model</div>`, followed by one or two short paragraphs.

Use summary labels instead of Markdown mini headings. They should feel like designed signposts inside the box, not like a second nested heading structure. This keeps the analytical path easy to scan while avoiding unclear tiny subtitles.

The mini sections should follow the full post's logic, but in compressed form. A good sequence is often: data and scope, main metric or normalization, second metric or transformation, analysis setup, descriptive result, model or deeper analysis, and takeaway. The exact labels should fit the post, not a fixed template.

Mention visuals only through the result they show, not by saying "the plot shows", unless the figure itself is the object of the post.

When the post uses a model, metric, normalization, or engineered feature, keep the technical spine in the short version. Include the core metric, formula, model definition, feature group, or final signal when it is central to the argument. Give formulas inline when possible and translate them into plain language. The summary should explain why the method was needed, not only name it.

Shorter does not mean less technical. It means removing repeated explanation, setup phrases, and wording that does not move the story forward. Each sentence should either define the setup, name the method, report the result, or connect the result to the takeaway.

The short version is not a replacement for the full post. It should compress the story, not copy whole sections. It should not include exploratory dead ends, minor diagnostics, implementation details, or every number from the notebook. It should also not introduce claims that the full post does not support later.

End the short version with what the analysis means: the practical answer, the reframed question, the limitation that changes interpretation, or the main takeaway the reader should carry into the full post.

## Overall Voice
- Write like a data scientist explaining a personal project to an interested technical reader.
- Keep the voice personal, analytical, direct, and grounded in data science.
- Preserve the connection between personal curiosity, endurance sports, mathematics, statistics, and modeling.
- Be honest about assumptions, uncertainty, and limitations.
- Avoid corporate portfolio language, generic SEO blog phrasing, and sales-like claims.
- Do not over-polish the writing until it loses the user's natural voice.

## Sentence-Level Voice
- Keep the writing approachable for readers who are curious but not necessarily mathematicians.
- Prefer plain-language intuition before formal notation, formulas, or model details.
- Use sentences that sound like someone thinking through the problem with the reader, not lecturing from above.
- Allow small conversational pivots such as `But`, `So`, `Of course`, `In other words`, `At this point`, `The idea is simple`, or `Well` when they make the writing feel more human.
- Use light humor or self-awareness sparingly, especially when a result is humbling, ambitious, or slightly unrealistic.
- Keep jokes subtle and tied to the analysis; do not force jokes into serious technical explanations.
- Preserve small personal asides when they reveal motivation, uncertainty, or a realistic reaction to the result.
- Make technical sections feel less strict by alternating formal explanation with ordinary-language interpretation.
- Use rhetorical questions when they naturally introduce the next analytical step.
- Use contrast to make the story clear, such as `not only ..., but ...`, `rather than ...`, or `the problem is ...`.
- Let some sentences be short for emphasis, especially after a complex explanation or surprising result.
- Avoid making every sentence polished to the same rhythm; some natural unevenness is part of the voice.
- Fix grammar, typos, and awkward wording, but do not erase the slightly personal, exploratory feel of the writing.
- Do not turn the voice into academic paper style, LinkedIn thought-leader style, or corporate portfolio style.

## Distinctive Personal Voice
- Keep the recurring theme that mathematics and statistics are a lens for understanding real life, not just technical tools.
- Let endurance-sport motivation sit next to analytical reasoning; the writing often works because trail running, training, and modeling are treated as one connected curiosity.
- Preserve the sense of long-term ambition, especially when writing about UTMB or training goals, but balance it with realism and humility.
- Use the pattern of starting with a personal dream or practical problem, then making it measurable with data.
- Keep the "thought process" visible: the writing should show how the question became clearer, not only the final answer.
- Include moments where the model challenges the original expectation; these are part of the voice, not mistakes to smooth away.
- Use self-aware phrasing when appropriate, such as admitting that a benchmark may be too ambitious or that a result is humbling.
- Prefer honest reframing over forced certainty: when the original question is too strict, guide the reader toward a more useful question.
- Make numbers feel like part of a story about preparation, adaptation, risk, uncertainty, or curiosity.
- Keep a light human touch in transitions, but avoid making the writing jokey for its own sake.
- Preserve the mix of rigor and creativity; the writing should feel analytical, but still a little artistic and personal.
- When editing, do not remove sentences that reveal motivation, surprise, doubt, or learning unless they are clearly distracting.

## Explaining Technical Ideas To Non-Specialists
- Start with why the idea matters in the real project before naming the method.
- Explain the practical meaning of a metric before giving its formula.
- After a formula, translate it back into words.
- Use examples from running, training, racing, or data collection to make abstract concepts concrete.
- If a model has assumptions, describe what they mean practically, not only statistically.
- When a result is uncertain, say what that uncertainty means for decisions.
- Make limitations readable and useful, not defensive.
- Avoid assuming the reader knows statistical language such as calibration, residuals, heteroskedasticity, censoring, or quantiles.
- Define technical terms close to where they first appear.
- Use bold text for the most important concept in a paragraph, but do not bold too much.

## Typical Sentence Framing
- Start posts with a simple motivation or observation, then sharpen it into the analytical question.
- Use phrases like `The goal is...`, `The idea is...`, `To understand this...`, or `This leads to...` to guide the reader.
- When introducing a method, first explain why simpler approaches are not enough.
- When showing a result, state the number first, then explain why it matters.
- When a result challenges the initial expectation, acknowledge it directly.
- End important sections by connecting the result back to the project goal or real-world decision.
- Prefer honest statements like `this is not perfect`, `the signal is limited`, `the result is humbling`, or `this gives a useful approximation` when they fit the analysis.
- Keep the tone confident about the reasoning, but humble about what the model can actually know.

## Pronoun Style
- Use `I` when discussing personal motivation, training goals, curiosity, or project decisions.
- Use `we` when guiding the reader through a method, model, formula, or analytical step.
- Use passive voice sparingly, mostly when the object of analysis matters more than the actor.

## Writing Flow
- Start from a real personal or analytical motivation.
- Convert that motivation into a concrete question.
- Explain the data and method clearly.
- Interpret results in plain language.
- End with what the result changes, teaches, or reframes.
- Define technical terms before using them heavily.
- Explain why a method was chosen, not only what the method does.
- Use formulas when they clarify the logic, and explain them in words before and after.
- Place visuals near the text that interprets them.
- After a figure, explain what the reader should notice.

## Headings
- Use short `###` headings inside posts.
- Prefer clear analytical labels over clever titles.

Common headings:

- `### Idea`
- `### Methodology`
- `### Data preparation`
- `### Finish probability`
- `### Race time conditional on finishing`
- `### Probability of sub-27 hour race time`
- `### Conclusion`
- `### Implementation`

## Cards And Link Blocks
Use blog cards for child posts.

```markdown
::: {.blog-card}
[**Post Title**](project/post.qmd)  
Short summary of the post, written as a useful teaser rather than a generic abstract.
<span class="blog-date">YYYY-MM-DD</span>
:::
```

Blog card summaries should:

- explain the post's practical question
- mention the data or method when useful
- be one compact paragraph
- avoid vague phrases like "this post explores"

Use project link containers for GitHub/code references, and keep link text concrete. Mention the directory or script if possible.

## Visuals
- Use images when they support the story, not as decoration.
- Use `saved_files/<post-name>/...` paths for post-specific visuals inside project subpages, where the folder name matches the `.qmd` file stem.
- Use `saved_files/...` at the project level only for images shared across multiple posts.
- Use `{ class="click-zoom" }` for important analysis images when consistent with nearby pages.
- Do not dump figures at the end; place each figure near its explanation.

Preferred image pattern:

```markdown
![](saved_files/example.png){ class="click-zoom" }
```

## Path To UTMB Style
- Blend personal ambition with statistical modeling.
- Start with the race, dream, or readiness question.
- Convert the personal goal into a measurable question.
- Define the metric, often UTMB Index.
- Explain the data, model, diagnostics, and interpretation.
- Keep the tone ambitious but grounded.
- If a result is humbling, say so plainly.
- End with what the result means for preparation, uncertainty, pacing, nutrition, experience, or future training.

## Training Log Style
- Connect daily training, endurance sports, and analytics.
- Start with a practical training question.
- Explain why raw metrics alone are not enough.
- Define the metric or framework.
- Explain baseline versus recent training.
- Use formulas when needed.
- Show visual diagnostics.
- Interpret what changes in the metric mean for training decisions.
- End with how the metric can guide future workouts or analysis.

## Editing Existing Text
- Preserve personal motivation and analytical framing.
- Improve grammar, transitions, and flow without changing the voice into generic professional copy.
- Remove obvious typos.
- Keep the post's level of technical detail unless the user asks to shorten it.
- Challenge unclear claims or unsupported conclusions.
- Make the text cleaner without making it sound like a different person.

## Critical Collaboration
- Treat user ideas for page structure, wording, and content as hypotheses, not final answers.
- Ask sharp questions when the goal, audience, or structure is unclear.
- Do not turn every small edit into an interview.
- Suggest stronger alternatives when a different structure, title, or explanation would make the portfolio clearer.
- For active step-by-step collaboration rules, use `.agents/portfolio-workflow.md`.

## Adding New Portfolio Content
When adding a new project:

1. Create or update a project landing page at `projects/<project>.qmd`.
2. Put detailed posts under `projects/<project>/`.
3. Add saved figures under `projects/<project>/saved_files/<post-name>/` for post-specific assets, or `projects/<project>/saved_files/` for shared project assets.
4. Add a blog card on the project landing page.
5. Add a featured project card on `index.qmd` only if it is a major project.

When adding a new post:

1. Choose whether it is a data post, method post, analysis post, or visual result post.
2. Start with the question or motivation.
3. Explain data and method before showing conclusions.
4. Add figures where they support the argument.
5. End with interpretation and next step.
6. Link to the relevant code or repository.

## What To Avoid
- Do not edit `_site` output directly.
- Do not convert the portfolio into a corporate resume site.
- Do not remove the personal endurance-sport motivation.
- Do not over-compress detailed analytical posts.
- Do not add large marketing hero sections.
- Do not make every article sound like an academic paper.
- Do not hide uncertainty or limitations.
- Do not make unsupported performance or health claims.
- Do not invent results that are not in the source analysis.

## Code Snippets In Posts
- Keep code examples short and focused.
- Prefer snippets that show how to use a helper rather than full implementation details.
- Link to the full repository for complete code.
- Use the existing data science code style when showing Python snippets, including spaced keyword arguments such as `race_id = "..."` and `access_token = ...`.

## Verification
- Preview or render the Quarto site when making structural or visual changes.
- Check links to internal posts, GitHub repositories, images, and embedded sheets.
- Confirm images render from the correct relative paths.
- Summarize what changed and note any follow-up.
