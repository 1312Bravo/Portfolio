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

## Detailed Article Blueprint

The article should be a deep explanation of how the project is structured and
why, but not a code reference manual.

### 1. Idea

Keep the existing Idea section almost unchanged.

Add only the point that:

- The card concept was clear from the beginning.
- The surrounding system was not fully defined yet.
- The structure developed while working.
- The schema, workflows, and application emerged from the needs of the card
  system.

The Idea section should remain personal and relatively warm. It should not
become technical too early.

### 2. From Cards To A System

Use a short bridge between the personal idea and the technical project.

Explain that creating useful cards required more than writing descriptions. The
cards needed:

- a consistent shape
- different planning levels
- reusable relationships
- coaching context
- validation
- a way to reach the application

The reader should understand why the project grew from a visual card idea into a
structured data system.

### 3. Architecture Overview

Present the architecture of the full project before going deeply into individual
classes or workflows.

Use a simplified architecture sketch based on responsibilities rather than
individual files:

```text
Coaching knowledge
        ↓
Card schemas and content
        ↓
Validation, relationships, and reuse
        ↓
Cloud library and application bundle
        ↓
Streamlit user interface
```

Present the main project areas:

- `coaching`: coaching foundation, philosophy profiles, source notes, and
  card-authoring guidance
- `training_cards`: schemas, serialization, validation, cloud/cache tools,
  pathway logic, and metadata generation
- `streamlit_app`: data loading, application state, views, filters, and card
  renderers
- `tests`: checks for storage, pathways, and philosophy metadata
- `notes`: durable technical and workflow documentation
- `archive`: retired artwork experiments, clearly separated from the active
  project

Explain each area’s responsibility and how it connects to the others. Do not
turn this into a complete file catalogue.

### 4. The Card Model

Make this the main technical section.

Explain the four levels:

- Macro phase
- Mezzo block
- Micro week
- Session workout

Explain the classes:

- `BaseTrainingCard` provides the common structure.
- `MacroCard`, `MezzoCard`, and `MicroCard` extend the shared structure for
  different planning horizons.
- `SessionCard` adds workout-specific content.
- `SessionFamily`, `WorkoutBlock`, `WorkoutOption`, and `SessionPart` provide
  the detailed session structure.

Present the actual current Python class definitions inside collapsible sections.
The main text should explain the design decisions, while readers can open the
code when interested.

Cover:

- shared fields
- level-specific fields
- required versus optional fields
- controlled values
- nested session structure
- inheritance
- `slots=True`
- `default_factory`

Do not show the full implementation of every storage or validation function.

### 5. Coaching Knowledge And Philosophy Profiles

Explain where the training content comes from.

Cover:

- the shared coaching foundation
- separate training-method profiles
- the structure of every philosophy profile:
  - summary
  - detailed philosophy
  - source record
- the purpose of `philosophy_profile_ids`
- the difference between shared coaching guidance and specific philosophy
  provenance
- the fact that the profiles are documented interpretations, not official
  material from the named systems

Introduce the specialised coaching AI agent in this section.

Explain that it uses:

- the shared coaching foundation
- the card hierarchy
- card-authoring guidance
- philosophy documentation
- source material and interpretation boundaries

The goal is to show that training content is prepared through a defined
knowledge structure, not generated as isolated generic workout text.

### 6. How The Card Library Was Built

Describe the development methodology and its order:

1. Define the macro-level training taxonomy.
2. Build mainstream baseline macro cards.
3. Review each macro concept through the named philosophies.
4. Build mezzo cards inside the accepted macro structure.
5. Build micro cards inside the mezzo structure.
6. Build reusable session cards.
7. Review philosophy-specific differences at every level.
8. Create separate philosophy cards only when the difference is meaningful.
9. Add reuse metadata where an existing card is still appropriate.
10. Validate the complete library before accepting or publishing it.

Explain why broad planning decisions come first and why specific workouts should
not be created without a clear place in the larger system.

Explain the philosophy-specificity rule:

- A separate card is justified only if the philosophy changes selection,
  structure, progression, explanation, filtering, or sequencing.
- Different wording alone is not enough.
- A card should not be duplicated merely because it has a different philosophy
  label.

### 7. Data Lifecycle And Cloud Storage

Explain how cards move through the system.

Use a simple workflow:

```text
Authoring
   ↓
Local JSON cache
   ↓
Schema conversion and validation
   ↓
Bundle, manifest, index, and reuse metadata
   ↓
Google Drive
   ↓
Streamlit application
```

Explain accurately:

- Google Drive JSON is the accepted source of truth.
- The local cache is a temporary working copy.
- Python card objects are useful for temporary authoring and transformation.
- Accepted content ultimately becomes validated JSON.
- JSON cards can be converted into temporary Python authoring files.
- Python-authored cards can be converted back into JSON.
- The application consumes the generated bundle rather than directly depending
  on authoring files.

Describe the cloud contents:

- individual cards organised by level and profile
- manifest
- display configuration
- reuse metadata
- card-library index
- bundled library file

### 8. Validation, Relationships, And Reuse

Combine these topics into one data-integrity section rather than scattering
them across the article.

Explain:

- schema validation checks the shape of individual cards
- pathway validation checks the meaning of card relationships
- `CardReference` creates explicit machine-readable links
- parent and child links connect adjacent planning levels
- sequence and alternative links stay at the same level
- support links can cross levels
- broken references and invalid hierarchy jumps are errors
- incomplete pathways and orphan cards are allowed while the library grows

Explain reuse metadata for:

- macro-to-mezzo reuse
- mezzo-to-micro reuse
- micro-to-session reuse

The key lesson is that the system separates content ownership from pathway use.
A card can be reused in another philosophy or pathway without copying the card
itself.

### 9. The Streamlit Application

Explain the current application as a read-only beta/prototype built on top of
the validated library.

Describe the implemented features:

- **Browse cards:** search, filtering, tags, philosophy filters, and previews
- **Card library:** grouped card metadata and direct/reused card information
- **Build pathway:** selecting Macro → Mezzo → Micro → Session cards
- **Today session:** browsing session cards
- **Coaching philosophies:** reading philosophy summaries and reviewed sources
- **Card detail view:** deeper coaching information, workout guides, and linked
  cards

Explain the application responsibilities:

- data loading and validation
- application state
- views
- filters
- preview renderers
- detail renderers
- styling

Describe the current visual direction as typography-first and restrained.
Artwork experiments are archived and are not part of the active app.

The article should explicitly state that Today session is currently a browser,
not an intelligent recommendation engine.

### 10. AI-Assisted Development

Describe the AI work as a role-separated collaboration.

Explain the roles:

- I defined the original concept, system direction, boundaries, visual
  expectations, and review criteria.
- A specialised coaching agent prepared training-related content from the
  documented coaching knowledge.
- Other AI assistance supported schemas, storage workflows, validation,
  pathways, and application implementation.
- I continuously reviewed, corrected, redirected, and accepted the outputs.
- The agents had defined responsibilities rather than being treated as one
  general-purpose assistant.

Focus on the division of responsibility rather than simply stating that AI
wrote code or content.

### 11. Current Status

End with a short paragraph explaining:

- the current app is an early read-only beta
- it is a foundation rather than the finished Training Platform
- the current system already supports the card library and core browsing
  experience
- future work can add richer interactions, editing, recommendation logic, and
  additional training-support features

The archive and artwork experiments should not receive a large section.

## Main Recommendations

- Use the architecture overview before the class definitions.
- Combine validation, references, and reuse into one coherent data-integrity
  section.
- Treat the AI work as a defined multi-role workflow, not as a general claim
  that AI helped.
- Include one complete end-to-end data flow from card authoring to Streamlit
  display.
- Keep actual code limited to the current schema classes, inside collapsible
  sections.
- Explain design decisions and trade-offs more than individual functions.
- Clearly separate active functionality, temporary authoring tools, and archived
  experiments.

## Open Decisions

- Whether the additional Idea paragraph should be personal and short or explain
  the iterative development process in more detail.
- Whether the proposed article order should remain unchanged.
- Whether validation and reuse should remain one section or become two sections.
- Which article section should be reviewed first.
