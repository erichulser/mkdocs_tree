The `mkdocs_tree` extension will allow you to load a hierarchy of markdown files
into your [mkdocs](https://github.com/tomchristie/mkdocs) project.

### Usage

Create a folder structure of `*.md` files somewhere in your documents root, for instance

    [-] ./docs/api/mkdocs
     |- index.md
     |- [+] contrib
     |- [-] utils
     |   |- index.md

To serve this hierarchy, you will need to include the `mkdocs_tree` extension in your `mkdocs.yml`
configuration file:

    mkdocs_extensions:
        - mkdocs_tree

Once that is included, you can load your folder hierarchy by including it in your `pages` configuration:

    pages:
        - ['tree:api/mkdocs', 'API', 'mkdocs']

As you can see, the syntax is `tree:<path/to/root>`.  It will load only a _single_ page to the `API` header,
named `mkdocs`, but register all the sub-pages for reference within the documentation.