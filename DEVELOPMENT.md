# Development tips and howtos

## Molecule tests

The test suite uses [molecule], Ansible's solution for unit testing roles
using virtual machines or containers. We use Docker containers by default.

Since molecule is not packaged for Debian (see ITP at [#986204]), it must be
installed with `pip` or `pipx` (molecule provides no importable modules, so
`pipx` is probably best). On macOS, it can also be installed with `brew
install`.

[molecule]: https://ansible.readthedocs.io/projects/molecule/
[#986204]: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=986204


### Running tests

Tests are located in the [molecule/default] directory, and can be run with:

```sh
$ molecule test
```

A Github workflow runs this on every pull request, and pushes to main.

[molecule/default]: molecule/default


### Developing tests

Running `molecule test` takes a while, since instances (containers or VMs) are
created, configured, and destroyed on every run.

During development, it's more ergonomic to run `molecule converge` and
`molecule verify` as appropriate:

  - _molecule converge_ applies the [converge.yml] playbook to configured
    instances (should be run after making changes to the collection or the
    test fixtures);

  - _molecule verify_ runs the [verify.yml] playbook to assert the correctness
    of the resulting state (should be run after _molecule converge_).

[converge.yml]: molecule/default/converge.yml
[verify.yml]: molecule/default/verify.yml



## Plugging your development copy into another repository

Ansible repositories may import collections in a variety of ways (for example,
a requirements file, or a Git submodule). During development, it can be useful
to use _your_ development copy of `tina_pm.common` (or some other collection).

**TL;DR:** List in `$ANSIBLE_COLLECTIONS_PATH` a directory which contains
your modified version under `ansible_collections/tina_pm/common`.

### Detailed instructions

1.  Create an “override directory” that can be used as a
    `collection_path`. (A _per-collection_ override directory is recommended.
    As an example, I use `~/work/tinapm/.ansible_collections/<fqcn>`).

  - Inside override directories, create an `ansible_collections` subdirectory,
    and symlink your Git repository into it using nested directories for FQCN.
    As an example, this is what I have:

        $ cd ~/work/tinapm; ls -A1
        .ansible_collections
        tina-roles.repo
        tina-sysadm.repo

        $ cd .ansible_collections/tina_pm.common
        $ ls -l ansible_collections/tina_pm
        lrwxr-xr-x  ...  common -> ../../../../tina-roles.repo

   - For every collection you want to override, place the override directory
     in the colon-separated `ANSIBLE_COLLECTIONS_PATH` environment variable:

         $ export ANSIBLE_COLLECTIONS_PATH=$HOME/work/tinapm/.ansible_collections/tina_pm.common

   - Beware of not removing access to collections you're not overriding. For
     this, ensure you append to `$ANSIBLE_COLLECTIONS_PATH` the collection
     locations shown by running `ansible --version` in your repository.
