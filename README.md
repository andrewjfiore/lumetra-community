# Lumetra community profiles

Film and camera profiles for the Lumetra light meter app, shared by photographers. The app reads `index.json` and every pack it lists, once a day and whenever you tap **Get profiles from GitHub** in Settings.

## Add a profile

1. Fork this repository.
2. Add a file in `packs/`, for example `packs/my-camera.json`. In the app, Settings > Community profiles > File format shows a template you can copy.
3. List your file in `index.json`.
4. Run `python3 tools/validate.py`, then open a pull request.

## The one rule

Every film and every kit needs a `citation`: where the numbers came from, such as a maker's datasheet, a camera manual or a reference page, with a link when there is one. The app refuses entries without one, and so does the check on every pull request.

## What a pack holds

- `films`: `id`, `name`, `manufacturer`, `iso`, `kind` (`blackAndWhiteNegative`, `colorNegative` or `slide`), `reciprocity` (`model` is `table` with `points` of `[metered, corrected]` seconds, `schwarzschild` with `p`, or `none`; optional `limit`, the longest metered time the data covers, in seconds), `citation`, optional `author`.
- `kits`: `id`, `name`, `fastest` and `slowest` in seconds (0.001 is 1/1000), `bulb`, optional `widest` and `smallest` f-numbers, optional `shutterSteps` (`full`, `half` or `third`, full when left out), optional `mount` named as Lensfun names it (`Canon FD`, `Nikon F`, `Olympus OM`, `Pentax K`, `Leica M`) so lens search shows lenses that fit, `citation`, optional `author`.

Questions: hello@anjafio.com
