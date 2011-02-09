# -*- coding: utf-8 -*-
import pkg_resources, os, re
from paste.script import command, create_distro

beginning_letter = re.compile(r"^[^a-z]*")
valid_only = re.compile(r"[^a-z0-9_]")

class StartCommand(command.Command):
    """Create a new Lapin project.

Create a new Lapin project with this command.

Example usage::

    $ paster lapin_start yourproject
    """

    max_args = None
    min_args = 1
    version = pkg_resources.get_distribution('lapin').version
    usage = '\n' + __doc__
    summary = __doc__.splitlines()[0]
    group_name = "Lapin"

    name = None
    template = "lapin_template"
    svn_repository = None
    cookiesecret = None

    parser = command.Command.standard_parser(verbose = True)

    parser.add_option('-p', '--package',
                      action = 'store',
                      dest = 'package',
                      help = "package name for the code",)

    parser.add_option("-r", "--svn-repository", metavar = "REPOS",
                    help = "create project in given SVN repository",
                    dest = "svn_repository", default = svn_repository)

    def command(self):
        self.__dict__.update(self.options.__dict__)

        if self.args:  self.name = self.args[0]

        package = self.name.lower()
        package = beginning_letter.sub("", package)
        package = valid_only.sub("", package)
        if not self.package:
            while not self.package:
                self.package = raw_input(
                    "Enter package name [%s]: " % package).strip() or package

        env = pkg_resources.Environment()
        if self.name.lower() in env:
            print 'The name "%s" is already in use by' % self.name,
            for dist in env[self.name]:
                print dist
                return

        import imp
        try:
            if imp.find_module(self.package):
                print 'The package name "%s" is already in use' % self.package
                return
        except ImportError:
            pass

        if os.path.exists(self.name):
            print 'A directory called "%s" already exists. Exiting.' % self.name
            return


        self.cookiesecret = None
        try:
            import uuid
            self.cookiesecret = str(uuid.uuid4())
        except ImportError:
            import random
            import base64
            self.cookiesecret = base64.b64encode(base64(random.randrange(2 ** 32))).strip()

        create_command = create_distro.CreateDistroCommand("create")
        cmd_args = []
        for template in self.template.split():
            cmd_args.append("--template=%s" % self.template)
        if self.svn_repository:
            cmd_args.append("--svn-repository=%s" % self.svn_repository)

        cmd_args.append(self.name)
        cmd_args.append("package=%s" % self.package)
        cmd_args.append("cookiesecret=%s" % self.cookiesecret)
        create_command.run(cmd_args)
