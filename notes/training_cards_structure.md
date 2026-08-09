# Training Cards Structure

This note explains the training-card schema as a data model, not as a content story. The goal is to describe the object shape, the controlled vocabulary, and the way the classes fit together.

## Supporting Types

`CardType`, `CardRelationship`, and `TrainingLevel` act as the controlled vocabulary of the model.

`CardType` is the type discriminator. It tells the code whether a card belongs to the `macro`, `mezzo`, `micro`, or `session` layer. That matters because the card library is not a flat list of records. It is a typed hierarchy, and the enum makes that hierarchy machine-readable instead of leaving it as a naming convention.

`TrainingLevel` is the suitability axis. It describes which athlete groups a card is relevant for, using a fixed vocabulary rather than free text. That keeps the model compact and avoids writing the same concept in slightly different ways across cards.

`CardRelationship` defines how cards connect to one another. Instead of vague links, the schema uses explicit labels such as `parent`, `child`, `previous`, `next`, `alternative`, and `support`. That turns navigation into structured metadata rather than prose.

`CardReference` is the small linking object that uses that vocabulary. It stores the target card id, the relationship type, and optional tags. In data-model terms, it is a lightweight graph edge: a structured pointer between two cards with enough metadata to preserve context without cluttering the main object.

## Shared Base Class

`BaseTrainingCard` is the shared base class for all card types. It holds the fields that are useful everywhere: identifiers, display fields, suitability, descriptive context, and references. That is the part of the model that keeps the library coherent.

The shape is intentionally broad because the base class should capture the shared contract without forcing every subclass to repeat the same structure. This is a standard domain-model pattern: keep shared semantics in one place, then let the specialized types add only the fields they actually need.

The list-based fields are deliberate. They fit semi-structured metadata such as tags, context notes, adaptations, warnings, and progression rules. These values are easy to display in a UI, easy to compare across cards, and easy to extend later without breaking the object shape.

The `__post_init__()` validation is intentionally light. It checks that a card can actually be identified and understood, but it does not try to enforce every possible domain rule. That is a good engineering tradeoff here: validate the minimum needed to prevent broken records, without making the schema brittle.

## MacroCard

`MacroCard` represents the highest planning granularity. It inherits the shared contract and adds only the fields that matter for a broad phase-level object: `recommended_duration_weeks` and `timing_guidance`.

This keeps the phase card focused on planning horizon rather than on week-level or workout-level detail. The object says what the phase is and how long it usually lasts, but leaves finer structure to lower layers.

## MezzoCard

`MezzoCard` is the intermediate block layer. It extends the shared base with `recommended_duration_weeks` and `placement_guidance`.

This layer needs guidance about placement inside the wider structure. It is the place where sequencing matters more than exact workout composition, so the class stays deliberately small and adds only the metadata needed to position the block correctly.

## MicroCard

`MicroCard` is the week-level object. It adds `recommended_duration_days`, `week_structure`, `key_sessions`, `load_pattern`, `placement_guidance`, and `recovery_requirements`.

This is where the model becomes more operational. A micro card needs to describe what the week looks like, how the load is arranged, which sessions matter most, and what recovery the week assumes. Those fields make the card useful for planning because they describe the week as a reusable pattern rather than a one-off schedule.

## SessionCard

`SessionCard` is the most detailed card type. It describes an individual workout pattern and therefore needs fields like `session_family`, `typical_duration`, and `workout_parts`.

That is why it is modeled separately rather than folded into a generic workout object. The session card is a reusable template for execution, not just a label. It also carries the guidance needed to keep the session readable and consistent across uses.

The `session_family` field is now its own object, which is a useful refinement. It lets the schema separate the family label from the session itself, so the session card can stay focused on one reusable workout pattern while the family object carries the broader grouping and summary context. Using `kw_only=True` on `SessionCard` also makes the object safer to construct, because the required family object has to be passed explicitly instead of getting buried in a long positional argument list.

## SessionFamily

`SessionFamily` is the higher-level grouping object for related sessions. It carries a stable identity, a human-readable title, a summary, and optional description or tags.

This is useful because sessions often belong to a broader workout family rather than existing as isolated objects. The family object gives that grouping a proper schema, which keeps the model cleaner than repeating the same family metadata across many session cards.

## SessionPart

`SessionPart` is a small but important helper object. It breaks a session into named components such as warm-up, main set, recovery, or cooldown.

That is a good design choice because it turns a long workout description into a structured sequence of parts, which is easier to read, easier to reuse, and easier to render cleanly in an interface. The `rpe` field gives each part a simple effort label alongside duration and instructions.

## Why This Shape Works

Overall, this is a good domain model because it separates concerns cleanly:

- the enums define the vocabulary
- `CardReference` defines relationships
- `BaseTrainingCard` defines the common contract
- the subclasses define the level-specific extensions
- `SessionFamily` defines the reusable session grouping
- `SessionPart` defines the internal structure of a workout

That gives the library consistency without making the objects over-engineered. It is a compact schema, but it still has enough structure to stay readable, reusable, and easy to extend later.
