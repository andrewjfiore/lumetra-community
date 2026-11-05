# Lens list used by Meterology

`lensfun-lenses.json` is adapted from the [Lensfun](https://github.com/lensfun/lensfun) lens database by the Lensfun contributors. It keeps each lens's maker, model, mounts, focal range and aperture range, and fills a missing widest aperture from the lens name or Lensfun's own calibration data. It is shared under the same license, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), with the license text in `LICENSE-lensfun-CC-BY-SA-3.0.txt`. The Lensfun revision it was built from is in the file's `revision` field.

`extra-lenses.json` adds medium format lenses Lensfun does not list, such as the Mamiya RB67 Sekor C lenses, Hasselblad V lenses and Pentax 67 lenses. Each entry carries the page or brochure its aperture range came from in `source`. It is shared under CC BY-SA 3.0 as well.

Both files are built by `tools/lensfun/convert.py` and `tools/cameras/build.py` in the Meterology app.
