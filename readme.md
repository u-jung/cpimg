# What is this? #

A command line tool, which should help to copy JPEG files from a source (whit sub directories) into a date based directory structure usind the information from exif field 306.

# How to use #

    python cpimg  source destination


The result directory structure will be like this:

<pre>
├── 2020
│   ├── 02
│   │    └── 28
│   │        ├── foo.jpg
│   │        └── bar.jpg
│   └── 03
├── 2021
│   ├── 01
│   ├── 02
│   └── 03
</pre>
