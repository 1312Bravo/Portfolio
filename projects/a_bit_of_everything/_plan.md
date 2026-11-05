# UV Scout blog post plan

## Goal

Write a personal, readable post about the thinking behind UV Scout, with the main focus on its data sources and on how the app turns forecast data and public-health guidance into its own outing recommendations. The existing `### Idea` section and post summary provide the personal motivation and brief app introduction; the full post does not need to repeat a feature-by-feature tour.

## Agreed direction

- Keep the app walkthrough brief. Explain only enough of the user flow to make the data and recommendation process understandable.
- Focus on where the information comes from, how the app retrieves and interprets it, and which parts are UV Scout's own work.
- Leave the Info tab out of the article plan.
- Keep the tone personal and explanatory, rather than turning the post into API documentation.

## Proposed post structure

### Idea

Keep the existing personal story: summer sunburns, the autumn question about sunscreen, and the thought that grew into UV Scout. The current section already establishes why the UV Index deserves attention alongside familiar weather information.

### Data sources — drafted in `uv_scout_tmp.qmd`

- Explain that the forecast comes from the [Open-Meteo Forecast API](https://open-meteo.com/en/docs). UV Scout requests current and hourly UV and supporting weather variables for the selected coordinates, along with the location's time zone and a forecast covering the next two local days.
- Describe the location inputs briefly: place search uses Open-Meteo's geocoding service and GeoNames data; map selection uses OpenStreetMap; device or browser location is available with permission. Reverse geocoding supplies a readable place label for coordinates.
- Explain the path in plain language: the app sends the selected location to the relevant services, receives forecast data, and organizes it around local time for the outlook and planned outing.
- Make clear that forecast values are model estimates, not measurements taken at the user's exact location. Keep the description proportionate; detailed API field lists belong in the code or source notes, not the post.

### From forecast to outing guidance — drafted in `uv_scout_tmp.qmd`

- Explain the user's contribution: choose a location, start time, and intended duration outside.
- Describe the core calculation: UV and weather forecast periods are matched to the planned time window, then summarized to show the UV levels and weather context expected during that outing.
- Explain how the app handles a changing UV forecast: it identifies the relevant UV periods across the outing, so guidance can describe when different levels are expected rather than reducing the plan to one reading.
- Include a concise note that forecast coverage can be incomplete and that the result depends on the available forecast. Confirm exact interval handling and summary calculations against the current implementation before drafting.

### Limitations — to draft in `uv_scout_tmp.qmd`

- Explain that the outing summary uses one selected location throughout, even when an activity follows a route through multiple places.
- Describe how UV and weather conditions may vary along a route, while UV Scout does not follow the user's changing position.
- Treat route-level shade as a separate limitation: the app does not map tree cover, building shade, or exposed sections.
- Note separately that guidance does not change by activity type, with examples such as walking, running, hiking, cycling, and swimming.
- Avoid presenting ordinary forecast uncertainty or the short-term planning scope as special product limitations; do not repeat the personal-guidance limits already covered in the outing-guidance section.

### Future development — to draft separately later

- Reflect on how using the app may reveal useful features or improvements.
- Keep this grounded in the author's experience rather than promising a particular roadmap.

## Editorial boundaries

- Do not write a detailed screen-by-screen tutorial; the summary already gives readers the basic app flow.
- Keep secondary weather variables in their supporting role around the UV-focused purpose.
- Separate externally sourced facts from UV Scout's own calculations, thresholds, presentation, and product choices.
- Include attribution and any relevant provider terms in a reader-friendly way. Recheck current provider terms and source links before publishing, especially if the app's release or use changes.

## Source notes to consult while drafting

In the UV Scout app repository (`uv-index-app`):

- `notes/data-sources.md` — source register, attribution, licensing, data limitations, and code paths.
- `notes/active-uv-guidance.md` — current outing guidance rules and their interpretation.
- `notes/forecast.md` and `notes/location.md` — forecast and location behavior.
- `src/services/forecast/getHourlyForecast.ts` — forecast request and parsing.
- `src/domain/outing/calculateOutingForecast.ts` — outing interval and weather summaries.
- `src/domain/guidance/` — UV Scout's rule definitions and recommendation logic.

## Drafting checklist

- [x] Verify the source descriptions and app behavior against the current code and source register.
- [x] Decide how much detail to give about location services; keep it brief unless it clarifies the data path.
- [x] Explain the difference between forecast data, public-health evidence, and UV Scout's own interpretation.
- [x] Draft the data-source section.
- [x] Draft the outing calculation and recommendation section.
- [x] Draft the route and location limitation section.
- [ ] Draft a separate reflection on future development.
- [ ] Check external links, attribution, and consistency with the existing Idea and post summary.
