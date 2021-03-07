# conzip
`conzip` is a python tool that aims to make publishing conlang grammars to pdf and html from yaml, csv, plain text, and other tex sources easy while eliminating the need to work heavily in tex. yaml sources define the overall structure, various chapters, and text in them while referencing tables defined in csv or sections in plain text. Extra tex sources are used to parameterize packages, define new commands, and other more tex direct needs.

## conzip common and default

`conzip` provides a set of common tex utilities to make final products look polished, such as present `microtype` and `ipa` set ups, that may optionally be used. These can be found in the `common` directory, and they can be selected for use via your top level yaml file, default `guide.yaml`. These common utils are as follows:

- `cz_microtype` : a baseline `microtype` set up
- `cz_ipa` : a very wide set up to help with the `tipa` package
- `cz_geometry` : high level controls for margins

Similarly, a small handful of utilities are provided as defaults to make building final products a bit more streamlined. They can be found in the `default` directory, and if desired they can be excluded by using the `--no-defaults` option when invoking `conzip`. The utilities provided as default are:

- `cz_commands` : a collection of `newcommands` to make building with `conzip` easier

## to do

- top file generation -- Closing out
  -  top file gen safeguards (ie no date or author)
- chapters generation -- started
- yaml macro replacer -- essentially done
- table generator -- waiting
- pdf fine tuning -- far off
- html fine tuning -- far off
- pdf build -- far off, but easy
- html build -- far off, slightly bumpier than pdf
- actually set up the `common` and `default` directories -- I'm lazy
