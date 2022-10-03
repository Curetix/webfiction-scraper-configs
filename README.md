# Web Fiction Scraper - Configs

This repository stores all remote configs for the [Web Fiction Scraper](https://github.com/curetix/webfiction-scraper).

These configs can be listed using the command `webfictionscraper list-configs --remote`
and downloaded with `webfictionscraper download-config [--all] [config_name]`.

## Config naming conventions

File names of fiction configs should be alphanumerical, with underscores replacing whitespaces.
Other special characters should be avoided as they might cause issues depending on the OS.

Since the naming convention for Python dictionaries is [snake_case](https://en.wikipedia.org/wiki/Snake_case),
all keys inside the configs for this project should use this convention as well.

That said, configs using [camelCase](https://en.wikipedia.org/wiki/Camel_case) *are* supported and converted internally when they are loaded,
thanks to the [Camel Killer Box](https://github.com/cdgriffith/Box/wiki/Types-of-Boxes#camel-killer-box).

## Creating configs

The config for [The Wandering Inn - Volume 1](./configs/Wandering_Inn_Vol_1.yaml) contains detailed comments
on all available configuration options.

For a step-by-step guide, view this: [creating_configs.md](./docs/creating_configs.md) *(Work-in-Progress)*.

## Help

If you have problems with either an existing config or while creating one for a particular web fiction,
you are welcome to open a GitHub issue.
