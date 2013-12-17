# OSI uploader & killer

`post.py` is a simple script to grab the OSI report source and post it onto the OpenSpending WordPress site as a tree of Pages, with a nice hierarchical structure for slugs.

The script takes a YAML file `post.yaml`, containing attributes `source-tree` and `root-name`. The former is a tree-structured object whose nodes are pages to be posted. Each node gives its page's URL (`name`), slug (`slug`), and list of children pages (`children`); optionally it also gives the ID of the page on the site (`id`) and the ID of the node's parent page, where this cannot be deduced from context (`parent`). URLs preceded by `/` are prefixed with the config file's `root-name` at execution time; other values of `name` are treated as bare URLs. When `post.py` runs, `post.yaml` will be overwritten with an updated file that records the new IDs generated in the course of creating any new pages.

To use `post.py`, simply rename `wordpress.ini.template` to `wordpress.ini` and edit it to fill in your authentication information. Then run the script like so:

    python post.py

This repo also includes `kill.py`, which reads a list of Page IDs from `kill.yaml` and sends them to the trash. When `post.py` runs, it writes the IDs of the Pages it creates to `kill.yaml` so that they can be easily erased on the next iteration. *Note that you still have to empty the trash before running `post.py`, as the slugs of Pages in the trash are not usable.*