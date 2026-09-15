# Training Cards Blog Plan

This is a shared planning document for the Training Cards article. It records
agreed content and the writing decisions that will later guide the blog post.
It is not the blog post itself.

## Collaboration Workflow

1. The user provides ideas, preferred wording, or content priorities.
2. Codex refines the instruction into a clear writing brief and suggests useful
   additions or improvements.
3. Codex keeps the user's direction and recommendations visibly separate.
4. The user accepts, rejects, or changes the proposal.
5. Only accepted decisions are added to the agreed plan.
6. Once the plan is complete, Codex writes one final-quality article draft based
   on it.
7. The article is then reviewed section by section without changing the agreed
   project story accidentally.

## Writing Principles

- Keep the personal, analytical, and approachable voice of the existing Training
  Log posts.
- Preserve the user's natural way of explaining the project.
- Improve grammar, clarity, and flow without replacing the personal voice with
  generic portfolio language.
- Treat technical additions as recommendations until the user accepts them.
- Keep the article aligned with the current project structure and avoid outdated
  implementation details.

## Agreed Content

### Idea

The existing Idea section should remain almost word for word. Its personal
motivation, the origin of the card idea, and the connection with Pokémon and
Yu-Gi-Oh should be preserved.

The section should additionally explain that the cards were the clear starting
idea, while the application itself was intentionally not fully designed in
advance. At the beginning, there was no clean final picture of what the app
would look like, what actions it would support, or exactly how it would be used.
The application and user experience were meant to develop gradually while the
card system was being built.

The article should present this as an exploratory part of the project: the card
concept provided the direction, while the practical form of the application was
allowed to emerge from the structure, content, and possibilities discovered
during development.

### Architecture Overview

Include an overview of the full project before going deeply into individual
classes or workflows.

Present the architecture through functional areas rather than a file-by-file
inventory. Use a compact project sketch followed by short explanations of what
each area is responsible for.

The overview should cover:

- coaching knowledge and source documentation
- card schemas and controlled vocabularies
- card content and temporary authoring examples
- validation, serialization, and data transformation
- cloud storage and local cache workflow
- pathway, reference, reuse, and library-index logic
- Streamlit data loading, state, views, and renderers
- tests and project documentation
- archived experiments as a clearly separate non-active area

The explanation should focus on the responsibility of each area and how it
connects to the others. It should not become a complete file catalogue.

### Design Decisions And Learning

For each major part of the system, explain the design reasoning rather than only
listing its features.

The article should address:

- why the part is separate
- what problem it solves
- how it connects to the rest of the system
- what would become difficult without the separation
- how the decision improves clarity, validation, maintenance, or reuse

This should make the post useful as a practical example of how to structure a
growing data-oriented project.

### Final Project Status

End the article with one short paragraph explaining that the current Streamlit
application is an early, mostly read-only prototype rather than the finished
Training Platform.

The ending should state that the current app provides a foundation for future
functionality, including additional ideas, richer interaction, and more advanced
training-support features.

## Open Decisions

- Whether the additional Idea paragraph should be personal and short or explain
  the iterative development process in more detail.
- Which article section should be planned next.
