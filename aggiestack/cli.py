"""
aggiestack

Usage:
  aggiestack config --hardware <input_file>
  aggiestack config --images <input_file>
  aggiestack config --flavors <input_file>
  aggiestack show hardware
  aggiestack show images
  aggiestack show flavors
  aggiestack show all

Examples:
  aggiestack config --hardware hdwr-config.txt
  aggiestack config --images image-config.txt
  aggiestack config --flavors flavor-config.txt
  aggiestack show hardware
  aggiestack show images
  aggiestack show flavors
  aggiestack show all
  

Help:
  Have only two types of commands aggiestack config or aggiestack show
"""

from commands.config import config_command
from docopt import docopt


def main():
    import aggiestack.commands
    options = docopt(__doc__, version='0.1')
    
    #print "option"
    #print options

    # for config commands
    if options['config'] == True:
        if options['--hardware'] == True:
            if options['<input_file>']:
                config_command('hardware', options['<input_file>'])

        elif options['--images'] == True:
            if options['<input_file>']:
                config_command('images', options['<input_file>'])
 
        elif options['--flavors'] == True:
            if options['<input_file>']:
                config_command('flavors', options['<input_file>'])

    if options['show'] == True:
        if options['hardware'] == True:
            show_command('hardware')

        elif options['images'] == True:
            show_command('images')

        elif options['flavors'] == True:
            show_command('flavors')
 
        elif options['all'] == True:
            show_command('all')

    #parser = ArgumentParser()
    #action_parsers = parser.add_subparsers(title="available actions")

    #config_parser = action_parsers.add_parser("config")
    #show_parser = actions_parser.add_parser("show")

    # other arguments for show
    # show_parser.add_argument
    #print sys.argv[0]
    #print sys.argv[1]
    #print len(sys.argv)

    #print "args"
    #import argparse
    #parser = argparse.ArgumentParser()
    #args = parser.parse_args()
   
    #        aggiestack.commands = getmembers(module, isclass)
    #        command = [command[1] for command in aggiestack.commands if command[0] != 'Base'][0]
    #        command = command(options)
    #        command.run()
    #print "hello"
